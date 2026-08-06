# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 11:00:04 EDT`
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
- Equity: `$33,820.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$1,980.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   1     55     15757.5                 17737.5         2.86           3.22       58.15         58.96          bid_ask_mid                       3.22                bid_ask_mid                    True          1980.0                  12.57         91.18               34              0.66         31.86           30.86                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ISRG           86.84               38            0.59              1.56        374.53                72.98         0.661          pass              0.543             35.8                           0.344               12.33              1.068                                 ok            True                  False
  GEHC           94.29               35            0.56              0.28         70.12                58.07         0.633          pass              0.655             14.8                           0.195               12.74              1.565                                 ok            True                  False
   ROP           96.55               29            0.72              2.00        393.67                46.42         0.599          pass              0.708             40.4                           0.420               10.29              0.802                                 ok            True                  False
  MNST           93.10               29            0.57              0.38         94.30                25.70         0.518          pass              0.682             51.4                           0.617                0.38             -0.066                                 ok            True                  False
   PEP           83.33               24            0.68              0.66        138.50                25.05         0.518          pass              0.359             41.7                           0.439                2.13              0.072                                 ok            True                  False
  WDAY           85.19               27            2.27              2.71        169.47                67.74         0.515          pass              0.474             56.9                           0.649               30.42              2.474                                 ok            True                  False
  ADSK           80.65               31            1.08              1.82        239.25                45.93         0.507          pass              0.420             70.7                           0.743               15.67              1.223                                 ok            True                  False
  DRAM           77.42               31            2.50              0.94         53.34               109.54         0.591          pass              0.418             72.8                           0.643              -10.13             -0.095           downtrend_blocked_streak           False                  False
   MAR           95.83               24            1.00              2.54        360.22                38.12         0.566          pass              0.592             14.1                           0.206               -1.86             -0.702 downtrend_blocked_slope_and_streak           False                  False
   EXC           94.44               18            0.87              0.28         45.64                21.34         0.543          pass              0.567             24.6                           0.383               -4.06             -0.493            downtrend_blocked_slope           False                  False
  VRSK           93.75               16            2.15              2.84        187.53                43.94         0.540          pass              0.561             33.6                           0.450               -4.39             -0.882 downtrend_blocked_slope_and_streak           False                  False
  CTAS           93.75               32            0.70              0.99        200.98                37.87         0.522          pass              0.655             29.9                           0.404               -1.60             -0.396 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-06T11:00:04.213482-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                          {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "entry_ask": 31.85, "entry_bid": 30.45, "entry_mode": "early", "entry_option_price": 31.15, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 4.49, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.767, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "matched_signals": 46, "recovery_stability_score": 0.767, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-06T10:55:01.181311-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "entry_ask": 12.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.725, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 12.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "top_candidates": [{"current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "matched_signals": 38, "recovery_stability_score": 0.675, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:50:02.211616-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "entry_ask": 12.45, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 11.825, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 10.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "top_candidates": [{"current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "matched_signals": 38, "recovery_stability_score": 0.67, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.724, "early_reclaim_pct": 80.9, "matched_signals": 46, "recovery_stability_score": 0.838, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:45:03.090387-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:40:02.578783-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:35:01.175064-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:30:01.363128-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:25:06.040333-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:20:04.089785-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:15:02.220237-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806110004)

</details>
