# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 10:20:06 EDT`
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

- Cash: `$65,704.80`
- Equity: `$127,084.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-1,650.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 61380.0         19.1           18.6       273.7        274.46          bid_ask_mid                       18.6                bid_ask_mid                    True         -1650.0                  -2.62         81.25               16              2.09         51.04           49.63                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           80.00               15            1.66              8.57        733.05                55.08         0.604            pass              0.114              6.7                           0.112               -0.49              0.075                                 ok            True                  False
    ZS           85.71               14            2.84              4.38        218.55                59.37         0.515            pass              0.329             32.9                           0.322                8.94              0.979                                 ok            True                  False
   APP           86.49               37            1.12              2.19        278.35                54.48         0.500            pass              0.468             21.7                           0.238                2.96             -0.159                                 ok            True                  False
  SNPS           76.92               13            2.06              6.76        465.21                53.97         0.588            pass              0.149             23.4                           0.312               -6.42             -0.617 downtrend_blocked_slope_and_streak           False                  False
  QCOM           84.00               25            1.49              1.86        177.60                54.84         0.545            pass              0.410             49.5                           0.541               -4.94             -0.419 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.24               17            1.16              0.89        109.47                35.07         0.543            pass              0.455             44.8                           0.529               -3.23             -0.380 downtrend_blocked_slope_and_streak           False                  False
  MPWR           78.26               23            1.61             14.06       1243.17                56.34         0.529            pass              0.296             52.2                           0.771              -14.63             -1.974            downtrend_blocked_slope           False                  False
   CEG           88.64               44            0.08              0.16        274.93                60.14         0.527            pass              0.767             94.6                           0.863                6.71              0.202                                 ok           False                  False
  CTSH           94.59               37            0.55              0.25         65.66                43.59         0.497 below_threshold              0.736             39.0                           0.247               11.79              1.319                                 ok           False                  False
  INTU           85.71               28            1.21              2.80        328.97                41.38         0.485 below_threshold              0.386             21.9                           0.222               16.58              1.494                                 ok           False                  False
  UPRO           88.89               36            0.23              0.25        151.41                28.58         0.482 below_threshold              0.633             58.3                           0.389                0.19             -0.139                                 ok           False                  False
  MELI           77.78               36            0.80             10.45       1852.50                40.67         0.478 below_threshold              0.257             12.1                           0.270                8.58              0.360                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T10:20:06.431756-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:15:05.691918-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:10:05.479242-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:05:01.369333-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:00:05.270363-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T00:00:05.052179-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-15T15:10:06.431411-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-15T15:05:05.112020-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-15T15:00:05.139552-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-15T14:55:07.089564-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016102006)

</details>
