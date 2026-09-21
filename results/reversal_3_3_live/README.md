# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:05:05 EDT`
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
   KHC           94.12               17            0.53              0.09         24.39                22.04         0.548            pass              0.555             25.8                           0.301               -2.21             -0.128                                 ok            True                  False
  WDAY           94.29               35            0.57              0.78        193.54                50.60         0.543            pass              0.752             50.1                           0.379               -1.55              0.312                                 ok            True                  False
   PEP          100.00               11            0.81              0.73        129.44                15.76         0.558            pass              0.585             41.0                           0.519               -6.48             -0.638 downtrend_blocked_slope_and_streak           False                  False
  CHTR           88.89               27            1.92              1.72        127.43                64.18         0.546            pass              0.481             25.2                           0.309              -17.29             -1.443 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.34              0.59        248.67                46.23         0.535            pass              0.886             81.9                           0.700               -6.92             -0.437            downtrend_blocked_slope           False                  False
   ADP           95.00               20            0.68              1.28        270.67                22.01         0.529            pass              0.682             54.1                           0.593               -2.35              0.127           downtrend_blocked_streak           False                  False
  TMUS           94.74               19            1.08              1.27        167.63                33.56         0.511            pass              0.718             71.2                           0.824               -8.35             -0.869            downtrend_blocked_slope           False                  False
  VRSK           86.67               15            2.08              2.55        174.32                39.25         0.506            pass              0.321             19.6                           0.365               -7.30             -0.265            downtrend_blocked_slope           False                  False
  PAYX           83.33               18            1.18              0.96        115.73                23.92         0.496 below_threshold              0.282             30.1                           0.494               -5.70             -0.206           downtrend_blocked_streak           False                  False
  SBUX           81.82               11            1.50              1.01         95.40                22.99         0.494 below_threshold              0.209             34.7                           0.388               -9.65             -0.837 downtrend_blocked_slope_and_streak           False                  False
   BKR           94.87               39            0.10              0.04         57.23                30.72         0.493 below_threshold              0.912             91.0                           0.729               -9.94             -1.331 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.55               29            0.02              0.01         42.07                15.92         0.488 below_threshold              0.870             98.1                           0.670               -3.62             -0.454 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:35:04.666862-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:30:01.878721-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:20:05.839585-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921110505)

</details>
