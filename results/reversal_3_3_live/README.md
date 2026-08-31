# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 11:05:01 EDT`
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
  MNST           81.82               11            1.56              0.51         46.64               551.82         1.000          pass              0.221             21.8                           0.475                1.34              0.008                      ok            True                  False
  ABNB          100.00               10            2.45              3.26        188.03                62.79         0.678          pass              0.470              0.9                           0.076                3.06              0.274                      ok            True                  False
   TRI           94.12               34            0.58              0.43        106.04                60.45         0.597          pass              0.860             87.9                           0.760                7.31              0.458                      ok            True                   True
  MELI          100.00               30            1.07             14.69       1959.95                48.83         0.577          pass              0.747             52.2                           0.578                8.82              0.840                      ok            True                  False
  SBUX           95.00               20            0.73              0.55        107.61                22.68         0.539          pass              0.681             53.6                           0.709               -0.79              0.151                      ok            True                  False
  VRTX           96.77               31            0.77              2.92        540.44                33.03         0.536          pass              0.761             55.9                           0.685                4.26              0.290                      ok            True                  False
   KDP           84.00               25            0.93              0.21         32.09                30.92         0.526          pass              0.405             48.7                           0.659                5.28              0.491                      ok            True                  False
 CMCSA           90.91               22            0.94              0.18         26.98                25.33         0.521          pass              0.558             45.2                           0.675                4.83              0.375                      ok            True                  False
  BKNG           94.44               18            2.06              2.96        204.36                35.32         0.519          pass              0.569             26.1                           0.388               -1.64             -0.249                      ok            True                  False
  WDAY           86.96               23            3.15              4.51        202.79                72.83         0.511          pass              0.369             15.4                           0.388                3.71              0.270                      ok            True                  False
   WDC           76.67               30            1.65              5.32        457.17                84.45         0.614          pass              0.292             32.3                           0.311              -15.70             -1.074 downtrend_blocked_slope           False                  False
   STX           85.29               34            0.70              4.05        828.03                71.38         0.610          pass              0.581             72.8                           0.601              -17.17             -1.158 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-31T11:05:01.440197-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.9, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.9, "matched_signals": 34, "recovery_stability_score": 0.76, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T11:00:05.262610-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 88.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 88.0, "matched_signals": 34, "recovery_stability_score": 0.758, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.781, "early_reclaim_pct": 60.3, "matched_signals": 32, "recovery_stability_score": 0.678, "success_rate": 96.88, "ticker": "VRTX", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:55:05.440022-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.65, "early_entry_score": 0.855, "early_reclaim_pct": 86.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.855, "early_reclaim_pct": 86.4, "matched_signals": 34, "recovery_stability_score": 0.788, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:50:05.679459-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.813, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "matched_signals": 34, "recovery_stability_score": 0.813, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:45:06.342022-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.822, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.861, "early_reclaim_pct": 88.1, "matched_signals": 34, "recovery_stability_score": 0.822, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:40:01.468771-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.856, "early_reclaim_pct": 86.7, "matched_signals": 34, "recovery_stability_score": 0.823, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:35:05.984137-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.786, "early_reclaim_pct": 79.1, "matched_signals": 30, "recovery_stability_score": 0.81, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:30:05.230960-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.857, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.843, "early_reclaim_pct": 86.0, "matched_signals": 33, "recovery_stability_score": 0.857, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.597, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:25:01.260797-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.841, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "matched_signals": 34, "recovery_stability_score": 0.841, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:20:06.273399-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831110501)

</details>
