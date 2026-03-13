from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
import requests


NASDAQ_HEADERS = {
    "user-agent": "Mozilla/5.0",
    "accept": "application/json, text/plain, */*",
    "origin": "https://www.nasdaq.com",
    "referer": "https://www.nasdaq.com/",
}
EXCHANGES = ("nasdaq", "nyse", "amex")
NAME_EXCLUDE_PATTERNS = (
    " warrant",
    " rights",
    " unit",
    " units",
    " etf",
    " etn",
    " fund",
    " trust",
    " depositary shares",
    " preferred",
    " notes",
    " note",
    " bond",
    " debenture",
)
TICKER_RE = re.compile(r"^[A-Z]{1,5}(-[A-Z])?$")


def normalize_symbol(symbol: str) -> str:
    return str(symbol).strip().upper().replace(".", "-")


def _parse_number(value: object) -> float | None:
    if value is None:
        return None
    text = str(value).replace("$", "").replace(",", "").strip()
    if not text or text == "N/A":
        return None
    try:
        return float(text)
    except ValueError:
        return None


def load_spy_tickers(spy_tickers_path: str | Path) -> set[str]:
    path = Path(spy_tickers_path)
    if not path.exists():
        raise FileNotFoundError(f"SPY ticker file not found: {path}")

    tickers: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        ticker = normalize_symbol(line)
        if ticker and ticker != "-" and TICKER_RE.match(ticker):
            tickers.add(ticker)
    return tickers


def fetch_exchange_rows(exchange: str) -> pd.DataFrame:
    url = (
        "https://api.nasdaq.com/api/screener/stocks"
        f"?tableonly=true&download=true&exchange={exchange}"
    )
    response = requests.get(url, headers=NASDAQ_HEADERS, timeout=60)
    response.raise_for_status()
    rows = response.json()["data"]["rows"]
    df = pd.DataFrame(rows)
    df["exchange"] = exchange.upper()
    return df


def build_nasdaq_spy_universe(
    min_market_cap: float = 1e9,
    min_price: float = 10.0,
    spy_tickers_path: str | Path | None = None,
    save_path: str | Path | None = None,
) -> pd.DataFrame:
    if spy_tickers_path is None:
        spy_tickers_path = Path.cwd() / "spy_tickers.txt"

    spy_tickers = load_spy_tickers(spy_tickers_path)
    frames = [fetch_exchange_rows(exchange) for exchange in EXCHANGES]
    listings = pd.concat(frames, ignore_index=True)

    listings["ticker"] = listings["symbol"].map(normalize_symbol)
    listings["last_sale"] = listings["lastsale"].map(_parse_number)
    listings["market_cap"] = listings["marketCap"].map(_parse_number)
    listings["name_lower"] = listings["name"].astype(str).str.lower()

    valid_ticker = listings["ticker"].map(lambda x: bool(TICKER_RE.match(x)))
    eligible = (
        valid_ticker
        & listings["last_sale"].fillna(0).ge(min_price)
        & listings["market_cap"].fillna(0).ge(min_market_cap)
    )
    for pattern in NAME_EXCLUDE_PATTERNS:
        eligible &= ~listings["name_lower"].str.contains(pattern, na=False)

    in_spy = listings["ticker"].isin(spy_tickers)
    in_nasdaq = listings["exchange"].eq("NASDAQ")
    selected = listings.loc[eligible & (in_nasdaq | in_spy)].copy()

    selected["source"] = selected.apply(
        lambda row: "NASDAQ+SPY" if row["exchange"] == "NASDAQ" and row["ticker"] in spy_tickers
        else ("NASDAQ" if row["exchange"] == "NASDAQ" else "SPY"),
        axis=1,
    )

    universe = (
        selected.loc[:, ["ticker", "name", "exchange", "source", "last_sale", "market_cap", "volume", "sector", "industry"]]
        .sort_values(["source", "market_cap", "ticker"], ascending=[True, False, True])
        .drop_duplicates(subset=["ticker"], keep="first")
        .reset_index(drop=True)
    )

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        universe.to_csv(save_path, index=False)

    return universe
