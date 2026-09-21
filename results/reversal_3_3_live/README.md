# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:30:05 EDT`
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
   KHC           94.12               17            0.51              0.09         24.39                22.04         0.549            pass              0.586             35.9                           0.315               -2.19             -0.127                                 ok            True                  False
   PEP          100.00                9            1.05              0.96        129.34                15.76         0.555            pass              0.524             22.9                           0.302               -6.72             -0.650 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.00               20            0.74              1.40        270.62                22.01         0.525            pass              0.669             50.0                           0.378               -2.41              0.124           downtrend_blocked_streak           False                  False
  WDAY           95.45               44            0.06              0.08        193.84                50.60         0.521            pass              0.937             95.1                           0.717               -1.04              0.335                                 ok           False                  False
  ADBE           97.30               37            0.68              1.19        248.41                46.23         0.521            pass              0.824             63.9                           0.376               -7.24             -0.453            downtrend_blocked_slope           False                  False
  CHTR           88.57               35            1.52              1.36        127.59                64.18         0.521            pass              0.570             40.7                           0.655              -16.96             -1.425 downtrend_blocked_slope_and_streak           False                  False
  TMUS           94.12               17            1.16              1.37        167.59                33.56         0.518            pass              0.682             69.2                           0.704               -8.42             -0.872            downtrend_blocked_slope           False                  False
  CTSH          100.00               39            0.09              0.04         59.85                41.33         0.511            pass              0.822             59.2                           0.403               -4.00              0.134                                 ok           False                  False
  VRSK           85.71               14            2.13              2.61        174.29                39.25         0.508            pass              0.282             17.5                           0.263               -7.35             -0.268            downtrend_blocked_slope           False                  False
  INTU          100.00               33            0.79              1.68        302.47                42.64         0.503            pass              0.815             70.3                           0.487               -9.59             -0.597 downtrend_blocked_slope_and_streak           False                  False
   BKR           94.87               39            0.04              0.02         57.24                30.72         0.496 below_threshold              0.928             96.3                           0.801               -9.88             -1.328 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               28            0.06              0.03         72.29                19.27         0.495 below_threshold              0.840             90.0                           0.698               -3.80             -0.523            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:30:05.864479-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:25:04.810284-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:20:06.298711-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:15:05.659477-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:10:04.948141-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921113005)

</details>
