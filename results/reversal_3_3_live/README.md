# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 11:15:05 EDT`
Last processed slot: `early_entry_1115`

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
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15440.0         9.85           9.65       98.17         98.79          bid_ask_mid                       9.65                bid_ask_mid                    True          -320.0                  -2.03         95.65               23              3.29          79.1            78.7                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   TRI           81.25               16            1.96              1.18         85.53                69.04         0.639          pass              0.232             31.6                           0.339               -1.76              0.147                       ok            True                  False
  TEAM           95.24               42            0.68              0.47         99.27                86.36         0.635          pass              0.903             79.9                           0.607               15.66              1.851                       ok            True                   True
  CRWD           91.18               34            0.93              4.39        669.14                64.90         0.570          pass              0.642             42.2                           0.207                2.55              0.996                       ok            True                  False
  MSFT           85.19               27            0.90              2.62        415.55                34.82         0.557          pass              0.399             30.4                           0.426               -1.35              0.128                       ok            True                  False
  PANW           91.67               36            0.86              1.64        271.35                60.15         0.545          pass              0.747             69.3                           0.593                6.64              1.225                       ok            True                   True
  FAST           94.12               17            1.24              0.41         46.62                21.36         0.535          pass              0.540             21.2                           0.152                5.17              0.682                       ok            True                  False
    ZS           82.05               39            0.53              0.49        130.57               157.69         0.895          pass              0.569             77.2                           0.546              -28.67             -2.381  downtrend_blocked_slope           False                  False
  PAYX          100.00               25            0.24              0.17        100.46                33.39         0.596          pass              0.823             87.8                           0.801                3.39              0.591                       ok           False                  False
   CEG           84.21               38            0.22              0.39        254.66                55.63         0.575          pass              0.621             88.3                           0.682              -11.04             -1.470  downtrend_blocked_slope           False                  False
  REGN           66.67                9            2.23              9.91        631.20                43.33         0.568          pass              0.073              5.3                           0.223               -2.75             -0.137 downtrend_blocked_streak           False                  False
   EXC           85.71                7            1.29              0.41         45.57                19.68         0.565          pass              0.237              9.2                           0.222               -1.40             -0.212                       ok           False                  False
  ROST           95.00               40            0.26              0.41        230.19                43.36         0.555          pass              0.839             61.2                           0.376               -2.14             -0.127                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-08T11:15:05.901647-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "entry_ask": 18.5, "entry_bid": 17.65, "entry_mode": "early", "entry_option_price": 18.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.7, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "matched_signals": 36, "recovery_stability_score": 0.593, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:10:01.726670-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "entry_ask": 19.2, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.26, "option_volume": 194.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "matched_signals": 36, "recovery_stability_score": 0.55, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:05:05.716618-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:00:02.542633-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:55:05.812781-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "matched_signals": 36, "recovery_stability_score": 0.674, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:50:02.695273-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:45:02.722635-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:40:04.426517-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "matched_signals": 35, "recovery_stability_score": 0.567, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.764, "early_reclaim_pct": 74.7, "matched_signals": 36, "recovery_stability_score": 0.653, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.555, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:35:06.500524-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "entry_ask": 20.0, "entry_bid": 18.15, "entry_mode": "early", "entry_option_price": 19.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 9.7, "option_volume": 188.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "matched_signals": 40, "recovery_stability_score": 0.696, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T10:30:04.814654-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.53, "early_entry_score": 0.836, "early_reclaim_pct": 71.3, "entry_ask": 9.9, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.9, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 22.47, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.836, "early_reclaim_pct": 71.3, "matched_signals": 36, "recovery_stability_score": 0.657, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608111505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608111505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608111505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608111505)

</details>
