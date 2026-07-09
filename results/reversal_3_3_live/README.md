# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 10:50:03 EDT`
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
  AAPL           95.83               24            0.80              1.75        312.64                38.12         0.570          pass              0.707             52.2                           0.458                6.08              1.236                                 ok            True                  False
  AMGN           92.31               13            1.27              3.28        366.58                27.70         0.542          pass              0.414              3.9                           0.183                3.38              0.437                                 ok            True                  False
  GILD           89.47               19            1.02              0.97        135.41                35.14         0.538          pass              0.579             71.0                           0.428                7.41              0.917                                 ok            True                  False
  META           81.48               27            0.95              3.99        601.41                51.28         0.532          pass              0.440             78.1                           0.750                7.13              1.151                                 ok            True                  False
   ADP           94.44               18            1.26              2.13        240.46                32.32         0.531          pass              0.644             50.6                           0.492                8.40              1.207                                 ok            True                  False
  TMUS           89.29               28            0.91              1.14        179.65                36.95         0.506          pass              0.555             45.5                           0.302               -1.26              0.075                                 ok            True                  False
  MDLZ          100.00                9            1.13              0.47         59.28                30.45         0.592          pass              0.585             41.8                           0.517               -3.96             -0.227           downtrend_blocked_streak           False                  False
   KDP          100.00                6            1.65              0.36         30.82                33.74         0.574          pass              0.504             15.7                           0.212               -2.30             -0.500 downtrend_blocked_slope_and_streak           False                  False
  CPRT           87.50               16            1.77              0.35         28.44                44.46         0.531          pass              0.351             19.2                           0.213               -7.62             -0.529            downtrend_blocked_slope           False                  False
   XEL          100.00               22            0.63              0.35         79.47                21.16         0.523          pass              0.606             24.6                           0.276               -2.89             -0.299            downtrend_blocked_slope           False                  False
  CTAS           70.00               10            1.84              2.32        179.18                32.70         0.523          pass              0.096             14.6                           0.153                3.47              0.693                                 ok           False                  False
 CMCSA           50.00                8            1.25              0.20         23.10                30.42         0.522          pass              0.132             26.5                           0.355                2.53              0.251                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-09T10:50:03.977506-04:00 early_entry_1050 early_entry_shadow    {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.54, "early_entry_score": 0.885, "early_reclaim_pct": 79.9, "entry_ask": 125.8, "entry_bid": 105.6, "entry_mode": "early", "entry_option_price": 115.7, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 107.0, "option_spread_pct": 17.46, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 95.0, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.885, "early_reclaim_pct": 79.9, "matched_signals": 40, "recovery_stability_score": 0.81, "success_rate": 95.0, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:45:05.917318-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "MELI260821C01790000", "current_drop_pct": 0.97, "early_entry_score": 0.774, "early_reclaim_pct": 63.9, "entry_ask": 134.3, "entry_bid": 108.0, "entry_mode": "early", "entry_option_price": 121.15, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.71, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.697, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.774, "early_reclaim_pct": 63.9, "matched_signals": 34, "recovery_stability_score": 0.697, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:40:06.204831-04:00 early_entry_1040 early_entry_shadow  {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "entry_ask": 108.1, "entry_bid": 93.6, "entry_mode": "early", "entry_option_price": 100.85, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 14.38, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.824, "early_reclaim_pct": 69.9, "matched_signals": 37, "recovery_stability_score": 0.698, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:35:05.080363-04:00 early_entry_1035 early_entry_shadow  {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "entry_ask": 113.1, "entry_bid": 93.4, "entry_mode": "early", "entry_option_price": 103.25, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 19.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.613, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.779, "early_reclaim_pct": 65.3, "matched_signals": 34, "recovery_stability_score": 0.613, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:30:03.109252-04:00 early_entry_1030 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.732, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.758, "success_rate": 91.43, "ticker": "ROP", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:25:04.014382-04:00 early_entry_1025 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.749, "early_reclaim_pct": 67.6, "matched_signals": 31, "recovery_stability_score": 0.713, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:20:03.107544-04:00 early_entry_1020 early_entry_shadow      {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.694, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:15:06.221157-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:10:04.085991-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:05:06.090866-04:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "entry_ask": 109.3, "entry_bid": 81.4, "entry_mode": "early", "entry_option_price": 95.35, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 29.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "matched_signals": 37, "recovery_stability_score": 0.823, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709105003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709105003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709105003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709105003)

</details>
