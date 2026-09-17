# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 11:25:02 EDT`
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
   WMT           85.00               20            1.07              0.80        107.16                39.87         0.587            pass              0.289             10.2                           0.304                0.25              0.067                                 ok            True                  False
  CTSH          100.00               35            0.54              0.23         61.75                43.69         0.509            pass              0.795             59.1                           0.576               -2.97             -0.105                                 ok            True                  False
   TRI           91.67               24            1.80              1.27        100.76                57.96         0.573            pass              0.503             13.7                           0.211               -6.03             -0.592 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.33               15            0.34              0.06         24.70                25.04         0.567            pass              0.561             38.3                           0.397               -4.65             -0.319            downtrend_blocked_slope           False                  False
   PEP          100.00               11            0.84              0.79        134.00                14.34         0.547            pass              0.521             19.9                           0.324               -4.19             -0.379            downtrend_blocked_slope           False                  False
  ADSK           85.29               34            0.69              1.07        219.85                56.33         0.542            pass              0.538             61.0                           0.704               -9.49             -0.458 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.48               42            0.37              0.35        134.85                64.77         0.538            pass              0.736             67.7                           0.609              -15.39             -1.330 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.00               25            0.09              0.03         42.43                15.25         0.512            pass              0.791             80.0                           0.582               -2.65             -0.417 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.88               32            0.07              0.14        273.13                24.48         0.509            pass              0.884             95.5                           0.802               -2.28             -0.125                                 ok           False                  False
 CMCSA           86.67               15            1.79              0.30         23.60                34.54         0.500            pass              0.321             19.8                           0.401              -13.07             -1.361 downtrend_blocked_slope_and_streak           False                  False
  ISRG           87.50               32            0.85              2.28        381.31                34.87         0.488 below_threshold              0.451             18.6                           0.253                1.92              0.463                                 ok           False                  False
  PAYX           87.10               31            0.36              0.29        116.59                25.45         0.487 below_threshold              0.594             72.0                           0.744               -6.21             -0.588            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-17T11:25:02.294340-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:20:05.657470-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:15:04.369387-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:10:05.281935-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:05:01.167254-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:00:02.392544-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:55:01.499758-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:50:04.360759-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:45:01.293299-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917112502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917112502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917112502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917112502)

</details>
