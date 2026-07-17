# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:20:01 EDT`
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
  PYPL           83.33               12            1.63              0.65         56.45                63.95         0.687          pass              0.284             37.7                           0.377               22.73              2.458                      ok            True                  False
   TXN           90.00               20            2.22              4.53        289.28                64.46         0.598          pass              0.531             46.1                           0.704               -2.84             -0.213                      ok            True                  False
  MPWR           82.35               34            0.84              7.70       1302.35                74.72         0.589          pass              0.537             85.3                           0.918                0.50              0.104                      ok            True                  False
  AAPL           95.83               24            0.81              1.88        332.45                36.90         0.577          pass              0.662             36.8                           0.304                7.11              0.700                      ok            True                  False
   ADI           86.67               30            1.10              2.93        379.27                54.65         0.574          pass              0.577             69.6                           0.882               -0.22              0.013                      ok            True                  False
  ASML           91.67               24            2.18             27.19       1773.22                64.12         0.555          pass              0.617             52.3                           0.787               -1.32             -0.070                      ok            True                  False
  NXPI           85.19               27            1.32              2.51        269.59                54.99         0.545          pass              0.518             70.5                           0.864               -2.30             -0.216                      ok            True                  False
  UPRO           94.44               18            1.91              1.92        142.79                37.18         0.512          pass              0.649             53.0                           0.798                0.06              0.086                      ok            True                  False
  SBUX           84.21               19            1.03              0.78        108.03                23.69         0.509          pass              0.226              0.9                           0.153                2.86              0.431                      ok            True                  False
  AVGO           86.49               37            0.56              1.46        373.82                50.81         0.508          pass              0.666             87.5                           0.952                3.31              0.283                      ok            True                  False
  BKNG           83.33               18            2.23              2.88        183.38                41.98         0.501          pass              0.209              5.6                           0.071               -2.20             -0.010                      ok            True                  False
  SOXL           85.71               21            5.18              5.17        140.27               207.84         0.659          pass              0.506             71.6                           0.900              -25.55             -2.590 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T10:20:01.107680-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:15:01.837180-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:04.802091-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717102001)

</details>
