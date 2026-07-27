# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 09:45:02 EDT`
Last processed slot: `manual`

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

- Cash: `$17,668.00`
- Equity: `$33,918.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$-125.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16250.0         6.55            6.5       129.9        130.96          bid_ask_mid                        6.5                bid_ask_mid                    True          -125.0                  -0.76         91.67               24              0.73         32.92            32.9                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WDC           82.14               28            1.16              4.21        518.00               113.75         0.737          pass              0.320             22.9                           0.238               -7.52              0.061                                 ok            True                  False
   STX           90.32               31            0.73              4.35        849.83               103.51         0.731          pass              0.590             33.8                           0.178               -1.76              0.590                                 ok            True                  False
   CSX           93.75               16            1.03              0.38         53.07                24.65         0.556          pass              0.586             41.2                           0.337                6.12              0.605                                 ok            True                  False
  SOXL           85.29               34            1.14              1.09        136.32               179.12         0.823          pass              0.546             54.1                           0.316              -18.23             -1.532            downtrend_blocked_slope           False                  False
  KLAC           89.29               28            1.70              2.50        209.45                94.03         0.679          pass              0.513             25.8                           0.231               -6.88             -0.729 downtrend_blocked_slope_and_streak           False                  False
  PYPL           90.00               40            0.12              0.05         56.13                61.92         0.635          pass              0.799             89.6                           0.652               17.69              1.307                                 ok           False                  False
  AMAT           92.31               26            1.80              6.76        533.35                84.50         0.619          pass              0.576             26.4                           0.220               -8.48             -0.807 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           93.33               30            0.11              0.05         60.50                31.78         0.571          pass              0.804             85.9                           0.476                0.99              0.174                                 ok           False                  False
  LRCX           83.33               24            2.54              5.43        302.88                85.02         0.566          pass              0.324             28.3                           0.238               -9.84             -1.051 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.55               29            0.21              0.07         47.50                24.01         0.538          pass              0.848             89.1                           0.788                0.72              0.140                                 ok           False                  False
   WBD           88.24               17            0.87              0.16         25.70                22.96         0.537          pass              0.490             56.7                           0.574               -5.70             -0.829            downtrend_blocked_slope           False                  False
   XEL          100.00               30            0.06              0.03         81.66                20.22         0.531          pass              0.845             86.1                           0.516                1.42              0.181                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-27T09:35:01.555025-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:30:04.489033-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:25:02.551278-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:20:01.575598-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:15:05.384671-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:10:05.509301-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:05:02.526128-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:00:04.546327-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:55:01.530928-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:50:01.513320-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727094502)

</details>
