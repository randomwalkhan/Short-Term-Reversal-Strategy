# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 14:55:06 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$19,575.25`
- Equity: `$30,995.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-590.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11420.0        60.05           57.1       531.8        527.17          bid_ask_mid                       57.1                bid_ask_mid                    True          -590.0                  -4.91         97.22               36              0.52         54.56           54.29                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            1.04              2.41        331.64                92.16         0.634            pass              0.536             42.0                           0.433               11.89              1.210                                 ok            True                  False
  INTC           95.65               23            2.58              2.23        122.56                91.80         0.612            pass              0.700             50.6                           0.697               -0.23              0.418                                 ok            True                  False
  PAYX           95.00               20            0.52              0.34         94.65                30.13         0.580            pass              0.621             31.9                           0.382                1.93              0.576                                 ok            True                  False
  ASML           88.89               27            1.87             21.40       1622.86                54.27         0.512            pass              0.515             37.7                           0.440                5.29              0.584                                 ok            True                  False
  INSM           67.86               28            1.85              1.41        108.27               110.60         0.725            pass              0.279             28.7                           0.276               -7.88             -0.883            downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.03              0.61         83.46                55.63         0.643            pass              0.185             29.1                           0.212               -4.34              0.180                                 ok           False                  False
   AEP           66.67               12            0.89              0.82        130.55                25.21         0.594            pass              0.139             22.0                           0.268               -1.68              0.141                                 ok           False                  False
  GEHC           74.29               35            0.54              0.24         64.08                58.90         0.581            pass              0.403             59.4                           0.573                2.48              0.454                                 ok           False                  False
  REGN           88.24               34            0.56              2.50        633.55                48.91         0.578            pass              0.626             62.9                           0.460              -12.64             -1.480 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00                6            4.24              3.98        132.25                66.88         0.575            pass              0.543             28.6                           0.476               12.65              1.391                                 ok           False                  False
   ADP           94.44               36            0.42              0.64        218.08                40.06         0.525            pass              0.829             72.8                           0.447                1.70              0.493                                 ok           False                  False
  PYPL           87.10               31            0.78              0.24         44.06                32.11         0.499 below_threshold              0.546             55.8                           0.451               -3.58             -0.307 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527145506)

</details>
