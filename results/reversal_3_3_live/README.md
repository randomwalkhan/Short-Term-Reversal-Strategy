# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 09:40:04 EDT`
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
  SNPS           69.57               23            1.79              4.97        395.25                60.55         0.569            pass              0.208             21.4                           0.193              -11.82             -1.214            downtrend_blocked_slope           False                  False
  NVDA          100.00                3            4.21              6.43        215.54                43.68         0.517            pass              0.458              1.9                           0.175               -3.77             -0.214           downtrend_blocked_streak           False                  False
  UPRO           92.86               14            2.07              2.15        147.09                26.03         0.510            pass              0.471             16.9                           0.435               -4.50             -0.364 downtrend_blocked_slope_and_streak           False                  False
  CDNS           71.43               21            1.94              3.93        287.69                43.36         0.491 below_threshold              0.180             19.0                           0.307              -16.64             -1.857 downtrend_blocked_slope_and_streak           False                  False
  MELI           97.44               39            0.32              4.20       1895.57                37.25         0.489 below_threshold              0.838             65.2                           0.381               -3.81             -0.483 downtrend_blocked_slope_and_streak           False                  False
   BKR           91.67               12            1.74              0.72         58.75                29.92         0.472 below_threshold              0.396              8.0                           0.202               -7.02             -0.810 downtrend_blocked_slope_and_streak           False                  False
   LIN           78.57               28            0.33              1.07        465.76                15.11         0.465 below_threshold              0.251             28.1                           0.291               -4.76             -0.623 downtrend_blocked_slope_and_streak           False                  False
  AMZN           76.67               30            0.98              1.75        256.03                26.09         0.458 below_threshold              0.355             58.5                           0.568               -4.56             -0.312 downtrend_blocked_slope_and_streak           False                  False
   CSX           87.50               32            0.27              0.09         48.91                18.07         0.456 below_threshold              0.636             81.2                           0.664               -4.54             -0.316            downtrend_blocked_slope           False                  False
  PCAR           95.65               23            1.16              0.99        122.30                17.68         0.452 below_threshold              0.688             52.0                           0.534               -3.22             -0.206                                 ok           False                  False
  CSCO           66.67               15            2.02              1.58        111.45                22.50         0.449 below_threshold              0.136             19.3                           0.387               -0.05             -0.002                                 ok           False                  False
  ROST           85.37               41            0.15              0.24        230.64                29.12         0.444 below_threshold              0.655             89.1                           0.629                1.00             -0.001                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914094004)

</details>
