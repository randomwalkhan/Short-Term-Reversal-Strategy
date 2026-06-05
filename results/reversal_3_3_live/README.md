# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 10:35:05 EDT`
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
  WDAY           86.21               29            1.95              2.02        147.04                69.97         0.553          pass              0.350              0.7                           0.159               13.17              1.928                      ok            True                  False
  CTSH           93.55               31            0.56              0.21         53.31                51.38         0.552          pass              0.783             75.6                           0.384                0.66              0.173                      ok            True                  False
    MU           83.33               12            5.09             35.46        980.80               105.49         0.552          pass              0.271             38.0                           0.689               25.88              1.819                      ok            True                  False
  TEAM           96.43               28            2.67              1.89        100.69                86.36         0.548          pass              0.647             24.0                           0.260               15.66              1.851                      ok            True                  False
  PANW           91.89               37            0.66              1.28        278.70                60.15         0.545          pass              0.776             74.8                           0.742                9.69              1.353                      ok            True                   True
  CRWD           81.82               11            3.09             15.57        712.42                64.90         0.533          pass              0.223             38.1                           0.603                7.50              1.210                      ok            True                  False
  FTNT          100.00               25            1.47              1.54        149.01                44.88         0.516          pass              0.687             45.0                           0.682               10.11              1.478                      ok            True                  False
    ZS           82.35               34            1.03              0.97        134.84               157.69         0.880          pass              0.449             45.9                           0.375              -26.59             -2.251 downtrend_blocked_slope           False                  False
  MELI           93.33               45            0.06              0.67       1634.49                60.42         0.592          pass              0.897             94.2                           0.615               -1.84             -0.283 downtrend_blocked_slope           False                  False
  CSCO          100.00                1            3.58              3.26        128.60                55.20         0.583          pass              0.497             12.8                           0.230                4.10              0.802                      ok           False                  False
  QCOM           80.00                5            4.66              7.91        239.18                97.97         0.577          pass              0.152             31.4                           0.581               -2.53             -0.234                      ok           False                  False
   ADI          100.00                9            2.57              7.71        425.46                45.54         0.550          pass              0.557             34.0                           0.583                5.50              0.405                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-05T10:35:05.997480-04:00 early_entry_1035 early_entry_shadow           {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "entry_ask": 11.75, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.25, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 157.0, "option_spread_pct": 8.89, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.584, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.776, "early_reclaim_pct": 74.8, "matched_signals": 37, "recovery_stability_score": 0.742, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:30:06.002783-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "entry_ask": 12.6, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 11.65, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 16.31, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.826, "early_reclaim_pct": 79.7, "matched_signals": 41, "recovery_stability_score": 0.644, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.483, "trend_health_status": "ok"}, {"current_drop_pct": 0.98, "early_entry_score": 0.724, "early_reclaim_pct": 62.3, "matched_signals": 36, "recovery_stability_score": 0.677, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:25:06.279311-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:20:03.989401-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 83.6, "matched_signals": 41, "recovery_stability_score": 0.706, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:15:05.401344-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "matched_signals": 41, "recovery_stability_score": 0.587, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:10:05.013482-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "entry_ask": 13.3, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 27.35, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "matched_signals": 41, "recovery_stability_score": 0.574, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:05:02.004075-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:05:02.004075-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "SOXL260717C00270000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SOXL"}
2026-06-05T10:00:04.998731-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T09:35:04.249601-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605103505)

</details>
