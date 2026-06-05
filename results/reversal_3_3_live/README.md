# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 10:50:04 EDT`
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
   TRI           84.00               25            0.55              0.33         85.60                69.04         0.673          pass              0.313             13.0                           0.100               -0.69              0.196                      ok            True                  False
  WDAY           86.67               30            1.76              1.82        147.13                69.97         0.556          pass              0.435             22.6                           0.240               13.40              1.937                      ok            True                  False
  PANW           90.32               31            1.08              2.11        278.35                60.15         0.555          pass              0.646             58.5                           0.565                9.22              1.334                      ok            True                  False
  TEAM           96.43               28            2.63              1.87        100.70                86.36         0.551          pass              0.650             25.0                           0.329               15.70              1.853                      ok            True                  False
  CTSH           93.33               30            0.80              0.30         53.27                51.38         0.542          pass              0.739             65.4                           0.362                0.43              0.162                      ok            True                  False
    MU           81.82               11            5.51             38.38        979.55               105.49         0.529          pass              0.207             32.9                           0.595               25.32              1.799                      ok            True                  False
  CRWD           80.00               10            3.38             17.01        711.80                64.90         0.520          pass              0.149             32.4                           0.532                7.18              1.197                      ok            True                  False
  FTNT          100.00               27            1.32              1.39        149.08                44.88         0.512          pass              0.716             50.6                           0.716               10.27              1.485                      ok            True                  False
    ZS           81.82               33            1.30              1.23        134.73               157.69         0.875          pass              0.384             31.5                           0.333              -26.80             -2.263 downtrend_blocked_slope           False                  False
  MELI           93.33               45            0.05              0.54       1634.55                60.42         0.593          pass              0.901             95.4                           0.535               -1.83             -0.282 downtrend_blocked_slope           False                  False
  CSCO          100.00                3            3.22              2.93        128.75                55.20         0.592          pass              0.524             21.6                           0.552                4.49              0.819                      ok           False                  False
   ADI          100.00                7            2.71              8.14        425.27                45.54         0.554          pass              0.546             30.3                           0.550                5.34              0.399                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-05T10:50:04.031385-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:45:02.885647-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:40:02.027944-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                         {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "entry_ask": 18.2, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.475, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 8.3, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "matched_signals": 36, "recovery_stability_score": 0.738, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:35:05.997480-04:00 early_entry_1035 early_entry_shadow           {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "entry_ask": 11.75, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.25, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 157.0, "option_spread_pct": 8.89, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.584, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.776, "early_reclaim_pct": 74.8, "matched_signals": 37, "recovery_stability_score": 0.742, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:30:06.002783-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "entry_ask": 12.6, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 11.65, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 16.31, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "matched_signals": 41, "recovery_stability_score": 0.644, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "trend_health_status": "ok"}, {"current_drop_pct": 0.98, "early_entry_score": 0.724, "early_reclaim_pct": 62.3, "matched_signals": 36, "recovery_stability_score": 0.677, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:25:06.279311-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:20:03.989401-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "matched_signals": 41, "recovery_stability_score": 0.706, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:15:05.401344-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "matched_signals": 41, "recovery_stability_score": 0.587, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:10:05.013482-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "entry_ask": 13.3, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 27.35, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "matched_signals": 41, "recovery_stability_score": 0.574, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:05:02.004075-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605105004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605105004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605105004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605105004)

</details>
