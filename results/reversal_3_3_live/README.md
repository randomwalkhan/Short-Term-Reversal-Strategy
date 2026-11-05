# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 09:30:06 EST`
Last processed slot: `manage_0930`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           90.32               31            1.38              1.38        141.95                73.89         0.583          pass              0.624             50.0                           0.472               -3.59             -0.575                                 ok            True                  False
  UPRO           85.71               28            0.89              0.92        146.90                38.96         0.543          pass              0.394             22.5                           0.139               -0.38             -0.256                                 ok            True                  False
  NXPI           92.31               13            2.23              4.13        263.24                39.79         0.503          pass              0.500             33.9                           0.307                8.97              1.065                                 ok            True                  False
   CEG           85.19               27            1.75              3.01        244.43                51.86         0.500          pass              0.410             36.0                           0.424               -5.40             -0.247                                 ok            True                  False
  INTC           53.85               13            3.75              1.53         57.61               128.90         0.746          pass              0.117              7.4                           0.119              -34.40             -5.619            downtrend_blocked_slope           False                  False
  FTNT           80.95               21            2.22              2.01        128.53                91.87         0.690          pass              0.195              9.2                           0.111              -26.86             -4.519 downtrend_blocked_slope_and_streak           False                  False
   CSX           72.73               11            1.35              0.49         51.88                28.96         0.556          pass              0.062              0.0                           0.250               -0.54              0.010                                 ok           False                  False
  SHOP           73.68               19            2.03              2.17        152.10                59.06         0.544          pass              0.149             11.7                           0.326              -11.18             -1.512 downtrend_blocked_slope_and_streak           False                  False
  INSM           78.95               38            0.91              0.70        109.70                61.82         0.519          pass              0.239              0.0                           0.217               14.66              1.915                                 ok           False                  False
   TXN           72.73               11            1.82              3.97        309.79                33.35         0.512          pass              0.216             52.8                           0.478                9.95              0.863                                 ok           False                  False
  TEAM           94.12               17            2.41              3.20        188.51                53.55         0.510          pass              0.563             29.7                           0.352              -16.96             -2.346            downtrend_blocked_slope           False                  False
  SNPS           63.64               11            2.75              8.91        459.13                45.81         0.509          pass              0.104             15.4                           0.276                6.57              0.548                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105093006)

</details>
