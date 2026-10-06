# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 11:55:05 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           84.00               25            2.04              0.88         61.29                49.40         0.538            pass              0.289              9.4                           0.202               -5.04             -0.188                                 ok            True                  False
  ASML           80.00               30            0.83             10.77       1855.24                40.48         0.538            pass              0.280             31.1                           0.315                5.52              0.784                                 ok            True                  False
  ABNB           82.61               23            1.45              1.66        163.36                40.56         0.530            pass              0.243             11.1                           0.199               -0.07              0.586                                 ok            True                  False
  TMUS           85.71               28            0.73              0.84        164.28                30.04         0.522            pass              0.402             25.9                           0.316                0.63             -0.082                                 ok            True                  False
  MPWR           91.18               34            0.47              4.83       1477.82                53.63         0.581            pass              0.747             76.9                           0.538                6.85              0.827                                 ok           False                  False
  META           85.71               42            0.14              0.73        741.59                55.50         0.579            pass              0.650             80.0                           0.501                0.58             -0.215                                 ok           False                  False
  QCOM           90.24               41            0.15              0.20        180.71                57.17         0.566            pass              0.772             80.8                           0.546               -8.96             -1.084 downtrend_blocked_slope_and_streak           False                  False
  INTC           87.50               32            2.07              1.69        115.47                74.54         0.541            pass              0.410              3.0                           0.218               -8.14             -0.772 downtrend_blocked_slope_and_streak           False                  False
  AMAT           82.76               29            2.09              7.94        538.88                48.32         0.491 below_threshold              0.292             14.3                           0.265               12.38              1.575                                 ok           False                  False
  MCHP           92.86               42            0.20              0.12         81.44                36.65         0.483 below_threshold              0.720             43.1                           0.196                7.26              0.820                                 ok           False                  False
  TEAM          100.00               32            1.59              2.19        195.71                55.00         0.482 below_threshold              0.625             10.2                           0.168                2.58              0.102                                 ok           False                  False
  DXCM          100.00                4            2.79              1.70         86.17                23.46         0.477 below_threshold              0.504             18.9                           0.387               -5.65             -0.378 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-06T11:55:05.274079-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:50:04.350583-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:45:06.217443-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:40:04.013409-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:10:04.455783-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006115505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006115505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006115505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006115505)

</details>
