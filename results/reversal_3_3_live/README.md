# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$4,014.25`
- Equity: `$32,284.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$20.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14120.0        35.25           35.3      477.34        476.90          bid_ask_mid                       35.3                bid_ask_mid                    True            20.0                   0.14         97.22               36              0.69         45.69           51.76                  40.06                 115.0           67.0               0.11                      ok
  MRVL     option         option MRVL260717C00200000       2026-06-01                   0      5     14150.0                 14150.0        28.30           28.3      203.79        203.79          bid_ask_mid                       28.3                bid_ask_mid                    True             0.0                   0.00        100.00               32              0.59         91.49           91.49                  65.80                4958.0           50.0               0.05                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.85              0.71        120.11                51.99         0.617          pass              0.652             51.9                           0.523                1.01              0.252                  ok            True                  False
  SOXL           95.00               20            4.43              6.96        221.36               138.67         0.592          pass              0.616             30.0                           0.266               30.59              4.334                  ok            True                  False
  ROST           88.24               17            1.41              2.28        230.75                40.27         0.582          pass              0.440             38.4                           0.503                7.39              1.040                  ok            True                  False
  ASML           93.55               31            1.05             11.82       1607.70                52.38         0.565          pass              0.682             41.3                           0.273                6.26              0.946                  ok            True                  False
  KLAC           88.00               25            1.38             18.56       1913.76                50.27         0.538          pass              0.444             25.7                           0.210                5.17              1.037                  ok            True                  False
  MRVL          100.00               32            0.59              0.85        204.64                65.80         0.526          pass              0.862             87.6                           0.551               15.20              1.949                  ok            True                   True
  LRCX           86.96               23            2.04              4.54        316.23                55.15         0.526          pass              0.451             41.9                           0.337                9.47              1.534                  ok            True                  False
  INSM           66.67               30            1.67              1.25        106.37               110.85         0.744          pass              0.274             22.2                           0.239               -3.68             -0.186                  ok           False                  False
  MELI           95.12               41            0.30              3.54       1694.13                60.97         0.595          pass              0.854             64.7                           0.272                9.30              0.847                  ok           False                  False
   AEP           70.00               10            1.11              0.98        126.25                24.34         0.571          pass              0.113             18.8                           0.276                0.09             -0.031                  ok           False                  False
  AMAT           92.11               38            0.01              0.04        450.04                49.82         0.546          pass              0.863             99.5                           0.722                3.19              0.879                  ok           False                  False
  AMGN           80.00                5            2.04              4.82        334.73                25.52         0.539          pass              0.103             16.4                           0.205                1.10              0.254                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-06-01T10:15:04.991229-04:00 early_entry_1015                   entry {"allocated_cash": 14150.0, "asset_type": "option", "contract_symbol": "MRVL260717C00200000", "contracts": 5, "early_entry_score": 0.862, "entry_mode": "early", "entry_option_price": 28.3, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4958.0, "option_spread_pct": 5.3, "option_volume": 50.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.526}
2026-06-01T10:10:06.342773-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:05:05.997517-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                          {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
2026-06-01T03:00:05.806892-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
2026-05-30T02:55:03.369308-04:00   share_ext_0255           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00   share_ext_0250           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00   share_ext_0245           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00   share_ext_0240           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601101504)

</details>
