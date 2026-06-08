# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 12:00:05 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$32,490.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-880.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 14880.0         9.85            9.3       98.17         97.65          bid_ask_mid                        9.3                bid_ask_mid                    True          -880.0                  -5.58         95.65               23              3.29          79.1           80.15                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           93.75               32            1.82              1.27         98.93                86.36         0.624            pass              0.713             45.8                           0.254               14.32              1.798                      ok            True                  False
  PAYX          100.00               13            1.22              0.86        100.16                33.39         0.609            pass              0.593             37.2                           0.220                2.37              0.546                      ok            True                  False
  CRWD           80.00               15            2.37             11.15        666.24                64.90         0.580            pass              0.107              5.2                           0.167                1.06              0.929                      ok            True                  False
  ROST           93.94               33            0.59              0.96        229.96                43.36         0.578            pass              0.612              9.9                           0.185               -2.47             -0.143                      ok            True                  False
  PANW           85.00               20            2.00              3.81        270.42                60.15         0.570            pass              0.343             28.6                           0.201                5.41              1.173                      ok            True                  False
  FAST           94.12               17            1.26              0.41         46.61                21.36         0.533            pass              0.536             19.8                           0.271                5.14              0.681                      ok            True                  False
   ADP           96.55               29            0.95              1.54        231.29                32.55         0.503            pass              0.724             49.0                           0.299                1.97              0.597                      ok            True                  False
  WDAY           88.89               36            1.00              1.01        143.85                69.97         0.500 below_threshold              0.621             53.6                           0.334               11.46              1.859                      ok            True                  False
    ZS           81.82               33            1.23              1.13        130.30               157.69         0.891            pass              0.432             47.1                           0.289              -29.17             -2.413 downtrend_blocked_slope           False                  False
   TRI           76.92               13            2.51              1.51         85.39                69.04         0.618            pass              0.119             12.5                           0.154               -2.31              0.122                      ok           False                  False
  MSFT           72.73               11            1.56              4.54        414.72                34.82         0.605            pass              0.067              0.0                           0.207               -2.00              0.098                      ok           False                  False
   CEG           84.21               38            0.16              0.29        254.71                55.63         0.578            pass              0.631             91.3                           0.734              -10.99             -1.467 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:50:04.863668-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:45:02.732022-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:40:03.636153-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:35:06.615496-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:30:04.779379-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:25:01.866024-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "entry_ask": 9.7, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 20.45, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.609, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "matched_signals": 36, "recovery_stability_score": 0.609, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T11:20:06.683285-04:00 early_entry_1120 early_entry_shadow                           {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "entry_ask": 18.45, "entry_bid": 17.55, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 5.0, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "matched_signals": 36, "recovery_stability_score": 0.644, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T11:15:05.901647-04:00 early_entry_1115 early_entry_shadow                        {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "entry_ask": 18.5, "entry_bid": 17.65, "entry_mode": "early", "entry_option_price": 18.075, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 4.7, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.747, "early_reclaim_pct": 69.3, "matched_signals": 36, "recovery_stability_score": 0.593, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608120005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608120005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608120005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608120005)

</details>
