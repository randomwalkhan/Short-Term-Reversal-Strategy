# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 10:45:05 EDT`
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
  AAPL           96.55               29            0.54              1.19        312.88                38.12         0.556          pass              0.785             67.5                           0.691                6.35              1.248                                 ok            True                  False
  GILD           89.47               19            1.00              0.95        135.41                35.14         0.540          pass              0.581             71.5                           0.465                7.43              0.918                                 ok            True                  False
  AMGN           93.33               15            1.19              3.06        366.68                27.70         0.536          pass              0.470              9.1                           0.152                3.47              0.441                                 ok            True                  False
   ADP           95.00               20            1.02              1.73        240.63                32.32         0.535          pass              0.700             60.0                           0.592                8.66              1.218                                 ok            True                  False
  CTAS           84.21               19            1.41              1.78        179.41                32.70         0.511          pass              0.327             34.5                           0.278                3.92              0.713                                 ok            True                  False
  VRTX           91.67               12            1.56              5.44        496.10                34.56         0.506          pass              0.422             15.6                           0.258                3.25              0.609                                 ok            True                  False
  MDLZ          100.00                9            1.01              0.42         59.30                30.45         0.601          pass              0.605             48.3                           0.590               -3.83             -0.222           downtrend_blocked_streak           False                  False
   KDP          100.00                6            1.65              0.36         30.82                33.74         0.574          pass              0.504             15.7                           0.245               -2.30             -0.500 downtrend_blocked_slope_and_streak           False                  False
  META           73.33               15            1.78              7.53        599.89                51.28         0.543          pass              0.264             58.7                           0.625                6.22              1.112                                 ok           False                  False
  CPRT           87.50               16            1.70              0.34         28.44                44.46         0.535          pass              0.361             22.4                           0.235               -7.55             -0.525            downtrend_blocked_slope           False                  False
   XEL          100.00               22            0.49              0.27         79.50                21.16         0.533          pass              0.659             41.8                           0.408               -2.75             -0.292            downtrend_blocked_slope           False                  False
  PAYX          100.00               32            0.25              0.19        106.50                32.56         0.524          pass              0.871             90.5                           0.767               10.39              1.188                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-09T10:45:05.917318-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "MELI260821C01790000", "current_drop_pct": 0.97, "early_entry_score": 0.774, "early_reclaim_pct": 63.9, "entry_ask": 134.3, "entry_bid": 108.0, "entry_mode": "early", "entry_option_price": 121.15, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.71, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.697, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.774, "early_reclaim_pct": 63.9, "matched_signals": 34, "recovery_stability_score": 0.697, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:40:06.204831-04:00 early_entry_1040 early_entry_shadow  {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "entry_ask": 108.1, "entry_bid": 93.6, "entry_mode": "early", "entry_option_price": 100.85, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 14.38, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "matched_signals": 37, "recovery_stability_score": 0.698, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:35:05.080363-04:00 early_entry_1035 early_entry_shadow  {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "entry_ask": 113.1, "entry_bid": 93.4, "entry_mode": "early", "entry_option_price": 103.25, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 19.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.613, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "matched_signals": 34, "recovery_stability_score": 0.613, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:30:03.109252-04:00 early_entry_1030 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.758, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:25:04.014382-04:00 early_entry_1025 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "matched_signals": 31, "recovery_stability_score": 0.713, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:20:03.107544-04:00 early_entry_1020 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.694, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:15:06.221157-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:10:04.085991-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:05:06.090866-04:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "entry_ask": 109.3, "entry_bid": 81.4, "entry_mode": "early", "entry_option_price": 95.35, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 29.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "matched_signals": 37, "recovery_stability_score": 0.823, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:05:06.090866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "PAYX260821C00110000", "fill_price": 2.2725, "pnl": -1262.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709104505)

</details>
