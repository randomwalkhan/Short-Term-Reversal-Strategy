# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 10:50:02 EDT`
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
- Equity: `$33,683.25`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$1,842.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   1     55     15757.5                 17600.0         2.86            3.2       58.15         58.78          bid_ask_mid                        3.2                bid_ask_mid                    True          1842.5                  11.69         91.18               34              0.66         31.86           31.71                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  ISRG           86.84               38            0.65              1.70        374.47                72.98         0.658          pass              0.525             30.1                           0.278               12.27              1.065                       ok            True                  False
   ROP           96.55               29            0.77              2.13        393.62                46.42         0.596          pass              0.696             36.7                           0.429               10.24              0.800                       ok            True                  False
  MNST           88.24               17            0.98              0.65         94.18                25.70         0.565          pass              0.371             16.2                           0.249               -0.03             -0.085                       ok            True                  False
  ADSK           81.25               32            0.90              1.52        239.38                45.93         0.513          pass              0.458             75.6                           0.770               15.88              1.231                       ok            True                  False
   PEP           83.33               24            0.78              0.76        138.46                25.05         0.512          pass              0.335             33.7                           0.316                2.04              0.068                       ok            True                  False
  WDAY           85.19               27            2.38              2.85        169.42                67.74         0.507          pass              0.467             54.8                           0.700               30.27              2.469                       ok            True                  False
   HON           84.21               19            1.37              2.37        247.10                25.91         0.503          pass              0.238              5.0                           0.148               -0.63              0.084                       ok            True                  False
  SOXL           81.08               37            0.32              0.29        131.94               181.59         0.836          pass              0.532             79.7                           0.334              -16.41             -0.388 downtrend_blocked_streak           False                  False
  ALNY           84.62               26            1.45              2.32        227.72               127.65         0.828          pass              0.321              2.9                           0.077              -16.13             -2.873  downtrend_blocked_slope           False                  False
  AMAT           91.89               37            0.45              1.69        533.51                86.87         0.672          pass              0.833             89.6                           0.643               -5.50              0.172 downtrend_blocked_streak           False                  False
  GEHC           94.59               37            0.40              0.20         70.16                58.07         0.633          pass              0.685             17.6                           0.150               12.92              1.573                       ok           False                  False
  AMZN           75.00               20            1.62              3.15        276.07                61.64         0.632          pass              0.168             12.9                           0.227               16.80              2.327                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-06T10:50:02.211616-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "entry_ask": 12.45, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 11.825, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 10.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "top_candidates": [{"current_drop_pct": 1.44, "early_entry_score": 0.73, "early_reclaim_pct": 61.3, "matched_signals": 38, "recovery_stability_score": 0.67, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.363, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.724, "early_reclaim_pct": 80.9, "matched_signals": 46, "recovery_stability_score": 0.838, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:45:03.090387-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:40:02.578783-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:35:01.175064-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:30:01.363128-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:25:06.040333-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:20:04.089785-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:15:02.220237-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:10:03.068587-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:05:03.941894-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                               {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806105002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806105002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806105002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806105002)

</details>
