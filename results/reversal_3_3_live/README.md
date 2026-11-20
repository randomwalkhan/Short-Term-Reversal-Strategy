# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 09:45:06 EST`
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

- Cash: `$52,781.30`
- Equity: `$95,681.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$-5,265.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 42900.0        37.05           33.0      380.27        374.86          bid_ask_mid                       33.0                bid_ask_mid                    True         -5265.0                 -10.93         94.74               19              2.72          61.7           61.47                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           84.62               13            1.97              3.94        284.06                59.73         0.608          pass              0.310             35.4                           0.464                1.00             -0.293                                 ok            True                  False
  NXPI           93.75               32            1.00              1.76        251.01                49.35         0.513          pass              0.664             33.1                           0.267                0.38             -0.310                                 ok            True                  False
  INTC           65.52               29            2.10              0.82         55.37               141.91         0.789          pass              0.399             64.5                           0.798               -3.07             -0.856 downtrend_blocked_slope_and_streak           False                  False
   APP           92.50               40            1.17              3.10        377.69               122.37         0.756          pass              0.828             73.2                           0.775               -4.25             -0.493 downtrend_blocked_slope_and_streak           False                  False
  FTNT           70.00               20            2.36              2.17        130.53                96.17         0.677          pass              0.200             21.7                           0.333                8.01              0.687                                 ok           False                  False
   BKR           71.43               14            1.74              0.57         46.43                56.86         0.605          pass              0.193             35.4                           0.404               -3.74             -0.410 downtrend_blocked_slope_and_streak           False                  False
  MCHP           84.62               26            1.83              0.75         58.15                78.21         0.601          pass              0.398             35.9                           0.263               -1.63             -0.421            downtrend_blocked_slope           False                  False
  UPRO           85.19               27            1.09              0.90        117.48                72.20         0.595          pass              0.520             69.8                           0.829               -9.58             -1.527 downtrend_blocked_slope_and_streak           False                  False
  AVGO           58.33               12            2.59              6.29        343.96                72.02         0.591          pass              0.180             35.7                           0.323               14.97              1.007                                 ok           False                  False
  QCOM           90.48               42            0.40              0.45        161.82                69.46         0.562          pass              0.794             86.0                           0.781               -2.45             -0.694 downtrend_blocked_slope_and_streak           False                  False
   ADI           75.00                8            3.37              8.91        373.62                64.58         0.557          pass              0.103             15.9                           0.198                0.32             -0.404                                 ok           False                  False
  CSCO           77.42               31            0.53              0.35         94.55                50.60         0.550          pass              0.413             72.7                           0.706                0.37             -0.333                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120094506)

</details>
