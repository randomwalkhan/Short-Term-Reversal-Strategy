# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 10:30:05 EDT`
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

- Cash: `$50,178.10`
- Equity: `$50,178.10`
- Realized PnL: `$40,178.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-31)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00155000     29          2026-08-28         2026-08-31          9.0         8.1 -2610.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ABNB          100.00               14            1.91              2.53        188.35                62.79         0.686          pass              0.544             16.3                           0.352                3.64              0.299                  ok            True                  False
   TRI           93.94               33            0.67              0.50        106.01                60.45         0.597          pass              0.843             86.0                           0.857                7.21              0.453                  ok            True                   True
  AMGN          100.00               21            0.63              1.92        431.60                27.94         0.580          pass              0.703             57.3                           0.554                3.05              0.245                  ok            True                  False
  MELI          100.00               31            0.95             13.12       1960.63                48.83         0.578          pass              0.770             57.3                           0.772                8.95              0.846                  ok            True                  False
  PAYX          100.00               28            0.53              0.47        126.84                24.67         0.537          pass              0.738             54.9                           0.685                6.61              0.620                  ok            True                  False
  VRTX           96.55               29            0.99              3.74        540.09                33.03         0.535          pass              0.711             43.5                           0.376                4.03              0.281                  ok            True                  False
 CMCSA           94.12               17            1.42              0.27         26.94                25.33         0.530          pass              0.528             17.2                           0.327                4.32              0.353                  ok            True                  False
  UPRO           83.33               18            1.67              1.78        151.02                30.93         0.515          pass              0.219              8.3                           0.210               -3.34             -0.106                  ok            True                  False
   KDP           82.61               23            1.32              0.30         32.05                30.92         0.513          pass              0.290             27.4                           0.374                4.87              0.473                  ok            True                  False
   CSX           86.67               15            1.14              0.41         50.96                13.15         0.508          pass              0.262              0.0                           0.223               -0.05              0.145                  ok            True                  False
  NFLX           86.67               30            0.91              0.52         81.50                32.56         0.504          pass              0.454             30.8                           0.334                6.52              0.514                  ok            True                  False
  MNST           75.00                8            1.79              0.59         46.61               551.82         1.000          pass              0.116              5.3                           0.136                1.10             -0.003                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-31T10:30:05.230960-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.857, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "matched_signals": 33, "recovery_stability_score": 0.857, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:25:01.260797-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.841, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "matched_signals": 34, "recovery_stability_score": 0.841, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:20:06.273399-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                    {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:15:05.509244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:10:04.381634-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T10:05:01.432627-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "entry_ask": 24.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 21.65, "hypothetical_budget": 25089.05, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 39.0, "option_spread_pct": 30.02, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "matched_signals": 34, "recovery_stability_score": 0.675, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.777, "early_reclaim_pct": 76.3, "matched_signals": 30, "recovery_stability_score": 0.634, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.586, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:00:05.270470-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T09:50:01.420574-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-29T02:55:05.202083-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831103005)

</details>
