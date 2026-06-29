# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 10:15:12 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  GILD           88.89               18            0.93              0.83        127.52                29.34         0.566          pass              0.457             36.7                           0.380                1.54              0.104                      ok            True                  False
  PCAR           82.61               23            1.07              0.91        120.29                36.52         0.538          pass              0.297             28.8                           0.291                0.73              0.026                      ok            True                  False
  MRVL          100.00               11            5.44             10.16        262.42               157.15         0.767          pass              0.515             10.7                           0.182               -9.81             -1.157 downtrend_blocked_slope           False                  False
  AVGO           82.61               23            1.17              2.99        363.74                77.46         0.706          pass              0.227              0.0                           0.157               -5.43             -0.623 downtrend_blocked_slope           False                  False
  SOXL           92.31               13            9.49             14.32        209.46               243.65         0.691          pass              0.446              9.5                           0.192              -16.85             -1.594 downtrend_blocked_slope           False                  False
  ASML           96.30               27            1.16             14.60       1788.36                67.49         0.673          pass              0.581              0.0                           0.197               -4.82             -0.542 downtrend_blocked_slope           False                  False
   ADI           94.29               35            0.19              0.52        386.69                64.34         0.650          pass              0.669             18.7                           0.149               -7.57             -0.773 downtrend_blocked_slope           False                  False
   TXN           88.89                9            3.11              6.21        282.76                70.58         0.604          pass              0.321              8.0                           0.221               -8.16             -0.719 downtrend_blocked_slope           False                  False
   STX           97.14               35            0.30              1.88        899.10                85.77         0.602          pass              0.886             86.5                           0.488               -3.56             -0.782 downtrend_blocked_slope           False                  False
  MCHP          100.00               15            2.72              1.67         87.21                74.63         0.602          pass              0.513              6.6                           0.203              -10.18             -1.104 downtrend_blocked_slope           False                  False
  MPWR           86.96               23            2.26             20.81       1304.40                89.21         0.599          pass              0.374             13.9                           0.205              -18.62             -1.986 downtrend_blocked_slope           False                  False
  NXPI           92.86               14            2.45              4.76        274.98                66.10         0.596          pass              0.463             11.3                           0.217              -11.06             -1.086 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-06-29T10:15:12.530028-04:00 early_entry_1015 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-06-26T14:50:01.669190-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-26", "training_samples": 5312, "window": 5}
2026-06-26T14:50:01.669190-04:00       entry_1500      entry_skipped                   {"budget": 14680.25, "entry_cost": 16617.5, "reason": "insufficient_cash", "ticker": "MU"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629101512)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629101512)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629101512)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629101512)

</details>
