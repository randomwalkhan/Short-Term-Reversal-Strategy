# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 12:50:01 EDT`
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
  ASML           93.94               33            0.75              9.58       1811.16                66.00         0.620          pass              0.798             70.4                           0.432               -9.44             -0.642                                 ok            True                  False
  META           81.82               22            1.54              7.37        678.15                54.55         0.592          pass              0.294             35.5                           0.280                9.44              1.338                                 ok            True                  False
  MPWR           81.25               16            4.28             40.54       1335.29                84.79         0.583          pass              0.160              9.3                           0.135               -6.34             -0.045                                 ok            True                  False
  UPRO           88.46               26            0.96              0.98        145.45                41.96         0.566          pass              0.514             41.8                           0.349                1.89              0.274                                 ok            True                  False
  BKNG           86.21               29            0.86              1.11        182.33                43.83         0.527          pass              0.476             43.6                           0.304                1.67             -0.208                                 ok            True                  False
  KLAC           81.82               22            2.70              4.24        222.68               109.33         0.692          pass              0.302             34.8                           0.257              -27.60             -2.150 downtrend_blocked_slope_and_streak           False                  False
  AMAT           82.35               17            2.86             11.60        574.46                98.89         0.667          pass              0.284             36.0                           0.209              -22.15             -1.509 downtrend_blocked_slope_and_streak           False                  False
   TXN           85.71                7            3.66              7.72        297.88                65.52         0.590          pass              0.250             13.0                           0.230               -2.66              0.114                                 ok           False                  False
  MSTR           67.74               31            3.14              2.14         96.55               100.18         0.581          pass              0.270             24.0                           0.224                8.61              0.290                                 ok           False                  False
   ADI           75.00               12            2.95              8.08        387.50                55.85         0.576          pass              0.108             12.4                           0.134               -4.47             -0.023                                 ok           False                  False
  LRCX           85.71               14            4.65             10.91        330.75                98.70         0.557          pass              0.256              7.0                           0.181              -26.19             -1.962 downtrend_blocked_slope_and_streak           False                  False
    MU           78.57               14            6.15             38.91        887.60               112.73         0.545          pass              0.096              5.0                           0.203              -26.46             -1.717            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716125001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716125001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716125001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716125001)

</details>
