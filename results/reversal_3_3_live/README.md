# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:35:03 EDT`
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
  PYPL           81.82               22            1.11              0.44         56.54                63.95         0.656          pass              0.367             57.5                           0.621               23.38              2.482                      ok            True                  False
   TXN           90.00               20            2.27              4.63        289.24                64.46         0.594          pass              0.527             44.8                           0.530               -2.89             -0.216                      ok            True                  False
  MPWR           81.25               32            1.05              9.56       1301.55                74.72         0.587          pass              0.484             81.7                           0.636                0.30              0.094                      ok            True                  False
   ADI           84.00               25            1.41              3.77        378.92                54.65         0.583          pass              0.448             60.9                           0.618               -0.53             -0.002                      ok            True                  False
  ASML           95.65               23            2.33             29.17       1772.37                64.12         0.556          pass              0.689             48.9                           0.626               -1.48             -0.078                      ok            True                  False
  NXPI           86.96               23            1.94              3.68        269.08                54.99         0.531          pass              0.495             56.7                           0.547               -2.91             -0.245                      ok            True                  False
  AVGO           84.38               32            0.99              2.59        373.34                50.81         0.509          pass              0.547             77.7                           0.681                2.86              0.263                      ok            True                  False
   WDC           83.33               30            0.72              2.34        465.81               109.88         0.666          pass              0.561             90.8                           0.792              -14.01             -1.549 downtrend_blocked_slope           False                  False
  KLAC           82.35               17            3.46              5.32        217.09               106.93         0.644          pass              0.320             48.6                           0.554              -10.10             -0.564 downtrend_blocked_slope           False                  False
  MSTR           77.78               45            0.48              0.32         93.89                90.37         0.631          pass              0.531             89.3                           0.717               -7.14             -0.532 downtrend_blocked_slope           False                  False
  MRVL           91.18               34            0.70              0.93        187.90                94.74         0.610          pass              0.782             87.7                           0.675              -23.75             -2.732 downtrend_blocked_slope           False                  False
  SOXL           85.71               21            5.90              5.88        139.96               207.84         0.608          pass              0.490             67.7                           0.635              -26.12             -2.625 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T10:35:03.822723-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:30:06.695303-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:25:01.970111-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:20:01.107680-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:15:01.837180-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:04.802091-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717103503)

</details>
