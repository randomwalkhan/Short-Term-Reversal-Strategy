# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 09:30:05 EST`
Last processed slot: `manage_0930`

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

- Cash: `$52,781.30`
- Equity: `$105,756.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$4,810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 52975.0        37.05          40.75      380.27        376.75     last_price_stale                        NaN                unavailable                   False          4810.0                   9.99         94.74               19              2.72          61.7            0.78                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT           82.93               41            0.83              0.76        131.13                96.17         0.665          pass              0.562             72.5                           0.596                9.70              0.758                                 ok            True                  False
   ADI           86.36               22            1.60              4.22        375.63                64.58         0.610          pass              0.360             16.5                           0.299                2.16             -0.321                                 ok            True                  False
   TXN           83.33               12            2.13              4.27        283.92                59.73         0.605          pass              0.226             21.3                           0.419                0.83             -0.300                                 ok            True                  False
  INSM           83.33               42            0.76              0.77        144.13                87.95         0.577          pass              0.512             55.3                           0.511               25.30              1.880                                 ok            True                  False
  GILD           83.33               18            1.45              1.71        168.25                31.00         0.515          pass              0.318             41.5                           0.436               -0.22             -0.097                                 ok            True                  False
  NXPI           94.12               34            0.87              1.53        251.10                49.35         0.509          pass              0.713             41.8                           0.527                0.52             -0.304                                 ok            True                  False
   CEG           90.32               31            1.71              3.02        250.74                57.98         0.500          pass              0.580             38.3                           0.508               -0.74             -0.463                                 ok            True                  False
  INTC           62.96               27            2.48              0.97         55.31               141.91         0.779          pass              0.366             58.2                           0.705               -3.45             -0.874 downtrend_blocked_slope_and_streak           False                  False
   APP           94.12               17            3.04              8.32        387.34               122.37         0.763          pass              0.537             12.4                           0.305               -3.12             -0.440            downtrend_blocked_slope           False                  False
  ALNY           78.38               37            1.06              1.11        148.93               110.46         0.728          pass              0.389             45.3                           0.276               -5.21             -0.515 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.73               44            0.16              0.75        689.33                78.44         0.699          pass              0.670              0.0                           0.250                1.85             -0.027                                 ok           False                  False
  SOXL           60.00               15            9.67              3.07         43.99               254.86         0.648          pass              0.159             20.2                           0.363              -10.99             -2.474            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                    detail
2026-11-20T01:25:03.363046-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:15:06.809821-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:10:05.934124-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:05:05.898904-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:00:05.809710-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:55:04.836951-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:50:02.820195-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:45:05.761865-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:40:04.740309-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120093005)

</details>
