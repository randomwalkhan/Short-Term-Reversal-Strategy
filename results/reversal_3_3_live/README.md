# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:55:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            1.02              0.77        107.17                39.87         0.580          pass              0.157              0.0                           0.185                0.29              0.069                                 ok            True                  False
  CTSH          100.00               35            0.53              0.23         61.75                43.69         0.509          pass              0.797             59.8                           0.495               -2.97             -0.105                                 ok            True                  False
   TRI           92.31               26            1.50              1.06        100.85                57.96         0.583          pass              0.517              7.9                           0.158               -5.74             -0.578 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.33               15            0.47              0.08         24.70                25.04         0.560          pass              0.445              0.0                           0.150               -4.77             -0.325            downtrend_blocked_slope           False                  False
  ADBE           97.37               38            0.03              0.06        250.48                47.92         0.544          pass              0.936             98.4                           0.797              -10.50             -1.025 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               11            0.90              0.85        133.98                14.34         0.543          pass              0.488              9.0                           0.181               -4.25             -0.382            downtrend_blocked_slope           False                  False
  ADSK           82.76               29            1.21              1.86        219.51                56.33         0.538          pass              0.350             32.1                           0.309               -9.96             -0.482 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.24               41            0.64              0.60        134.74                64.77         0.527          pass              0.659             44.5                           0.448              -15.62             -1.342 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.22              0.07         42.41                15.25         0.521          pass              0.690             52.5                           0.448               -2.78             -0.423 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.43               28            0.35              0.67        272.90                24.48         0.516          pass              0.807             78.4                           0.611               -2.55             -0.137                                 ok           False                  False
  INTU          100.00               37            0.49              1.10        317.66                44.10         0.505          pass              0.821             63.6                           0.397               -7.69             -0.546 downtrend_blocked_slope_and_streak           False                  False
  PAYX           88.46               26            0.66              0.54        116.49                25.45         0.500          pass              0.527             48.3                           0.534               -6.50             -0.602            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-17T10:55:01.499758-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:50:04.360759-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:45:01.293299-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:30:05.183690-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:25:03.246728-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:20:02.157972-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917105501)

</details>
