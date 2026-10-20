# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 14:10:09 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           96.00               25            0.51              0.12         34.41                30.22         0.559            pass              0.661             35.2                           0.266               10.13              1.300                                 ok            True                  False
  SNPS           70.59               17            1.58              5.03        452.42                54.29         0.588            pass              0.246             46.7                           0.614              -11.44             -1.362 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               24            1.34              2.48        262.13                59.49         0.579            pass              0.455             34.6                           0.394              -13.56             -1.460 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               10            2.17             10.70        700.85                40.24         0.525            pass              0.164             37.3                           0.311               -6.59             -0.397 downtrend_blocked_slope_and_streak           False                  False
  DRAM           80.56               36            0.37              0.13         48.28                49.05         0.493 below_threshold              0.511             91.3                           0.666              -19.10             -2.654 downtrend_blocked_slope_and_streak           False                  False
  DASH           89.36               47            0.01              0.01        193.52                49.82         0.489 below_threshold              0.797             99.4                           0.739               -0.06             -0.077                                 ok           False                  False
  CDNS           80.00               30            1.02              2.33        324.86                37.22         0.478 below_threshold              0.372             63.6                           0.614              -10.29             -1.260 downtrend_blocked_slope_and_streak           False                  False
  ALNY           81.08               37            0.84              1.37        232.70                43.08         0.472 below_threshold              0.377             40.4                           0.355                3.30              0.376                                 ok           False                  False
   LIN           77.27               22            0.73              2.55        502.35                13.47         0.471 below_threshold              0.265             46.0                           0.580                2.01              0.372                                 ok           False                  False
   WMT           88.89               36            0.34              0.28        118.58                25.19         0.467 below_threshold              0.588             43.7                           0.425               10.35              1.110                                 ok           False                  False
  MSFT           94.12               34            0.18              0.67        533.23                21.83         0.465 below_threshold              0.846             87.6                           0.597                0.62              0.089                                 ok           False                  False
 GOOGL           83.33               24            1.00              2.41        343.15                22.41         0.461 below_threshold              0.249              7.0                           0.236               -2.00             -0.245                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:40:09.833456-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:35:07.546342-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:30:04.347725-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:25:10.020404-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:20:08.949800-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:15:05.273794-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:10:09.912817-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:05:06.503440-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:00:06.812644-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020141009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020141009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020141009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020141009)

</details>
