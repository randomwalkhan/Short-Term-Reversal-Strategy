# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:00:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$20,330.25`
- Equity: `$35,380.25`
- Realized PnL: `$26,885.25`
- Unrealized PnL: `$-1,505.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   2     86     16555.0                 15050.0         1.92           1.75       50.11         50.08          bid_ask_mid                       1.75                bid_ask_mid                    True         -1505.0                  -9.09         92.31               13              1.24         25.34           25.27                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03          2.5       3.055 3663.0        22.2 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           95.24               21            0.74              0.26         50.29                27.78         0.579            pass              0.606             25.0                           0.240               -0.17             -0.071                                 ok            True                  False
  MNST           88.89               18            1.15              0.78         96.05                24.15         0.555            pass              0.384             12.6                           0.143               -0.19              0.231                                 ok            True                  False
  AMGN          100.00               25            0.88              2.37        384.14                25.80         0.504            pass              0.599             16.3                           0.156                4.83              0.672                                 ok            True                  False
  AMAT           91.18               34            0.61              2.18        506.74                87.25         0.635            pass              0.769             82.4                           0.721               -4.02             -1.412 downtrend_blocked_slope_and_streak           False                  False
  AAPL           95.24               21            1.07              2.32        307.92                37.33         0.592            pass              0.567             11.5                           0.166               -6.43             -0.345 downtrend_blocked_slope_and_streak           False                  False
  DRAM           75.86               29            2.51              0.89         49.99               111.30         0.544            pass              0.340             52.9                           0.688               -7.46             -1.762 downtrend_blocked_slope_and_streak           False                  False
  GILD           88.57               35            0.28              0.26        130.10                32.59         0.523            pass              0.639             63.7                           0.373               -2.53             -0.038           downtrend_blocked_streak           False                  False
  ASML           91.89               37            0.14              1.60       1628.31                49.80         0.522            pass              0.835             95.1                           0.912               -6.34             -1.259 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               32            0.03              0.01         78.19                17.46         0.500            pass              0.888             97.2                           0.702               -0.62             -0.181                                 ok           False                  False
  CSCO           83.33               24            1.11              0.90        115.60                33.42         0.499 below_threshold              0.368             45.3                           0.515                3.61              0.322                                 ok           False                  False
   BKR           64.71               17            1.72              0.73         60.18                35.32         0.497 below_threshold              0.175             26.2                           0.259                7.80              0.854                                 ok           False                  False
  LRCX           82.61               23            3.02              6.20        290.36                90.68         0.491 below_threshold              0.341             45.2                           0.591               -7.37             -1.425 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-03T10:00:05.013413-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:00:05.013413-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.055, "pnl": 3663.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 22.2, "ticker": "PYPL"}
2026-08-03T03:00:01.318857-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-01T02:55:05.543757-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:50:03.559727-04:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:45:01.711119-04:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:40:01.558683-04:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:35:03.491522-04:00   share_ext_0235      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:30:02.590104-04:00   share_ext_0230      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:25:05.555029-04:00   share_ext_0225      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803100005)

</details>
