# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 13:45:08 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               10            1.07              0.46         61.22                33.43         0.617          pass              0.505             14.3                           0.269               -0.25              0.059                  ok            True                  False
   TXN           88.00               25            1.64              3.35        289.79                64.46         0.601          pass              0.554             60.1                           0.468               -2.27             -0.186                  ok            True                  False
   ADI           86.67               30            1.05              2.79        379.34                54.65         0.578          pass              0.582             71.1                           0.543               -0.16              0.015                  ok            True                  False
  AAPL           96.00               25            0.73              1.69        332.53                36.90         0.576          pass              0.687             43.2                           0.431                7.20              0.704                  ok            True                  False
   XEL          100.00               11            1.24              0.69         79.68                21.95         0.563          pass              0.529             22.0                           0.354               -3.62             -0.205                  ok            True                  False
   WBD           83.33               12            1.12              0.21         27.20                20.20         0.541          pass              0.248             30.7                           0.265                1.91              0.468                  ok            True                  False
  NXPI           85.29               34            0.80              1.51        270.01                54.99         0.533          pass              0.601             82.2                           0.584               -1.78             -0.192                  ok            True                  False
   ADP           95.65               23            1.07              1.93        255.73                34.79         0.523          pass              0.678             46.2                           0.596                4.76              0.556                  ok            True                  False
  GILD           90.48               21            1.12              1.07        135.84                34.67         0.523          pass              0.445             13.4                           0.197                2.67              0.105                  ok            True                  False
  BKNG           85.71               21            1.58              2.04        183.73                41.98         0.518          pass              0.428             50.1                           0.693               -1.56              0.020                  ok            True                  False
  TMUS           88.46               26            0.93              1.25        192.31                36.68         0.517          pass              0.507             40.8                           0.504                7.63              0.694                  ok            True                  False
  PAYX          100.00               26            1.03              0.83        114.35                35.43         0.507          pass              0.696             46.4                           0.603                6.74              0.739                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T12:00:05.871771-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:55:01.882856-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.906755-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:45:01.890808-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:40:01.919825-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:35:01.723156-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:30:05.718379-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:25:05.915843-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:20:01.891090-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:15:01.934131-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717134508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717134508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717134508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717134508)

</details>
