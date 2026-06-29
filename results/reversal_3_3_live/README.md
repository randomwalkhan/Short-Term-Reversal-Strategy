# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 14:35:09 EDT`
Last processed slot: `manage_1430`

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
  DRAM           92.00               25            0.88              0.44         71.69               125.47         0.828          pass              0.768             88.3                           0.739                9.59              0.694                                 ok            True                  False
    MU           90.91               33            0.65              5.13       1130.13               130.58         0.756          pass              0.800             93.3                           0.761               14.61              1.178                                 ok            True                   True
   XEL          100.00               20            0.55              0.32         82.09                23.26         0.590          pass              0.641             38.4                           0.398                4.01              0.528                                 ok            True                  False
   EXC           83.33               12            1.08              0.36         47.25                19.58         0.575          pass              0.176              5.6                           0.168                1.47              0.239                                 ok            True                  False
   KDP          100.00               19            0.64              0.15         33.34                25.91         0.556          pass              0.547             10.4                           0.182                5.40              0.524                                 ok            True                  False
  GILD           87.50               16            1.31              1.17        127.38                29.34         0.549          pass              0.385             30.1                           0.618                1.15              0.087                                 ok            True                  False
  PCAR           81.82               22            1.13              0.95        120.27                36.52         0.536          pass              0.305             40.9                           0.482                0.67              0.023                                 ok            True                  False
  PAYX          100.00               27            0.61              0.43         99.72                33.42         0.522          pass              0.744             59.6                           0.422               -1.33             -0.222                                 ok            True                  False
   AEP           81.82               11            1.22              1.18        138.18                21.35         0.507          pass              0.349             81.2                           0.593                6.01              0.803                                 ok            True                  False
   HON           66.67                3            3.65              6.21        240.75               250.29         0.998          pass              0.200             33.3                           0.201                6.46              6.016                                 ok           False                  False
  ROST           87.50                8            1.96              2.93        212.01                36.17         0.566          pass              0.280              7.7                           0.199              -12.93             -1.296 downtrend_blocked_slope_and_streak           False                  False
  CTAS           66.67                9            1.83              2.21        170.96                30.93         0.562          pass              0.075              6.3                           0.169               -4.27             -0.375            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629143509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629143509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629143509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629143509)

</details>
