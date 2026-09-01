# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 14:50:05 EDT`
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

- Cash: `$23,958.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   0    144     23760.0                 23760.0         1.65           1.65       32.33         32.35          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0          87.5               16              1.99         38.72           38.72                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           80.95               21            3.50              4.76        192.13               115.35         0.697          pass              0.235             22.1                           0.236               14.95              1.384                      ok            True                  False
   TRI           93.75               32            0.87              0.65        107.04                60.77         0.593          pass              0.709             45.5                           0.283                8.10              0.528                      ok            True                  False
  PAYX          100.00               14            1.41              1.25        126.80                24.69         0.559          pass              0.536             17.7                           0.320                5.91              0.599                      ok            True                  False
  CPRT           87.50               16            1.99              0.46         32.79                40.13         0.554          pass              0.311              5.1                           0.197                2.00              0.065                      ok            True                  False
  SBUX           95.24               21            0.63              0.47        106.05                22.95         0.549          pass              0.595             22.1                           0.295               -2.17              0.033                      ok            True                  False
  CSCO           83.87               31            1.03              0.80        110.15                40.87         0.541          pass              0.378             27.0                           0.328               -3.14             -0.097                      ok            True                  False
 CMCSA           91.67               24            0.90              0.17         26.55                24.41         0.523          pass              0.474              5.9                           0.222                3.17              0.242                      ok            True                  False
  NVDA           88.46               26            1.71              2.63        219.37                45.52         0.515          pass              0.475             30.4                           0.202               -1.37              0.114                      ok            True                  False
   WBD           91.30               23            0.81              0.16         28.46                15.83         0.503          pass              0.438              0.0                           0.079                1.32              0.144                      ok            True                  False
  MNST           75.00                8            1.77              0.57         45.68               551.67         1.000          pass              0.122              7.4                           0.240               -0.91             -0.168                      ok           False                  False
  INSM           86.11               36            0.94              0.81        121.47               109.80         0.781          pass              0.564             50.0                           0.553               -5.96             -0.697 downtrend_blocked_slope           False                  False
   APP           73.33               45            0.21              0.45        311.87                88.04         0.649          pass              0.542             92.4                           0.441               -0.18              0.074                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-01T14:50:05.175915-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 23760.0, "asset_type": "option", "contract_symbol": "CPRT261016C00032500", "contracts": 144, "early_entry_score": 0.311, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 398.0, "option_spread_pct": 6.06, "option_volume": 105.0, "success_rate": 87.5, "ticker": "CPRT", "timing_score": 0.554}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"early_entry_score": 0.536, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 36.0, "option_spread_pct": 15.38, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "PAYX", "timing_score": 0.559}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"early_entry_score": 0.709, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 25.0, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.593}
2026-09-01T14:50:05.175915-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"early_entry_score": 0.235, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 11.24, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.697}
2026-09-01T14:50:05.175915-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-01", "training_samples": 5739, "window": 5}
2026-09-01T12:00:06.980016-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:55:07.200979-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:50:02.104495-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:45:02.019132-04:00 early_entry_1145      early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "entry_ask": 12.75, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 12.225, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 39, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.59, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.718, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.718, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:40:05.886827-04:00 early_entry_1140      early_entry_shadow  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "entry_ask": 12.6, "entry_bid": 11.55, "entry_mode": "early", "entry_option_price": 12.075, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.7, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "matched_signals": 40, "recovery_stability_score": 0.713, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901145005)

</details>
