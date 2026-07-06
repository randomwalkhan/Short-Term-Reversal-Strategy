# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 11:20:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$26,504.50`
- Equity: `$26,504.50`
- Realized PnL: `$16,504.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-06)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KDP     option         option KDP260821C00033000     96          2026-07-02         2026-07-06         1.45       1.305 -1392.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AMAT           95.83               24            1.28              5.40        600.73               110.01         0.676          pass              0.644             27.7                           0.243               -3.53              0.315                  ok            True                  False
  GILD           90.00               10            1.67              1.53        130.61                30.05         0.549          pass              0.427             35.2                           0.547                4.30              0.428                  ok            True                  False
  MNST          100.00               16            1.11              0.76         97.28                16.38         0.536          pass              0.570             25.5                           0.372                5.67              0.574                  ok            True                  False
  PAYX          100.00               29            0.51              0.38        106.19                31.56         0.534          pass              0.785             68.2                           0.819                7.71              0.907                  ok            True                  False
  PYPL           81.25               16            1.50              0.48         45.27                34.53         0.526          pass              0.305             59.8                           0.805                5.36              0.719                  ok            True                  False
   ADP           92.00               25            0.88              1.48        241.63                30.79         0.514          pass              0.640             56.3                           0.775                9.95              1.124                  ok            True                  False
  BKNG           87.88               33            0.77              1.00        184.13                41.33         0.507          pass              0.581             55.7                           0.704                6.61              0.847                  ok            True                  False
   XEL          100.00                3            1.77              1.01         81.53                20.81         0.597          pass              0.475              5.2                           0.193                4.00              0.276                  ok           False                  False
   PEP           80.00                5            1.46              1.48        143.59                27.18         0.597          pass              0.137             25.7                           0.481                0.06             -0.020                  ok           False                  False
   EXC           85.71                7            1.48              0.50         47.67                22.14         0.585          pass              0.232              7.2                           0.265                2.97              0.259                  ok           False                  False
   KHC          100.00                2            2.82              0.50         25.16                36.79         0.581          pass              0.514             18.8                           0.483                8.04              1.238                  ok           False                  False
  CTAS           66.67                9            1.83              2.33        180.37                35.27         0.553          pass              0.111             18.7                           0.265                4.21              0.512                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-07-06T11:20:05.831796-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "matched_signals": 38, "recovery_stability_score": 0.827, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:15:04.342098-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "matched_signals": 38, "recovery_stability_score": 0.806, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:10:04.321314-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "IDXX260821C00550000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "entry_ask": 39.6, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 35.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 3, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 20.31, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "matched_signals": 42, "recovery_stability_score": 0.747, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "trend_health_status": "ok"}, {"current_drop_pct": 0.64, "early_entry_score": 0.782, "early_reclaim_pct": 77.3, "matched_signals": 38, "recovery_stability_score": 0.758, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.404, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:05:05.715043-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.64, "shadow_only": true, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "matched_signals": 33, "recovery_stability_score": 0.64, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:00:02.142551-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "matched_signals": 32, "recovery_stability_score": 0.602, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:55:01.329795-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:50:01.323991-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:45:01.326292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:40:05.174623-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:35:05.425058-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706112005)

</details>
