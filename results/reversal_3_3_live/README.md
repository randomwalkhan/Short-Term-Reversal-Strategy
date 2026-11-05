# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 09:50:06 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSFT          100.00               14            1.52              5.91        553.27                33.48         0.566            pass              0.515             10.7                           0.171                5.04              0.274                                 ok            True                  False
  IDXX           95.00               40            0.45              2.21        697.60                74.33         0.651            pass              0.848             60.9                           0.366               22.70              2.487                                 ok           False                  False
  FTNT           60.00                5            4.61              4.18        127.60                91.87         0.607            pass              0.061              0.0                           0.150              -28.65             -4.631 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           88.89               36            0.42              0.84        288.57                52.55         0.575            pass              0.622             51.4                           0.293              -11.25             -1.641            downtrend_blocked_slope           False                  False
  INTC           50.00                4            7.34              2.99         56.99               128.90         0.565            pass              0.059              0.8                           0.039              -36.84             -5.791            downtrend_blocked_slope           False                  False
  GOOG           88.89               36            0.45              0.91        286.91                51.02         0.563            pass              0.597             43.5                           0.265              -10.84             -1.583            downtrend_blocked_slope           False                  False
   BKR           84.21               19            1.58              0.55         49.63                49.30         0.528            pass              0.264             13.1                           0.253               -8.47             -1.160 downtrend_blocked_slope_and_streak           False                  False
  ABNB           75.00                8            2.77              3.42        174.90                35.12         0.498 below_threshold              0.064              4.9                           0.220               -2.43             -0.072           downtrend_blocked_streak           False                  False
  INSM           66.67               24            2.25              1.73        109.26                61.82         0.492 below_threshold              0.208             21.9                           0.229               13.11              1.854                                 ok           False                  False
  NXPI           95.45               22            1.55              2.88        263.78                39.79         0.490 below_threshold              0.691             53.9                           0.566                9.72              1.097                                 ok           False                  False
   CEG           77.78                9            3.51              6.04        243.13                51.86         0.486 below_threshold              0.074              8.6                           0.251               -7.10             -0.329            downtrend_blocked_slope           False                  False
  META           61.54               13            2.52             11.11        625.24                38.86         0.484 below_threshold              0.084              5.3                           0.179               -5.35             -0.400 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105095006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105095006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105095006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105095006)

</details>
