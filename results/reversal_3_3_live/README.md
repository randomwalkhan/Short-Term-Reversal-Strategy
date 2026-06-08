# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 11:10:01 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$33,210.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15600.0         9.85           9.75       98.17         98.88          bid_ask_mid                       9.75                bid_ask_mid                    True          -160.0                  -1.02         95.65               23              3.29          79.1           78.98                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  TEAM           95.24               42            0.60              0.42         99.29                86.36         0.641          pass              0.911             82.2                           0.638               15.75              1.855                       ok            True                   True
   TRI           82.35               17            1.94              1.17         85.54                69.04         0.636          pass              0.270             32.4                           0.365               -1.74              0.148                       ok            True                  False
  CRWD           92.11               38            0.64              2.99        669.74                64.90         0.564          pass              0.748             60.6                           0.276                2.86              1.009                       ok            True                  False
  MSFT           85.19               27            0.94              2.74        415.49                34.82         0.555          pass              0.388             27.1                           0.395               -1.39              0.126                       ok            True                  False
  PANW           91.67               36            0.88              1.67        271.33                60.15         0.544          pass              0.745             68.7                           0.550                6.62              1.225                       ok            True                   True
  FAST           94.74               19            1.18              0.38         46.63                21.36         0.526          pass              0.581             25.3                           0.180                5.23              0.685                       ok            True                  False
    ZS           81.58               38            0.63              0.58        130.53               157.69         0.894          pass              0.536             72.7                           0.380              -28.74             -2.386  downtrend_blocked_slope           False                  False
  PAYX          100.00               25            0.15              0.11        100.48                33.39         0.602          pass              0.837             92.3                           0.851                3.48              0.595                       ok           False                  False
  REGN           75.00               12            1.90              8.47        631.82                43.33         0.580          pass              0.128             19.0                           0.360               -2.43             -0.122 downtrend_blocked_streak           False                  False
   CEG           84.21               38            0.21              0.38        254.67                55.63         0.575          pass              0.622             88.5                           0.697              -11.03             -1.469  downtrend_blocked_slope           False                  False
   EXC           85.71                7            1.26              0.40         45.58                19.68         0.567          pass              0.244             11.5                           0.245               -1.36             -0.211                       ok           False                  False
   AEP           69.23               13            1.05              0.94        128.74                24.28         0.555          pass              0.195             39.7                           0.366               -2.89             -0.249 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-08T11:10:01.726670-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "entry_ask": 19.2, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.26, "option_volume": 194.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.745, "early_reclaim_pct": 68.7, "matched_signals": 36, "recovery_stability_score": 0.55, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.544, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:05:05.716618-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:00:02.542633-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:55:05.812781-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.84, "early_reclaim_pct": 72.6, "matched_signals": 36, "recovery_stability_score": 0.674, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:50:02.695273-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:45:02.722635-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T10:40:04.426517-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 24.44, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 67.6, "matched_signals": 35, "recovery_stability_score": 0.567, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.487, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.764, "early_reclaim_pct": 74.7, "matched_signals": 36, "recovery_stability_score": 0.653, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.555, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:35:06.500524-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "entry_ask": 20.0, "entry_bid": 18.15, "entry_mode": "early", "entry_option_price": 19.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 9.7, "option_volume": 188.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.8, "matched_signals": 40, "recovery_stability_score": 0.696, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T10:30:04.814654-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.53, "early_entry_score": 0.836, "early_reclaim_pct": 71.3, "entry_ask": 9.9, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.9, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 22.47, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.836, "early_reclaim_pct": 71.3, "matched_signals": 36, "recovery_stability_score": 0.657, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:25:01.721372-04:00 early_entry_1025 early_entry_shadow   {"contract_symbol": "DASH260717C00155000", "current_drop_pct": 0.62, "early_entry_score": 0.835, "early_reclaim_pct": 82.2, "entry_ask": 13.05, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.275, "hypothetical_budget": 8805.38, "hypothetical_contracts": 7, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1085.0, "option_spread_pct": 12.63, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.835, "early_reclaim_pct": 82.2, "matched_signals": 41, "recovery_stability_score": 0.701, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.501, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.704, "early_reclaim_pct": 73.4, "matched_signals": 38, "recovery_stability_score": 0.641, "success_rate": 89.47, "ticker": "VRTX", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608111001)

</details>
