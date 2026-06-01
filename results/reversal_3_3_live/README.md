# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:00:03 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$34,324.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$2,060.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 16160.0        35.25           40.4      477.34        476.18          bid_ask_mid                       40.4                bid_ask_mid                    True          2060.0                  14.61         97.22               36              0.69         45.69           55.01                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           91.67               24            1.18              0.99        119.99                51.99         0.608          pass              0.564             33.0                           0.281                0.67              0.237                                 ok            True                  False
  ROST           92.86               14            1.59              2.58        230.62                40.27         0.595          pass              0.520             30.2                           0.311                7.19              1.032                                 ok            True                  False
  ASML           92.86               28            1.40             15.82       1605.98                52.38         0.561          pass              0.583             21.4                           0.261                5.88              0.929                                 ok            True                  False
  LRCX           88.00               25            1.86              4.15        316.40                55.15         0.525          pass              0.507             47.0                           0.531                9.67              1.543                                 ok            True                  False
  INSM           73.68               38            0.88              0.66        106.63               110.85         0.750          pass              0.439             59.1                           0.656               -2.90             -0.149                                 ok           False                  False
   AEP           66.67                9            1.26              1.11        126.19                24.34         0.565          pass              0.073              5.4                           0.158               -0.06             -0.037                                 ok           False                  False
  AMGN           83.33                6            1.71              4.03        335.06                25.52         0.557          pass              0.235             30.0                           0.304                1.45              0.269                                 ok           False                  False
  AMAT           91.67               36            0.06              0.20        449.97                49.82         0.556          pass              0.833             97.6                           0.892                3.14              0.876                                 ok           False                  False
  KLAC           91.43               35            0.43              5.78       1919.23                50.27         0.537          pass              0.756             76.9                           0.639                6.18              1.081                                 ok           False                  False
   HON           76.92               13            1.31              2.17        236.93                24.41         0.532          pass              0.187             37.9                           0.498               10.09              1.105                                 ok           False                  False
  REGN           88.24               34            0.66              2.84        613.56                42.14         0.523          pass              0.576             48.1                           0.510              -12.40             -0.792 downtrend_blocked_slope_and_streak           False                  False
  GOOG           89.47               19            1.44              3.79        374.81                25.35         0.517          pass              0.423             19.5                           0.249               -5.67             -0.411            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                   detail
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                   {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
2026-06-01T03:00:05.806892-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                            {'saved': 92}
2026-05-30T02:55:03.369308-04:00   share_ext_0255           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00   share_ext_0250           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00   share_ext_0245           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00   share_ext_0240           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:35:01.344797-04:00   share_ext_0235           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:30:06.367900-04:00   share_ext_0230           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:25:04.377495-04:00   share_ext_0225           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601100003)

</details>
