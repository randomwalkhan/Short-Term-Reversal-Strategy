# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 10:40:05 EDT`
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
- Equity: `$127,579.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-1,155.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 61875.0         19.1          18.75       273.7        275.48          bid_ask_mid                      18.75                bid_ask_mid                    True         -1155.0                  -1.83         81.25               16              2.09         51.04           48.62                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           72.73               11            2.00             10.31        732.30                55.08         0.596            pass              0.104             12.5                           0.191               -0.84              0.060                                 ok           False                  False
  SNPS           71.43                7            2.69              8.81        464.33                53.97         0.580            pass              0.101             14.4                           0.223               -7.02             -0.646 downtrend_blocked_slope_and_streak           False                  False
  QCOM           88.57               35            0.50              0.62        178.13                54.84         0.551            pass              0.700             83.2                           0.894               -3.98             -0.374           downtrend_blocked_streak           False                  False
  PAYX           77.78               36            0.39              0.30        110.65                41.26         0.549            pass              0.254              8.5                           0.075               11.53              1.152                                 ok           False                  False
  CSCO           91.30               23            0.81              0.63        109.58                35.07         0.530            pass              0.625             61.3                           0.732               -2.89             -0.364 downtrend_blocked_slope_and_streak           False                  False
  MPWR           82.86               35            0.51              4.45       1247.29                56.34         0.527            pass              0.550             84.9                           0.912              -13.67             -1.924            downtrend_blocked_slope           False                  False
   APP           86.11               36            1.23              2.40        278.26                54.48         0.499 below_threshold              0.428             14.0                           0.213                2.85             -0.164                                 ok           False                  False
  SHOP           83.33               36            0.67              0.83        177.78                48.01         0.497 below_threshold              0.408             32.1                           0.267               16.89              1.417                                 ok           False                  False
  CTSH           94.59               37            0.68              0.32         65.63                43.59         0.485 below_threshold              0.752             44.8                           0.333               11.64              1.312                                 ok           False                  False
  UPRO           86.49               37            0.05              0.05        151.50                28.58         0.485 below_threshold              0.676             91.7                           0.591                0.38             -0.130                                 ok           False                  False
  MSFT           96.15               26            0.68              2.56        538.34                21.00         0.483 below_threshold              0.655             33.2                           0.345                3.53              0.356                                 ok           False                  False
  INTC           87.10               31            1.99              1.33         94.80                62.72         0.482 below_threshold              0.504             42.1                           0.598              -21.67             -2.425            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T10:40:05.484912-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:30:04.273613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:25:03.664701-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:20:06.431756-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:15:05.691918-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:10:05.479242-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:05:01.369333-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:00:05.270363-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T00:00:05.052179-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016104005)

</details>
