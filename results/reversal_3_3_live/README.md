# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:30:06 EDT`
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
  PYPL           84.62               26            1.00              0.40         56.56                63.95         0.641          pass              0.479             61.6                           0.632               23.51              2.487                      ok            True                  False
   TXN           88.89               18            2.47              5.03        289.07                64.46         0.593          pass              0.470             40.1                           0.562               -3.08             -0.225                      ok            True                  False
   ADI           85.19               27            1.25              3.33        379.10                54.65         0.582          pass              0.506             65.4                           0.724               -0.37              0.006                      ok            True                  False
  MPWR           81.25               32            1.43             13.08       1300.05                74.72         0.560          pass              0.461             75.0                           0.642               -0.09              0.077                      ok            True                  False
  ASML           95.65               23            2.37             29.55       1772.20                64.12         0.553          pass              0.687             48.2                           0.681               -1.51             -0.079                      ok            True                  False
  NXPI           86.96               23            1.84              3.49        269.17                54.99         0.538          pass              0.503             59.0                           0.636               -2.81             -0.240                      ok            True                  False
  AVGO           82.14               28            1.18              3.09        373.13                50.81         0.520          pass              0.450             73.5                           0.766                2.66              0.255                      ok            True                  False
  UPRO           94.44               18            1.88              1.89        142.80                37.18         0.515          pass              0.652             53.9                           0.712                0.10              0.087                      ok            True                  False
  BKNG           85.71               21            1.83              2.37        183.59                41.98         0.510          pass              0.345             22.7                           0.311               -1.81              0.008                      ok            True                  False
  KLAC           80.00               20            3.22              4.95        217.25               106.93         0.638          pass              0.287             52.2                           0.667               -9.87             -0.552 downtrend_blocked_slope           False                  False
   STX           91.67               36            0.03              0.18        745.41                93.61         0.637          pass              0.847             99.5                           0.952               -9.14             -0.980 downtrend_blocked_slope           False                  False
   WDC           79.17               24            1.71              5.60        464.41               109.88         0.631          pass              0.390             77.9                           0.864              -14.88             -1.595 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T10:30:06.695303-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:25:01.970111-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:20:01.107680-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:15:01.837180-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:04.802091-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717103006)

</details>
