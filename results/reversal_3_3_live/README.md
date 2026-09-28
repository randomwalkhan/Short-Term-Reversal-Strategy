# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 13:25:05 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           84.21               19            1.26              2.32        262.28                41.90         0.562            pass              0.360             43.8                           0.643               -1.74              0.027                                 ok            True                  False
  AMAT           85.00               40            0.53              1.78        484.24                51.73         0.528            pass              0.640             84.7                           0.727               13.73              1.747                                 ok            True                  False
  MPWR           84.62               26            1.66             15.91       1360.61                54.48         0.524            pass              0.452             56.6                           0.604               17.62              2.187                                 ok            True                  False
  PYPL           88.89               18            1.44              0.55         54.80                60.08         0.515            pass              0.529             62.4                           0.743                0.41              0.088                                 ok            True                  False
  UPRO           89.47               19            1.54              1.64        151.50                32.02         0.506            pass              0.507             48.0                           0.539                2.83              0.574                                 ok            True                  False
  NXPI           85.19               27            1.18              1.97        237.23                39.27         0.503            pass              0.491             63.0                           0.400                5.39              0.671                                 ok            True                  False
   TRI           85.19               27            1.62              1.12         98.51                56.74         0.571            pass              0.416             35.7                           0.244               -7.97             -0.542 downtrend_blocked_slope_and_streak           False                  False
  LRCX           79.55               44            0.27              0.60        314.95                61.39         0.545            pass              0.534             93.2                           0.784               15.06              1.866                                 ok           False                  False
   KHC           95.83               24            0.23              0.04         23.61                20.56         0.498 below_threshold              0.751             69.1                           0.439               -2.86             -0.482 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.15               26            0.84              3.04        514.87                25.07         0.484 below_threshold              0.762             68.8                           0.600                1.27              0.254                                 ok           False                  False
  SNPS           72.00               25            1.47              4.38        423.88                45.66         0.483 below_threshold              0.274             41.8                           0.419                9.98              1.483                                 ok           False                  False
  CTSH           95.00               40            0.12              0.05         57.31                40.48         0.482 below_threshold              0.936             95.9                           0.898              -10.67             -1.187            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-28T12:00:07.024087-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "entry_ask": 30.4, "entry_bid": 29.1, "entry_mode": "early", "entry_option_price": 29.75, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.37, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "matched_signals": 34, "recovery_stability_score": 0.704, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:55:06.078627-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "entry_ask": 30.9, "entry_bid": 29.7, "entry_mode": "early", "entry_option_price": 30.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 3.96, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "matched_signals": 33, "recovery_stability_score": 0.676, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:50:06.060997-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:45:04.059310-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:40:05.053761-04:00 early_entry_1140 early_entry_shadow      {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "entry_ask": 30.1, "entry_bid": 28.7, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.76, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "matched_signals": 30, "recovery_stability_score": 0.556, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:35:05.945998-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:30:05.957358-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:25:05.958568-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:20:06.180521-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:15:05.555577-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928132505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928132505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928132505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928132505)

</details>
