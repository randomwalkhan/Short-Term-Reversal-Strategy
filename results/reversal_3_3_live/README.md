# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 09:45:01 EDT`
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

- Cash: `$41,035.60`
- Equity: `$74,035.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$-7,125.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00145000       2026-09-04                   1     30     40125.0                 33000.0        13.38           11.0      142.86        136.99          bid_ask_mid                       11.0                bid_ask_mid                    True         -7125.0                 -17.76         82.86               35              1.36         73.28            80.7                 101.55                5516.0          964.0               0.01                      ok
```

## Today's Closed Trades (2026-09-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           82.61               23            2.24              3.35        211.67                91.63         0.648          pass              0.335             37.8                           0.278                9.25              1.036                                 ok            True                  False
  MELI          100.00               25            1.45             20.03       1969.78                45.80         0.566          pass              0.679             40.8                           0.434                0.09              0.095                                 ok            True                  False
   WMT           84.85               33            0.65              0.49        106.93                40.24         0.544          pass              0.467             43.5                           0.472               -0.04              0.248                                 ok            True                  False
  CPRT           88.24               17            2.06              0.49         33.51                42.28         0.544          pass              0.357             12.0                           0.229               -0.71              0.037                                 ok            True                  False
  CHTR           89.29               28            1.86              1.98        151.14                60.37         0.524          pass              0.486             21.8                           0.204               -0.76             -0.073                                 ok            True                  False
  MSFT           88.89               18            1.46              5.10        497.52                23.39         0.505          pass              0.381             13.3                           0.134                1.05              0.128                                 ok            True                  False
  REGN          100.00               18            1.30              7.51        824.50                29.02         0.503          pass              0.690             62.1                           0.487               -1.39              0.136                                 ok            True                  False
  PYPL           85.71                7            2.49              0.96         54.55                57.43         0.628          pass              0.230              4.9                           0.180              -12.90             -1.537 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                7            1.77              0.31         24.72                29.15         0.585          pass              0.509             17.0                           0.228               -3.39             -0.013                                 ok           False                  False
  MSTR           77.27               22            3.88              3.88        141.14               102.15         0.577          pass              0.214             25.3                           0.242               11.93              1.169                                 ok           False                  False
    MU           86.84               38            0.00              0.01       1016.59                54.29         0.549          pass              0.723             99.8                           0.544               11.66              0.911                                 ok           False                  False
  NVDA           92.31               39            0.28              0.45        230.17                44.80         0.535          pass              0.658             27.8                           0.315               10.18              0.930                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908094501)

</details>
