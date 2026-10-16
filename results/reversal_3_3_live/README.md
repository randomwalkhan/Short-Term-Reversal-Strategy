# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 11:20:05 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$126,094.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-2,640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 60390.0         19.1           18.3       273.7        272.49          bid_ask_mid                       18.3                bid_ask_mid                    True         -2640.0                  -4.19         81.25               16              2.09         51.04           50.35                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           90.00               30            0.94              1.81        274.22                60.14         0.561            pass              0.571             38.2                           0.212                5.80              0.163                                 ok            True                  False
  MSFT          100.00               15            1.39              5.24        537.20                21.00         0.503            pass              0.507              7.7                           0.111                2.79              0.323                                 ok            True                  False
  META           72.73               11            2.17             11.18        731.93                55.08         0.586            pass              0.089              8.0                           0.207               -1.01              0.052                                 ok           False                  False
  QCOM           84.00               25            1.34              1.67        177.68                54.84         0.555            pass              0.426             54.6                           0.481               -4.79             -0.412 downtrend_blocked_slope_and_streak           False                  False
  CSCO           83.33               12            1.61              1.24        109.32                35.07         0.542            pass              0.227             23.4                           0.178               -3.67             -0.401 downtrend_blocked_slope_and_streak           False                  False
  MPWR           81.25               32            0.73              6.40       1246.46                56.34         0.530            pass              0.468             78.2                           0.605              -13.87             -1.934            downtrend_blocked_slope           False                  False
  PAYX           81.40               43            0.09              0.07        110.75                41.26         0.529            pass              0.526             78.7                           0.561               11.87              1.165                                 ok           False                  False
  SNPS           60.00                5            4.02             13.18        462.46                53.97         0.500 below_threshold              0.066              5.5                           0.114               -8.29             -0.709 downtrend_blocked_slope_and_streak           False                  False
  SHOP           86.21               29            1.38              1.72        177.40                48.01         0.493 below_threshold              0.404             21.0                           0.170               16.05              1.384                                 ok           False                  False
  DASH           88.37               43            0.46              0.63        192.78                48.67         0.488 below_threshold              0.629             52.4                           0.349                1.59             -0.014                                 ok           False                  False
  CDNS           77.78               18            2.04              4.63        322.40                38.31         0.486 below_threshold              0.141             13.2                           0.209               -9.56             -1.124 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.89               27            0.97              1.03        151.08                28.58         0.485 below_threshold              0.413              4.5                           0.134               -0.55             -0.173                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T11:20:05.272593-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:15:05.298347-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:10:06.285080-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:05:05.360304-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:00:06.194646-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:55:05.447906-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:50:06.080905-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:45:05.613636-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:40:05.484912-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016112005)

</details>
