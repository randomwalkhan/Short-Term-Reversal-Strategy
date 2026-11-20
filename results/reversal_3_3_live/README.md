# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 09:35:04 EST`
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
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 52975.0        37.05          40.75      380.27        375.52     last_price_stale                        NaN                unavailable                   False          4810.0                   9.99         94.74               19              2.72          61.7            0.39                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           90.00               20            2.19              3.87        250.37                57.98         0.541          pass              0.450             20.8                           0.349               -1.23             -0.485                                 ok            True                  False
  NXPI           94.29               35            0.70              1.23        251.23                49.35         0.514          pass              0.759             53.2                           0.495                0.69             -0.296                                 ok            True                  False
  INTC           56.25               16            3.88              1.51         55.07               141.91         0.758          pass              0.219             34.5                           0.481               -4.83             -0.939 downtrend_blocked_slope_and_streak           False                  False
   APP           90.91               44            0.82              2.18        378.08               122.37         0.751          pass              0.809             81.1                           0.901               -3.92             -0.477 downtrend_blocked_slope_and_streak           False                  False
  MCHP           84.62               26            1.83              0.75         58.15                78.21         0.601          pass              0.398             35.9                           0.320               -1.63             -0.421            downtrend_blocked_slope           False                  False
   TXN           77.78                9            2.54              5.08        283.57                59.73         0.592          pass              0.078              6.3                           0.227                0.41             -0.319                                 ok           False                  False
  AVGO           58.33               12            2.65              6.42        343.90                72.02         0.588          pass              0.175             34.3                           0.370               14.91              1.004                                 ok           False                  False
   BKR           69.23               13            2.10              0.69         46.38                56.86         0.586          pass              0.144             21.8                           0.267               -4.10             -0.426 downtrend_blocked_slope_and_streak           False                  False
  UPRO           84.62               26            1.35              1.11        117.39                72.20         0.584          pass              0.476             62.6                           0.767               -9.82             -1.539 downtrend_blocked_slope_and_streak           False                  False
  QCOM           87.88               33            0.99              1.12        161.53                69.46         0.582          pass              0.618             65.4                           0.702               -3.02             -0.721 downtrend_blocked_slope_and_streak           False                  False
   ADI           66.67                9            2.94              7.76        374.12                64.58         0.574          pass              0.080              7.5                           0.288                0.77             -0.384                                 ok           False                  False
  ASML           77.78                9            3.24             30.75       1343.02                61.72         0.558          pass              0.071              4.9                           0.220               -7.90             -1.229 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120093504)

</details>
