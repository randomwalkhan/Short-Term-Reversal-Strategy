# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 10:30:06 EDT`
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
   ADI           84.00               25            1.48              4.05        389.23                55.85         0.594          pass              0.434             56.1                           0.696               -3.02              0.045                                 ok            True                  False
  CTSH           80.00               35            0.85              0.26         43.07                65.21         0.592          pass              0.288             20.7                           0.131               10.55              0.865                                 ok            True                  False
   TXN           85.71               14            3.09              6.52        298.40                65.52         0.582          pass              0.301             21.2                           0.391               -2.08              0.140                                 ok            True                  False
  META           86.49               37            0.55              2.60        680.19                54.55         0.567          pass              0.641             77.2                           0.797               10.55              1.384                                 ok            True                  False
  NXPI           85.71               21            2.35              4.59        277.04                58.07         0.565          pass              0.375             31.0                           0.539               -3.05              0.131                                 ok            True                  False
   WBD           87.50               16            0.68              0.13         27.21                20.00         0.540          pass              0.534             80.0                           0.425                1.59              0.253                                 ok            True                  False
  BKNG           86.21               29            0.93              1.19        182.29                43.83         0.522          pass              0.462             39.3                           0.377                1.60             -0.211                                 ok            True                  False
  KLAC           89.47               38            0.24              0.38        224.34               109.33         0.745          pass              0.796             94.2                           0.666              -25.77             -2.037 downtrend_blocked_slope_and_streak           False                  False
    MU           84.21               19            4.07             25.78        893.23               112.73         0.649          pass              0.329             30.5                           0.345              -24.84             -1.617            downtrend_blocked_slope           False                  False
  LRCX           88.00               25            2.12              4.97        333.30                98.70         0.647          pass              0.548             56.7                           0.528              -24.23             -1.843 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               18            8.79             10.19        161.18               219.49         0.647          pass              0.299             30.8                           0.475              -43.39             -3.467            downtrend_blocked_slope           False                  False
  MPWR           78.57               28            2.18             20.62       1343.82                84.79         0.632          pass              0.340             52.2                           0.648               -4.28              0.053                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-16T10:30:06.149838-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:25:02.335727-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:20:04.346056-04:00 early_entry_1020 early_entry_shadow  {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "entry_ask": 15.3, "entry_bid": 13.15, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 15.11, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "matched_signals": 37, "recovery_stability_score": 0.803, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.696, "early_reclaim_pct": 69.4, "matched_signals": 38, "recovery_stability_score": 0.831, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:15:01.181570-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "entry_ask": 15.35, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 42, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 17.73, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "matched_signals": 42, "recovery_stability_score": 0.786, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.754, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.827, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:10:01.416514-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "entry_ask": 15.6, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 19.33, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "matched_signals": 44, "recovery_stability_score": 0.725, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:05:04.361041-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "entry_ask": 16.05, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 14.725, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 18.0, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.56, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "matched_signals": 37, "recovery_stability_score": 0.56, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:00:05.335836-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:00:05.335836-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "ADI260821C00380000", "fill_price": 31.635, "pnl": -1406.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ADI"}
2026-07-15T15:10:01.366399-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716103006)

</details>
