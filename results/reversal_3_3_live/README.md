# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 11:20:02 EDT`
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
   ADI           82.35               17            2.44              6.68        388.10                55.85         0.584          pass              0.251             27.6                           0.278               -3.97              0.000                                 ok            True                  False
  META           84.85               33            0.76              3.61        679.76                54.55         0.577          pass              0.545             68.4                           0.565               10.32              1.374                                 ok            True                  False
  MPWR           81.82               22            3.85             36.41       1337.05                84.79         0.573          pass              0.233             15.6                           0.185               -5.91             -0.025                                 ok            True                  False
  UPRO           86.67               30            0.55              0.56        145.63                41.96         0.564          pass              0.568             66.7                           0.520                2.31              0.293                                 ok            True                  False
  NXPI           80.00               15            3.19              6.22        276.34                58.07         0.547          pass              0.107              6.3                           0.176               -3.88              0.092                                 ok            True                  False
   WBD           87.50               16            0.79              0.15         27.21                20.00         0.532          pass              0.523             76.7                           0.487                1.48              0.247                                 ok            True                  False
  BKNG           87.50               32            0.72              0.92        182.41                43.83         0.518          pass              0.558             53.2                           0.417                1.82             -0.201                                 ok            True                  False
  TEAM           80.65               31            1.90              1.22         91.25                73.34         0.510          pass              0.349             46.8                           0.371                8.25              1.010                                 ok            True                  False
  KLAC           84.62               26            1.44              2.27        223.53               109.33         0.741          pass              0.499             65.2                           0.348              -26.66             -2.092 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.46               26            1.11              4.51        577.50                98.89         0.719          pass              0.630             75.1                           0.407              -20.75             -1.428 downtrend_blocked_slope_and_streak           False                  False
  LRCX           84.21               19            3.14              7.38        332.27                98.70         0.618          pass              0.342             35.8                           0.285              -25.03             -1.891 downtrend_blocked_slope_and_streak           False                  False
   TXN           85.71                7            3.80              8.00        297.76                65.52         0.584          pass              0.223              4.1                           0.170               -2.79              0.107                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-16T11:20:02.331594-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "entry_ask": 16.55, "entry_bid": 15.65, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.59, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.566, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "matched_signals": 40, "recovery_stability_score": 0.566, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:15:01.227761-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:10:01.140332-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:05:05.344803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:00:06.208164-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:55:05.410744-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:50:02.316903-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "entry_ask": 16.2, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 15.7, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 6.37, "option_volume": 41.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "matched_signals": 38, "recovery_stability_score": 0.741, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:45:01.218260-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:40:01.176250-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:35:02.369345-04:00 early_entry_1035 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "entry_ask": 16.5, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 15.775, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 761.0, "option_spread_pct": 9.19, "option_volume": 68.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "matched_signals": 37, "recovery_stability_score": 0.55, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716112002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716112002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716112002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716112002)

</details>
