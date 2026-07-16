# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 11:25:01 EDT`
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
  MPWR           81.82               22            3.56             33.75       1338.20                84.79         0.590          pass              0.253             21.8                           0.221               -5.64             -0.012                                 ok            True                  False
   ADI           81.25               16            2.49              6.82        388.04                55.85         0.586          pass              0.210             26.1                           0.254               -4.02             -0.002                                 ok            True                  False
  META           84.85               33            0.75              3.56        679.79                54.55         0.578          pass              0.547             68.9                           0.545               10.33              1.375                                 ok            True                  False
  NXPI           80.00               15            2.97              5.81        276.52                58.07         0.560          pass              0.127             12.5                           0.226               -3.67              0.102                                 ok            True                  False
   WBD           87.50               16            0.72              0.14         27.21                20.00         0.537          pass              0.530             78.9                           0.489                1.56              0.251                                 ok            True                  False
  BKNG           88.24               34            0.56              0.72        182.49                43.83         0.517          pass              0.621             63.2                           0.508                1.98             -0.194                                 ok            True                  False
  TEAM           80.65               31            1.79              1.15         91.28                73.34         0.517          pass              0.358             49.8                           0.361                8.37              1.015                                 ok            True                  False
  KLAC           86.21               29            1.21              1.90        223.69               109.33         0.739          pass              0.579             70.9                           0.378              -26.49             -2.081 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.46               26            1.21              4.90        577.33                98.89         0.714          pass              0.623             73.0                           0.398              -20.83             -1.432 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.71               21            2.90              6.80        332.51                98.70         0.622          pass              0.410             40.8                           0.297              -24.84             -1.879 downtrend_blocked_slope_and_streak           False                  False
    MU           81.25               16            4.81             30.46        891.22               112.73         0.622          pass              0.189             18.0                           0.266              -25.42             -1.653            downtrend_blocked_slope           False                  False
  MSTR           68.75               32            2.74              1.87         96.67               100.18         0.600          pass              0.307             33.6                           0.408                9.05              0.308                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-16T11:25:01.178080-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "entry_ask": 16.0, "entry_bid": 15.6, "entry_mode": "early", "entry_option_price": 15.8, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 2.53, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "matched_signals": 43, "recovery_stability_score": 0.663, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:20:02.331594-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "entry_ask": 16.55, "entry_bid": 15.65, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.59, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.566, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "matched_signals": 40, "recovery_stability_score": 0.566, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:15:01.227761-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:10:01.140332-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:05:05.344803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:00:06.208164-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:55:05.410744-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:50:02.316903-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "entry_ask": 16.2, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 15.7, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 6.37, "option_volume": 41.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "matched_signals": 38, "recovery_stability_score": 0.741, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:45:01.218260-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:40:01.176250-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716112501)

</details>
