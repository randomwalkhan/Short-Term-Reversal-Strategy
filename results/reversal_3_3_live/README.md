# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 11:00:08 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   ROP           96.88               32            0.55              1.53        394.58                44.32         0.599            pass              0.741             44.7                           0.259                0.98              0.181                       ok            True                  False
  FAST          100.00               23            0.51              0.19         52.14                25.01         0.575            pass              0.707             54.3                           0.313               11.35              1.195                       ok            True                  False
  PCAR           95.45               22            1.34              1.23        130.53                29.70         0.539            pass              0.581             15.9                           0.114               -3.33             -0.210                       ok            True                  False
  ADSK           80.65               31            0.92              1.60        248.82                45.76         0.525            pass              0.418             69.5                           0.366                5.21              0.833                       ok            True                  False
  INSM           66.67               12            3.41              3.16        130.93               107.72         0.716            pass              0.087              0.6                           0.038               25.89              3.741                       ok           False                  False
  ISRG           87.50               40            0.16              0.45        401.08                69.94         0.668            pass              0.708             80.4                           0.614               13.50              1.346                       ok           False                  False
  MPWR           84.21               38            0.46              4.57       1423.05                55.33         0.562            pass              0.540             61.8                           0.544                7.77              0.614                       ok           False                  False
  BKNG           97.56               41            0.08              0.12        212.21                44.60         0.556            pass              0.942             95.4                           0.579                9.75              1.223                       ok           False                  False
   BKR           78.57               14            1.47              0.66         64.00                33.24         0.556            pass              0.223             46.8                           0.651                6.12              0.770                       ok           False                  False
  ROST           83.33               12            1.78              3.09        246.93                22.10         0.517            pass              0.224             23.3                           0.160               -3.46             -0.142 downtrend_blocked_streak           False                  False
   HON           91.43               35            0.57              0.94        234.94                35.57         0.514            pass              0.679             52.1                           0.624               -3.27             -0.598  downtrend_blocked_slope           False                  False
  CTAS           89.19               37            0.55              0.78        203.18                34.24         0.454 below_threshold              0.571             33.5                           0.175               -2.12             -0.092 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-13T11:00:08.468855-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:55:08.693001-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:50:06.656727-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:45:05.716693-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:40:10.431028-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:35:08.719100-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:30:06.616446-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:25:07.519899-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:20:10.643979-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813110008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813110008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813110008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813110008)

</details>
