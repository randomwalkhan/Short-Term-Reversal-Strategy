from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class OpenPosition:
    product_id: str
    entry_time: str
    entry_price: float
    stop_price: float
    take_profit_price: float
    planned_quote_size: float
    client_order_id: str
    exchange_order_id: str | None = None
    dry_run: bool = True
    close_deadline: str | None = None


@dataclass
class BotState:
    positions: dict[str, OpenPosition] = field(default_factory=dict)
    last_trade_times: dict[str, str] = field(default_factory=dict)
    realized_pnl_by_day: dict[str, float] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "BotState":
        if not path.exists():
            return cls()

        payload = json.loads(path.read_text())
        positions = {
            product_id: OpenPosition(**position_payload)
            for product_id, position_payload in payload.get("positions", {}).items()
        }
        return cls(
            positions=positions,
            last_trade_times=payload.get("last_trade_times", {}),
            realized_pnl_by_day=payload.get("realized_pnl_by_day", {}),
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        serializable = {
            "positions": {product_id: asdict(position) for product_id, position in self.positions.items()},
            "last_trade_times": self.last_trade_times,
            "realized_pnl_by_day": self.realized_pnl_by_day,
        }
        path.write_text(json.dumps(serializable, indent=2, sort_keys=True))

    def position_for(self, product_id: str) -> OpenPosition | None:
        return self.positions.get(product_id)

    def open_position(self, position: OpenPosition) -> None:
        self.positions[position.product_id] = position
        self.last_trade_times[position.product_id] = position.entry_time

    def close_position(self, product_id: str, realized_pnl: float, closed_at: datetime | None = None) -> None:
        self.positions.pop(product_id, None)
        timestamp = closed_at or utc_now()
        day_key = timestamp.date().isoformat()
        self.realized_pnl_by_day[day_key] = self.realized_pnl_by_day.get(day_key, 0.0) + realized_pnl
        self.last_trade_times[product_id] = timestamp.isoformat()

    def in_cooldown(self, product_id: str, now: datetime, cooldown_seconds: int) -> bool:
        raw = self.last_trade_times.get(product_id)
        if raw is None:
            return False
        last_trade_time = datetime.fromisoformat(raw)
        return (now - last_trade_time).total_seconds() < cooldown_seconds

    def open_position_count(self) -> int:
        return len(self.positions)

    def realized_loss_today(self, now: datetime | None = None) -> float:
        current_time = now or utc_now()
        day_key = current_time.date().isoformat()
        realized = self.realized_pnl_by_day.get(day_key, 0.0)
        return abs(realized) if realized < 0 else 0.0

