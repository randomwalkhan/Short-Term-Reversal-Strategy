# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 16:00:05 EST`
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

- Cash: `$56,193.80`
- Equity: `$107,643.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$1,725.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00400000       2026-11-18                   0     15     49725.0                 51450.0        33.15           34.3      389.81        391.67          bid_ask_mid                       34.3                bid_ask_mid                    True          1725.0                   3.47         90.91               22              2.29         60.57           61.13                 121.47                4183.0           24.0               0.06                      ok
```

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           92.59               27            2.01              5.62        396.53               121.47         0.778          pass              0.605             25.9                           0.394               43.85              2.220                                 ok            True                  False
   TXN           91.30               23            1.13              2.34        294.86                59.80         0.611          pass              0.614             55.1                           0.702               -6.09              0.183                                 ok            True                  False
  COST           80.00               10            1.23              9.54       1105.99                22.66         0.575          pass              0.067              3.1                           0.159                4.78              0.601                                 ok            True                  False
   CEG           90.91               22            1.99              3.73        266.47                61.66         0.561          pass              0.474             15.7                           0.209                7.09              1.092                                 ok            True                  False
   ADP           87.50               24            0.88              1.90        307.47                28.72         0.541          pass              0.432             28.0                           0.235                0.67              0.187                                 ok            True                  False
  INTC           71.43               35            0.89              0.34         55.02               143.31         0.833          pass              0.465             71.7                           0.720               -6.16             -0.075           downtrend_blocked_streak           False                  False
  MRVL           75.86               29            2.14              2.23        147.78               124.48         0.695          pass              0.340             47.9                           0.656               -8.92              0.129                                 ok           False                  False
  MPWR           74.29               35            0.48              4.44       1315.47                97.00         0.691          pass              0.471             78.4                           0.603                3.96              1.061                                 ok           False                  False
    MU           68.75               32            1.04              5.19        710.19               106.43         0.679          pass              0.426             70.4                           0.701              -11.35              0.059           downtrend_blocked_streak           False                  False
  ALNY           55.56                9            4.54              4.97        154.37               110.55         0.664          pass              0.128             20.4                           0.313               -7.25             -0.156                                 ok           False                  False
  UPRO           86.21               29            0.89              0.79        126.20                70.97         0.616          pass              0.539             61.9                           0.501              -14.84             -0.698 downtrend_blocked_slope_and_streak           False                  False
   BKR           88.57               35            0.34              0.11         47.41                58.51         0.605          pass              0.684             76.1                           0.528               -4.70             -0.021                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:55:05.603926-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:50:05.341851-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 49725.0, "asset_type": "option", "contract_symbol": "APP270115C00400000", "contracts": 15, "early_entry_score": 0.497, "entry_mode": "regular", "entry_option_price": 33.15, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 4183.0, "option_spread_pct": 5.73, "option_volume": 24.0, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.787}
2026-11-18T14:50:05.341851-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-18", "training_samples": 6259, "window": 5}
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:55:05.147885-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:50:04.203803-05:00 early_entry_1150 early_entry_shadow      {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "entry_ask": 6.3, "entry_bid": 5.7, "entry_mode": "early", "entry_option_price": 6.0, "hypothetical_budget": 52959.4, "hypothetical_contracts": 88, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 10.0, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "matched_signals": 39, "recovery_stability_score": 0.7, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:45:05.124213-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "entry_ask": 6.1, "entry_bid": 5.6, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 52959.4, "hypothetical_contracts": 90, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 8.55, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "matched_signals": 39, "recovery_stability_score": 0.694, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118160005)

</details>
