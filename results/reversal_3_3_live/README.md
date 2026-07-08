# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-08 15:25:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$431.75`
- Equity: `$26,401.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$655.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option  CSX260821C00047500       2026-07-07                   1     54     12690.0                 13095.0         2.35           2.42       48.48         48.47          bid_ask_mid                       2.42                bid_ask_mid                    True           405.0                   3.19          91.3               23              0.68         28.35           30.27                  21.52                2967.0           20.0               0.09                      ok
  PAYX     option         option PAYX260821C00110000       2026-07-08                   0     50     12625.0                 12875.0         2.53           2.58      106.22        106.61          bid_ask_mid                       2.58                bid_ask_mid                    True           250.0                   1.98         100.0               12              1.76         27.87           27.60                  32.70                 820.0          338.0               0.06                      ok
```

## Today's Closed Trades (2026-07-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               13            0.68              0.29         60.10                30.26         0.604          pass              0.664             61.3                           0.461               -1.23             -0.171                  ok            True                  False
  UPRO           86.96               23            1.04              1.04        141.77                46.91         0.578          pass              0.537             69.0                           0.621                4.18              0.706                  ok            True                  False
  GILD           89.47               19            0.98              0.93        135.96                35.29         0.564          pass              0.454             28.5                           0.203                7.98              0.830                  ok            True                  False
   KDP          100.00               12            1.06              0.23         31.39                33.17         0.563          pass              0.628             52.8                           0.647                1.64              0.055                  ok            True                  False
  PAYX          100.00               17            1.40              1.06        107.67                32.70         0.549          pass              0.656             51.4                           0.604                8.79              1.178                  ok            True                  False
   ADP           94.12               17            1.42              2.44        244.55                31.95         0.539          pass              0.587             36.5                           0.434                9.80              1.294                  ok            True                  False
  PCAR           84.62               26            1.00              0.87        124.09                37.78         0.526          pass              0.456             58.0                           0.635                5.51              0.556                  ok            True                  False
  GOOG           81.82               11            2.14              5.44        361.29                34.43         0.519          pass              0.146             12.9                           0.380                2.82              0.623                  ok            True                  False
   XEL          100.00               10            1.21              0.68         80.38                21.69         0.516          pass              0.470              6.3                           0.263               -0.79             -0.150                  ok            True                  False
   APP           85.37               41            0.92              3.39        526.53                76.24         0.503          pass              0.624             76.9                           0.534               12.02              1.813                  ok            True                  False
  TMUS           85.71               14            1.87              2.42        183.69                35.69         0.503          pass              0.355             41.9                           0.250               -1.78             -0.057                  ok            True                  False
 CMCSA           69.23               13            0.32              0.05         23.39                30.25         0.560          pass              0.251             58.3                           0.326                3.74              0.523                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-08T15:10:05.590905-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-08T15:05:01.586553-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-08T15:00:04.551542-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-08T14:55:01.624651-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-08T14:50:06.638018-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 12625.0, "asset_type": "option", "contract_symbol": "PAYX260821C00110000", "contracts": 50, "early_entry_score": 0.586, "entry_mode": "regular", "entry_option_price": 2.525, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 820.0, "option_spread_pct": 5.94, "option_volume": 338.0, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.558}
2026-07-08T14:50:06.638018-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 27.1, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.578}
2026-07-08T14:50:06.638018-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.647, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 102.0, "option_spread_pct": 13.04, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.606}
2026-07-08T14:50:06.638018-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-08", "training_samples": 5443, "window": 5}
2026-07-08T12:00:02.532330-04:00 early_entry_1200      early_entry_shadow                                  {"contract_symbol": "TMUS260821C00185000", "current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "entry_ask": 9.7, "entry_bid": 9.2, "entry_mode": "early", "entry_option_price": 9.45, "hypothetical_budget": 6528.38, "hypothetical_contracts": 6, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 378.0, "option_spread_pct": 5.29, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "matched_signals": 35, "recovery_stability_score": 0.622, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T11:57:36.728497-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "entry_ask": 24.7, "entry_bid": 21.4, "entry_mode": "early", "entry_option_price": 23.05, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 53.0, "option_spread_pct": 14.32, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "matched_signals": 45, "recovery_stability_score": 0.636, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260708152502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260708152502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260708152502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260708152502)

</details>
