# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:00:02 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$31,765.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12190.0        60.05          60.95       531.8        528.39          bid_ask_mid                      60.95                bid_ask_mid                    True           180.0                    1.5         97.22               36              0.52         54.56           58.33                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            1.02              2.38        331.65                92.16         0.635            pass              0.539             42.8                           0.470               11.91              1.210                                 ok            True                  False
  ISRG           88.24               17            1.96              5.99        434.07                35.34         0.518            pass              0.397             26.2                           0.300               -0.88              0.157                                 ok            True                  False
  ASML           88.89               27            2.02             23.02       1622.16                54.27         0.502            pass              0.499             32.9                           0.487                5.14              0.577                                 ok            True                  False
  INSM           67.86               28            1.79              1.36        108.29               110.60         0.736            pass              0.200              2.3                           0.105               -7.82             -0.881            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.84              0.77        130.57                25.21         0.598            pass              0.153             26.7                           0.222               -1.62              0.143                                 ok           False                  False
  REGN           86.67               30            0.83              3.69        633.04                48.91         0.585            pass              0.505             45.2                           0.238              -12.87             -1.493 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00                4            4.62              4.33        132.10                66.88         0.565            pass              0.523             22.3                           0.314               12.21              1.373                                 ok           False                  False
  INTC           92.31               13            4.34              3.75        121.91                91.80         0.561            pass              0.455             17.0                           0.388               -2.03              0.336           downtrend_blocked_streak           False                  False
  ORLY           72.22               18            1.36              0.85         89.50                38.82         0.551            pass              0.129              6.9                           0.150               -3.47             -0.010                                 ok           False                  False
  NVDA           77.78                9            2.81              4.22        213.05                40.94         0.508            pass              0.051              0.0                           0.222               -5.41             -0.724 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.44               36            0.43              0.44        145.67                30.88         0.500 below_threshold              0.656             15.7                           0.193                4.09              0.279                                 ok           False                  False
   WDC           95.12               41            0.41              1.50        524.00                63.86         0.495 below_threshold              0.731             27.1                           0.282                6.91              0.513                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:35:01.630649-04:00 early_entry_1035         entry {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SNPS260717C00500000", "contracts": 2, "early_entry_score": 0.805, "entry_mode": "early", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 9.83, "option_volume": 157.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.413}
2026-05-27T10:30:06.423656-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527110002)

</details>
