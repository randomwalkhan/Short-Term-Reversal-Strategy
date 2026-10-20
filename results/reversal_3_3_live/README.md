# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 11:30:04 EDT`
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
  SNPS           72.22               18            1.49              4.75        452.55                54.29         0.589            pass              0.261             49.7                           0.341              -11.36             -1.358 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.24               34            0.74              1.35        262.61                59.49         0.556            pass              0.628             64.2                           0.451              -13.03             -1.432 downtrend_blocked_slope_and_streak           False                  False
  META           83.33               12            1.73              8.56        701.77                40.24         0.541            pass              0.306             49.9                           0.537               -6.18             -0.377 downtrend_blocked_slope_and_streak           False                  False
   LIN           70.00               10            1.20              4.21        501.63                13.47         0.508            pass              0.055              1.3                           0.076                1.52              0.350                                 ok           False                  False
  DASH           88.64               44            0.27              0.37        193.37                49.82         0.504            pass              0.481              0.0                           0.190               -0.32             -0.089                                 ok           False                  False
  DRAM           82.35               34            0.64              0.22         48.24                49.05         0.490 below_threshold              0.527             85.0                           0.552              -19.32             -2.666 downtrend_blocked_slope_and_streak           False                  False
  CDNS           80.77               26            1.25              2.85        324.64                37.22         0.489 below_threshold              0.342             55.5                           0.329              -10.50             -1.271 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.55               29            0.45              1.69        532.79                21.83         0.480 below_threshold              0.780             68.5                           0.611                0.34              0.077                                 ok           False                  False
  CSCO           91.67               36            0.23              0.17        106.42                35.33         0.473 below_threshold              0.769             79.2                           0.390               -9.91             -1.162 downtrend_blocked_slope_and_streak           False                  False
  NVDA           81.25               32            0.13              0.20        217.00                23.81         0.462 below_threshold              0.506             93.3                           0.454               -9.38             -1.093 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           85.71               28            0.70              1.68        343.46                22.41         0.460 below_threshold              0.392             24.5                           0.209               -1.70             -0.231                                 ok           False                  False
  AAPL           83.33               24            0.76              1.82        342.16                16.04         0.458 below_threshold              0.396             56.2                           0.379                2.01              0.216                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-20T11:30:04.347725-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:25:10.020404-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:20:08.949800-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:15:05.273794-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:10:09.912817-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:05:06.503440-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:00:06.812644-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:55:08.897321-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:50:04.954872-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "entry_ask": 2.85, "entry_bid": 2.55, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 268, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 11.11, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "matched_signals": 40, "recovery_stability_score": 0.604, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:45:05.488379-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020113004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020113004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020113004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020113004)

</details>
