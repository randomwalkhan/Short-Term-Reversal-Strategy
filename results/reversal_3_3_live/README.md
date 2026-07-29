# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:10:01 EDT`
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
  FAST          100.00               11            1.27              0.43         47.92                27.18         0.589          pass              0.564             33.0                           0.336                4.40              0.456                                 ok            True                  False
   CSX           96.00               25            0.52              0.19         50.76                28.82         0.542          pass              0.650             32.1                           0.306                2.32              0.303                                 ok            True                  False
   HON           80.00               15            1.64              2.83        245.84                39.75         0.516          pass              0.109              8.0                           0.181                9.13              1.147                                 ok            True                  False
   MAR          100.00               32            0.64              1.71        382.79                28.18         0.505          pass              0.801             68.1                           0.530                4.93              0.411                                 ok            True                  False
  AVGO           82.86               35            0.63              1.69        380.19                41.80         0.500          pass              0.488             65.1                           0.448               -4.00             -0.012                                 ok            True                  False
  ISRG           76.92               26            1.18              3.00        360.52                72.57         0.640          pass              0.325             51.4                           0.605               -8.09             -0.877                                 ok           False                  False
  DRAM           80.65               31            0.96              0.32         47.63               100.66         0.595          pass              0.490             91.3                           0.559              -17.58             -1.184 downtrend_blocked_slope_and_streak           False                  False
  META           91.67               36            0.69              2.86        592.18                53.87         0.581          pass              0.650             35.8                           0.304              -13.50             -1.521 downtrend_blocked_slope_and_streak           False                  False
  MRVL           85.29               34            1.15              1.41        173.87                89.75         0.564          pass              0.596             79.3                           0.447              -16.39             -1.039 downtrend_blocked_slope_and_streak           False                  False
  TMUS           91.89               37            0.34              0.43        182.20                56.22         0.563          pass              0.774             73.5                           0.510               -3.12             -0.861            downtrend_blocked_slope           False                  False
   XEL          100.00               30            0.07              0.04         80.31                19.80         0.533          pass              0.842             85.2                           0.535                0.12              0.143                                 ok           False                  False
   APP           74.19               31            2.50              7.32        415.08                74.36         0.516          pass              0.192              0.0                           0.197               -9.93             -0.922            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-07-29T10:10:01.513835-04:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:05:02.493653-04:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T09:50:04.461343-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:30:03.798822-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:25:01.530149-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:20:02.789351-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:15:01.480372-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:10:04.312418-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729101001)

</details>
