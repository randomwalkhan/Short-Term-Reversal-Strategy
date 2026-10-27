# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 15:00:05 EDT`
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

- Cash: `$1,421.80`
- Equity: `$129,404.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-8,287.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 60640.0         20.0          18.95      220.60        219.89          bid_ask_mid                      18.95                bid_ask_mid                    True         -3360.0                  -5.25         100.0               12              3.08         70.90           69.46                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 67342.5          1.1           1.02       44.42         44.22          bid_ask_mid                       1.02                bid_ask_mid                    True         -4927.5                  -6.82          80.0               15              0.97         20.09           22.95                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   WMT           80.00               15            1.04              0.87        119.92                23.89         0.545          pass              0.144             18.6                           0.377                6.03              0.467                      ok            True                  False
   KDP           96.00               25            0.50              0.12         34.94                25.67         0.539          pass              0.780             75.4                           0.683                6.60              0.560                      ok            True                  False
   EXC           86.96               23            0.69              0.21         44.45                21.50         0.527          pass              0.392             22.5                           0.253                4.47              0.552                      ok            True                  False
  ORLY          100.00               14            1.42              0.90         90.66                20.34         0.521          pass              0.538             19.9                           0.364                4.34              0.471                      ok            True                  False
  TEAM          100.00               28            1.58              2.47        222.36                43.78         0.520          pass              0.660             29.3                           0.389                5.70              0.873                      ok            True                  False
  ABNB           85.71               21            1.37              1.64        170.35                25.32         0.500          pass              0.390             38.1                           0.529                1.89              0.147                      ok            True                  False
  TMUS           87.80               41            0.07              0.08        146.90                64.06         0.634          pass              0.750             92.9                           0.542               -4.49             -0.674 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.33              0.58         62.72                25.86         0.590          pass              0.301             13.9                           0.402                1.03              0.130                      ok           False                  False
 CMCSA           88.89                9            1.29              0.20         21.96                26.02         0.567          pass              0.335             13.6                           0.298                4.24              0.554                      ok           False                  False
   ROP           76.92               13            1.56              4.84        439.58                39.00         0.563          pass              0.194             39.3                           0.309               18.00              2.011                      ok           False                  False
   KHC           83.33                6            2.49              0.43         24.55                34.80         0.560          pass              0.159              4.7                           0.276                7.51              0.931                      ok           False                  False
  COST           77.78                9            1.41              9.90       1000.92                16.36         0.540          pass              0.068              4.8                           0.260                3.81              0.380                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-27T15:00:05.952985-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T14:55:05.068283-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T14:50:03.992702-04:00       entry_1500      entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
2026-10-27T14:50:03.992702-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-27", "training_samples": 6196, "window": 5}
2026-10-27T12:00:05.676478-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "matched_signals": 42, "recovery_stability_score": 0.692, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T11:55:06.030396-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:50:05.158961-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:45:04.083038-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:40:06.585395-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:35:05.021467-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.823, "early_reclaim_pct": 78.9, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.823, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.774, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027150005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027150005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027150005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027150005)

</details>
