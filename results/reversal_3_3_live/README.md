# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:20:03 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$31,074.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$-1,190.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14160.0        35.25           35.4      477.34        478.06          bid_ask_mid                       35.4                bid_ask_mid                    True            60.0                   0.43         97.22               36              0.69         45.69           51.07                  40.06                 115.0           67.0               0.11                      ok
  MRVL     option         option MRVL260717C00200000       2026-06-01                   0      5     14150.0                 12900.0        28.30           25.8      203.79        208.49          bid_ask_mid                       25.8                bid_ask_mid                    True         -1250.0                  -8.83        100.00               32              0.59         91.49           72.96                  65.80                4958.0           50.0               0.05                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           91.30               23            2.95              4.63        222.35               138.67         0.666          pass              0.615             53.4                           0.634               32.61              4.404                                 ok            True                  False
  CSCO           93.10               29            0.56              0.47        120.22                51.99         0.617          pass              0.743             68.4                           0.652                1.30              0.265                                 ok            True                  False
  ROST           88.24               17            1.41              2.29        230.75                40.27         0.582          pass              0.439             38.2                           0.523                7.38              1.040                                 ok            True                  False
  ASML           93.55               31            0.98             11.01       1608.04                52.38         0.570          pass              0.694             45.3                           0.323                6.34              0.949                                 ok            True                  False
  KLAC           88.00               25            1.38             18.58       1913.75                50.27         0.538          pass              0.444             25.7                           0.176                5.17              1.037                                 ok            True                  False
  LRCX           88.00               25            1.87              4.16        316.40                55.15         0.524          pass              0.506             46.8                           0.443                9.66              1.542                                 ok            True                  False
  INSM           67.86               28            1.75              1.31        106.35               110.85         0.752          pass              0.251             18.7                           0.214               -3.76             -0.189                                 ok           False                  False
  MELI           94.87               39            0.50              5.89       1693.12                60.97         0.595          pass              0.773             41.3                           0.192                9.08              0.838                                 ok           False                  False
   AEP           72.73               11            1.01              0.90        126.28                24.34         0.574          pass              0.141             25.7                           0.456                0.19             -0.026                                 ok           False                  False
  AMAT           91.67               36            0.14              0.43        449.87                49.82         0.551          pass              0.824             94.8                           0.680                3.06              0.873                                 ok           False                  False
   HON           75.00                8            1.64              2.74        236.69                24.41         0.543          pass              0.120             21.8                           0.293                9.71              1.090                                 ok           False                  False
  REGN           86.67               30            0.85              3.67        613.21                42.14         0.536          pass              0.463             32.9                           0.334              -12.57             -0.801 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-06-01T10:20:03.923727-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:15:04.991229-04:00 early_entry_1015                   entry {"allocated_cash": 14150.0, "asset_type": "option", "contract_symbol": "MRVL260717C00200000", "contracts": 5, "early_entry_score": 0.862, "entry_mode": "early", "entry_option_price": 28.3, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4958.0, "option_spread_pct": 5.3, "option_volume": 50.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.526}
2026-06-01T10:10:06.342773-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:05:05.997517-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                          {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
2026-06-01T03:00:05.806892-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
2026-05-30T02:55:03.369308-04:00   share_ext_0255           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00   share_ext_0250           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00   share_ext_0245           market_closed                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601102003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601102003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601102003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601102003)

</details>
