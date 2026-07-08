# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-08 13:10:02 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$13,056.75`
- Equity: `$25,881.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260821C00047500       2026-07-07                   1     54     12690.0                 12825.0         2.35           2.38       48.48         48.21          bid_ask_mid                       2.38                bid_ask_mid                    True           135.0                   1.06          91.3               23              0.68         28.35           31.74                  21.52                2967.0           20.0               0.09                      ok
```

## Today's Closed Trades (2026-07-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               14            0.61              0.26         60.11                30.26         0.603          pass              0.682             65.1                           0.568               -1.16             -0.168                  ok            True                  False
  UPRO           90.00               20            1.34              1.33        141.64                46.91         0.580          pass              0.572             60.1                           0.736                3.87              0.692                  ok            True                  False
  PAYX          100.00               12            1.73              1.31        107.56                32.70         0.560          pass              0.590             40.1                           0.302                8.43              1.163                  ok            True                  False
   ADP           91.67               12            1.60              2.75        244.42                31.95         0.557          pass              0.466             28.6                           0.240                9.60              1.286                  ok            True                  False
  GILD           88.00               25            0.73              0.69        136.06                35.29         0.540          pass              0.508             46.8                           0.382                8.25              0.841                  ok            True                  False
  PCAR           80.95               21            1.37              1.20        123.95                37.78         0.527          pass              0.278             42.0                           0.688                5.11              0.538                  ok            True                  False
  TMUS           88.24               17            1.34              1.74        183.99                35.69         0.522          pass              0.493             58.3                           0.297               -1.26             -0.033                  ok            True                  False
  GOOG           85.00               20            1.56              3.96        361.92                34.43         0.512          pass              0.297             15.3                           0.280                3.43              0.649                  ok            True                  False
   CSX           91.67               24            0.62              0.21         48.42                21.11         0.510          pass              0.553             32.6                           0.452                4.44              0.516                  ok            True                  False
  IDXX           87.50               16            2.11              8.44        566.63                37.15         0.501          pass              0.416             42.1                           0.667                3.12              0.349                  ok            True                  False
  META           69.23               13            1.80              7.74        612.26                50.92         0.579          pass              0.161             27.9                           0.437                7.53              1.146                  ok           False                  False
   KDP          100.00                7            1.48              0.33         31.35                33.17         0.568          pass              0.560             34.5                           0.385                1.22              0.036                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-08T12:00:02.532330-04:00 early_entry_1200 early_entry_shadow                                  {"contract_symbol": "TMUS260821C00185000", "current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "entry_ask": 9.7, "entry_bid": 9.2, "entry_mode": "early", "entry_option_price": 9.45, "hypothetical_budget": 6528.38, "hypothetical_contracts": 6, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 378.0, "option_spread_pct": 5.29, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "matched_signals": 35, "recovery_stability_score": 0.622, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T11:57:36.728497-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "entry_ask": 24.7, "entry_bid": 21.4, "entry_mode": "early", "entry_option_price": 23.05, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 53.0, "option_spread_pct": 14.32, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "matched_signals": 45, "recovery_stability_score": 0.636, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T11:17:31.826171-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-08T10:00:23.726420-04:00 early_entry_1000 early_entry_shadow              {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "entry_ask": 24.2, "entry_bid": 21.6, "entry_mode": "early", "entry_option_price": 22.9, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 53.0, "option_spread_pct": 11.35, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "matched_signals": 43, "recovery_stability_score": 0.607, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T00:00:05.492385-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-07T15:10:01.115389-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T15:05:02.177767-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T15:00:05.200618-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T14:55:05.093959-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T14:50:02.270348-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-07", "training_samples": 5385, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260708131002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260708131002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260708131002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260708131002)

</details>
