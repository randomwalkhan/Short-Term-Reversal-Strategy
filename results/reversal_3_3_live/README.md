# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-05 13:15:10 EDT`
Last processed slot: `manual`

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
  TEAM           83.33               36            2.18              1.42         92.58               121.39            True
  FAST           95.83               24            0.89              0.28         44.76                39.95            True
  META           86.96               23            1.45              6.18        607.82                47.41            True
  MSFT           82.61               23            1.02              2.94        412.36                34.18            True
  PANW           83.87               31            1.03              1.33        183.99                48.03            True
  MDLZ           84.00               25            0.61              0.26         61.27                26.22            True
  FANG          100.00               10            2.66              3.98        211.98                31.30            True
  DDOG           92.68               41            0.64              0.65        146.41                55.45            True
  CHTR           62.50                8            3.67              4.25        163.52               118.91           False
 CMCSA           75.00                4            2.60              0.49         26.86                61.32           False
    ZS           84.44               45            0.49              0.49        141.99                69.57           False
  GEHC           78.38               37            0.79              0.34         60.86                59.35           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-05T13:10:09.568185-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-05T13:05:09.617226-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-05T13:00:07.034754-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-05T12:55:06.325768-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-05T12:40:06.300878-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-05T12:35:06.312532-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-05T12:30:06.303564-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-05T12:25:06.302342-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-05T12:10:06.308673-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-05T12:05:06.304003-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260505131510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260505131510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260505131510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260505131510)

</details>
