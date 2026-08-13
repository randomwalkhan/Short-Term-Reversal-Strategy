# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:55:08 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   ROP           96.88               32            0.63              1.75        394.48                44.32         0.594          pass              0.716             36.5                           0.207                0.89              0.177                       ok            True                  False
  FAST          100.00               20            0.66              0.24         52.12                25.01         0.585          pass              0.647             40.5                           0.265               11.18              1.188                       ok            True                  False
  MPWR           84.21               38            0.73              7.31       1421.88                55.33         0.545          pass              0.470             38.8                           0.397                7.48              0.602                       ok            True                  False
   BKR           85.71               21            1.24              0.56         64.04                33.24         0.537          pass              0.445             55.3                           0.754                6.37              0.781                       ok            True                  False
  PCAR           96.00               25            1.12              1.03        130.62                29.70         0.533          pass              0.641             29.3                           0.175               -3.12             -0.200                       ok            True                  False
  ADSK           80.65               31            0.90              1.58        248.83                45.76         0.526          pass              0.420             70.0                           0.352                5.23              0.834                       ok            True                  False
  INSM           66.67               12            3.39              3.14        130.94               107.72         0.718          pass              0.086              0.3                           0.060               25.92              3.742                       ok           False                  False
  ISRG           86.84               38            0.30              0.85        400.91                69.94         0.671          pass              0.625             63.0                           0.489               13.34              1.339                       ok           False                  False
  BKNG           97.50               40            0.28              0.41        212.08                44.60         0.550          pass              0.908             84.2                           0.396                9.54              1.214                       ok           False                  False
   MAR           93.02               43            0.04              0.09        354.54                36.15         0.529          pass              0.860             86.6                           0.495               -5.60             -0.445  downtrend_blocked_slope           False                  False
  ROST           83.33               12            1.61              2.79        247.05                22.10         0.527          pass              0.247             30.7                           0.195               -3.29             -0.135 downtrend_blocked_streak           False                  False
  CTSH           88.64               44            0.01              0.00         58.20                52.45         0.523          pass              0.782             99.7                           0.436                7.97              0.780                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-13T10:55:08.693001-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:50:06.656727-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:45:05.716693-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:40:10.431028-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:35:08.719100-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:30:06.616446-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:25:07.519899-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:20:10.643979-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:10:10.565177-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813105508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813105508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813105508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813105508)

</details>
