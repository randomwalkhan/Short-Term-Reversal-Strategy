# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 09:50:01 EDT`
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

- Cash: `$17,668.00`
- Equity: `$33,918.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$-125.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16250.0         6.55            6.5       129.9         130.3          bid_ask_mid                        6.5                bid_ask_mid                    True          -125.0                  -0.76         91.67               24              0.73         32.92           34.86                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WDC           83.33               30            0.89              3.24        518.41               113.75         0.740          pass              0.446             49.9                           0.336               -7.27              0.074                                 ok            True                  False
  SOXL           86.11               36            0.00              0.00        136.81               179.12         0.858          pass              0.722             99.9                           0.461              -17.27             -1.479            downtrend_blocked_slope           False                  False
  KLAC           90.62               32            1.05              1.55        209.85                94.03         0.695          pass              0.661             53.8                           0.317               -6.28             -0.699 downtrend_blocked_slope_and_streak           False                  False
  AMAT           93.10               29            1.02              3.83        534.61                84.50         0.650          pass              0.716             58.3                           0.348               -7.75             -0.771 downtrend_blocked_slope_and_streak           False                  False
  PYPL           89.47               38            0.37              0.15         56.09                61.92         0.630          pass              0.708             68.7                           0.448               17.40              1.296                                 ok           False                  False
  INTC           87.18               39            0.42              0.27         92.20                79.50         0.621          pass              0.447              0.0                           0.197              -10.85             -0.902 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.19               27            1.56              3.34        303.78                85.02         0.613          pass              0.481             56.0                           0.336               -8.93             -1.006 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.48               21            0.31              0.13         60.46                31.78         0.611          pass              0.590             58.7                           0.325                0.79              0.165                                 ok           False                  False
   CSX          100.00                9            1.39              0.52         53.01                24.65         0.587          pass              0.521             20.9                           0.181                5.74              0.589                                 ok           False                  False
   EXC           96.00               25            0.32              0.10         47.49                24.01         0.557          pass              0.807             83.7                           0.773                0.62              0.135                                 ok           False                  False
   XEL          100.00               25            0.32              0.18         81.59                20.22         0.545          pass              0.638             27.8                           0.169                1.16              0.169                                 ok           False                  False
   WBD           86.67               15            1.14              0.21         25.68                22.96         0.530          pass              0.394             43.3                           0.545               -5.96             -0.841            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727095001)

</details>
