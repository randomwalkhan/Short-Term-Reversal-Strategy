# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 15:50:04 EST`
Last processed slot: `manage_1600`

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

- Cash: `$58,029.80`
- Equity: `$109,114.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$-2,125.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP261218C00400000       2026-11-17                   0     17     53210.0                 51085.0         31.3          30.05      402.79        397.79          bid_ask_mid                      30.05                bid_ask_mid                    True         -2125.0                  -3.99         94.12               17              2.99         63.29           66.32                  119.5                1252.0          197.0               0.01                      ok
```

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           96.15               26            1.23              6.01        698.07                77.90         0.721          pass              0.680             33.6                           0.536                2.98              0.330                  ok            True                  False
   ADI           91.18               34            0.73              1.97        382.33                67.56         0.606          pass              0.658             46.6                           0.427               -9.39             -0.147                  ok            True                  False
  MDLZ           92.31               13            1.12              0.53         67.31                29.55         0.602          pass              0.412              1.3                           0.188                2.56              0.171                  ok            True                  False
   TXN           93.33               30            0.75              1.55        293.54                59.80         0.595          pass              0.742             64.5                           0.559               -6.56             -0.018                  ok            True                   True
   CSX           80.00               10            1.68              0.61         51.77                34.26         0.594          pass              0.086              8.9                           0.177                0.86              0.245                  ok            True                  False
 CMCSA           91.30               23            0.64              0.12         25.55                34.44         0.579          pass              0.581             45.0                           0.333                7.46              0.507                  ok            True                  False
  QCOM           86.36               22            2.04              2.40        167.49                68.75         0.578          pass              0.438             43.4                           0.431                0.40              0.331                  ok            True                  False
   ADP           80.00               10            1.68              3.69        311.85                28.40         0.572          pass              0.066              3.0                           0.253                4.10              0.364                  ok            True                  False
  SBUX           86.67               15            1.11              0.85        108.36                31.47         0.570          pass              0.353             28.4                           0.354                3.22              0.192                  ok            True                  False
  TMUS           83.33               30            0.78              0.92        169.61                46.99         0.562          pass              0.278              0.0                           0.275                9.25              0.913                  ok            True                  False
  ODFL           80.95               21            1.50              1.83        173.50                43.33         0.559          pass              0.253             32.8                           0.550               -3.38             -0.128                  ok            True                  False
  CTAS           95.24               21            0.87              1.36        223.58                28.21         0.553          pass              0.586             19.1                           0.378               -0.46             -0.028                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:50:06.628486-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 53210.0, "asset_type": "option", "contract_symbol": "APP261218C00400000", "contracts": 17, "early_entry_score": 0.66, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 1252.0, "option_spread_pct": 1.28, "option_volume": 197.0, "success_rate": 94.12, "ticker": "APP", "timing_score": 0.778}
2026-11-17T14:50:06.628486-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-17", "training_samples": 6239, "window": 5}
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:55:01.833366-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:50:06.047053-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:45:03.924491-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "entry_ask": 23.75, "entry_bid": 21.55, "entry_mode": "early", "entry_option_price": 22.65, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 9.71, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "matched_signals": 32, "recovery_stability_score": 0.589, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117155004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117155004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117155004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117155004)

</details>
