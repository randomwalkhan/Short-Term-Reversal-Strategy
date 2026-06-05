# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 11:00:03 EDT`
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

- Cash: `$33,370.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  WDAY           86.67               30            1.71              1.77        147.15                69.97         0.559          pass              0.441             24.7                           0.357               13.45              1.939                      ok            True                  False
  TEAM           96.30               27            2.75              1.95        100.66                86.36         0.549          pass              0.633             21.6                           0.359               15.56              1.847                      ok            True                  False
  PANW           91.67               36            0.71              1.38        278.66                60.15         0.548          pass              0.758             72.8                           0.619                9.63              1.351                      ok            True                   True
  CTSH           93.55               31            0.71              0.27         53.29                51.38         0.541          pass              0.763             69.1                           0.366                0.51              0.166                      ok            True                  False
  CRWD           81.82               11            3.29             16.54        712.00                64.90         0.521          pass              0.210             34.3                           0.508                7.29              1.201                      ok            True                  False
    ZS           80.00               30            1.36              1.29        134.71               157.69         0.881          pass              0.306             28.2                           0.340              -26.84             -2.266 downtrend_blocked_slope           False                  False
   TRI           86.67               30            0.20              0.12         85.69                69.04         0.666          pass              0.601             74.4                           0.408               -0.34              0.212                      ok           False                  False
  CSCO          100.00                1            3.51              3.19        128.63                55.20         0.587          pass              0.502             14.4                           0.388                4.18              0.805                      ok           False                  False
   ADI          100.00                9            2.58              7.76        425.44                45.54         0.549          pass              0.556             33.6                           0.553                5.48              0.405                      ok           False                  False
  QCOM           80.00                5            5.10              8.67        238.86                97.97         0.548          pass              0.129             24.8                           0.332               -2.99             -0.255 downtrend_blocked_slope           False                  False
    MU           76.92               13            4.98             34.74        981.11               105.49         0.544          pass              0.192             39.3                           0.669               26.01              1.824                      ok           False                  False
   CEG           78.26               23            2.19              4.06        262.85                55.63         0.518          pass              0.206             22.7                           0.334               -9.46             -1.390 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-05T11:00:03.928468-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                            {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "entry_ask": 17.8, "entry_bid": 17.0, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 4.6, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "matched_signals": 36, "recovery_stability_score": 0.619, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:55:02.043885-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:50:04.031385-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:45:02.885647-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:40:02.027944-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                         {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "entry_ask": 18.2, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.475, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 8.3, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "matched_signals": 36, "recovery_stability_score": 0.738, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:35:05.997480-04:00 early_entry_1035 early_entry_shadow           {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "entry_ask": 11.75, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.25, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 157.0, "option_spread_pct": 8.89, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.584, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.776, "early_reclaim_pct": 74.8, "matched_signals": 37, "recovery_stability_score": 0.742, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:30:06.002783-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "entry_ask": 12.6, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 11.65, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 16.31, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "matched_signals": 41, "recovery_stability_score": 0.644, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "trend_health_status": "ok"}, {"current_drop_pct": 0.98, "early_entry_score": 0.724, "early_reclaim_pct": 62.3, "matched_signals": 36, "recovery_stability_score": 0.677, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:25:06.279311-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:20:03.989401-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "matched_signals": 41, "recovery_stability_score": 0.706, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:15:05.401344-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "matched_signals": 41, "recovery_stability_score": 0.587, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605110003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605110003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605110003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605110003)

</details>
