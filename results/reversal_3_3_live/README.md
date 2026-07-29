# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 13:05:01 EDT`
Last processed slot: `manage_1300`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               12            1.20              0.68         80.04                19.80         0.571            pass              0.531             20.2                           0.323               -1.00              0.092                                 ok            True                  False
   MAR          100.00               20            1.15              3.09        382.20                28.18         0.552            pass              0.654             44.2                           0.488                4.38              0.388                                 ok            True                  False
  ISRG           71.43               14            1.94              4.91        359.70                72.57         0.658            pass              0.154             20.4                           0.221               -8.79             -0.911                                 ok           False                  False
  TMUS           90.32               31            0.71              0.91        182.00                56.22         0.574            pass              0.607             44.7                           0.366               -3.48             -0.878            downtrend_blocked_slope           False                  False
  FAST          100.00               22            0.48              0.16         48.03                27.18         0.571            pass              0.761             74.7                           0.808                5.23              0.492                                 ok           False                  False
  META           93.48               46            0.08              0.34        593.27                53.87         0.554            pass              0.897             94.1                           0.841              -12.97             -1.493 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.00               25            0.40              0.13         47.25                23.57         0.546            pass              0.696             47.2                           0.322                0.43              0.220                                 ok           False                  False
   CSX           96.30               27            0.49              0.17         50.77                28.82         0.527            pass              0.727             53.7                           0.563                2.35              0.305                                 ok           False                  False
   CEG           70.59               34            0.64              1.16        259.32                41.76         0.504            pass              0.375             54.8                           0.519                0.02              0.493                                 ok           False                  False
  GILD           91.43               35            0.22              0.21        134.23                34.28         0.499 below_threshold              0.770             82.8                           0.714                3.06             -0.003                                 ok           False                  False
  ASML           92.00               25            1.88             20.86       1574.01                55.40         0.499 below_threshold              0.628             52.7                           0.561              -14.33             -1.243 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.89               36            0.45              0.36        115.42                34.74         0.498 below_threshold              0.645             61.8                           0.580                2.94              0.500                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-29T12:00:04.480323-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:55:04.538258-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:50:05.595902-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:45:05.536367-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:40:04.512640-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:35:01.518792-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:30:04.462568-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:25:01.480196-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:20:05.598758-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:15:04.531641-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729130501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729130501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729130501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729130501)

</details>
