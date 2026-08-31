# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 10:45:06 EDT`
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
  MNST           80.00               10            1.58              0.52         46.64               551.82         1.000          pass              0.163             20.9                           0.329                1.32              0.007                  ok            True                  False
  ABNB          100.00               13            2.05              2.72        188.27                62.79         0.684          pass              0.519             10.2                           0.297                3.49              0.293                  ok            True                  False
   TRI           94.12               34            0.57              0.42        106.04                60.45         0.598          pass              0.861             88.1                           0.822                7.32              0.458                  ok            True                   True
  MELI          100.00               30            1.08             14.84       1959.89                48.83         0.576          pass              0.746             51.7                           0.683                8.81              0.840                  ok            True                  False
  SBUX           92.31               13            1.16              0.88        107.47                22.68         0.554          pass              0.482             26.0                           0.317               -1.22              0.131                  ok            True                  False
  VRTX           96.55               29            0.88              3.35        540.26                33.03         0.541          pass              0.729             49.5                           0.504                4.14              0.285                  ok            True                  False
  CHTR           88.89               27            1.87              2.02        152.76                53.40         0.528          pass              0.431              9.4                           0.189                4.61              0.360                  ok            True                  False
   KDP           84.00               25            0.93              0.21         32.09                30.92         0.526          pass              0.405             48.7                           0.633                5.28              0.491                  ok            True                  False
  BKNG           94.44               18            2.02              2.91        204.38                35.32         0.521          pass              0.573             27.5                           0.530               -1.60             -0.247                  ok            True                  False
  CTAS           84.21               19            0.94              1.34        203.60                14.76         0.518          pass              0.274             16.7                           0.256                2.24              0.225                  ok            True                  False
 CMCSA           89.47               19            1.33              0.25         26.95                25.33         0.515          pass              0.432             22.6                           0.339                4.42              0.357                  ok            True                  False
  NFLX           86.67               30            0.97              0.55         81.48                32.56         0.501          pass              0.440             26.2                           0.248                6.46              0.511                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-31T10:45:06.342022-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.822, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "matched_signals": 34, "recovery_stability_score": 0.822, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:40:01.468771-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "matched_signals": 34, "recovery_stability_score": 0.823, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:35:05.984137-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "matched_signals": 30, "recovery_stability_score": 0.81, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:30:05.230960-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.857, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "matched_signals": 33, "recovery_stability_score": 0.857, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:25:01.260797-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.841, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "matched_signals": 34, "recovery_stability_score": 0.841, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:20:06.273399-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                    {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:15:05.509244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:10:04.381634-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T10:05:01.432627-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "entry_ask": 24.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 21.65, "hypothetical_budget": 25089.05, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 39.0, "option_spread_pct": 30.02, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "matched_signals": 34, "recovery_stability_score": 0.675, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.777, "early_reclaim_pct": 76.3, "matched_signals": 30, "recovery_stability_score": 0.634, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.586, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:00:05.270470-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831104506)

</details>
