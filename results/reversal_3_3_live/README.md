# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 14:10:06 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           94.12               17            0.82              0.27         47.41                24.01         0.565            pass              0.652             57.6                           0.398                0.11              0.112                                 ok            True                  False
  MPWR           82.86               35            1.25             11.70       1328.80                65.61         0.506            pass              0.491             65.8                           0.606                1.99              0.288                                 ok            True                  False
   XEL          100.00                9            1.40              0.80         81.33                20.22         0.563            pass              0.490             11.2                           0.260                0.06              0.119                                 ok           False                  False
  DRAM           78.26               23            3.19              1.19         52.69                97.77         0.560            pass              0.271             42.9                           0.591              -10.11             -0.575            downtrend_blocked_slope           False                  False
   WBD           75.00                8            1.46              0.26         25.66                22.96         0.540            pass              0.138             27.9                           0.340               -6.26             -0.855            downtrend_blocked_slope           False                  False
  META           89.13               46            0.06              0.26        595.08                53.75         0.535            pass              0.731             78.0                           0.414               -9.43             -1.211 downtrend_blocked_slope_and_streak           False                  False
  CSCO           90.00               40            0.02              0.01        114.16                39.56         0.525            pass              0.815             98.6                           0.844               -4.28             -0.203                                 ok           False                  False
  KLAC           84.62               13            4.89              7.21        207.43                94.03         0.511            pass              0.288             31.1                           0.567               -9.91             -0.879 downtrend_blocked_slope_and_streak           False                  False
   AEP           76.92               13            1.43              1.36        134.96                20.37         0.508            pass              0.113             14.2                           0.279               -1.50             -0.029                                 ok           False                  False
   TXN           88.57               35            0.82              1.60        278.89                50.69         0.505            pass              0.629             61.3                           0.541               -7.13             -0.726            downtrend_blocked_slope           False                  False
  CRWD           90.91               44            0.52              0.67        182.99                61.00         0.500            pass              0.711             56.8                           0.558               -2.97             -1.150 downtrend_blocked_slope_and_streak           False                  False
   CSX          100.00                2            3.26              1.21         52.71                24.65         0.493 below_threshold              0.475              8.4                           0.243                3.74              0.502                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-27T12:00:02.583905-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:50:05.732067-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:45:02.697826-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:40:04.711421-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:35:01.677814-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:30:01.582772-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:25:02.749051-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:20:01.767844-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:15:01.581718-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727141006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727141006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727141006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727141006)

</details>
