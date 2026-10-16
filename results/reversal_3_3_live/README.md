# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 11:10:06 EDT`
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
- Equity: `$126,919.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-1,815.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 61215.0         19.1          18.55       273.7        272.63          bid_ask_mid                      18.55                bid_ask_mid                    True         -1815.0                  -2.88         81.25               16              2.09         51.04           50.38                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.57               35            0.71              1.38        274.41                60.14         0.543            pass              0.609             53.0                           0.295                6.04              0.174                                 ok            True                  False
  SHOP           80.95               21            1.67              2.08        177.25                48.01         0.520            pass              0.151              0.0                           0.223               15.71              1.371                                 ok            True                  False
  META           72.73               11            2.14             11.05        731.98                55.08         0.588            pass              0.084              6.1                           0.181               -0.98              0.053                                 ok           False                  False
  QCOM           84.00               25            1.54              1.93        177.57                54.84         0.542            pass              0.404             47.8                           0.376               -4.99             -0.422 downtrend_blocked_slope_and_streak           False                  False
  CSCO           83.33               12            1.60              1.23        109.32                35.07         0.542            pass              0.229             24.0                           0.248               -3.66             -0.400 downtrend_blocked_slope_and_streak           False                  False
  MPWR           79.17               24            1.52             13.26       1243.52                56.34         0.530            pass              0.311             54.9                           0.526              -14.55             -1.970            downtrend_blocked_slope           False                  False
  SNPS           60.00                5            4.02             13.18        462.46                53.97         0.502            pass              0.050              0.0                           0.223               -8.29             -0.709 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00               17            1.33              5.01        537.29                21.00         0.497 below_threshold              0.503              2.3                           0.227                2.85              0.326                                 ok           False                  False
  CDNS           77.78               18            1.94              4.41        322.49                38.31         0.496 below_threshold              0.103              0.0                           0.223               -9.47             -1.120 downtrend_blocked_slope_and_streak           False                  False
  DASH           87.18               39            0.77              1.04        192.60                48.67         0.492 below_threshold              0.496             20.7                           0.185                1.27             -0.028                                 ok           False                  False
  CTSH           93.94               33            1.03              0.48         65.57                43.59         0.488 below_threshold              0.624             16.6                           0.213               11.25              1.296                                 ok           False                  False
  UPRO           88.89               27            0.96              1.02        151.08                28.58         0.486 below_threshold              0.399              0.0                           0.237               -0.54             -0.172                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T11:10:06.285080-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:05:05.360304-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:00:06.194646-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:55:05.447906-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:50:06.080905-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:45:05.613636-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:40:05.484912-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:30:04.273613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:25:03.664701-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016111006)

</details>
