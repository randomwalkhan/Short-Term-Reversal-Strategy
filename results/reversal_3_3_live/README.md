# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 11:30:04 EDT`
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
- Equity: `$33,050.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-320.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15440.0         9.85           9.65       98.17         98.37          bid_ask_mid                       9.65                bid_ask_mid                    True          -320.0                  -2.03         95.65               23              3.29          79.1           79.57                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  TEAM           94.59               37            1.11              0.77         99.14                86.36         0.639          pass              0.835             67.2                           0.412               15.16              1.832                       ok            True                  False
   TRI           83.33               18            1.84              1.11         85.57                69.04         0.637          pass              0.314             36.0                           0.449               -1.63              0.153                       ok            True                  False
  CRWD           83.33               18            1.73              8.13        667.54                64.90         0.613          pass              0.214              3.4                           0.153                1.72              0.959                       ok            True                  False
  MSFT           82.35               17            1.34              3.90        415.00                34.82         0.593          pass              0.169              0.0                           0.239               -1.79              0.108                       ok            True                  False
  PANW           88.00               25            1.47              2.79        270.85                60.15         0.575          pass              0.514             47.7                           0.416                5.99              1.197                       ok            True                  False
  FAST           93.75               16            1.33              0.43         46.60                21.36         0.536          pass              0.508             15.8                           0.173                5.08              0.678                       ok            True                  False
  WDAY           90.00               40            0.61              0.62        144.02                69.97         0.501          pass              0.732             71.8                           0.404               11.91              1.877                       ok            True                  False
    ZS           82.35               34            0.93              0.85        130.42               157.69         0.897          pass              0.493             60.2                           0.423              -28.95             -2.399  downtrend_blocked_slope           False                  False
  PAYX          100.00               23            0.43              0.30        100.40                33.39         0.596          pass              0.780             78.1                           0.614                3.20              0.582                       ok           False                  False
   CEG           84.21               38            0.22              0.40        254.66                55.63         0.574          pass              0.620             87.8                           0.691              -11.05             -1.470  downtrend_blocked_slope           False                  False
  REGN           66.67                9            2.16              9.63        631.32                43.33         0.572          pass              0.081              7.9                           0.215               -2.69             -0.134 downtrend_blocked_streak           False                  False
   AEP           70.00               10            1.18              1.06        128.68                24.28         0.567          pass              0.153             32.1                           0.288               -3.02             -0.255 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-06-08T11:30:04.779379-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:25:01.866024-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "entry_ask": 9.7, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 20.45, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.609, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "matched_signals": 36, "recovery_stability_score": 0.609, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T11:20:06.683285-04:00 early_entry_1120 early_entry_shadow                           {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "entry_ask": 18.45, "entry_bid": 17.55, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 5.0, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "matched_signals": 36, "recovery_stability_score": 0.644, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:15:05.901647-04:00 early_entry_1115 early_entry_shadow                        {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "entry_ask": 18.5, "entry_bid": 17.65, "entry_mode": "early", "entry_option_price": 18.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.7, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "matched_signals": 36, "recovery_stability_score": 0.593, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:10:01.726670-04:00 early_entry_1110 early_entry_shadow                            {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "entry_ask": 19.2, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.26, "option_volume": 194.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "matched_signals": 36, "recovery_stability_score": 0.55, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:05:05.716618-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:00:02.542633-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:55:05.812781-04:00 early_entry_1055 early_entry_shadow   {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "matched_signals": 36, "recovery_stability_score": 0.674, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:50:02.695273-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:45:02.722635-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608113004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608113004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608113004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608113004)

</details>
