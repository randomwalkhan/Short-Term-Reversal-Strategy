# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:45:03 EDT`
Last processed slot: `early_entry_1145`

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
- Equity: `$31,325.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-260.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11750.0        60.05          58.75       531.8        526.08          bid_ask_mid                      58.75                bid_ask_mid                    True          -260.0                  -2.16         97.22               36              0.52         54.56           57.72                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            0.99              2.30        331.69                92.16         0.637            pass              0.545             44.8                           0.431               11.95              1.212                                 ok            True                  False
  ORLY           80.77               26            1.20              0.76         89.55                38.82         0.512            pass              0.275             32.1                           0.439               -3.32             -0.003                                 ok            True                  False
  ASML           91.30               23            2.37             27.08       1620.43                54.27         0.511            pass              0.502             21.1                           0.258                4.76              0.560                                 ok            True                  False
  INSM           66.67               24            2.53              1.93        108.04               110.60         0.707            pass              0.171              2.3                           0.165               -8.52             -0.915            downtrend_blocked_slope           False                  False
   AEP           76.47               17            0.42              0.38        130.74                25.21         0.604            pass              0.297             63.3                           0.647               -1.21              0.163                                 ok           False                  False
  REGN           87.10               31            0.79              3.53        633.11                48.91         0.581            pass              0.530             47.6                           0.401              -12.84             -1.491 downtrend_blocked_slope_and_streak           False                  False
  INTC           92.31               13            4.27              3.70        121.94                91.80         0.566            pass              0.459             18.2                           0.252               -1.97              0.339           downtrend_blocked_streak           False                  False
  FTNT          100.00                3            5.20              4.87        131.87                66.88         0.535            pass              0.491             12.6                           0.150               11.53              1.346                                 ok           False                  False
  ISRG          100.00                6            3.19              9.76        432.46                35.34         0.523            pass              0.460              2.6                           0.166               -2.12              0.100           downtrend_blocked_streak           False                  False
  NVDA           78.57               14            2.31              3.48        213.37                40.94         0.506            pass              0.132             18.3                           0.387               -4.93             -0.701 downtrend_blocked_slope_and_streak           False                  False
  UPRO           93.94               33            0.69              0.71        145.56                30.88         0.499 below_threshold              0.607             10.6                           0.249                3.81              0.267                                 ok           False                  False
   ADP           95.45               44            0.09              0.13        218.29                40.06         0.492 below_threshold              0.932             94.3                           0.459                2.03              0.508                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T11:45:03.631384-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527114503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527114503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527114503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527114503)

</details>
