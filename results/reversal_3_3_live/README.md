# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 10:00:06 EDT`
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

- Cash: `$77,148.10`
- Equity: `$77,148.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           83.33               24            2.16              3.23        211.72                91.63         0.648          pass              0.367             40.1                           0.295                9.34              1.040                                 ok            True                  False
   WMT           83.33               24            0.90              0.68        106.85                40.24         0.581          pass              0.305             21.5                           0.231               -0.30              0.236                                 ok            True                  False
  MELI          100.00               26            1.24             17.13       1971.02                45.80         0.573          pass              0.712             49.4                           0.646                0.31              0.105                                 ok            True                  False
  CPRT           86.67               15            2.37              0.56         33.48                42.28         0.533          pass              0.298             11.1                           0.160               -1.02              0.022                                 ok            True                  False
  GILD          100.00               11            2.05              2.17        150.07                24.06         0.520          pass              0.591             44.2                           0.618                0.79              0.182                                 ok            True                  False
  CHTR           90.00               30            1.80              1.92        151.17                60.37         0.517          pass              0.525             24.3                           0.229               -0.70             -0.070                                 ok            True                  False
  MSFT           88.89               18            1.39              4.87        497.61                23.39         0.508          pass              0.396             18.2                           0.231                1.12              0.131                                 ok            True                  False
  PYPL           90.00               10            1.95              0.75         54.64                57.43         0.645          pass              0.424             31.0                           0.281              -12.41             -1.512 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                9            1.29              0.22         24.75                29.15         0.600          pass              0.579             39.6                           0.421               -2.91              0.010                                 ok           False                  False
  MSTR           76.00               25            3.50              3.50        141.30               102.15         0.580          pass              0.256             32.6                           0.584               12.37              1.187                                 ok           False                  False
  SBUX           92.86               14            1.25              0.91        104.08                22.08         0.546          pass              0.424              0.0                           0.183               -4.02             -0.323            downtrend_blocked_slope           False                  False
  PANW           83.33               36            1.39              3.24        331.87                70.93         0.543          pass              0.442             41.7                           0.307               -6.35             -0.732            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-09-08T10:00:06.216987-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T09:50:04.503186-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00145000", "fill_price": 12.0375, "pnl": -4012.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-08T00:00:05.865092-04:00     data_refresh       data_refresh                                                                                                                                                                       {'saved': 93}
2026-09-07T23:55:04.287626-04:00   share_ext_2355      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:50:01.089933-04:00   share_ext_2350      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:45:01.091566-04:00   share_ext_2345      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:40:05.520694-04:00   share_ext_2340      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:35:01.092604-04:00   share_ext_2335      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:30:01.100040-04:00   share_ext_2330      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:25:04.214118-04:00   share_ext_2325      market_closed                                                                                                                             {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908100006)

</details>
