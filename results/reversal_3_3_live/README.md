# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 11:00:06 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$127,744.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-990.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 62040.0         19.1           18.8       273.7        273.71          bid_ask_mid                       18.8                bid_ask_mid                    True          -990.0                  -1.57         81.25               16              2.09         51.04           50.61                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           75.00               12            1.90              9.81        732.52                55.08         0.598            pass              0.123             16.7                           0.323               -0.74              0.064                                 ok           False                  False
  SNPS           66.67                6            2.71              8.87        464.31                53.97         0.580            pass              0.099             13.8                           0.323               -7.03             -0.647 downtrend_blocked_slope_and_streak           False                  False
  QCOM           85.71               28            1.15              1.44        177.78                54.84         0.550            pass              0.510             61.0                           0.647               -4.61             -0.404 downtrend_blocked_slope_and_streak           False                  False
  CSCO           87.50               16            1.22              0.94        109.45                35.07         0.544            pass              0.420             42.0                           0.444               -3.29             -0.383 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.84               38            0.45              0.88        274.62                60.14         0.539            pass              0.633             70.1                           0.434                6.31              0.185                                 ok           False                  False
  PAYX           80.95               42            0.17              0.13        110.72                41.26         0.530            pass              0.457             59.6                           0.454               11.77              1.162                                 ok           False                  False
  MPWR           82.86               35            0.47              4.07       1247.45                56.34         0.529            pass              0.554             86.1                           0.814              -13.64             -1.922            downtrend_blocked_slope           False                  False
  DASH           88.37               43            0.43              0.58        192.80                48.67         0.496 below_threshold              0.476              1.2                           0.098                1.62             -0.012                                 ok           False                  False
  INTU           85.71               21            1.72              3.97        328.47                41.38         0.489 below_threshold              0.357             27.4                           0.359               15.99              1.471                                 ok           False                  False
   APP           84.85               33            1.62              3.17        277.93                54.48         0.489 below_threshold              0.343              3.8                           0.224                2.44             -0.182                                 ok           False                  False
  CTSH           93.94               33            1.03              0.48         65.57                43.59         0.488 below_threshold              0.624             16.6                           0.267               11.25              1.296                                 ok           False                  False
  MSFT           95.65               23            0.88              3.32        538.02                21.00         0.488 below_threshold              0.575             13.2                           0.246                3.32              0.346                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T11:00:06.194646-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:55:05.447906-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:50:06.080905-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:45:05.613636-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:40:05.484912-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:30:04.273613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:25:03.664701-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:20:06.431756-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:15:05.691918-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016110006)

</details>
