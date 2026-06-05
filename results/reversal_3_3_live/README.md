# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 13:25:02 EDT`
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
  FTNT          100.00               10            2.24              2.34        148.67                44.88         0.568            pass              0.506             16.6                           0.265                9.25              1.443                                 ok            True                  False
  PANW           88.00               25            1.51              2.95        277.98                60.15         0.564            pass              0.495             41.8                           0.306                8.74              1.314                                 ok            True                  False
  CTSH           93.33               30            0.82              0.31         53.27                51.38         0.540            pass              0.736             64.2                           0.423                0.40              0.161                                 ok            True                  False
  WDAY           86.21               29            1.97              2.04        147.04                69.97         0.540            pass              0.447             33.6                           0.575               13.16              1.927                                 ok            True                  False
  ROST           92.86               28            0.90              1.47        232.43                43.36         0.532            pass              0.712             65.3                           0.370               -1.64             -0.104                                 ok            True                  False
  TEAM           95.65               23            3.17              2.25        100.53                86.36         0.532            pass              0.635             31.7                           0.557               15.06              1.827                                 ok            True                  False
    ZS           76.47               17            3.00              2.84        134.04               157.69         0.858            pass              0.159              9.0                           0.217              -28.06             -2.342            downtrend_blocked_slope           False                  False
  MELI           91.67               24            1.45             16.60       1627.66                60.42         0.627            pass              0.487              6.7                           0.213               -3.21             -0.346            downtrend_blocked_slope           False                  False
   APP           86.05               43            0.47              1.84        558.08                74.69         0.510            pass              0.612             66.6                           0.275               14.48              1.784                                 ok           False                  False
  ADSK           90.91               33            0.92              1.51        232.99                42.86         0.508            pass              0.598             34.3                           0.383               -3.95             -0.348            downtrend_blocked_slope           False                  False
  TTWO           96.97               33            0.93              1.41        216.04                37.81         0.497 below_threshold              0.724             40.2                           0.491               -5.68             -0.346            downtrend_blocked_slope           False                  False
  AMZN           91.43               35            0.23              0.40        253.62                26.09         0.492 below_threshold              0.741             73.5                           0.476               -4.92             -0.778 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605132502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605132502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605132502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605132502)

</details>
