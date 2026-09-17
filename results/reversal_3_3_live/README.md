# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 11:20:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            1.03              0.78        107.17                39.87         0.579            pass              0.173              5.5                           0.310                0.28              0.068                                 ok            True                  False
  CTSH          100.00               35            0.63              0.27         61.73                43.69         0.503            pass              0.774             52.4                           0.424               -3.06             -0.109                                 ok            True                  False
   TRI           91.67               24            1.85              1.31        100.75                57.96         0.570            pass              0.496             11.4                           0.168               -6.07             -0.594 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.33               15            0.44              0.08         24.70                25.04         0.561            pass              0.506             20.3                           0.240               -4.75             -0.324            downtrend_blocked_slope           False                  False
   PEP          100.00               11            0.90              0.85        133.98                14.34         0.543            pass              0.504             14.2                           0.257               -4.25             -0.382            downtrend_blocked_slope           False                  False
  ADSK           84.38               32            0.91              1.40        219.71                56.33         0.540            pass              0.463             48.7                           0.618               -9.69             -0.468 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.48               42            0.38              0.36        134.85                64.77         0.537            pass              0.733             66.8                           0.593              -15.40             -1.330 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.88               32            0.13              0.25        273.08                24.48         0.506            pass              0.873             92.0                           0.752               -2.34             -0.127                                 ok           False                  False
   EXC           96.30               27            0.02              0.01         42.44                15.25         0.505            pass              0.849             95.0                           0.658               -2.58             -0.414 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           87.50               16            1.75              0.29         23.61                34.54         0.498 below_threshold              0.355             21.7                           0.404              -13.04             -1.360 downtrend_blocked_slope_and_streak           False                  False
  PAYX           90.00               30            0.45              0.36        116.56                25.45         0.492 below_threshold              0.645             65.3                           0.707               -6.29             -0.592            downtrend_blocked_slope           False                  False
  NFLX           89.29               28            1.17              0.63         76.14                36.27         0.488 below_threshold              0.458             13.9                           0.219               -8.72             -0.615 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-17T11:20:05.657470-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:15:04.369387-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:10:05.281935-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:05:01.167254-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:00:02.392544-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:55:01.499758-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:50:04.360759-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:45:01.293299-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917112005)

</details>
