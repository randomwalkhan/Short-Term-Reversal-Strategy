# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:10:01 EDT`
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
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12190.0        60.05          60.95       531.8        526.79          bid_ask_mid                      60.95                bid_ask_mid                    True           180.0                    1.5         97.22               36              0.52         54.56           60.06                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.88               33            0.85              1.98        331.82                92.16         0.639            pass              0.585             52.4                           0.452               12.10              1.218                                 ok            True                  False
  ISRG           88.24               17            1.87              5.72        434.19                35.34         0.524            pass              0.407             29.5                           0.467               -0.79              0.161                                 ok            True                  False
  ASML           89.29               28            1.79             20.45       1623.26                54.27         0.511            pass              0.540             40.4                           0.448                5.38              0.587                                 ok            True                  False
  INSM           72.97               37            1.07              0.82        108.52               110.60         0.731            pass              0.377             41.2                           0.372               -7.16             -0.848            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.68              0.62        130.63                25.21         0.605            pass              0.202             40.7                           0.341               -1.46              0.151                                 ok           False                  False
  REGN           87.10               31            0.79              3.52        633.11                48.91         0.581            pass              0.531             47.7                           0.309              -12.84             -1.491 downtrend_blocked_slope_and_streak           False                  False
  INTC           94.12               17            3.86              3.34        122.09                91.80         0.567            pass              0.558             26.1                           0.317               -1.54              0.358           downtrend_blocked_streak           False                  False
  FTNT          100.00                3            4.78              4.48        132.04                66.88         0.562            pass              0.515             19.6                           0.213               12.02              1.366                                 ok           False                  False
  ORLY           69.23               13            1.71              1.08         89.41                38.82         0.554            pass              0.085              3.1                           0.053               -3.82             -0.026                                 ok           False                  False
  UPRO           94.44               36            0.20              0.21        145.77                30.88         0.515            pass              0.790             60.1                           0.343                4.33              0.290                                 ok           False                  False
  NVDA           78.57               14            2.46              3.69        213.28                40.94         0.496 below_threshold              0.116             13.2                           0.288               -5.07             -0.707 downtrend_blocked_slope_and_streak           False                  False
  LRCX           80.77               26            1.66              3.75        321.07                57.65         0.484 below_threshold              0.284             36.2                           0.351                9.71              0.951                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:35:01.630649-04:00 early_entry_1035         entry {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SNPS260717C00500000", "contracts": 2, "early_entry_score": 0.805, "entry_mode": "early", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 9.83, "option_volume": 157.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.413}
2026-05-27T10:30:06.423656-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527111001)

</details>
