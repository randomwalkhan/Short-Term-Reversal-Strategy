# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 11:40:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PANW           88.00               25            1.41              2.75        278.07                60.15         0.571            pass              0.508             45.8                           0.357                8.86              1.319                      ok            True                  False
  FTNT          100.00               12            2.09              2.19        148.73                44.88         0.564            pass              0.536             21.9                           0.207                9.42              1.449                      ok            True                  False
  CTSH           89.47               19            1.49              0.56         53.16                51.38         0.564            pass              0.475             35.4                           0.185               -0.27              0.130                      ok            True                  False
  WDAY           83.33               24            2.42              2.51        146.84                69.97         0.546            pass              0.243              1.9                           0.182               12.63              1.906                      ok            True                  False
  TEAM           94.12               17            4.16              2.95        100.23                86.36         0.509            pass              0.474              0.0                           0.157               13.88              1.781                      ok            True                  False
    ZS           77.78               18            2.49              2.36        134.25               157.69         0.877            pass              0.150              3.0                           0.130              -27.68             -2.318 downtrend_blocked_slope           False                  False
  MELI           94.59               37            0.59              6.80       1631.87                60.42         0.610            pass              0.755             41.5                           0.210               -2.36             -0.307 downtrend_blocked_slope           False                  False
   ADI          100.00                3            3.73             11.18        423.97                45.54         0.516            pass              0.464              4.2                           0.105                4.24              0.351                      ok           False                  False
  TTWO           96.77               31            1.00              1.52        216.00                37.81         0.512            pass              0.601              3.2                           0.161               -5.74             -0.349 downtrend_blocked_slope           False                  False
  ADSK           91.43               35            0.79              1.30        233.08                42.86         0.506            pass              0.636             38.0                           0.208               -3.82             -0.342 downtrend_blocked_slope           False                  False
   CEG           76.19               21            2.54              4.71        262.57                55.63         0.505            pass              0.155             10.3                           0.219               -9.79             -1.406 downtrend_blocked_slope           False                  False
   BKR           71.43                7            2.71              1.25         65.57                32.54         0.495 below_threshold              0.049              0.0                           0.207               -2.63             -0.102                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-05T11:40:05.991728-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:35:06.269367-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:30:05.821687-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:25:03.851940-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:20:04.824659-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:15:04.845440-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:10:06.011587-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:05:02.012867-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.77, "early_entry_score": 0.749, "early_reclaim_pct": 70.2, "entry_ask": 17.7, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.2, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 5.81, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.749, "early_reclaim_pct": 70.2, "matched_signals": 36, "recovery_stability_score": 0.631, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:00:03.928468-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "entry_ask": 17.8, "entry_bid": 17.0, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 4.6, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "matched_signals": 36, "recovery_stability_score": 0.619, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:55:02.043885-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605114005)

</details>
