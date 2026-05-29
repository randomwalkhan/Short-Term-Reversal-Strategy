# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 15:50:01 EDT`
Last processed slot: `manage_1600`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$18,164.25`
- Equity: `$32,284.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$20.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14120.0        35.25           35.3      477.34        478.68          bid_ask_mid                       35.3                bid_ask_mid                    True            20.0                   0.14         97.22               36              0.69         45.69           46.86                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.00               20            3.23              2.74        119.72                85.20         0.532            pass              0.531              3.7                           0.363                0.91              0.952                                 ok            True                  False
  MDLZ           90.91               11            1.55              0.68         62.10                12.98         0.506            pass              0.448             33.1                           0.269                0.74              0.173                                 ok            True                  False
  SOXL           93.75               32            0.12              0.18        224.55               139.09         0.783            pass              0.879             95.7                           0.823               20.51              3.783                                 ok           False                  False
  INSM           72.22               36            0.97              0.74        108.05               111.11         0.769            pass              0.401             50.2                           0.608               -7.18             -0.373            downtrend_blocked_slope           False                  False
  MELI           94.87               39            0.32              3.77       1693.91                61.27         0.620            pass              0.854             67.4                           0.538                5.15              0.812                                 ok           False                  False
   AEP           69.23               13            0.64              0.57        127.51                25.60         0.596            pass              0.158             26.1                           0.417               -1.29              0.103                                 ok           False                  False
  REGN           84.62               26            1.05              4.58        619.56                44.05         0.557            pass              0.407             40.6                           0.586              -13.60             -1.087 downtrend_blocked_slope_and_streak           False                  False
  SBUX           91.67               12            1.18              0.83        100.39                16.60         0.516            pass              0.563             62.4                           0.611               -5.88             -0.722            downtrend_blocked_slope           False                  False
 GOOGL           80.00                5            2.70              7.37        386.97                41.30         0.510            pass              0.051              0.0                           0.287               -5.35             -0.376            downtrend_blocked_slope           False                  False
  GOOG           75.00                4            2.67              7.22        383.03                41.01         0.507            pass              0.051              0.0                           0.275               -5.38             -0.390            downtrend_blocked_slope           False                  False
   PEP           84.21               19            1.24              1.27        145.74                23.56         0.496 below_threshold              0.323             33.7                           0.328               -2.83             -0.274            downtrend_blocked_slope           False                  False
  NXPI           94.74               19            2.00              4.63        328.29                46.79         0.494 below_threshold              0.603             33.7                           0.505               10.02              1.460                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-29T15:10:06.877260-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-29T15:05:06.057787-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-29T15:00:04.945442-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-29T14:55:02.058255-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-29T14:50:03.249987-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T14:50:03.249987-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-29", "training_samples": 5149, "window": 5}
2026-05-29T12:00:03.057178-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529155001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529155001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529155001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529155001)

</details>
