# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 13:35:04 EDT`
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

- Cash: `$68,764.30`
- Equity: `$128,604.30`
- Realized PnL: `$122,764.30`
- Unrealized PnL: `$-4,160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 59840.0         20.0           18.7       220.6        219.73          bid_ask_mid                       18.7                bid_ask_mid                    True         -4160.0                   -6.5         100.0               12              3.08          70.9           69.55                  47.89                 302.0           39.0                0.1                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.91               11            0.89              0.39         62.18                25.51         0.606          pass              0.430             24.0                           0.226               -1.24             -0.106                                 ok            True                  False
  MSTR           90.91               33            1.32              1.30        140.84                70.33         0.589          pass              0.599             31.9                           0.371               -2.58             -0.158                                 ok            True                  False
 CMCSA           90.91               11            0.94              0.14         21.78                26.07         0.582          pass              0.485             43.1                           0.365                2.78              0.239                                 ok            True                  False
   KHC           87.50               24            0.99              0.17         23.99                36.33         0.555          pass              0.403             18.1                           0.224                4.94              0.628                                 ok            True                  False
   KDP           96.15               26            0.50              0.12         34.81                24.92         0.532          pass              0.722             53.9                           0.543                4.73              0.337                                 ok            True                  False
   PEP           80.00               25            0.63              0.59        133.25                25.80         0.522          pass              0.299             49.0                           0.530                2.62              0.403                                 ok            True                  False
    ZS           90.62               32            1.45              2.64        259.02                56.99         0.520          pass              0.507              8.4                           0.139               16.12              2.329                                 ok            True                  False
  TTWO           87.50               24            1.31              1.85        200.49                30.21         0.507          pass              0.361              5.7                           0.201               -1.29             -0.234                                 ok            True                  False
  TMUS           86.49               37            0.31              0.32        146.69                63.84         0.633          pass              0.681             88.3                           0.520               -7.24             -0.912            downtrend_blocked_slope           False                  False
   CEG           86.11               36            0.69              1.25        258.45                65.80         0.598          pass              0.578             60.7                           0.339               -7.99             -0.875 downtrend_blocked_slope_and_streak           False                  False
  MPWR           72.73               33            0.68              5.77       1209.42                59.51         0.573          pass              0.403             64.1                           0.397               -3.17             -0.590            downtrend_blocked_slope           False                  False
  PAYX           50.00                2            1.94              1.48        108.62                35.39         0.563          pass              0.107             16.9                           0.246               -0.13              0.271                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-28T12:00:04.408643-04:00 early_entry_1200 early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "matched_signals": 43, "recovery_stability_score": 0.759, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:55:06.476667-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "matched_signals": 44, "recovery_stability_score": 0.776, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:50:06.101583-04:00 early_entry_1150 early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:45:03.424860-04:00 early_entry_1145 early_entry_shadow  {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "entry_ask": 18.3, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 15.29, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "matched_signals": 43, "recovery_stability_score": 0.769, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:40:06.443481-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:35:05.885505-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:30:05.433292-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:25:02.485358-04:00 early_entry_1125 early_entry_shadow    {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "entry_ask": 18.3, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.9, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.795, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.795, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:20:06.604106-04:00 early_entry_1120 early_entry_shadow    {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "entry_ask": 18.3, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.9, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.803, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:15:06.636724-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028133504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028133504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028133504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028133504)

</details>
