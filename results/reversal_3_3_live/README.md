# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 11:20:06 EDT`
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

- Cash: `$17,610.75`
- Equity: `$32,890.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15280.0         9.85           9.55       98.17         98.65          bid_ask_mid                       9.55                bid_ask_mid                    True          -480.0                  -3.05         95.65               23              3.29          79.1           78.05                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  TEAM           95.00               40            0.82              0.57         99.22                86.36         0.638          pass              0.890             75.5                           0.569               15.49              1.845                       ok            True                   True
   TRI           80.00               15            2.12              1.27         85.49                69.04         0.635          pass              0.176             26.3                           0.288               -1.91              0.140                       ok            True                  False
  MSFT           88.00               25            1.05              3.08        415.35                34.82         0.564          pass              0.425             18.3                           0.316               -1.50              0.121                       ok            True                  False
  CRWD           91.89               37            0.75              3.51        669.51                64.90         0.563          pass              0.715             53.7                           0.283                2.74              1.004                       ok            True                  False
  PANW           91.67               36            0.80              1.53        271.39                60.15         0.549          pass              0.753             71.4                           0.644                6.70              1.228                       ok            True                   True
  FAST           94.12               17            1.26              0.41         46.61                21.36         0.533          pass              0.536             19.8                           0.146                5.14              0.681                       ok            True                  False
  ADBE           81.48               27            1.75              3.09        250.12                48.16         0.513          pass              0.341             45.7                           0.387                0.93              0.646                       ok            True                  False
    ZS           82.05               39            0.52              0.47        130.58               157.69         0.895          pass              0.571             77.8                           0.593              -28.66             -2.381  downtrend_blocked_slope           False                  False
  PAYX          100.00               23            0.41              0.29        100.41                33.39         0.598          pass              0.784             79.1                           0.705                3.22              0.583                       ok           False                  False
   CEG           84.21               38            0.13              0.23        254.73                55.63         0.580          pass              0.636             93.0                           0.717              -10.96             -1.466  downtrend_blocked_slope           False                  False
   EXC           85.71                7            1.22              0.39         45.58                19.68         0.569          pass              0.251             13.8                           0.287               -1.33             -0.209                       ok           False                  False
  REGN           66.67                9            2.23              9.93        631.20                43.33         0.568          pass              0.072              5.1                           0.207               -2.76             -0.138 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-08T11:20:06.683285-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                   {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "entry_ask": 18.45, "entry_bid": 17.55, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 5.0, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "matched_signals": 36, "recovery_stability_score": 0.644, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:15:05.901647-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "entry_ask": 18.5, "entry_bid": 17.65, "entry_mode": "early", "entry_option_price": 18.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.7, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "matched_signals": 36, "recovery_stability_score": 0.593, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:10:01.726670-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "entry_ask": 19.2, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.26, "option_volume": 194.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "matched_signals": 36, "recovery_stability_score": 0.55, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:05:05.716618-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:00:02.542633-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:55:05.812781-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "matched_signals": 36, "recovery_stability_score": 0.674, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:50:02.695273-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:45:02.722635-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:40:04.426517-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "matched_signals": 35, "recovery_stability_score": 0.567, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.764, "early_reclaim_pct": 74.7, "matched_signals": 36, "recovery_stability_score": 0.653, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.555, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:35:06.500524-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "entry_ask": 20.0, "entry_bid": 18.15, "entry_mode": "early", "entry_option_price": 19.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 9.7, "option_volume": 188.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "matched_signals": 40, "recovery_stability_score": 0.696, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608112006)

</details>
