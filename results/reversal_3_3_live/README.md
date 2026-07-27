# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 13:40:05 EDT`
Last processed slot: `manage_1330`

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
   EXC           94.12               17            0.86              0.29         47.41                24.01         0.562            pass              0.646             55.4                           0.321                0.06              0.110                                 ok            True                  False
   XEL          100.00               10            1.38              0.79         81.33                20.22         0.559            pass              0.471              5.0                           0.198                0.07              0.120                                 ok            True                  False
   AEP           83.33               12            1.53              1.45        134.92                20.37         0.519            pass              0.163              2.8                           0.134               -1.59             -0.034                                 ok            True                  False
   WBD           75.00                8            1.47              0.27         25.66                22.96         0.539            pass              0.135             26.9                           0.252               -6.28             -0.856            downtrend_blocked_slope           False                  False
  CSCO           88.57               35            0.44              0.35        114.02                39.56         0.526            pass              0.643             65.2                           0.533               -4.68             -0.222                                 ok           False                  False
  DRAM           76.19               21            3.90              1.45         52.58                97.77         0.524            pass              0.216             30.1                           0.377              -10.78             -0.609            downtrend_blocked_slope           False                  False
  PANW           93.75               32            1.61              3.65        322.22                61.51         0.509            pass              0.627             20.9                           0.200               -3.55             -0.835 downtrend_blocked_slope_and_streak           False                  False
   TXN           87.88               33            1.11              2.17        278.65                50.69         0.497 below_threshold              0.556             47.5                           0.343               -7.40             -0.739            downtrend_blocked_slope           False                  False
  CRWD           90.24               41            0.87              1.12        182.80                61.00         0.495 below_threshold              0.606             27.9                           0.245               -3.32             -1.166 downtrend_blocked_slope_and_streak           False                  False
   CSX          100.00                2            3.26              1.21         52.71                24.65         0.495 below_threshold              0.462              4.1                           0.173                3.74              0.502                                 ok           False                  False
  UPRO           83.33               30            0.89              0.85        135.91                35.93         0.483 below_threshold              0.352             27.1                           0.349               -5.37             -0.571            downtrend_blocked_slope           False                  False
  AVGO           82.86               35            0.71              1.91        381.10                43.69         0.480 below_threshold              0.494             67.6                           0.422               -1.26              0.046                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727134005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727134005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727134005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727134005)

</details>
