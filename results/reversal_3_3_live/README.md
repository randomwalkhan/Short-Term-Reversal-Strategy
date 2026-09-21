# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:25:04 EDT`
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
   KHC           94.74               19            0.28              0.05         24.41                22.04         0.551            pass              0.702             64.5                           0.428               -1.97             -0.116                                 ok           False                  False
   PEP           93.33               15            0.73              0.66        129.47                15.76         0.528            pass              0.581             46.3                           0.544               -6.42             -0.635 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.00               20            0.75              1.42        270.61                22.01         0.524            pass              0.666             49.1                           0.374               -2.42              0.123           downtrend_blocked_streak           False                  False
  CHTR           89.47               38            1.19              1.07        127.71                64.18         0.524            pass              0.652             53.5                           0.754              -16.68             -1.409 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.30               37            0.65              1.14        248.43                46.23         0.523            pass              0.828             65.4                           0.409               -7.21             -0.452            downtrend_blocked_slope           False                  False
  WDAY           95.24               42            0.33              0.45        193.68                50.60         0.517            pass              0.865             71.2                           0.513               -1.31              0.323                                 ok           False                  False
  VRSK           86.67               15            2.07              2.54        174.32                39.25         0.507            pass              0.321             19.9                           0.297               -7.29             -0.265            downtrend_blocked_slope           False                  False
  INTU          100.00               35            0.72              1.53        302.54                42.64         0.496 below_threshold              0.835             73.0                           0.513               -9.53             -0.594 downtrend_blocked_slope_and_streak           False                  False
  PAYX           84.21               19            1.13              0.92        115.75                23.92         0.494 below_threshold              0.321             33.2                           0.424               -5.65             -0.204           downtrend_blocked_streak           False                  False
  TMUS           95.83               24            0.91              1.07        167.72                33.56         0.493 below_threshold              0.770             75.8                           0.766               -8.19             -0.861            downtrend_blocked_slope           False                  False
  SBUX           75.00                8            1.67              1.12         95.35                22.99         0.491 below_threshold              0.131             27.4                           0.283               -9.80             -0.845 downtrend_blocked_slope_and_streak           False                  False
  ORLY           93.75               16            1.61              0.95         84.30                19.71         0.483 below_threshold              0.509             18.1                           0.383               -5.17             -0.376            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:25:04.810284-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:20:06.298711-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:15:05.659477-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:10:04.948141-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921112504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921112504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921112504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921112504)

</details>
