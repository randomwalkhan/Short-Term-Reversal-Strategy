# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 09:45:01 EDT`
Last processed slot: `manual`

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
  SNPS           73.68               19            2.18              6.07        394.78                60.55         0.574            pass              0.130              4.0                           0.060              -12.18             -1.233            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.38              0.39        145.60                68.13         0.545            pass              0.794             86.7                           0.721               -5.48             -0.872            downtrend_blocked_slope           False                  False
  UPRO           92.86               14            1.88              1.95        147.19                26.03         0.521            pass              0.496             24.9                           0.511               -4.31             -0.355 downtrend_blocked_slope_and_streak           False                  False
  NVDA           80.00                5            3.66              5.60        215.89                43.68         0.510            pass              0.095             14.5                           0.385               -3.23             -0.189           downtrend_blocked_streak           False                  False
  CDNS           75.00               16            2.36              4.79        287.32                43.36         0.500 below_threshold              0.094              1.4                           0.102              -17.00             -1.876 downtrend_blocked_slope_and_streak           False                  False
  MELI           97.14               35            0.67              8.90       1893.55                37.25         0.492 below_threshold              0.694             26.2                           0.261               -4.15             -0.499 downtrend_blocked_slope_and_streak           False                  False
  ALNY           89.19               37            0.54              0.93        248.28                49.38         0.486 below_threshold              0.731             85.8                           0.695                4.32              0.246                                 ok           False                   True
   LIN           75.00               20            0.69              2.25        465.26                15.11         0.483 below_threshold              0.139              8.1                           0.139               -5.10             -0.639 downtrend_blocked_slope_and_streak           False                  False
   BKR           91.67               12            1.82              0.75         58.74                29.92         0.466 below_threshold              0.400              9.7                           0.151               -7.09             -0.814 downtrend_blocked_slope_and_streak           False                  False
  CSCO           75.00               20            1.58              1.24        111.60                22.50         0.454 below_threshold              0.222             36.8                           0.617                0.39              0.018                                 ok           False                  False
  AMZN           74.19               31            0.93              1.67        256.06                26.09         0.452 below_threshold              0.366             60.4                           0.631               -4.52             -0.310 downtrend_blocked_slope_and_streak           False                  False
   CSX           88.24               34            0.22              0.08         48.92                18.07         0.448 below_threshold              0.677             84.1                           0.710               -4.50             -0.315            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:55:01.842224-04:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:50:02.882708-04:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914094501)

</details>
