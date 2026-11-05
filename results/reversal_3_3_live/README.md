# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 10:00:05 EST`
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
  IDXX           94.44               36            0.77              3.74        696.95                74.33         0.655            pass              0.725             33.8                           0.218               22.31              2.472                                 ok            True                  False
  MSFT          100.00               11            1.94              7.55        552.57                33.48         0.553            pass              0.508             15.5                           0.201                4.59              0.254                                 ok            True                  False
  DXCM           86.11               36            0.77              0.48         88.27                45.01         0.507            pass              0.387              0.0                           0.183               12.10              1.309                                 ok            True                  False
  FTNT           55.56                9            3.67              3.33        127.96                91.87         0.635            pass              0.130             22.1                           0.245              -27.95             -4.587 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           87.10               31            0.61              1.24        288.40                52.55         0.590            pass              0.483             31.7                           0.277              -11.43             -1.650            downtrend_blocked_slope           False                  False
  GOOG           86.67               30            0.69              1.39        286.70                51.02         0.580            pass              0.454             28.4                           0.256              -11.05             -1.594            downtrend_blocked_slope           False                  False
  INTC           50.00                4            7.77              3.17         56.91               128.90         0.525            pass              0.089             12.3                           0.186              -37.13             -5.812            downtrend_blocked_slope           False                  False
   BKR           81.25               16            1.84              0.64         49.59                49.30         0.524            pass              0.171             15.2                           0.217               -8.71             -1.172 downtrend_blocked_slope_and_streak           False                  False
  ISRG           95.00               40            0.32              1.07        481.64                40.52         0.506            pass              0.849             66.0                           0.431                8.27              0.465                                 ok           False                  False
  AMZN           76.67               30            1.06              1.97        265.18                42.79         0.502            pass              0.250             22.1                           0.225                5.12              0.393                                 ok           False                  False
   KHC           92.11               38            0.24              0.04         25.42                36.26         0.499 below_threshold              0.769             70.0                           0.423                1.16              0.204                                 ok           False                  False
  INSM           65.22               23            2.30              1.77        109.24                61.82         0.494 below_threshold              0.198             20.6                           0.220               13.05              1.851                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-05T10:00:05.848004-05:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105100005)

</details>
