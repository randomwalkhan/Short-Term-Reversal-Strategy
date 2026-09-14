# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 09:30:03 EDT`
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
  SNPS           73.08               26            1.54              4.29        395.54                60.55         0.577            pass              0.164              0.0                           0.197              -11.61             -1.203            downtrend_blocked_slope           False                  False
  NVDA           80.00                5            3.57              5.46        215.95                43.68         0.520            pass              0.061              3.0                           0.284               -3.14             -0.184           downtrend_blocked_streak           False                  False
  UPRO           92.86               14            2.18              2.25        147.04                26.03         0.504            pass              0.458             12.7                           0.304               -4.61             -0.369 downtrend_blocked_slope_and_streak           False                  False
   CSX           81.82               22            0.51              0.17         48.88                18.07         0.493 below_threshold              0.369             63.8                           0.404               -4.77             -0.328            downtrend_blocked_slope           False                  False
  PCAR           92.86               14            1.61              1.39        122.14                17.68         0.478 below_threshold              0.477             19.8                           0.246               -3.66             -0.227                                 ok           False                  False
  AMZN           69.57               23            1.39              2.50        255.71                26.09         0.473 below_threshold              0.171             12.4                           0.173               -4.96             -0.331 downtrend_blocked_slope_and_streak           False                  False
   CEG           83.33                6            3.25              6.47        281.98                34.33         0.469 below_threshold              0.222             28.6                           0.311               -0.45              0.231                                 ok           False                  False
  CDNS           84.00               50            0.20              0.40        289.20                43.36         0.452 below_threshold              0.601             83.0                           0.661              -15.16             -1.777 downtrend_blocked_slope_and_streak           False                  False
  CSCO           68.75               16            1.99              1.56        111.46                22.50         0.447 below_threshold              0.146             20.4                           0.367               -0.03             -0.001                                 ok           False                  False
  ROST           85.71               42            0.09              0.14        230.68                29.12         0.442 below_threshold              0.677             93.6                           0.581                1.07              0.002                                 ok           False                  False
   HON           63.16               19            1.58              2.24        201.40                19.45         0.436 below_threshold              0.178             24.9                           0.318               -8.40             -0.705            downtrend_blocked_slope           False                  False
   BKR           93.10               29            0.83              0.34         58.91                29.92         0.432 below_threshold              0.615             31.9                           0.282               -6.15             -0.768 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914093003)

</details>
