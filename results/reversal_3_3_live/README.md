# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 13:05:05 EDT`
Last processed slot: `manage_1300`

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
  MPWR           81.25               16            4.27             40.42       1335.34                84.79         0.584          pass              0.160              9.6                           0.218               -6.33             -0.045                                 ok            True                  False
   ADI           81.25               16            2.60              7.12        387.91                55.85         0.579          pass              0.200             22.8                           0.279               -4.12             -0.007                                 ok            True                  False
  UPRO           86.21               29            0.89              0.91        145.48                41.96         0.547          pass              0.484             45.7                           0.435                1.96              0.277                                 ok            True                  False
   WBD           83.33               12            1.16              0.22         27.18                20.00         0.531          pass              0.353             65.9                           0.469                1.11              0.231                                 ok            True                  False
  PANW           93.75               32            1.45              3.58        352.48                59.01         0.528          pass              0.644             26.0                           0.219               -0.89              0.037                                 ok            True                  False
  BKNG           86.67               30            0.85              1.08        182.34                43.83         0.522          pass              0.498             44.8                           0.410                1.69             -0.207                                 ok            True                  False
  FTNT           92.31               13            2.75              3.16        163.15                41.65         0.506          pass              0.449             16.8                           0.337                4.15              0.470                                 ok            True                  False
  KLAC           81.82               22            2.18              3.43        223.03               109.33         0.720          pass              0.342             47.3                           0.383              -27.22             -2.126 downtrend_blocked_slope_and_streak           False                  False
  AMAT           85.00               20            2.17              8.82        575.65                98.89         0.691          pass              0.423             51.3                           0.382              -21.60             -1.477 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.12               34            0.43              5.45       1812.94                66.00         0.635          pass              0.849             83.2                           0.527               -9.15             -0.627                                 ok           False                  False
  META           78.57               14            1.85              8.84        677.52                54.55         0.620          pass              0.156             22.6                           0.265                9.10              1.323                                 ok           False                  False
   TXN           75.00                8            3.50              7.38        298.03                65.52         0.580          pass              0.109             16.9                           0.356               -2.49              0.121                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-16T12:00:02.316099-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:55:05.282861-04:00 early_entry_1155 early_entry_shadow    {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "entry_ask": 16.9, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 16.5, "hypothetical_budget": 14612.13, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 4.85, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "matched_signals": 42, "recovery_stability_score": 0.646, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:50:01.317315-04:00 early_entry_1150 early_entry_shadow   {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "entry_ask": 16.7, "entry_bid": 15.75, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.86, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "matched_signals": 40, "recovery_stability_score": 0.61, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:45:04.302520-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:40:01.166933-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:35:06.405776-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 77.2, "entry_ask": 16.1, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.75, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 4.44, "option_volume": 71.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 77.2, "matched_signals": 41, "recovery_stability_score": 0.758, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:30:06.170773-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:25:01.178080-04:00 early_entry_1125 early_entry_shadow    {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "entry_ask": 16.0, "entry_bid": 15.6, "entry_mode": "early", "entry_option_price": 15.8, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 2.53, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "matched_signals": 43, "recovery_stability_score": 0.663, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:20:02.331594-04:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "entry_ask": 16.55, "entry_bid": 15.65, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.59, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.566, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "matched_signals": 40, "recovery_stability_score": 0.566, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:15:01.227761-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716130505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716130505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716130505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716130505)

</details>
