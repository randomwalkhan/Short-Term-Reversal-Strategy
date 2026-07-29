# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               14            1.05              0.35         47.95                27.18         0.584          pass              0.619             44.5                           0.589                4.63              0.466                                 ok            True                  False
  GILD           88.46               26            0.72              0.68        134.03                34.28         0.519          pass              0.516             43.9                           0.451                2.55             -0.026                                 ok            True                  False
   MAR          100.00               29            0.79              2.12        382.61                28.18         0.515          pass              0.759             60.3                           0.480                4.76              0.404                                 ok            True                  False
   HON           80.00               15            1.66              2.87        245.82                39.75         0.513          pass              0.123             12.8                           0.242                9.10              1.146                                 ok            True                  False
  ISRG           78.57               28            1.12              2.84        360.58                72.57         0.633          pass              0.345             53.9                           0.582               -8.03             -0.874                                 ok           False                  False
   WDC           83.87               31            0.61              1.99        462.66                95.99         0.580          pass              0.574             91.0                           0.495              -10.35             -0.148           downtrend_blocked_streak           False                  False
  META           91.89               37            0.66              2.74        592.24                53.87         0.575          pass              0.687             44.2                           0.450              -13.48             -1.520 downtrend_blocked_slope_and_streak           False                  False
  TMUS           92.68               41            0.05              0.07        182.36                56.22         0.558          pass              0.881             95.7                           0.775               -2.84             -0.848            downtrend_blocked_slope           False                  False
   XEL          100.00               25            0.34              0.19         80.25                19.80         0.550          pass              0.655             33.3                           0.232               -0.14              0.131                                 ok           False                  False
  BKNG           95.24               42            0.15              0.21        199.22                45.62         0.539          pass              0.935             93.8                           0.604               13.81              0.782                                 ok           False                  False
  MSTR           75.00               40            0.88              0.60         95.90                69.55         0.536          pass              0.317             21.3                           0.222               -2.22             -0.079                                 ok           False                  False
  CDNS           75.00               20            2.03              4.90        342.62                47.22         0.504          pass              0.137              6.8                           0.172               -9.09             -0.611            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-29T10:45:02.234081-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:40:06.811413-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "entry_ask": 20.1, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 19.25, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 8.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.659, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:35:06.000891-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                          {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "entry_ask": 20.1, "entry_bid": 18.7, "entry_mode": "early", "entry_option_price": 19.4, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 7.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.647, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "matched_signals": 30, "recovery_stability_score": 0.647, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:30:04.319629-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "entry_ask": 20.1, "entry_bid": 17.9, "entry_mode": "early", "entry_option_price": 19.0, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 11.58, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "matched_signals": 31, "recovery_stability_score": 0.642, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:25:04.635109-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "entry_ask": 20.1, "entry_bid": 17.5, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 13.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.655, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:20:02.632182-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "entry_ask": 20.3, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1134.0, "option_spread_pct": 15.96, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "matched_signals": 32, "recovery_stability_score": 0.586, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.712, "early_reclaim_pct": 74.0, "matched_signals": 33, "recovery_stability_score": 0.574, "success_rate": 90.91, "ticker": "PCAR", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:15:01.489767-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:10:01.513835-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:05:02.493653-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729104502)

</details>
