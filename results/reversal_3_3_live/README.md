# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:20:04 EST`
Last processed slot: `manage_1030`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           72.73               22            1.65              1.73        148.56               127.24         0.760            pass              0.267             37.0                           0.428              -11.65             -0.951 downtrend_blocked_slope_and_streak           False                  False
  ASML           74.29               35            0.05              0.50       1302.87                72.71         0.611            pass              0.509             93.8                           0.576              -13.01             -1.361            downtrend_blocked_slope           False                  False
   KDP           88.57               35            0.34              0.08         35.59                47.31         0.574            pass              0.596             47.8                           0.360                0.25             -0.015                                 ok           False                  False
   CEG           89.19               37            0.97              1.60        234.60                66.73         0.547            pass              0.503              7.9                           0.080              -17.37             -2.048 downtrend_blocked_slope_and_streak           False                  False
   AEP           96.30               27            0.05              0.04        127.57                16.32         0.527            pass              0.817             83.8                           0.614               -1.07             -0.130                                 ok           False                  False
  MDLZ          100.00               31            0.30              0.14         67.75                23.85         0.524            pass              0.769             59.0                           0.380                1.57              0.046                                 ok           False                  False
  PAYX           71.43               28            0.31              0.26        118.38                28.65         0.516            pass              0.245             24.5                           0.209                2.55              0.105                                 ok           False                  False
  ISRG           89.13               46            0.06              0.17        427.11                50.77         0.509            pass              0.776             93.9                           0.763               -2.94             -0.403           downtrend_blocked_streak           False                  False
  DXCM           86.67               45            0.16              0.09         84.80                47.84         0.505            pass              0.680             83.7                           0.708                4.07              0.319                                 ok           False                  False
  ROST           93.18               44            0.14              0.22        223.17                44.59         0.498 below_threshold              0.857             85.3                           0.607               -6.02             -0.465                                 ok           False                  False
  PANW           81.08               37            1.21              3.02        354.85                69.35         0.498 below_threshold              0.485             75.5                           0.766                9.04              1.310                                 ok           False                  False
  ORLY          100.00               21            1.17              0.79         96.35                21.83         0.493 below_threshold              0.525              0.9                           0.108                4.37              0.458                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:20:04.818619-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:15:06.172355-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:10:04.653720-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:05:06.125532-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00      manage_1530      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127102004)

</details>
