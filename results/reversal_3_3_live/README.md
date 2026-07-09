# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 10:40:06 EDT`
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

- Cash: `$28,399.25`
- Equity: `$28,399.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   CSX     option         option  CSX260821C00047500     54          2026-07-07         2026-07-09        2.350      3.0750  3915.0   30.851064 take_profit_day2_hit_at_scan
  PAYX     option         option PAYX260821C00110000     50          2026-07-08         2026-07-09        2.525      2.2725 -1262.5  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GILD           89.47               19            0.95              0.90        135.43                35.14         0.543          pass              0.586             72.9                           0.486                7.49              0.920                                 ok            True                  False
  AMGN           92.31               13            1.26              3.26        366.59                27.70         0.543          pass              0.406              1.3                           0.242                3.39              0.437                                 ok            True                  False
  META           80.95               21            1.37              5.78        600.64                51.28         0.541          pass              0.358             68.3                           0.704                6.67              1.131                                 ok            True                  False
   ADP           95.83               24            0.79              1.34        240.80                32.32         0.526          pass              0.753             69.1                           0.672                8.91              1.229                                 ok            True                  False
  GOOG           83.33               12            2.08              5.23        356.47                34.51         0.513          pass              0.231             25.7                           0.403                1.80              0.555                                 ok            True                  False
  CTAS           85.00               20            1.31              1.65        179.46                32.70         0.512          pass              0.368             39.1                           0.318                4.03              0.718                                 ok            True                  False
  MDLZ          100.00               10            0.99              0.41         59.30                30.45         0.596          pass              0.607             49.1                           0.614               -3.82             -0.221           downtrend_blocked_streak           False                  False
   KDP          100.00                9            1.42              0.31         30.84                33.74         0.569          pass              0.539             27.3                           0.361               -2.08             -0.490 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           50.00                8            1.03              0.17         23.12                30.42         0.537          pass              0.171             39.2                           0.565                2.75              0.261                                 ok           False                  False
  CPRT           87.50               16            1.78              0.36         28.44                44.46         0.530          pass              0.348             18.4                           0.202               -7.63             -0.530            downtrend_blocked_slope           False                  False
   XEL          100.00               22            0.57              0.32         79.48                21.16         0.528          pass              0.631             32.8                           0.389               -2.82             -0.296            downtrend_blocked_slope           False                  False
  PAYX          100.00               32            0.30              0.22        106.48                32.56         0.521          pass              0.865             88.7                           0.763               10.34              1.186                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-09T10:40:06.204831-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                    {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "entry_ask": 108.1, "entry_bid": 93.6, "entry_mode": "early", "entry_option_price": 100.85, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 14.38, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "matched_signals": 37, "recovery_stability_score": 0.698, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:35:05.080363-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                    {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "entry_ask": 113.1, "entry_bid": 93.4, "entry_mode": "early", "entry_option_price": 103.25, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 19.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.613, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "matched_signals": 34, "recovery_stability_score": 0.613, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:30:03.109252-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.758, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:25:04.014382-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "matched_signals": 31, "recovery_stability_score": 0.713, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:20:03.107544-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.694, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:15:06.221157-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:10:04.085991-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:05:06.090866-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "entry_ask": 109.3, "entry_bid": 81.4, "entry_mode": "early", "entry_option_price": 95.35, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 29.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "matched_signals": 37, "recovery_stability_score": 0.823, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:05:06.090866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PAYX260821C00110000", "fill_price": 2.2725, "pnl": -1262.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-07-09T10:00:05.048554-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 105.0, "hypothetical_budget": 8518.38, "hypothetical_contracts": 0, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "matched_signals": 39, "recovery_stability_score": 0.819, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 31, "recovery_stability_score": 0.751, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709104006)

</details>
