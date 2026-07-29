# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 09:50:04 EDT`
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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               15            0.96              0.32         47.96                27.18         0.584          pass              0.640             49.5                           0.446                4.73              0.470                                 ok            True                  False
   CSX           95.65               23            0.63              0.22         50.74                28.82         0.549          pass              0.567              8.6                           0.108                2.21              0.298                                 ok            True                  False
   HON           83.33               18            1.10              1.90        246.23                39.75         0.544          pass              0.235             13.0                           0.244                9.72              1.172                                 ok            True                  False
   MAR          100.00               29            0.76              2.04        382.64                28.18         0.517          pass              0.764             61.8                           0.491                4.79              0.405                                 ok            True                  False
  GILD           89.66               29            0.55              0.52        134.10                34.28         0.515          pass              0.581             48.6                           0.319                2.72             -0.018                                 ok            True                  False
  ISRG           72.73               22            1.40              3.54        360.28                72.57         0.645          pass              0.272             42.6                           0.296               -8.29             -0.886                                 ok           False                  False
  MRVL           86.11               36            0.17              0.21        174.38                89.75         0.617          pass              0.689             96.9                           0.760              -15.56             -0.994 downtrend_blocked_slope_and_streak           False                  False
  DRAM           81.25               32            0.58              0.19         47.69               100.66         0.614          pass              0.526             94.7                           0.595              -17.26             -1.166 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           84.21               19            0.23              0.04         24.17                39.20         0.611          pass              0.486             84.3                           0.617                2.75             -0.217                                 ok           False                  False
  META           90.91               33            0.80              3.33        591.98                53.87         0.595          pass              0.506              0.8                           0.108              -13.60             -1.526 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.91               33            0.48              0.62        182.13                56.22         0.578          pass              0.689             62.4                           0.346               -3.26             -0.868            downtrend_blocked_slope           False                  False
   APP           81.82               44            0.72              2.10        417.32                74.36         0.567          pass              0.512             69.0                           0.599               -8.29             -0.840            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-07-29T09:50:04.461343-04:00  manage_1000         exit {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:30:03.798822-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:25:01.530149-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:20:02.789351-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:15:01.480372-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:10:04.312418-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:05:01.483120-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:00:02.430762-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T08:55:05.405467-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729095004)

</details>
