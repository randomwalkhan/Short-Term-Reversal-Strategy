# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 11:10:04 EDT`
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

- Cash: `$16,083.25`
- Equity: `$33,545.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$1,705.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   1     55     15757.5                 17462.5         2.86           3.18       58.15          58.9          bid_ask_mid                       3.18                bid_ask_mid                    True          1705.0                  10.82         91.18               34              0.66         31.86           30.79                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ISRG           86.84               38            0.54              1.41        374.60                72.98         0.665          pass              0.562             42.2                           0.428               12.40              1.070                                 ok            True                  False
  GEHC           94.44               36            0.51              0.25         70.13                58.07         0.630          pass              0.689             22.3                           0.217               12.79              1.568                                 ok            True                  False
   ROP           96.55               29            0.79              2.18        393.60                46.42         0.595          pass              0.692             35.2                           0.420               10.22              0.799                                 ok            True                  False
   PEP           83.33               24            0.65              0.63        138.51                25.05         0.521          pass              0.368             44.5                           0.499                2.17              0.074                                 ok            True                  False
  ADSK           81.25               32            0.89              1.50        239.39                45.93         0.514          pass              0.459             75.9                           0.748               15.90              1.232                                 ok            True                  False
  WDAY           85.19               27            2.33              2.78        169.44                67.74         0.511          pass              0.470             55.8                           0.617               30.34              2.472                                 ok            True                  False
  ALNY           85.71               28            1.33              2.13        227.81               127.65         0.823          pass              0.463             36.1                           0.360              -16.02             -2.867            downtrend_blocked_slope           False                  False
  AMAT           91.89               37            0.23              0.87        533.87                86.87         0.689          pass              0.765             66.2                           0.302               -5.29              0.182           downtrend_blocked_streak           False                  False
  DRAM           78.12               32            1.46              0.55         53.50               109.54         0.657          pass              0.465             84.1                           0.852               -9.17             -0.046           downtrend_blocked_streak           False                  False
   MAR           95.83               24            1.00              2.52        360.23                38.12         0.566          pass              0.594             14.7                           0.195               -1.85             -0.701 downtrend_blocked_slope_and_streak           False                  False
  CTAS           92.31               26            0.83              1.17        200.90                37.87         0.552          pass              0.541             16.9                           0.306               -1.73             -0.402 downtrend_blocked_slope_and_streak           False                  False
   EXC           94.44               18            0.81              0.26         45.65                21.34         0.547          pass              0.584             30.2                           0.424               -4.00             -0.490            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-06T11:10:04.141911-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                         {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "entry_ask": 32.9, "entry_bid": 31.7, "entry_mode": "early", "entry_option_price": 32.3, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 3.72, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "matched_signals": 46, "recovery_stability_score": 0.657, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-06T11:05:02.141767-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 67.4, "entry_ask": 29.2, "entry_bid": 23.1, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 23.33, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.677, "shadow_only": true, "success_rate": 94.74, "ticker": "IDXX", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 67.4, "matched_signals": 38, "recovery_stability_score": 0.677, "success_rate": 94.74, "ticker": "IDXX", "timing_score": 0.425, "trend_health_status": "ok"}, {"current_drop_pct": 1.0, "early_entry_score": 0.714, "early_reclaim_pct": 78.0, "matched_signals": 46, "recovery_stability_score": 0.725, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T11:00:04.213482-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "entry_ask": 31.85, "entry_bid": 30.45, "entry_mode": "early", "entry_option_price": 31.15, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 4.49, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.767, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "matched_signals": 46, "recovery_stability_score": 0.767, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-06T10:55:01.181311-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                   {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "entry_ask": 12.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.725, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 12.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "top_candidates": [{"current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "matched_signals": 38, "recovery_stability_score": 0.675, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:50:02.211616-04:00 early_entry_1050 early_entry_shadow                             {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "entry_ask": 12.45, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 11.825, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 10.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "top_candidates": [{"current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "matched_signals": 38, "recovery_stability_score": 0.67, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.724, "early_reclaim_pct": 80.9, "matched_signals": 46, "recovery_stability_score": 0.838, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:45:03.090387-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:40:02.578783-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:35:01.175064-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:30:01.363128-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:25:06.040333-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806111004)

</details>
