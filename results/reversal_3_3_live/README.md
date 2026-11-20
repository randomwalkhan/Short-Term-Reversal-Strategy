# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 09:40:05 EST`
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
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 52975.0        37.05          40.75      380.27        371.06     last_price_stale                        NaN                unavailable                   False          4810.0                   9.99         94.74               19              2.72          61.7            1.56                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           91.89               37            0.60              1.06        251.30                49.35         0.504          pass              0.726             59.6                           0.499                0.79             -0.292                                 ok            True                  False
   APP           90.00               30            1.95              5.17        376.81               122.37         0.765          pass              0.642             55.3                           0.670               -5.00             -0.529 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.14               21            3.54              1.38         55.13               141.91         0.751          pass              0.269             40.3                           0.547               -4.50             -0.923 downtrend_blocked_slope_and_streak           False                  False
  FTNT           78.57               28            1.81              1.67        130.75                96.17         0.672          pass              0.307             39.9                           0.539                8.62              0.712                                 ok           False                  False
   BKR           73.33               15            1.69              0.55         46.43                56.86         0.604          pass              0.205             37.0                           0.418               -3.70             -0.408 downtrend_blocked_slope_and_streak           False                  False
  MCHP           83.33               24            2.12              0.87         58.10                78.21         0.594          pass              0.319             25.7                           0.244               -1.92             -0.434            downtrend_blocked_slope           False                  False
  UPRO           88.00               25            1.51              1.25        117.33                72.20         0.584          pass              0.546             58.0                           0.619               -9.97             -1.546 downtrend_blocked_slope_and_streak           False                  False
  AVGO           54.55               11            2.90              7.04        343.63                72.02         0.574          pass              0.148             28.0                           0.312               14.61              0.992                                 ok           False                  False
   TXN           66.67                6            2.89              5.77        283.27                59.73         0.573          pass              0.073              5.3                           0.171                0.05             -0.336                                 ok           False                  False
  QCOM           90.91               44            0.32              0.36        161.85                69.46         0.558          pass              0.813             88.7                           0.820               -2.37             -0.690 downtrend_blocked_slope_and_streak           False                  False
  CSCO           73.08               26            0.97              0.64         94.42                50.60         0.548          pass              0.311             49.7                           0.552               -0.07             -0.353                                 ok           False                  False
  DRAM           71.43                7            5.95              1.60         37.73               105.80         0.547          pass              0.055              0.0                           0.257               -8.04             -1.140 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120094005)

</details>
