# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 10:35:02 EDT`
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
- Equity: `$129,889.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$1,155.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 64185.0         19.1          19.45       273.7        275.78          bid_ask_mid                      19.45                bid_ask_mid                    True          1155.0                   1.83         81.25               16              2.09         51.04           49.66                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           86.49               37            1.11              2.18        278.36                54.48         0.500            pass              0.469             22.1                           0.258                2.97             -0.159                                 ok            True                  False
  META           72.73               11            2.03             10.46        732.24                55.08         0.594            pass              0.099             11.1                           0.188               -0.87              0.058                                 ok           False                  False
  SNPS           66.67                6            2.84              9.30        464.12                53.97         0.573            pass              0.086              9.6                           0.230               -7.16             -0.653 downtrend_blocked_slope_and_streak           False                  False
  QCOM           87.50               32            0.79              0.99        177.98                54.84         0.550            pass              0.621             73.1                           0.828               -4.27             -0.387           downtrend_blocked_streak           False                  False
  PAYX           77.78               36            0.39              0.30        110.65                41.26         0.549            pass              0.254              8.5                           0.181               11.53              1.152                                 ok           False                  False
  CSCO           88.24               17            1.16              0.89        109.47                35.07         0.543            pass              0.456             45.0                           0.535               -3.23             -0.380 downtrend_blocked_slope_and_streak           False                  False
  MPWR           81.82               33            0.65              5.65       1246.78                56.34         0.529            pass              0.497             80.8                           0.892              -13.79             -1.930            downtrend_blocked_slope           False                  False
  CTSH           94.29               35            0.85              0.39         65.60                43.59         0.487 below_threshold              0.690             31.3                           0.246               11.45              1.305                                 ok           False                  False
  SHOP           84.62               39            0.56              0.70        177.84                48.01         0.487 below_threshold              0.493             42.7                           0.347               17.01              1.422                                 ok           False                  False
  UPRO           88.89               36            0.24              0.25        151.41                28.58         0.481 below_threshold              0.630             57.1                           0.421                0.19             -0.139                                 ok           False                  False
  MSFT           96.00               25            0.81              3.08        538.12                21.00         0.481 below_threshold              0.607             19.7                           0.297                3.38              0.349                                 ok           False                  False
  INTC           85.71               28            2.35              1.57         94.70                62.72         0.478 below_threshold              0.415             31.7                           0.378              -21.96             -2.442            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:30:04.273613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:25:03.664701-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:20:06.431756-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:15:05.691918-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:10:05.479242-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:05:01.369333-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:00:05.270363-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T00:00:05.052179-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-15T15:10:06.431411-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016103502)

</details>
