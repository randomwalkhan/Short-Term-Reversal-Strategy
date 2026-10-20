# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 14:15:06 EDT`
Last processed slot: `manual`

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
  SNPS           70.59               17            1.61              5.13        452.38                54.29         0.586            pass              0.242             45.6                           0.488              -11.47             -1.364 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               24            1.42              2.61        262.07                59.49         0.574            pass              0.444             31.1                           0.361              -13.63             -1.463 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.00               25            0.48              0.12         34.41                30.22         0.561            pass              0.673             38.9                           0.243               10.17              1.301                                 ok           False                  False
  META           80.00               10            2.17             10.70        700.86                40.24         0.525            pass              0.165             37.4                           0.310               -6.59             -0.397 downtrend_blocked_slope_and_streak           False                  False
  DRAM           80.56               36            0.35              0.12         48.28                49.05         0.495 below_threshold              0.513             91.8                           0.676              -19.09             -2.653 downtrend_blocked_slope_and_streak           False                  False
  CDNS           80.00               30            1.07              2.45        324.81                37.22         0.475 below_threshold              0.366             61.8                           0.573              -10.34             -1.262 downtrend_blocked_slope_and_streak           False                  False
   LIN           77.27               22            0.72              2.54        502.35                13.47         0.471 below_threshold              0.266             46.2                           0.584                2.01              0.372                                 ok           False                  False
  ALNY           81.08               37            0.87              1.43        232.68                43.08         0.470 below_threshold              0.369             37.8                           0.314                3.26              0.375                                 ok           False                  False
  MSFT           94.12               34            0.15              0.55        533.28                21.83         0.467 below_threshold              0.852             89.7                           0.607                0.65              0.091                                 ok           False                  False
 GOOGL           83.33               24            0.97              2.35        343.17                22.41         0.463 below_threshold              0.258              9.7                           0.245               -1.97             -0.243                                 ok           False                  False
   WMT           89.47               38            0.29              0.25        118.59                25.19         0.458 below_threshold              0.637             50.7                           0.492               10.40              1.112                                 ok           False                  False
  AAPL           83.33               24            0.79              1.90        342.13                16.04         0.456 below_threshold              0.391             54.3                           0.396                1.98              0.214                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020141506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020141506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020141506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020141506)

</details>
