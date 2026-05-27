# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:25:02 EDT`
Last processed slot: `manage_1130`

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
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12190.0        60.05          60.95       531.8        524.85          bid_ask_mid                      60.95                bid_ask_mid                    True           180.0                    1.5         97.22               36              0.52         54.56            61.7                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            1.02              2.38        331.65                92.16         0.635            pass              0.539             42.8                           0.387               11.91              1.210                                 ok            True                  False
  ISRG           84.62               13            2.32              7.09        433.60                35.34         0.517            pass              0.233             12.6                           0.270               -1.24              0.141                                 ok            True                  False
  ASML           89.29               28            1.82             20.81       1623.11                54.27         0.509            pass              0.537             39.4                           0.426                5.35              0.586                                 ok            True                  False
  INSM           70.37               27            1.96              1.49        108.23               110.60         0.732            pass              0.198              3.8                           0.209               -7.99             -0.889            downtrend_blocked_slope           False                  False
   AEP           81.82               22            0.25              0.23        130.80                25.21         0.588            pass              0.422             78.3                           0.752               -1.03              0.170                                 ok           False                  False
  REGN           86.67               30            0.85              3.78        633.00                48.91         0.584            pass              0.501             43.9                           0.307              -12.89             -1.493 downtrend_blocked_slope_and_streak           False                  False
  INTC           92.31               13            4.16              3.60        121.98                91.80         0.573            pass              0.467             20.4                           0.237               -1.85              0.344           downtrend_blocked_streak           False                  False
  FTNT          100.00                3            4.99              4.68        131.96                66.88         0.548            pass              0.503             16.1                           0.135               11.78              1.356                                 ok           False                  False
  ORLY           73.68               19            1.31              0.83         89.52                38.82         0.545            pass              0.192             25.8                           0.321               -3.43             -0.008                                 ok           False                  False
  UPRO           94.44               36            0.44              0.45        145.67                30.88         0.497 below_threshold              0.700             30.6                           0.272                4.07              0.279                                 ok           False                  False
  NVDA           78.57               14            2.46              3.70        213.28                40.94         0.496 below_threshold              0.116             13.2                           0.307               -5.07             -0.708 downtrend_blocked_slope_and_streak           False                  False
  LRCX           80.77               26            1.73              3.91        321.01                57.65         0.480 below_threshold              0.276             33.6                           0.387                9.63              0.948                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527112502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527112502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527112502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527112502)

</details>
