# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 10:25:01 EDT`
Last processed slot: `manage_1030`

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
  ASML           84.85               33            0.60              6.51       1541.95                46.11            True
  MSTR           88.24               34            2.25              2.94        185.56                67.05            True
 CMCSA           90.91               33            0.15              0.03         26.43                61.67           False
   TXN           87.50                8            2.74              5.54        287.06                67.07           False
  NXPI           64.29               14            2.99              6.35        300.83                84.51           False
   KDP          100.00                4            2.31              0.46         28.36                34.76           False
  QCOM           92.31               39            0.23              0.31        192.53                72.73           False
  GEHC           75.00               40            0.38              0.16         61.66                55.11           False
  SBUX          100.00                5            3.15              2.35        105.43                31.94           False
  SOXL           78.26               23            3.30              3.84        164.21                95.28           False
   ADI           76.19               21            1.68              4.89        413.57                34.89           False
  ROST           94.74               19            1.11              1.78        228.15                15.20           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                  detail
2026-05-07T10:25:01.892823-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:20:01.930498-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "CRWD260618C00470000", "fill_price": 51.55, "pnl": 5557.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 56.09, "ticker": "CRWD"}
2026-05-07T10:10:04.036694-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:05:04.033139-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:00:03.903840-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:55:02.556058-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:40:01.922571-04:00 manage_0930 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:35:01.914408-04:00 manage_0930 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:30:01.925048-04:00 manage_0930 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:25:01.894252-04:00 manage_0930 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507102501)

</details>
