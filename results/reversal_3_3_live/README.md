# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 11:10:01 EDT`
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
   ADI           82.35               17            2.43              6.66        388.11                55.85         0.584          pass              0.251             27.8                           0.281               -3.96              0.001                                 ok            True                  False
  MPWR           81.82               22            3.77             35.68       1337.37                84.79         0.578          pass              0.238             17.3                           0.170               -5.84             -0.021                                 ok            True                  False
   WBD           87.50               16            0.81              0.15         27.20                20.00         0.531          pass              0.522             76.2                           0.492                1.46              0.247                                 ok            True                  False
  BKNG           86.67               30            0.80              1.02        182.36                43.83         0.525          pass              0.507             47.9                           0.373                1.74             -0.205                                 ok            True                  False
  TEAM           80.65               31            1.79              1.15         91.28                73.34         0.517          pass              0.358             49.7                           0.491                8.36              1.014                                 ok            True                  False
  CRWD           87.50               32            1.30              1.88        205.96                56.35         0.504          pass              0.577             59.9                           0.483                5.64              0.705                                 ok            True                  False
  KLAC           84.62               26            1.41              2.22        223.55               109.33         0.742          pass              0.502             65.9                           0.351              -26.64             -2.091 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.46               26            1.13              4.60        577.46                98.89         0.718          pass              0.628             74.6                           0.391              -20.77             -1.429 downtrend_blocked_slope_and_streak           False                  False
    MU           81.25               16            4.87             30.81        891.08               112.73         0.619          pass              0.186             16.9                           0.234              -25.46             -1.655            downtrend_blocked_slope           False                  False
  LRCX           85.00               20            3.13              7.34        332.28                98.70         0.614          pass              0.370             36.2                           0.245              -25.01             -1.890 downtrend_blocked_slope_and_streak           False                  False
   TXN           85.71                7            3.79              8.00        297.76                65.52         0.585          pass              0.223              4.1                           0.195               -2.79              0.107                                 ok           False                  False
  MCHP           92.86               14            3.57              2.16         85.34                68.63         0.577          pass              0.443              5.2                           0.157               -8.79             -0.404            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-16T11:10:01.140332-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:05:05.344803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:00:06.208164-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:55:05.410744-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:50:02.316903-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "entry_ask": 16.2, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 15.7, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 6.37, "option_volume": 41.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "matched_signals": 38, "recovery_stability_score": 0.741, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:45:01.218260-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:40:01.176250-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:35:02.369345-04:00 early_entry_1035 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "entry_ask": 16.5, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 15.775, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 761.0, "option_spread_pct": 9.19, "option_volume": 68.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "matched_signals": 37, "recovery_stability_score": 0.55, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:30:06.149838-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:25:02.335727-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716111001)

</details>
