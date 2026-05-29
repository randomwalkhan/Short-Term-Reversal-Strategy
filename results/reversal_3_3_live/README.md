# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 15:40:03 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$32,104.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$-160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 13940.0        35.25          34.85      477.34        478.06          bid_ask_mid                      34.85                bid_ask_mid                    True          -160.0                  -1.13         97.22               36              0.69         45.69           47.08                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.12               34            0.83              9.82       1691.32                61.27         0.618            pass              0.643             15.0                           0.260                4.61              0.789                                 ok            True                  False
  INTC           96.30               27            1.52              1.29        120.34                85.20         0.601            pass              0.737             54.7                           0.613                2.69              1.032                                 ok            True                  False
  MDLZ           91.67               12            1.30              0.57         62.15                12.98         0.517            pass              0.509             44.1                           0.296                1.00              0.185                                 ok            True                  False
  SOXL           93.55               31            0.29              0.46        224.43               139.09         0.779            pass              0.847             89.3                           0.728               20.30              3.775                                 ok           False                  False
  INSM           67.74               31            1.61              1.22        107.85               111.11         0.758            pass              0.268             17.5                           0.400               -7.78             -0.402            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.72              0.64        127.48                25.60         0.594            pass              0.124             17.1                           0.323               -1.37              0.099                                 ok           False                  False
  REGN           84.00               25            1.17              5.10        619.33                44.05         0.554            pass              0.363             33.8                           0.526              -13.71             -1.093 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           87.50                8            1.99              5.43        387.80                41.30         0.547            pass              0.316             20.4                           0.357               -4.66             -0.343            downtrend_blocked_slope           False                  False
  GOOG           87.50                8            1.90              5.12        383.92                41.01         0.546            pass              0.324             23.2                           0.364               -4.63             -0.354            downtrend_blocked_slope           False                  False
  SBUX           90.00               10            1.41              0.99        100.32                16.60         0.512            pass              0.483             54.9                           0.487               -6.10             -0.733            downtrend_blocked_slope           False                  False
   TXN          100.00               12            2.35              5.20        313.72                35.59         0.499 below_threshold              0.530             22.4                           0.469                0.11              0.453                                 ok           False                  False
  AMGN           91.43               35            0.22              0.51        336.26                27.03         0.495 below_threshold              0.757             78.7                           0.640                0.61              0.285                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529154003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529154003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529154003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529154003)

</details>
