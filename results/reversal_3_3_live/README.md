# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 13:45:05 EDT`
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
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$27,583.50`
- Equity: `$27,583.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CRWD     option         option CRWD260618C00470000      3          2026-05-06         2026-05-07       33.025       51.55 5557.5   56.093868 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
 CMCSA           91.67               12            1.08              0.20         26.35                61.67            True
  INTC          100.00               28            1.88              1.49        112.37                95.68            True
   XEL           95.65               23            0.73              0.41         80.37                28.12            True
   KDP           89.66               29            0.54              0.11         28.51                34.76            True
  SBUX           88.24               17            1.61              1.20        105.93                31.94            True
   TXN           88.89                9            2.35              4.76        287.40                67.07           False
  NXPI           66.67                3            4.19              8.90        299.74                84.51           False
  GEHC           72.97               37            0.72              0.31         61.60                55.11           False
  FAST           97.14               35            0.17              0.05         44.69                34.69           False
  NFLX           91.49               47            0.05              0.03         88.26                44.73           False
   ADI           69.23               13            2.10              6.10        413.05                34.89           False
  ROST          100.00                3            2.73              4.37        227.04                15.20           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-07T13:40:10.073286-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:35:04.908298-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:30:02.811193-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:25:01.880630-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:21:58.207270-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T11:05:05.932561-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-07T11:00:04.917667-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-07T10:55:01.919462-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-07T10:40:06.740458-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-07T10:35:01.914574-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507134505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507134505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507134505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507134505)

</details>
