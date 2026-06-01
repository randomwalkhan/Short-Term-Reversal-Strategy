# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:05:05 EDT`
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
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14220.0        35.25          35.55      477.34        480.13          bid_ask_mid                      35.55                bid_ask_mid                    True           120.0                   0.85         97.22               36              0.69         45.69           49.69                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.83              0.70        120.12                51.99         0.618          pass              0.654             52.6                           0.466                1.02              0.253                  ok            True                  False
  ROST           89.47               19            1.26              2.05        230.85                40.27         0.579          pass              0.504             44.6                           0.479                7.54              1.047                  ok            True                  False
  ASML           93.10               29            1.26             14.27       1606.65                52.38         0.564          pass              0.620             29.1                           0.261                6.03              0.936                  ok            True                  False
  SOXL           94.74               19            4.98              7.83        220.99               138.67         0.561          pass              0.573             21.3                           0.272               29.83              4.308                  ok            True                  False
  LRCX           88.00               25            1.78              3.96        316.48                55.15         0.531          pass              0.515             49.4                           0.494                9.77              1.547                  ok            True                  False
  KLAC           91.18               34            0.81             10.89       1917.04                50.27         0.518          pass              0.679             56.4                           0.397                5.78              1.063                  ok            True                  False
  MRVL          100.00               24            1.54              2.21        204.05                65.80         0.516          pass              0.748             67.8                           0.379               14.11              1.906                  ok            True                  False
  INSM           67.74               31            1.55              1.16        106.41               110.85         0.746          pass              0.299             28.0                           0.376               -3.56             -0.180                  ok           False                  False
  MELI           95.24               42            0.19              2.21       1694.71                60.97         0.596          pass              0.894             78.1                           0.357                9.42              0.852                  ok           False                  False
   AEP           70.00               10            1.16              1.03        126.23                24.34         0.568          pass              0.093             12.2                           0.214                0.04             -0.033                  ok           False                  False
  AMAT           91.67               36            0.20              0.63        449.79                49.82         0.546          pass              0.816             92.4                           0.757                3.00              0.870                  ok           False                  False
  AMGN           80.00                5            2.04              4.81        334.73                25.52         0.539          pass              0.103             16.5                           0.252                1.11              0.254                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                   detail
2026-06-01T10:05:05.997517-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                               {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                   {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
2026-06-01T03:00:05.806892-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                            {'saved': 92}
2026-05-30T02:55:03.369308-04:00   share_ext_0255           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00   share_ext_0250           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00   share_ext_0245           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00   share_ext_0240           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:35:01.344797-04:00   share_ext_0235           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:30:06.367900-04:00   share_ext_0230           market_closed                                                                                                                                                                                                                                              {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601100505)

</details>
