# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 13:50:08 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           90.48               21            1.60              0.80         71.54               125.47         0.813          pass              0.670             78.7                           0.665                8.80              0.661                                 ok            True                  False
    MU           89.29               28            1.65             13.07       1126.73               130.58         0.725          pass              0.689             82.8                           0.662               13.45              1.132                                 ok            True                  False
   XEL          100.00               18            0.74              0.43         82.05                23.26         0.592          pass              0.562             16.6                           0.158                3.81              0.519                                 ok            True                  False
   EXC           84.62               13            0.98              0.33         47.26                19.58         0.575          pass              0.242             13.9                           0.215                1.57              0.244                                 ok            True                  False
  GILD           91.67               12            1.60              1.43        127.27                29.34         0.565          pass              0.424             14.4                           0.311                0.85              0.073                                 ok            True                  False
  PCAR           80.95               21            1.15              0.97        120.26                36.52         0.540          pass              0.271             39.6                           0.595                0.65              0.022                                 ok            True                  False
  PAYX          100.00               24            0.85              0.59         99.65                33.42         0.527          pass              0.677             43.7                           0.348               -1.57             -0.233                                 ok            True                  False
   HON           60.00                5            2.65              4.52        241.47               250.29         0.998          pass              0.254             51.5                           0.486                7.55              6.063                                 ok           False                  False
  ROST           93.75               16            1.29              1.93        212.43                36.17         0.564          pass              0.574             36.8                           0.594              -12.34             -1.265 downtrend_blocked_slope_and_streak           False                  False
  CTAS           76.92               13            1.63              1.96        171.06                30.93         0.559          pass              0.126             16.8                           0.427               -4.07             -0.366            downtrend_blocked_slope           False                  False
  CDNS           94.44               36            0.57              1.49        376.63                56.11         0.557          pass              0.774             53.3                           0.537               -2.55             -0.523            downtrend_blocked_slope           False                  False
   KDP          100.00               21            0.46              0.11         33.35                25.91         0.556          pass              0.596             22.5                           0.264                5.59              0.532                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T12:00:02.850105-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:50:05.501340-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:45:01.788217-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:40:06.618174-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:35:03.964780-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:30:02.880420-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:25:02.270662-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:22:12.890748-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:15:24.828732-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629135008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629135008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629135008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629135008)

</details>
