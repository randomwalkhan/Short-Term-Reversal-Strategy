# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:25:01 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           90.00               20            2.14              4.35        289.35                64.46         0.603          pass              0.538             48.1                           0.665               -2.76             -0.209                      ok            True                  False
  MPWR           81.25               32            0.99              9.02       1301.79                74.72         0.591          pass              0.487             82.7                           0.805                0.36              0.097                      ok            True                  False
   ADI           86.21               29            1.15              3.07        379.21                54.65         0.577          pass              0.554             68.1                           0.799               -0.27              0.010                      ok            True                  False
  AAPL           96.00               25            0.78              1.82        332.48                36.90         0.572          pass              0.674             39.0                           0.357                7.14              0.701                      ok            True                  False
  ASML           92.00               25            2.06             25.73       1773.84                64.12         0.557          pass              0.640             54.9                           0.770               -1.20             -0.065                      ok            True                  False
  NXPI           84.62               26            1.47              2.79        269.46                54.99         0.541          pass              0.485             67.2                           0.779               -2.45             -0.223                      ok            True                  False
  UPRO           89.47               19            1.63              1.64        142.91                37.18         0.518          pass              0.544             59.9                           0.799                0.35              0.099                      ok            True                  False
  SBUX           83.33               18            1.13              0.86        108.00                23.69         0.507          pass              0.208              5.0                           0.165                2.76              0.427                      ok            True                  False
  AVGO           86.11               36            0.74              1.93        373.62                50.81         0.501          pass              0.637             83.4                           0.933                3.12              0.275                      ok            True                  False
  PYPL           77.78               18            1.28              0.51         56.51                63.95         0.666          pass              0.273             51.1                           0.447               23.17              2.474                      ok           False                  False
   WDC           81.48               27            1.01              3.30        465.39               109.88         0.663          pass              0.480             87.0                           0.955              -14.27             -1.562 downtrend_blocked_slope           False                  False
  KLAC           80.95               21            2.94              4.51        217.44               106.93         0.652          pass              0.333             56.4                           0.822               -9.60             -0.539 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T10:25:01.970111-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:20:01.107680-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:15:01.837180-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:04.802091-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717102501)

</details>
