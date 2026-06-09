# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 10:40:03 EDT`
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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTU           80.65               31            1.15              2.47        304.45               100.92         0.726          pass              0.405             58.4                           0.291               -0.78             -0.493                                 ok            True                  False
  TEAM           94.87               39            0.80              0.55         97.66                87.01         0.630          pass              0.878             75.2                           0.453               14.35              0.901                                 ok            True                  False
  PANW           89.66               29            1.18              2.19        265.39                58.75         0.589          pass              0.614             56.8                           0.422                2.51              0.434                                 ok            True                  False
   WDC           96.88               32            1.03              3.80        525.30                73.41         0.584          pass              0.741             45.3                           0.291               -0.57              0.070                                 ok            True                  False
  ADBE           81.48               27            1.67              2.86        243.76                49.77         0.531          pass              0.227              6.9                           0.114                0.17              0.153                                 ok            True                  False
   STX           96.67               30            1.21              7.46        873.57                63.66         0.528          pass              0.705             39.5                           0.277                2.41              0.141                                 ok            True                  False
  WDAY           84.62               13            3.79              3.82        142.12                70.13         0.523          pass              0.231             11.9                           0.290               11.52              1.262                                 ok            True                  False
    ZS           80.00               20            2.25              2.04        128.38               157.94         0.897          pass              0.159              1.0                           0.153              -31.56             -1.821            downtrend_blocked_slope           False                  False
  CSCO           85.71                7            1.89              1.64        123.45                58.94         0.683          pass              0.315             31.4                           0.416                2.93              0.510                                 ok           False                  False
  PAYX          100.00               24            0.15              0.11         98.87                34.09         0.628          pass              0.829             91.0                           0.544                4.19              0.505                                 ok           False                  False
  INTC           94.44               36            0.53              0.41        110.09                81.96         0.622          pass              0.811             63.4                           0.360              -11.20             -1.460 downtrend_blocked_slope_and_streak           False                  False
  AVGO           90.91               33            0.98              2.72        395.43                69.53         0.605          pass              0.563             19.4                           0.152               -6.94             -0.906            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-06-09T10:40:03.961827-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:30:02.001966-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:15:04.004316-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:10:02.035934-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "entry_ask": 13.8, "entry_bid": 12.25, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.722, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:05:03.054973-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "entry_ask": 14.25, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "matched_signals": 37, "recovery_stability_score": 0.761, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:00:05.039106-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.325, "pnl": -1572.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-09T10:00:05.039106-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609104003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609104003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609104003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609104003)

</details>
