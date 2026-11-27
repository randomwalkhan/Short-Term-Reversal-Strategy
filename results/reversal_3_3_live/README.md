# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:05:06 EST`
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
  DXCM           85.29               34            0.74              0.44         84.65                47.84         0.537          pass              0.427             24.1                           0.224                3.46              0.292                                 ok            True                  False
  NVDA           68.75               16            2.46              2.57        148.20               127.24         0.747          pass              0.133              6.0                           0.067              -12.38             -0.989 downtrend_blocked_slope_and_streak           False                  False
  KLAC           72.22               36            0.14              0.13        134.14               107.71         0.677          pass              0.414             57.8                           0.226              -14.68             -1.484            downtrend_blocked_slope           False                  False
  LRCX           66.67               39            0.60              0.78        184.68               114.86         0.660          pass              0.414             51.5                           0.254              -21.34             -2.153            downtrend_blocked_slope           False                  False
  MCHP           88.89               36            0.24              0.10         57.61                90.80         0.659          pass              0.709             77.6                           0.434               -6.59             -0.608            downtrend_blocked_slope           False                  False
  AMAT           66.67               36            0.59              1.28        310.63               107.91         0.659          pass              0.385             48.6                           0.233              -18.67             -1.925            downtrend_blocked_slope           False                  False
  ASML           73.33               30            0.80              7.27       1299.96                72.71         0.595          pass              0.218              8.5                           0.070              -13.65             -1.395            downtrend_blocked_slope           False                  False
   KDP           88.57               35            0.34              0.08         35.59                47.31         0.576          pass              0.547             31.4                           0.247                0.25             -0.015                                 ok           False                  False
  REGN           88.89               45            0.11              0.78        981.53                56.75         0.567          pass              0.727             77.8                           0.393                3.21              0.296                                 ok           False                  False
   CEG           87.80               41            0.37              0.62        235.02                66.73         0.561          pass              0.603             46.2                           0.255              -16.87             -2.021 downtrend_blocked_slope_and_streak           False                  False
  ISRG           86.84               38            0.38              1.13        426.69                50.77         0.537          pass              0.600             59.0                           0.344               -3.26             -0.418           downtrend_blocked_streak           False                  False
   AEP           96.30               27            0.16              0.14        127.53                16.32         0.520          pass              0.703             45.9                           0.272               -1.18             -0.135                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:05:06.125532-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00      manage_1530      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:11:16.077658-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T14:56:03.145316-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T14:52:31.871596-05:00       entry_1500      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127100506)

</details>
