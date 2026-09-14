# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 10:00:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           73.08               26            1.50              4.18        395.59                60.55         0.573            pass              0.266             33.9                           0.499              -11.57             -1.201            downtrend_blocked_slope           False                  False
  CHTR           90.24               41            0.60              0.61        145.51                68.13         0.537            pass              0.765             79.3                           0.484               -5.68             -0.882            downtrend_blocked_slope           False                  False
   EXC           94.44               18            0.30              0.09         43.12                14.68         0.530            pass              0.548             18.7                           0.308               -1.12             -0.062                                 ok           False                  False
  UPRO           94.12               17            1.55              1.61        147.33                26.03         0.524            pass              0.589             37.8                           0.682               -3.99             -0.340 downtrend_blocked_slope_and_streak           False                  False
  NVDA           83.33                6            3.40              5.19        216.06                43.68         0.523            pass              0.203             20.7                           0.538               -2.96             -0.176           downtrend_blocked_streak           False                  False
   CSX           77.78               18            0.74              0.25         48.84                18.07         0.498 below_threshold              0.247             47.8                           0.402               -4.99             -0.338            downtrend_blocked_slope           False                  False
   AEP           91.30               23            0.52              0.45        123.14                16.49         0.496 below_threshold              0.575             45.7                           0.276                0.31              0.073                                 ok           False                  False
  MELI           97.50               40            0.25              3.39       1895.92                37.25         0.487 below_threshold              0.865             72.2                           0.551               -3.75             -0.480 downtrend_blocked_slope_and_streak           False                  False
  CDNS           73.91               23            1.85              3.74        287.77                43.36         0.487 below_threshold              0.216             26.7                           0.282              -16.56             -1.852 downtrend_blocked_slope_and_streak           False                  False
  ALNY           90.00               40            0.39              0.67        248.39                49.38         0.478 below_threshold              0.784             89.8                           0.500                4.48              0.253                                 ok           False                  False
   LIN           75.00               20            0.74              2.43        465.18                15.11         0.477 below_threshold              0.184             23.1                           0.224               -5.16             -0.642 downtrend_blocked_slope_and_streak           False                  False
   BKR           88.89                9            2.01              0.83         58.70                29.92         0.470 below_threshold              0.295              3.7                           0.104               -7.27             -0.822 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-14T10:00:06.059973-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:55:01.842224-04:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914100006)

</details>
