# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 15:05:02 EDT`
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

- Cash: `$4,915.25`
- Equity: `$26,757.75`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-237.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   0     11     12705.0                 12732.5        11.55          11.58      315.21        315.61          bid_ask_mid                      11.58                bid_ask_mid                    True            27.5                   0.22         95.83               24              0.66         28.20           27.69                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9110.0        46.88          45.55      660.72        659.30          bid_ask_mid                      45.55                bid_ask_mid                    True          -265.0                  -2.83         81.82               22              1.27         53.38           53.21                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AAPL           96.15               26            0.57              1.27        316.77                35.57         0.582          pass              0.783             72.7                           0.675               11.98              1.128                  ok            True                  False
   EXC           95.00               20            0.53              0.17         47.02                22.01         0.560          pass              0.747             74.7                           0.462               -0.66             -0.000                  ok            True                  False
  AMGN           94.44               18            1.11              2.80        359.25                21.45         0.545          pass              0.584             30.3                           0.414               -1.14             -0.086                  ok            True                  False
  PYPL           80.00               20            1.20              0.40         47.48                33.27         0.540          pass              0.281             53.3                           0.458                6.08              0.666                  ok            True                  False
  PAYX          100.00               24            1.04              0.81        110.40                31.82         0.537          pass              0.766             72.9                           0.425                9.81              0.944                  ok            True                  False
  GILD           89.66               29            0.56              0.52        131.18                32.97         0.532          pass              0.625             62.6                           0.618                3.43              0.427                  ok            True                  False
  CTAS           89.29               28            0.83              1.07        183.29                31.28         0.521          pass              0.581             53.8                           0.599                7.77              0.653                  ok            True                  False
   AEP           80.00               25            0.52              0.50        135.42                21.53         0.520          pass              0.257             34.9                           0.493               -2.21             -0.171                  ok            True                  False
   KHC           88.89                9            0.77              0.14         25.17                36.18         0.673          pass              0.471             55.5                           0.557                3.49              0.339                  ok           False                  False
  MDLZ          100.00                4            1.58              0.66         59.58                31.17         0.643          pass              0.526             20.6                           0.313               -1.23              0.015                  ok           False                  False
   PEP           85.71                7            1.95              1.89        137.68                30.22         0.583          pass              0.218              2.5                           0.151               -2.08             -0.145                  ok           False                  False
   ADP          100.00                6            2.11              3.70        249.46                31.20         0.582          pass              0.578             39.8                           0.296                9.24              0.822                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-14T15:05:02.308534-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T15:00:04.423415-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:55:01.276896-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:50:02.479277-04:00       entry_1500              entry {"allocated_cash": 12705.0, "asset_type": "option", "contract_symbol": "AAPL260821C00315000", "contracts": 11, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 11.55, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 11042.0, "option_spread_pct": 1.73, "option_volume": 1070.0, "success_rate": 95.83, "ticker": "AAPL", "timing_score": 0.589}
2026-07-14T14:50:02.479277-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-14", "training_samples": 5400, "window": 5}
2026-07-14T12:00:02.352813-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:55:01.322008-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:50:02.227286-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:45:01.430125-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:40:01.377381-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714150502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714150502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714150502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714150502)

</details>
