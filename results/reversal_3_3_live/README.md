# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 11:00:06 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           85.71               14            3.03              6.38        298.45                65.52         0.586          pass              0.308             23.5                           0.393               -2.01              0.143                                 ok            True                  False
   ADI           86.36               22            2.00              5.47        388.61                55.85         0.583          pass              0.430             40.7                           0.407               -3.53              0.021                                 ok            True                  False
  NXPI           85.00               20            2.69              5.26        276.76                58.07         0.550          pass              0.318             20.9                           0.258               -3.39              0.115                                 ok            True                  False
   WBD           87.50               16            0.77              0.15         27.21                20.00         0.534          pass              0.525             77.3                           0.502                1.50              0.248                                 ok            True                  False
  BKNG           86.67               30            0.81              1.04        182.36                43.83         0.524          pass              0.505             47.1                           0.500                1.73             -0.205                                 ok            True                  False
  TEAM           82.86               35            1.35              0.86         91.40                73.34         0.522          pass              0.482             62.2                           0.816                8.86              1.035                                 ok            True                  False
  KLAC           88.89               36            0.61              0.96        224.09               109.33         0.736          pass              0.740             85.3                           0.516              -26.04             -2.054 downtrend_blocked_slope_and_streak           False                  False
  AMAT           90.91               33            0.28              1.14        578.94                98.89         0.728          pass              0.798             93.7                           0.555              -20.08             -1.390 downtrend_blocked_slope_and_streak           False                  False
    MU           84.21               19            4.11             26.01        893.13               112.73         0.647          pass              0.327             29.8                           0.235              -24.87             -1.619            downtrend_blocked_slope           False                  False
  LRCX           86.96               23            2.44              5.74        332.97                98.70         0.639          pass              0.486             50.1                           0.292              -24.48             -1.858 downtrend_blocked_slope_and_streak           False                  False
  MPWR           79.17               24            3.05             28.89       1340.28                84.79         0.606          pass              0.253             33.1                           0.281               -5.13              0.013                                 ok           False                  False
  SOXL           82.35               17            9.67             11.21        160.75               219.49         0.598          pass              0.241             23.9                           0.220              -43.93             -3.511            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-16T11:00:06.208164-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:55:05.410744-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:50:02.316903-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                             {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "entry_ask": 16.2, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 15.7, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 6.37, "option_volume": 41.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "matched_signals": 38, "recovery_stability_score": 0.741, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:45:01.218260-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:40:01.176250-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:35:02.369345-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                               {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "entry_ask": 16.5, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 15.775, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 761.0, "option_spread_pct": 9.19, "option_volume": 68.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "matched_signals": 37, "recovery_stability_score": 0.55, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:30:06.149838-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:25:02.335727-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:20:04.346056-04:00 early_entry_1020 early_entry_shadow  {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "entry_ask": 15.3, "entry_bid": 13.15, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 15.11, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "matched_signals": 37, "recovery_stability_score": 0.803, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.696, "early_reclaim_pct": 69.4, "matched_signals": 38, "recovery_stability_score": 0.831, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:15:01.181570-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "entry_ask": 15.35, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 42, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 17.73, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "matched_signals": 42, "recovery_stability_score": 0.786, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.754, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.827, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716110006)

</details>
