# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 09:55:05 EST`
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

- Cash: `$52,781.30`
- Equity: `$96,916.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$-4,030.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 44135.0        37.05          33.95      380.27        374.94          bid_ask_mid                      33.95                bid_ask_mid                    True         -4030.0                  -8.37         94.74               19              2.72          61.7           61.32                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           87.50               16            1.66              3.33        284.32                59.73         0.612          pass              0.437             45.4                           0.478                1.31             -0.279                                 ok            True                  False
   ADI           82.35               17            1.98              5.24        375.19                64.58         0.596          pass              0.321             50.6                           0.470                1.76             -0.339                                 ok            True                  False
  MCHP           88.89               36            1.03              0.42         58.29                78.21         0.595          pass              0.662             64.1                           0.440               -0.82             -0.384                                 ok            True                  False
  INTC           69.77               43            0.07              0.03         55.71               141.91         0.821          pass              0.578             98.8                           0.963               -1.07             -0.763                                 ok           False                  False
   APP           90.70               43            0.99              2.64        377.89               122.37         0.748          pass              0.792             77.2                           0.700               -4.08             -0.485 downtrend_blocked_slope_and_streak           False                  False
  FTNT           78.57               28            1.80              1.65        130.75                96.17         0.673          pass              0.309             40.4                           0.314                8.63              0.713                                 ok           False                  False
  SOXL           62.50               16            8.99              2.85         44.08               254.86         0.670          pass              0.213             35.5                           0.438              -10.31             -2.440            downtrend_blocked_slope           False                  False
   BKR           86.21               29            0.71              0.23         46.57                56.86         0.594          pass              0.573             73.7                           0.673               -2.73             -0.362 downtrend_blocked_slope_and_streak           False                  False
  UPRO           84.21               38            0.03              0.03        117.86                72.20         0.592          pass              0.655             99.1                           0.924               -8.62             -1.478 downtrend_blocked_slope_and_streak           False                  False
  AVGO           58.33               12            2.61              6.33        343.94                72.02         0.590          pass              0.178             35.3                           0.295               14.95              1.006                                 ok           False                  False
  MPWR           55.56               18            3.01             27.28       1284.17                90.01         0.583          pass              0.251             46.5                           0.490                5.58             -0.396                                 ok           False                  False
  QCOM           89.74               39            0.57              0.65        161.73                69.46         0.569          pass              0.750             79.9                           0.634               -2.62             -0.702 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120095505)

</details>
