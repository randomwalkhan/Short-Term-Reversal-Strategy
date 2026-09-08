# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 09:30:01 EDT`
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

- Cash: `$41,035.60`
- Equity: `$82,195.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$1,035.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00145000       2026-09-04                   1     30     40125.0                 41160.0        13.38          13.72      142.86        138.11     last_price_stale                        NaN                unavailable                   False          1035.0                   2.58         82.86               35              1.36         73.28            3.13                 101.55                5516.0          964.0               0.01                      ok
```

## Today's Closed Trades (2026-09-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           88.89               36            1.47              2.20        212.16                91.63         0.643          pass              0.513             12.9                           0.219               10.11              1.072                                 ok            True                  False
  MELI          100.00               23            1.53             21.13       1969.31                45.80         0.582          pass              0.556              3.8                           0.088                0.01              0.092                                 ok            True                  False
  WDAY           88.00               25            2.63              3.61        194.24                75.44         0.540          pass              0.465             32.7                           0.209               -4.27              0.088                                 ok            True                  False
  REGN          100.00               13            1.49              8.61        824.03                29.02         0.533          pass              0.577             34.4                           0.197               -1.58              0.127                                 ok            True                  False
   TRI           96.00               25            1.62              1.20        105.17                47.38         0.513          pass              0.551              0.0                           0.217               -4.29              0.103                                 ok            True                  False
  CPRT           81.82               33            0.95              0.22         33.62                42.28         0.511          pass              0.368             38.5                           0.348                0.42              0.088                                 ok            True                  False
  MSFT           88.89               18            1.38              4.83        497.63                23.39         0.511          pass              0.358              5.5                           0.118                1.13              0.132                                 ok            True                  False
  NFLX           89.66               29            1.09              0.59         78.00                39.36         0.509          pass              0.477             14.1                           0.122               -3.26             -0.236                                 ok            True                  False
  CTSH           93.33               30            1.19              0.52         62.09                34.09         0.502          pass              0.565              8.6                           0.289               -1.01              0.000                                 ok            True                  False
  PYPL           95.45               22            0.96              0.37         54.80                57.43         0.651          pass              0.649             34.5                           0.398              -11.54             -1.467 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               18            0.24              0.04         24.83                29.15         0.620          pass              0.728             70.7                           0.481               -1.88              0.057                                 ok           False                  False
  MSTR           76.92               26            3.01              3.01        141.51               102.15         0.618          pass              0.220             17.3                           0.286               12.94              1.210                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                  detail
2026-09-08T00:00:05.865092-04:00   data_refresh  data_refresh                                           {'saved': 93}
2026-09-07T23:55:04.287626-04:00 share_ext_2355 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:50:01.089933-04:00 share_ext_2350 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:45:01.091566-04:00 share_ext_2345 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:40:05.520694-04:00 share_ext_2340 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:35:01.092604-04:00 share_ext_2335 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:30:01.100040-04:00 share_ext_2330 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:25:04.214118-04:00 share_ext_2325 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:20:01.098530-04:00 share_ext_2320 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:15:02.108377-04:00 share_ext_2315 market_closed {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908093001)

</details>
