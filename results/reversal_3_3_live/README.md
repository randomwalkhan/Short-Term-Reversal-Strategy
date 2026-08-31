# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 11:00:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           85.71               14            1.41              0.46         46.66               551.82         1.000          pass              0.367             29.4                           0.621                1.49              0.015                      ok            True                  False
  ABNB          100.00               11            2.26              3.00        188.14                62.79         0.684          pass              0.477              0.7                           0.110                3.26              0.283                      ok            True                  False
   TRI           94.12               34            0.57              0.43        106.04                60.45         0.597          pass              0.860             88.0                           0.758                7.31              0.458                      ok            True                   True
  MELI          100.00               31            0.99             13.66       1960.39                48.83         0.575          pass              0.764             55.5                           0.604                8.90              0.844                      ok            True                  False
  SHOP           92.31               13            3.58              3.84        151.26                66.63         0.564          pass              0.500             31.7                           0.654               -0.83              0.322                      ok            True                  False
  SBUX           95.00               20            0.70              0.53        107.62                22.68         0.541          pass              0.688             55.6                           0.697               -0.76              0.152                      ok            True                  False
  VRTX           96.88               32            0.69              2.63        540.56                33.03         0.534          pass              0.781             60.3                           0.678                4.34              0.294                      ok            True                   True
 CMCSA           90.48               21            1.00              0.19         26.98                25.33         0.523          pass              0.531             41.9                           0.628                4.77              0.372                      ok            True                  False
   KDP           84.62               26            0.89              0.20         32.09                30.92         0.523          pass              0.436             51.3                           0.699                5.33              0.493                      ok            True                  False
  BKNG           95.00               20            1.93              2.78        204.44                35.32         0.515          pass              0.610             30.7                           0.537               -1.51             -0.243                      ok            True                  False
  WDAY           83.33               24            2.90              4.16        202.94                72.83         0.514          pass              0.300             22.1                           0.407                3.98              0.281                      ok            True                  False
   WDC           76.67               30            1.62              5.20        457.22                84.45         0.616          pass              0.297             33.9                           0.379              -15.67             -1.073 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-31T11:00:05.262610-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 88.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 88.0, "matched_signals": 34, "recovery_stability_score": 0.758, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.781, "early_reclaim_pct": 60.3, "matched_signals": 32, "recovery_stability_score": 0.678, "success_rate": 96.88, "ticker": "VRTX", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:55:05.440022-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.65, "early_entry_score": 0.855, "early_reclaim_pct": 86.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.855, "early_reclaim_pct": 86.4, "matched_signals": 34, "recovery_stability_score": 0.788, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:50:05.679459-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.813, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "matched_signals": 34, "recovery_stability_score": 0.813, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:45:06.342022-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.822, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "matched_signals": 34, "recovery_stability_score": 0.822, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:40:01.468771-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "matched_signals": 34, "recovery_stability_score": 0.823, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:35:05.984137-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "matched_signals": 30, "recovery_stability_score": 0.81, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:30:05.230960-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.857, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "matched_signals": 33, "recovery_stability_score": 0.857, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:25:01.260797-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.841, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "matched_signals": 34, "recovery_stability_score": 0.841, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:20:06.273399-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:15:05.509244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831110005)

</details>
