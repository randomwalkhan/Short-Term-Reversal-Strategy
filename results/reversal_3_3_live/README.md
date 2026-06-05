# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 14:40:04 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$33,370.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           87.88               33            1.16              1.20        147.39                69.97         0.570            pass              0.603             60.7                           0.659               14.09              1.964                                 ok            True                  False
  TEAM           95.65               23            3.22              2.29        100.52                86.36         0.529            pass              0.632             30.7                           0.224               15.00              1.825                                 ok            True                  False
  ROST           93.94               33            0.56              0.92        232.67                43.36         0.522            pass              0.812             78.4                           0.566               -1.30             -0.088                                 ok            True                   True
   APP           85.37               41            0.68              2.67        557.73                74.69         0.508            pass              0.549             51.5                           0.285               14.23              1.774                                 ok            True                  False
    ZS           72.73               11            4.10              3.88        133.60               157.69         0.832            pass              0.090              0.0                           0.150              -28.87             -2.394            downtrend_blocked_slope           False                  False
  MELI           91.67               24            1.32             15.06       1628.33                60.42         0.636            pass              0.514             15.4                           0.241               -3.07             -0.340            downtrend_blocked_slope           False                  False
  PANW           76.92               13            2.69              5.26        276.99                60.15         0.554            pass              0.075              0.0                           0.150                7.44              1.259                                 ok           False                  False
  CTSH           94.44               36            0.26              0.10         53.36                51.38         0.540            pass              0.878             88.6                           0.626                0.97              0.186                                 ok           False                  False
  ADSK           90.32               31            0.95              1.55        232.97                42.86         0.519            pass              0.565             32.5                           0.249               -3.97             -0.349            downtrend_blocked_slope           False                  False
  AMZN           90.91               11            2.06              3.67        252.22                26.09         0.512            pass              0.386             12.4                           0.158               -6.67             -0.862 downtrend_blocked_slope_and_streak           False                  False
  TTWO           96.97               33            0.93              1.41        216.05                37.81         0.497 below_threshold              0.724             40.4                           0.413               -5.68             -0.346            downtrend_blocked_slope           False                  False
 GOOGL           84.00               25            1.14              2.96        370.92                30.67         0.494 below_threshold              0.391             44.9                           0.352               -3.92             -0.696 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-06-05T12:00:02.830136-04:00 early_entry_1200 early_entry_shadow  {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "entry_ask": 17.4, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 3.81, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "matched_signals": 36, "recovery_stability_score": 0.673, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:55:06.016628-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "entry_ask": 17.15, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 16.575, "hypothetical_budget": 16685.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 6.94, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.624, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "matched_signals": 36, "recovery_stability_score": 0.624, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:50:01.555393-04:00 early_entry_1150 early_entry_shadow    {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 1.0, "early_entry_score": 0.709, "early_reclaim_pct": 61.4, "entry_ask": 17.15, "entry_bid": 16.5, "entry_mode": "early", "entry_option_price": 16.825, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 3.86, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.535, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.709, "early_reclaim_pct": 61.4, "matched_signals": 35, "recovery_stability_score": 0.562, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.535, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:45:02.029445-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:40:05.991728-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:35:06.269367-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:30:05.821687-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:25:03.851940-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:20:04.824659-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:15:04.845440-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605144004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605144004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605144004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605144004)

</details>
