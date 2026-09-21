# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:10:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           93.75               16            0.59              0.10         24.39                22.04         0.550            pass              0.513             17.1                           0.196               -2.27             -0.131                                 ok            True                  False
  WDAY           94.29               35            0.52              0.70        193.57                50.60         0.546            pass              0.767             55.0                           0.407               -1.49              0.314                                 ok            True                  False
   PEP          100.00               11            0.83              0.76        129.43                15.76         0.556            pass              0.579             39.0                           0.464               -6.51             -0.640 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.31              0.54        248.69                46.23         0.537            pass              0.891             83.6                           0.695               -6.89             -0.436            downtrend_blocked_slope           False                  False
  CHTR           90.32               31            1.70              1.53        127.52                64.18         0.537            pass              0.570             33.7                           0.514              -17.11             -1.433 downtrend_blocked_slope_and_streak           False                  False
   ADP           94.74               19            0.85              1.61        270.53                22.01         0.524            pass              0.633             42.6                           0.420               -2.51              0.119           downtrend_blocked_streak           False                  False
  VRSK           86.67               15            2.04              2.50        174.34                39.25         0.509            pass              0.326             21.2                           0.335               -7.26             -0.263            downtrend_blocked_slope           False                  False
   XEL          100.00               26            0.12              0.06         72.27                19.27         0.503            pass              0.789             77.5                           0.618               -3.87             -0.526            downtrend_blocked_slope           False                  False
  INTU          100.00               36            0.62              1.31        302.63                42.64         0.496 below_threshold              0.853             76.9                           0.652               -9.43             -0.589 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.30               27            0.10              0.03         42.06                15.92         0.495 below_threshold              0.841             92.7                           0.526               -3.69             -0.458 downtrend_blocked_slope_and_streak           False                  False
  TMUS           95.65               23            1.00              1.18        167.68                33.56         0.493 below_threshold              0.756             73.5                           0.857               -8.27             -0.865            downtrend_blocked_slope           False                  False
  PAYX           83.33               18            1.24              1.00        115.71                23.92         0.493 below_threshold              0.272             26.8                           0.442               -5.76             -0.209           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:10:04.948141-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:35:04.666862-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:30:01.878721-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921111004)

</details>
