# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:10:06 EDT`
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
- Equity: `$32,384.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$120.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14220.0        35.25          35.55      477.34        477.04          bid_ask_mid                      35.55                bid_ask_mid                    True           120.0                   0.85         97.22               36              0.69         45.69           50.93                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.79              0.66        120.14                51.99         0.621            pass              0.663             55.2                           0.490                1.07              0.255                  ok            True                  False
  SOXL           95.00               20            4.26              6.69        221.47               138.67         0.604            pass              0.625             32.7                           0.276               30.83              4.342                  ok            True                  False
  ROST           88.24               17            1.37              2.23        230.78                40.27         0.584            pass              0.444             39.9                           0.497                7.43              1.042                  ok            True                  False
  ASML           93.75               32            0.83              9.36       1608.75                52.38         0.573            pass              0.731             53.5                           0.352                6.50              0.956                  ok            True                  False
  LRCX           88.00               25            1.61              3.58        316.64                55.15         0.542            pass              0.530             54.2                           0.511                9.95              1.554                  ok            True                  False
  KLAC           91.18               34            0.84             11.34       1916.85                50.27         0.515            pass              0.673             54.6                           0.363                5.74              1.062                  ok            True                  False
  MRVL          100.00               28            1.20              1.72        204.26                65.80         0.511            pass              0.796             74.9                           0.400               14.50              1.921                  ok            True                  False
  AAPL           96.00               25            0.75              1.65        311.35                17.18         0.500 below_threshold              0.652             34.0                           0.453                3.16              0.493                  ok            True                  False
  INSM           68.97               29            1.72              1.29        106.36               110.85         0.749            pass              0.262             20.0                           0.248               -3.73             -0.188                  ok           False                  False
  MELI           95.35               43            0.15              1.77       1694.89                60.97         0.592            pass              0.906             82.4                           0.339                9.46              0.854                  ok           False                  False
   AEP           66.67                9            1.21              1.07        126.21                24.34         0.568            pass              0.091             11.3                           0.238               -0.01             -0.035                  ok           False                  False
  AMGN           80.00                5            2.10              4.94        334.67                25.52         0.535            pass              0.096             14.2                           0.215                1.05              0.251                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                   detail
2026-06-01T10:10:06.342773-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                               {"reason": "no_candidate"}
2026-06-01T10:05:05.997517-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                               {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                   {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
2026-06-01T03:00:05.806892-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                            {'saved': 92}
2026-05-30T02:55:03.369308-04:00   share_ext_0255           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00   share_ext_0250           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00   share_ext_0245           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00   share_ext_0240           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:35:01.344797-04:00   share_ext_0235           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601101006)

</details>
