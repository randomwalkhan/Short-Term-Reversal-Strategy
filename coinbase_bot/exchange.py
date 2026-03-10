from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_DOWN
from typing import Any

import pandas as pd
from coinbase.rest import RESTClient

from coinbase_bot.config import GRANULARITY_SECONDS


def _to_dict(response: Any) -> dict[str, Any]:
    if isinstance(response, dict):
        return response
    if hasattr(response, "to_dict"):
        return response.to_dict()
    if hasattr(response, "__dict__"):
        return dict(response.__dict__)
    raise TypeError(f"Unsupported Coinbase response type: {type(response)!r}")


def _as_decimal_string(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def floor_to_increment(value: float, increment: str) -> str:
    decimal_value = Decimal(str(value))
    decimal_increment = Decimal(str(increment))
    if decimal_increment <= 0:
        return _as_decimal_string(decimal_value)
    units = (decimal_value / decimal_increment).to_integral_value(rounding=ROUND_DOWN)
    floored = units * decimal_increment
    return _as_decimal_string(floored)


@dataclass(frozen=True)
class ProductDetails:
    product_id: str
    price: float
    base_currency: str
    quote_currency: str
    base_increment: str
    quote_increment: str
    base_min_size: float
    quote_min_size: float
    trading_disabled: bool


class CoinbaseAdvancedClient:
    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        timeout: int = 10,
        require_auth: bool = False,
    ) -> None:
        key = api_key or os.getenv("COINBASE_API_KEY")
        secret = api_secret or os.getenv("COINBASE_API_SECRET")
        self.is_authenticated = bool(key and secret)
        if require_auth and not self.is_authenticated:
            raise ValueError("Missing Coinbase credentials. Set COINBASE_API_KEY and COINBASE_API_SECRET.")
        kwargs: dict[str, Any] = {"timeout": timeout}
        if self.is_authenticated:
            kwargs["api_key"] = key
            kwargs["api_secret"] = secret
        self.client = RESTClient(**kwargs)

    def _get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return _to_dict(self.client.get(path, params=params or {}))

    def _post(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return _to_dict(self.client.post(path, data=data))

    def get_product(self, product_id: str) -> ProductDetails:
        payload = self._get(f"/api/v3/brokerage/products/{product_id}")
        base_currency = (
            payload.get("base_currency_id")
            or payload.get("base_display_symbol")
            or product_id.split("-")[0]
        )
        quote_currency = (
            payload.get("quote_currency_id")
            or payload.get("quote_display_symbol")
            or product_id.split("-")[-1]
        )
        return ProductDetails(
            product_id=payload["product_id"],
            price=float(payload["price"]),
            base_currency=str(base_currency).upper(),
            quote_currency=str(quote_currency).upper(),
            base_increment=str(payload["base_increment"]),
            quote_increment=str(payload["quote_increment"]),
            base_min_size=float(payload.get("base_min_size", 0.0)),
            quote_min_size=float(payload.get("quote_min_size", 0.0)),
            trading_disabled=bool(payload.get("trading_disabled", False)),
        )

    def get_available_balance(self, currency: str) -> float:
        payload = self._get("/api/v3/brokerage/accounts")
        currency = currency.upper()
        total = 0.0
        for account in payload.get("accounts", []):
            if str(account.get("currency", "")).upper() != currency:
                continue
            available_balance = account.get("available_balance", {})
            total += float(available_balance.get("value", 0.0))
        return total

    def get_fills(
        self,
        product_id: str,
        start_time: datetime | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {
            "product_ids": [product_id],
            "limit": limit,
        }
        if start_time is not None:
            params["start_sequence_timestamp"] = start_time.astimezone(timezone.utc).isoformat()
        payload = self._get("/api/v3/brokerage/orders/historical/fills", params=params)
        return list(payload.get("fills", []))

    def preview_order(self, order_body: dict[str, Any]) -> dict[str, Any]:
        return self._post("/api/v3/brokerage/orders/preview", order_body)

    def create_order(self, order_body: dict[str, Any]) -> dict[str, Any]:
        return self._post("/api/v3/brokerage/orders", order_body)

    def fetch_candles(self, product_id: str, granularity: str, candles_needed: int) -> pd.DataFrame:
        granularity = granularity.upper()
        seconds = GRANULARITY_SECONDS[granularity]
        end = datetime.now(timezone.utc)
        rows: list[dict[str, Any]] = []
        remaining = candles_needed

        while remaining > 0:
            batch_size = min(remaining, 350)
            start = end - timedelta(seconds=seconds * batch_size)
            params = {
                "product_id": product_id,
                "start": str(int(start.timestamp())),
                "end": str(int(end.timestamp())),
                "granularity": granularity,
                "limit": batch_size,
            }
            payload = _to_dict(self.client.get_public_candles(**params))
            rows.extend(payload.get("candles", []))
            end = start
            remaining -= batch_size

        frame = pd.DataFrame(rows)
        if frame.empty:
            raise ValueError(f"No candles returned for {product_id}")

        for column in ["open", "high", "low", "close", "volume"]:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
        frame["start"] = pd.to_datetime(pd.to_numeric(frame["start"], errors="coerce"), unit="s", utc=True)
        frame = frame.dropna(subset=["start", "open", "high", "low", "close"])
        frame = frame.sort_values("start").drop_duplicates("start")
        frame = frame.reset_index(drop=True)
        return frame[["start", "open", "high", "low", "close", "volume"]]
