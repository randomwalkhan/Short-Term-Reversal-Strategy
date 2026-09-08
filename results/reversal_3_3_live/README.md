# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 09:40:01 EDT`
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
  MSTR     option         option MSTR261016C00145000       2026-09-04                   1     30     40125.0                 41160.0        13.38          13.72      142.86        135.89     last_price_stale                        NaN                unavailable                   False          1035.0                   2.58         82.86               35              1.36         73.28            6.25                 101.55                5516.0          964.0               0.01                      ok
```

## Today's Closed Trades (2026-09-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.19               37            1.38              2.07        212.21                91.63         0.626          pass              0.673             61.6                           0.529               10.21              1.076                                 ok            True                  False
  MELI          100.00               20            1.60             22.18       1968.86                45.80         0.587          pass              0.629             34.5                           0.390               -0.06              0.088                                 ok            True                  False
   WMT           85.19               27            0.83              0.62        106.87                40.24         0.569          pass              0.393             28.0                           0.280               -0.22              0.240                                 ok            True                  False
  CPRT           87.50               16            2.22              0.52         33.50                42.28         0.541          pass              0.294              0.0                           0.217               -0.87              0.029                                 ok            True                  False
  CHTR           89.29               28            2.05              2.18        151.06                60.37         0.516          pass              0.419              0.0                           0.170               -0.95             -0.082                                 ok            True                  False
  MSFT           88.89               18            1.42              4.98        497.56                23.39         0.506          pass              0.387             15.2                           0.146                1.08              0.130                                 ok            True                  False
  PYPL           85.71                7            2.33              0.90         54.58                57.43         0.640          pass              0.216              0.0                           0.230              -12.76             -1.530 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                7            1.95              0.34         24.70                29.15         0.576          pass              0.458              0.0                           0.203               -3.57             -0.021                                 ok           False                  False
  PANW           86.96               46            0.16              0.38        333.10                70.93         0.564          pass              0.721             93.1                           0.699               -5.18             -0.676            downtrend_blocked_slope           False                  False
  MSTR           76.47               17            4.64              4.64        140.81               102.15         0.563          pass              0.129              8.6                           0.143               11.04              1.132                                 ok           False                  False
   PEP           90.48               21            0.10              0.09        137.59                16.72         0.558          pass              0.657             82.7                           0.527               -3.94             -0.305            downtrend_blocked_slope           False                  False
  REGN          100.00                5            2.10             12.16        822.51                29.02         0.535          pass              0.569             38.6                           0.393               -2.19              0.099                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908094001)

</details>
