# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:00:06 EDT`
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
  FAST          100.00               18            0.83              0.28         47.98                27.18         0.573          pass              0.679             56.0                           0.690                4.86              0.476                                 ok            True                  False
   HON           80.00               15            1.51              2.61        245.93                39.75         0.528          pass              0.086              0.0                           0.155                9.27              1.153                                 ok            True                  False
   MAR          100.00               27            0.86              2.30        382.53                28.18         0.524          pass              0.737             57.0                           0.524                4.69              0.401                                 ok            True                  False
  ISRG           77.78               27            1.16              2.93        360.55                72.57         0.636          pass              0.335             52.6                           0.591               -8.06             -0.875                                 ok           False                  False
  MRVL           85.71               35            0.66              0.81        174.12                89.75         0.590          pass              0.642             88.1                           0.523              -15.97             -1.017 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.32               31            0.73              0.93        181.99                56.22         0.573          pass              0.602             43.2                           0.371               -3.50             -0.879            downtrend_blocked_slope           False                  False
  DRAM           80.65               31            1.31              0.44         47.58               100.66         0.572          pass              0.479             88.1                           0.489              -17.87             -1.200 downtrend_blocked_slope_and_streak           False                  False
  META           92.50               40            0.46              1.90        592.59                53.87         0.571          pass              0.762             57.2                           0.373              -13.30             -1.510 downtrend_blocked_slope_and_streak           False                  False
   APP           76.47               34            1.95              5.72        415.77                74.36         0.539          pass              0.270             18.6                           0.267               -9.43             -0.897            downtrend_blocked_slope           False                  False
  MPWR           84.62               39            0.15              1.35       1281.43                58.32         0.536          pass              0.652             94.1                           0.519               -7.00             -0.219           downtrend_blocked_streak           False                  False
   CSX           96.30               27            0.43              0.15         50.77                28.82         0.535          pass              0.688             40.5                           0.275                2.41              0.307                                 ok           False                  False
   XEL          100.00               29            0.16              0.09         80.29                19.80         0.534          pass              0.784             67.9                           0.409                0.04              0.139                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T09:50:04.461343-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:30:03.798822-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:25:01.530149-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:20:02.789351-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:15:01.480372-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:10:04.312418-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:05:01.483120-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:00:02.430762-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729100006)

</details>
