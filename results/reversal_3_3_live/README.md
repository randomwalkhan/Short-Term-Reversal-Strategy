# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 10:15:05 EDT`
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

- Cash: `$65,704.80`
- Equity: `$124,939.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-3,795.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 59235.0         19.1          17.95       273.7         275.0          bid_ask_mid                      17.95                bid_ask_mid                    True         -3795.0                  -6.02         81.25               16              2.09         51.04           48.49                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           85.71               35            1.26              2.47        278.23                54.48         0.502            pass              0.404             11.5                           0.233                2.81             -0.166                                 ok            True                  False
  META           78.57               14            1.78              9.18        732.78                55.08         0.602            pass              0.087              0.0                           0.170               -0.62              0.070                                 ok           False                  False
  SNPS           78.57               14            2.00              6.55        465.30                53.97         0.587            pass              0.162             25.7                           0.278               -6.36             -0.614 downtrend_blocked_slope_and_streak           False                  False
  PAYX           78.95               38            0.23              0.18        110.70                41.26         0.550            pass              0.264              7.4                           0.127               11.71              1.159                                 ok           False                  False
  CSCO           87.50               16            1.24              0.95        109.44                35.07         0.543            pass              0.418             41.1                           0.437               -3.31             -0.384 downtrend_blocked_slope_and_streak           False                  False
  MPWR           78.26               23            1.64             14.35       1243.05                56.34         0.528            pass              0.293             51.2                           0.698              -14.66             -1.976            downtrend_blocked_slope           False                  False
  QCOM           84.00               25            1.81              2.26        177.43                54.84         0.527            pass              0.376             38.8                           0.387               -5.24             -0.434 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.64               44            0.11              0.20        274.91                60.14         0.526            pass              0.762             93.1                           0.839                6.69              0.201                                 ok           False                  False
  DASH           88.64               44            0.19              0.26        192.94                48.67         0.507            pass              0.559             26.0                           0.330                1.87             -0.001                                 ok           False                  False
    ZS           83.33               12            3.30              5.10        218.25                59.37         0.499 below_threshold              0.218             21.8                           0.225                8.42              0.957                                 ok           False                  False
  SHOP           85.71               42            0.20              0.25        178.03                48.01         0.493 below_threshold              0.626             74.9                           0.402               17.43              1.438                                 ok           False                  False
  CTSH           94.44               36            0.78              0.36         65.62                43.59         0.490 below_threshold              0.644             12.1                           0.188               11.54              1.308                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-16T10:15:05.691918-04:00 early_entry_1015 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:10:05.479242-04:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:05:01.369333-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:00:05.270363-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T00:00:05.052179-04:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-10-15T15:10:06.431411-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-15T15:05:05.112020-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-15T15:00:05.139552-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-15T14:55:07.089564-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-15T14:50:07.219015-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-15", "training_samples": 6074, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016101505)

</details>
