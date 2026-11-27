# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:00:04 EST`
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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DXCM           85.29               34            0.86              0.51         84.62                47.84         0.531          pass              0.356              0.7                           0.160                3.34              0.287                                 ok            True                  False
  GILD           89.29               28            1.05              1.30        176.18                34.85         0.505          pass              0.514             32.0                           0.287                4.13              0.525                                 ok            True                  False
  NVDA           64.71               17            2.22              2.32        148.31               127.24         0.750          pass              0.168             15.3                           0.119              -12.15             -0.977 downtrend_blocked_slope_and_streak           False                  False
  LRCX           67.50               40            0.24              0.31        184.88               114.86         0.676          pass              0.510             80.8                           0.346              -21.05             -2.136            downtrend_blocked_slope           False                  False
  AMAT           68.42               38            0.24              0.53        310.95               107.91         0.670          pass              0.490             78.7                           0.346              -18.39             -1.910            downtrend_blocked_slope           False                  False
  MCHP           89.19               37            0.15              0.06         57.63                90.80         0.659          pass              0.750             86.4                           0.406               -6.50             -0.604            downtrend_blocked_slope           False                  False
  ASML           72.73               33            0.39              3.53       1301.57                72.71         0.601          pass              0.380             55.5                           0.267              -13.30             -1.377            downtrend_blocked_slope           False                  False
   KDP           87.88               33            0.42              0.11         35.58                47.31         0.582          pass              0.464             14.3                           0.239                0.17             -0.019                                 ok           False                  False
  REGN           88.37               43            0.24              1.67        981.16                56.75         0.571          pass              0.639             52.9                           0.326                3.08              0.290                                 ok           False                  False
   CEG           87.80               41            0.45              0.74        234.96                66.73         0.558          pass              0.486              7.5                           0.045              -16.93             -2.024 downtrend_blocked_slope_and_streak           False                  False
  ISRG           84.38               32            0.76              2.28        426.20                50.77         0.548          pass              0.367             16.2                           0.126               -3.63             -0.436           downtrend_blocked_streak           False                  False
  ROST           90.32               31            0.81              1.26        222.72                44.59         0.536          pass              0.505             12.2                           0.212               -6.65             -0.496            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00      manage_1530      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:11:16.077658-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T14:56:03.145316-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T14:52:31.871596-05:00       entry_1500      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T14:35:06.546537-05:00      manage_1430       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127100004)

</details>
