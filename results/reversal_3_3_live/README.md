# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-21 15:50:05 EDT`
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

- Cash: `$17,264.25`
- Equity: `$34,589.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$412.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   0     55     16912.5                 17325.0         3.08           3.15       55.67         55.65          bid_ask_mid                       3.15                bid_ask_mid                    True           412.5                   2.44          80.0               10              2.03         42.85           43.75                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-21)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  ASML     option         option ASML260821C01800000      1          2026-07-20         2026-07-21        94.95       122.6 2765.0    29.12059 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.00               10            2.05              0.82         56.47                61.63         0.662          pass              0.163             32.3                           0.366               21.92              2.899                      ok            True                  False
  MDLZ          100.00               14            0.79              0.33         60.13                32.62         0.623          pass              0.668             59.6                           0.566               -0.71              0.200                      ok            True                  False
  GILD           90.00               10            2.21              2.06        132.33                34.42         0.547          pass              0.405             27.9                           0.268               -4.47             -0.199                      ok            True                  False
  TMUS           83.33               12            1.88              2.58        194.53                36.36         0.547          pass              0.238             27.0                           0.435                3.91              0.681                      ok            True                  False
  MNST          100.00               24            0.66              0.44         95.26                21.78         0.507          pass              0.731             62.3                           0.515               -2.17             -0.010                      ok            True                  False
  CTAS           90.62               32            0.72              1.01        201.37                36.94         0.503          pass              0.705             75.0                           0.650               10.19              1.529                      ok            True                   True
   KDP           91.30               23            0.44              0.09         30.40                36.71         0.609          pass              0.496             15.6                           0.170               -3.76             -0.266 downtrend_blocked_slope           False                  False
   KHC           87.50               16            0.44              0.08         25.83                34.83         0.600          pass              0.459             53.1                           0.441                1.76              0.450                      ok           False                  False
   PEP           86.36               22            0.47              0.45        135.27                30.90         0.590          pass              0.447             46.2                           0.471               -7.01             -0.523 downtrend_blocked_slope           False                  False
  ISRG           82.93               41            0.51              1.26        352.63                68.15         0.565          pass              0.559             74.9                           0.371              -17.77             -2.016 downtrend_blocked_slope           False                  False
   EXC           95.24               21            0.40              0.13         45.90                23.50         0.564          pass              0.752             73.9                           0.464               -3.77             -0.312 downtrend_blocked_slope           False                  False
   XEL          100.00               28            0.06              0.03         78.66                21.50         0.551          pass              0.853             92.8                           0.768               -2.54             -0.185                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-07-21T15:10:09.418772-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T15:05:04.539660-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T15:00:02.487183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T14:55:03.644573-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T14:50:05.500810-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 16912.5, "asset_type": "option", "contract_symbol": "PYPL260821C00055000", "contracts": 55, "early_entry_score": 0.165, "entry_mode": "regular", "entry_option_price": 3.075, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 6395.0, "option_spread_pct": 4.88, "option_volume": 68.0, "success_rate": 80.0, "ticker": "PYPL", "timing_score": 0.663}
2026-07-21T14:50:05.500810-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-21", "training_samples": 5488, "window": 5}
2026-07-21T11:17:25.409204-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:59:34.342189-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:16:24.427902-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "CTAS260821C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "entry_ask": 8.0, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 17088.38, "hypothetical_contracts": 22, "matched_signals": 34, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 548.0, "option_spread_pct": 14.77, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "matched_signals": 34, "recovery_stability_score": 0.727, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-21T09:33:02.218910-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "ASML260821C01800000", "fill_price": 122.6, "pnl": 2765.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 29.12, "ticker": "ASML"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260721155005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260721155005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260721155005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260721155005)

</details>
