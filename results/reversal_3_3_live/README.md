# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 14:10:01 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX          100.00               11            1.29              0.45         50.20                27.78         0.614          pass              0.473              1.5                           0.113               -0.72             -0.096                                 ok            True                  False
  MDLZ           93.33               15            1.02              0.44         62.12                33.81         0.603          pass              0.520             23.5                           0.426                2.33              0.521                                 ok            True                  False
   WDC           82.76               29            1.23              4.68        542.84               105.07         0.596          pass              0.514             84.7                           0.930               10.41             -0.140                                 ok            True                  False
   EXC           94.44               18            0.82              0.26         45.71                22.49         0.558          pass              0.569             25.0                           0.199               -1.12             -0.137                                 ok            True                  False
   ROP           93.55               31            0.76              2.08        391.08                47.47         0.536          pass              0.609             18.2                           0.171                7.21              1.426                                 ok            True                  False
  AMGN          100.00               11            1.70              4.57        383.20                25.80         0.530          pass              0.547             29.0                           0.463                3.97              0.634                                 ok            True                  False
   XEL          100.00               20            0.83              0.45         78.01                17.46         0.528          pass              0.549              9.7                           0.178               -1.42             -0.218                                 ok            True                  False
   STX           88.46               26            2.21             13.22        850.46                95.23         0.503          pass              0.606             74.5                           0.842                4.34             -0.573                                 ok            True                  False
  AAPL           96.00               25            0.93              2.01        308.05                37.33         0.567          pass              0.721             54.9                           0.462               -6.29             -0.338 downtrend_blocked_slope_and_streak           False                  False
   PEP           85.71               28            0.29              0.29        139.44                26.18         0.551          pass              0.483             51.8                           0.509                2.72              0.485                                 ok           False                  False
   KDP           84.62               26            0.47              0.10         31.08                33.11         0.543          pass              0.431             49.1                           0.519                1.76              0.456                                 ok           False                  False
  CTAS           94.87               39            0.25              0.36        204.48                38.81         0.536          pass              0.784             46.9                           0.270                1.15              0.354                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-03T12:00:03.854898-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CDNS260918C00335000", "current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "entry_ask": 25.3, "entry_bid": 22.6, "entry_mode": "early", "entry_option_price": 23.95, "hypothetical_budget": 17614.88, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.27, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "matched_signals": 45, "recovery_stability_score": 0.703, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-03T11:55:02.829313-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:50:02.007481-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:45:01.947551-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:40:02.921785-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:35:06.072757-04:00 early_entry_1135 early_entry_shadow                                       {"contract_symbol": "CSCO260918C00115000", "current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "entry_ask": 8.45, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.325, "hypothetical_budget": 17614.88, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 5712.0, "option_spread_pct": 3.0, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.671, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T11:30:04.782483-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:25:05.765544-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:20:03.871415-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:15:01.863770-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803141001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803141001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803141001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803141001)

</details>
