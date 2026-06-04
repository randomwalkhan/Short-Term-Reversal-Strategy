# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-04 15:15:04 EDT`
Last processed slot: `manual`

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

- Cash: `$22,561.75`
- Equity: `$33,946.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$-625.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260717C00270000       2026-06-04                   0      2     12010.0                 11385.0        60.05          56.92      270.38         265.1          bid_ask_mid                      56.92                bid_ask_mid                    True          -625.0                   -5.2         94.74               19              3.62        161.75          162.38                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.44               36            0.79              9.08       1634.65                61.24         0.588          pass              0.675             19.1                           0.260               -1.55             -0.055                                 ok            True                  False
   TXN           95.65               23            1.01              2.18        307.65                42.91         0.547          pass              0.729             62.6                           0.439                0.19             -0.100                                 ok            True                  False
   ADI          100.00               17            1.79              5.48        435.32                44.48         0.539          pass              0.663             54.2                           0.632                8.28              0.944                                 ok            True                  False
  LRCX           88.46               26            1.08              2.60        342.60                54.10         0.513          pass              0.625             80.5                           0.704               16.40              1.372                                 ok            True                  False
   APP           84.21               38            1.15              4.61        568.86                74.91         0.511          pass              0.531             60.4                           0.692               17.00              2.315                                 ok            True                  False
   CSX           86.96               23            0.61              0.20         46.35                23.25         0.508          pass              0.476             50.9                           0.374                0.78              0.076                                 ok            True                  False
  PANW           91.89               37            0.80              1.57        279.76                59.60         0.507          pass              0.800             84.1                           0.773               12.78              1.681                                 ok            True                   True
  INTU           78.26               23            2.22              4.84        309.36               102.00         0.682          pass              0.255             33.3                           0.467              -20.68             -0.642            downtrend_blocked_slope           False                  False
  QCOM           88.89                9            3.09              5.40        247.69                96.24         0.654          pass              0.446             47.8                           0.607               19.64              1.336                                 ok           False                  False
  INTC           97.06               34            0.54              0.43        112.53                77.78         0.585          pass              0.889             90.1                           0.734               -5.77             -1.014 downtrend_blocked_slope_and_streak           False                  False
  ROST           94.12               34            0.48              0.78        232.29                44.04         0.558          pass              0.634             14.0                           0.210                6.30              0.306                                 ok           False                  False
  TEAM           93.18               44            0.50              0.35        101.38                88.72         0.551          pass              0.847             80.0                           0.467               17.16              2.894                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-04T15:10:05.730387-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T15:05:04.544660-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T15:00:02.553545-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T14:55:06.549299-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T14:50:05.645592-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SOXL260717C00270000", "contracts": 2, "early_entry_score": 0.751, "entry_mode": "regular", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 5.33, "option_volume": 64.0, "success_rate": 94.74, "ticker": "SOXL", "timing_score": 0.565}
2026-06-04T14:50:05.645592-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.634, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 16.0, "option_spread_pct": 7.13, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.593}
2026-06-04T14:50:05.645592-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-04", "training_samples": 5195, "window": 5}
2026-06-04T11:33:58.038645-04:00 early_entry_1130      early_entry_shadow  {"contract_symbol": "SNPS260717C00510000", "current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "entry_ask": 29.4, "entry_bid": 27.7, "entry_mode": "early", "entry_option_price": 28.55, "hypothetical_budget": 17285.88, "hypothetical_contracts": 6, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 124.0, "option_spread_pct": 5.95, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "matched_signals": 34, "recovery_stability_score": 0.81, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:52:01.009972-04:00 early_entry_1050      early_entry_shadow {"contract_symbol": "ASML260717C01640000", "current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "entry_ask": 176.5, "entry_bid": 162.4, "entry_mode": "early", "entry_option_price": 169.45, "hypothetical_budget": 17285.88, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 116.0, "option_spread_pct": 8.32, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "matched_signals": 30, "recovery_stability_score": 0.7, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:07:26.962733-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "entry_ask": 19.1, "entry_bid": 17.1, "entry_mode": "early", "entry_option_price": 18.1, "hypothetical_budget": 17285.88, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1675.0, "option_spread_pct": 11.05, "option_volume": 84.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "top_candidates": [{"current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "matched_signals": 30, "recovery_stability_score": 0.831, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260604151504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260604151504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260604151504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260604151504)

</details>
