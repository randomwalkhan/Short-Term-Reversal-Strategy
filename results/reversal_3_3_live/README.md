# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 11:10:05 EDT`
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
   WMT           82.14               28            0.81              0.61        107.24                39.87         0.553            pass              0.306             24.7                           0.359                0.51              0.079                                 ok            True                  False
  CTSH          100.00               34            0.79              0.34         61.70                43.69         0.500 below_threshold              0.731             40.2                           0.359               -3.22             -0.117                                 ok            True                  False
   TRI           90.48               21            2.04              1.45        100.69                57.96         0.575            pass              0.417              2.1                           0.039               -6.26             -0.603 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.33               15            0.53              0.09         24.69                25.04         0.556            pass              0.456              3.7                           0.073               -4.82             -0.327            downtrend_blocked_slope           False                  False
   PEP          100.00                9            1.00              0.94        133.94                14.34         0.549            pass              0.468              4.3                           0.085               -4.35             -0.387            downtrend_blocked_slope           False                  False
  ADSK           85.71               28            1.34              2.06        219.43                56.33         0.540            pass              0.400             24.6                           0.336              -10.08             -0.488 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.48               42            0.36              0.34        134.85                64.77         0.538            pass              0.739             68.7                           0.606              -15.38             -1.329 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.15              0.27        250.38                47.92         0.536            pass              0.918             92.4                           0.769              -10.61             -1.031 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.55               29            0.26              0.50        272.98                24.48         0.515            pass              0.829             83.8                           0.663               -2.47             -0.133                                 ok           False                  False
  NFLX           85.71               21            1.35              0.72         76.10                36.27         0.514            pass              0.277              0.0                           0.150               -8.89             -0.623 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.15               26            0.05              0.01         42.43                15.25         0.510            pass              0.828             90.0                           0.638               -2.61             -0.415 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               42            0.07              0.16        318.06                44.10         0.500 below_threshold              0.935             95.1                           0.658               -7.30             -0.527 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-17T11:10:05.281935-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:05:01.167254-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:00:02.392544-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:55:01.499758-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:50:04.360759-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:45:01.293299-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:30:05.183690-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:25:03.246728-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917111005)

</details>
