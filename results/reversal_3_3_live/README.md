# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-05 11:30:06 EDT`
Last processed slot: `manage_1130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$23,087.50`
- Equity: `$23,087.50`
- Realized PnL: `$13,087.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00095000      8          2026-05-04         2026-05-05         10.7      17.475 5420.0   63.317757 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TEAM           84.21               38            1.77              1.15         92.70               121.39            True
  META           85.19               27            0.94              4.00        608.75                47.41            True
   KDP           89.29               28            0.57              0.12         28.82                34.67            True
  MDLZ           85.71               21            0.88              0.38         61.22                26.22            True
   ADP           80.95               21            1.06              1.56        210.65                37.69            True
  FANG          100.00               10            2.67              4.00        211.98                31.30            True
  MSFT           85.29               34            0.53              1.53        412.97                34.18            True
  CHTR           60.00               10            3.31              3.83        163.70               118.91           False
 CMCSA           75.00                4            2.64              0.50         26.86                61.32           False
   TXN           83.33               36            0.44              0.86        280.52                67.78           False
  FAST           97.22               36            0.08              0.02         44.87                39.95           False
  GEHC           82.22               45            0.16              0.07         60.97                59.35           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-05T11:30:06.314731-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:25:06.295587-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:10:06.308576-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-05T11:05:06.306421-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-05T11:00:06.364534-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-05T10:55:06.306031-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-05T10:40:01.278924-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-05T10:35:06.304253-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-05T10:30:06.301065-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-05T10:25:06.315562-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260505113006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260505113006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260505113006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260505113006)

</details>
