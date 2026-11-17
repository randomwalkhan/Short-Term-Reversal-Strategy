# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 11:40:06 EST`
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

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           96.43               28            1.16              5.70        698.21                77.90         0.720          pass              0.592              0.0                           0.200                3.05              0.333                  ok            True                  False
  FTNT           81.08               37            1.05              0.91        122.88                92.89         0.671          pass              0.434             52.6                           0.453               -4.79             -0.099                  ok            True                  False
   AEP          100.00               11            0.64              0.58        129.09                17.11         0.593          pass              0.527             20.2                           0.254               -0.29              0.150                  ok            True                  False
 GOOGL           80.77               26            1.10              2.19        282.78                55.10         0.590          pass              0.307             40.4                           0.395                0.20              0.171                  ok            True                  False
  QCOM           84.00               25            1.58              1.87        167.72                68.75         0.585          pass              0.433             56.0                           0.478                0.86              0.352                  ok            True                  False
  GOOG           80.00               25            1.17              2.30        280.27                53.19         0.585          pass              0.269             36.8                           0.383               -0.11              0.106                  ok            True                  False
   CSX           83.33               18            1.18              0.43         51.85                34.26         0.579          pass              0.308             35.9                           0.414                1.37              0.268                  ok            True                  False
  SBUX           86.67               15            1.09              0.83        108.36                31.47         0.571          pass              0.357             29.6                           0.433                3.24              0.192                  ok            True                  False
   ADP           81.25               16            1.26              2.76        312.25                28.40         0.563          pass              0.190             20.1                           0.344                4.55              0.384                  ok            True                  False
   CEG           88.00               25            1.90              3.70        276.24                60.48         0.558          pass              0.503             44.5                           0.522                3.63              1.258                  ok            True                  False
   WMT           86.36               22            0.77              0.69        128.11                25.56         0.538          pass              0.467             54.6                           0.392                2.05              0.088                  ok            True                  False
  AMZN           82.14               28            1.08              1.94        256.92                40.10         0.520          pass              0.307             26.0                           0.229                1.71              0.082                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-17T11:40:06.599969-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:35:05.679790-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "PYPL261218C00057500", "current_drop_pct": 0.51, "early_entry_score": 0.843, "early_reclaim_pct": 65.9, "entry_ask": 3.05, "entry_bid": 2.78, "entry_mode": "early", "entry_option_price": 2.915, "hypothetical_budget": 55619.9, "hypothetical_contracts": 190, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3814.0, "option_spread_pct": 9.26, "option_volume": 43.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.843, "early_reclaim_pct": 65.9, "matched_signals": 40, "recovery_stability_score": 0.562, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:30:05.827440-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:25:01.808669-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.62, "early_entry_score": 0.786, "early_reclaim_pct": 71.0, "entry_ask": 23.65, "entry_bid": 21.25, "entry_mode": "early", "entry_option_price": 22.45, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 10.69, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.786, "early_reclaim_pct": 71.0, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:20:04.857658-05:00 early_entry_1120 early_entry_shadow {"contract_symbol": "PYPL261218C00057500", "current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 61.1, "entry_ask": 2.89, "entry_bid": 2.59, "entry_mode": "early", "entry_option_price": 2.74, "hypothetical_budget": 55619.9, "hypothetical_contracts": 202, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3814.0, "option_spread_pct": 10.95, "option_volume": 43.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 61.1, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.461, "trend_health_status": "ok"}, {"current_drop_pct": 0.61, "early_entry_score": 0.786, "early_reclaim_pct": 71.2, "matched_signals": 32, "recovery_stability_score": 0.705, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:15:06.470113-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:10:04.744524-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:05:05.736370-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:00:04.828714-05:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:55:05.881265-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117114006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117114006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117114006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117114006)

</details>
