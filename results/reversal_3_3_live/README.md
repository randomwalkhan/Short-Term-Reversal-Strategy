# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 15:05:06 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$13,976.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   0     96     13920.0                 13920.0         1.45           1.45       33.12         33.08          bid_ask_mid                       1.45                bid_ask_mid                    True             0.0                    0.0         100.0               15              0.76         30.37           30.71                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  UPRO           93.33               15            1.82              1.80        140.62                55.10         0.621            pass              0.522             23.7                           0.311                0.28              0.029                      ok            True                  False
   KDP          100.00               13            0.97              0.23         33.27                28.32         0.608            pass              0.571             30.1                           0.395                7.74              1.064                      ok            True                  False
   WBD           80.00                5            1.29              0.24         26.71                21.87         0.607            pass              0.181             40.0                           0.422                0.86              0.094                      ok           False                  False
  AVGO           69.23               13            3.16              8.18        365.83                71.90         0.602            pass              0.080              0.0                           0.196               -8.83             -0.987 downtrend_blocked_slope           False                  False
   TXN           84.62               13            2.87              6.00        295.84                67.74         0.571            pass              0.227              8.8                           0.209               -3.99             -0.939 downtrend_blocked_slope           False                  False
  PCAR           78.57               14            1.60              1.36        120.66                34.47         0.535            pass              0.154             24.6                           0.375                1.67              0.216                      ok           False                  False
    MU           87.50                8            6.90             49.89       1010.90               134.25         0.518            pass              0.277              8.6                           0.266               -7.88             -0.622 downtrend_blocked_slope           False                  False
   ADI           66.67                6            3.66              9.96        384.71                61.24         0.516            pass              0.081              9.8                           0.247               -9.58             -1.303 downtrend_blocked_slope           False                  False
  NXPI           81.82               11            3.25              6.36        276.46                63.41         0.513            pass              0.171             21.5                           0.281               -9.12             -1.397 downtrend_blocked_slope           False                  False
  CDNS           94.44               36            0.53              1.39        377.13                42.41         0.502            pass              0.826             72.5                           0.591               -3.56             -0.373 downtrend_blocked_slope           False                  False
 CMCSA           57.14                7            1.41              0.23         23.63                36.53         0.498 below_threshold              0.242             64.0                           0.466                4.51              0.845                      ok           False                  False
  ODFL           86.49               37            0.52              0.80        217.62                43.21         0.497 below_threshold              0.519             38.7                           0.422               -0.71             -0.103                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-02T15:05:06.760446-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-02T15:00:02.818576-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-02T14:55:03.805247-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-02T14:50:01.813724-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 13920.0, "asset_type": "option", "contract_symbol": "KDP260821C00033000", "contracts": 96, "early_entry_score": 0.63, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 2956.0, "option_spread_pct": 13.79, "option_volume": 194.0, "success_rate": 100.0, "ticker": "KDP", "timing_score": 0.609}
2026-07-02T14:50:01.813724-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.47, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 22.49, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.614}
2026-07-02T14:50:01.813724-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-02", "training_samples": 5311, "window": 5}
2026-07-02T12:00:01.950437-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:55:04.784699-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:50:04.781471-04:00 early_entry_1150      early_entry_shadow  {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "entry_ask": 14.2, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 2.86, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:45:01.785204-04:00 early_entry_1145      early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "entry_ask": 14.9, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.87, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "matched_signals": 44, "recovery_stability_score": 0.678, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702150506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702150506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702150506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702150506)

</details>
