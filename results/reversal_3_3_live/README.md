# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 11:35:05 EDT`
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
- Equity: `$123,124.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$-5,610.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 57420.0         19.1           17.4       273.7        273.26          bid_ask_mid                       17.4                bid_ask_mid                    True         -5610.0                   -8.9         81.25               16              2.09         51.04            47.5                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.11               36            0.63              1.22        274.48                60.14         0.540            pass              0.565             58.3                           0.386                6.12              0.177                                 ok            True                  False
  MSFT          100.00               11            1.61              6.08        536.84                21.00         0.513            pass              0.475              5.8                           0.177                2.56              0.313                                 ok            True                  False
  META           72.73               11            2.08             10.72        732.12                55.08         0.590            pass              0.104             12.7                           0.282               -0.92              0.056                                 ok           False                  False
  QCOM           87.50               32            0.78              0.98        177.98                54.84         0.550            pass              0.622             73.4                           0.732               -4.26             -0.387           downtrend_blocked_streak           False                  False
  CSCO           81.82               11            1.66              1.27        109.30                35.07         0.543            pass              0.173             21.2                           0.226               -3.72             -0.403 downtrend_blocked_slope_and_streak           False                  False
  MPWR           82.86               35            0.48              4.24       1247.38                56.34         0.528            pass              0.552             85.6                           0.801              -13.65             -1.923            downtrend_blocked_slope           False                  False
  SNPS           60.00                5            3.82             12.51        462.75                53.97         0.511            pass              0.082             10.3                           0.245               -8.10             -0.699 downtrend_blocked_slope_and_streak           False                  False
  DASH           87.18               39            0.67              0.90        192.66                48.67         0.499 below_threshold              0.529             31.3                           0.301                1.38             -0.023                                 ok           False                  False
  CDNS           77.78               18            1.95              4.43        322.48                38.31         0.491 below_threshold              0.153             17.0                           0.260               -9.48             -1.120 downtrend_blocked_slope_and_streak           False                  False
  CTSH           94.12               34            0.94              0.43         65.58                43.59         0.488 below_threshold              0.657             23.9                           0.282               11.35              1.300                                 ok           False                  False
  SHOP           84.38               32            1.18              1.47        177.51                48.01         0.484 below_threshold              0.409             32.3                           0.327               16.28              1.393                                 ok           False                  False
  UPRO           88.46               26            1.04              1.11        151.05                28.58         0.483 below_threshold              0.449             22.9                           0.247               -0.62             -0.176                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T11:35:05.403603-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:30:05.425810-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:25:04.296462-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:20:05.272593-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:15:05.298347-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:10:06.285080-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:05:05.360304-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:00:06.194646-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:55:05.447906-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:50:06.080905-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016113505)

</details>
