# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 12:55:04 EDT`
Last processed slot: `manage_1300`

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
  DRAM           91.67               24            1.32              0.66         71.60               125.47         0.813          pass              0.733             82.4                           0.850                9.11              0.674                                 ok            True                  False
    MU           90.62               32            0.65              5.15       1130.12               130.58         0.761          pass              0.786             93.2                           0.936               14.61              1.178                                 ok            True                   True
  GILD           90.00               10            1.69              1.51        127.23                29.34         0.571          pass              0.353              9.6                           0.190                0.76              0.069                                 ok            True                  False
  PAYX          100.00               25            0.82              0.57         99.65                33.42         0.521          pass              0.689             45.7                           0.343               -1.54             -0.232                                 ok            True                  False
  SBUX           89.66               29            0.51              0.37        104.44                26.41         0.509          pass              0.619             61.2                           0.735                0.99              0.261                                 ok            True                  False
   HON           60.00                5            2.66              4.54        241.47               250.29         0.998          pass              0.254             51.3                           0.529                7.54              6.062                                 ok           False                  False
  INTC           94.87               39            0.02              0.02        128.31                98.20         0.662          pass              0.955             99.7                           0.882                2.99              0.633                                 ok           False                  False
   EXC           78.57               14            0.63              0.21         47.31                19.58         0.582          pass              0.218             44.4                           0.531                1.93              0.260                                 ok           False                  False
   XEL          100.00               25            0.27              0.16         82.16                23.26         0.572          pass              0.765             69.2                           0.721                4.30              0.540                                 ok           False                  False
  ROST           87.50                8            1.93              2.89        212.02                36.17         0.569          pass              0.274              5.6                           0.218              -12.91             -1.295 downtrend_blocked_slope_and_streak           False                  False
  AAPL           94.12               17            1.18              2.34        282.78                34.42         0.568          pass              0.523             14.5                           0.263               -3.67             -0.587 downtrend_blocked_slope_and_streak           False                  False
  CTAS           62.50                8            1.85              2.23        170.95                30.93         0.562          pass              0.071              4.8                           0.159               -4.29             -0.376            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629125504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629125504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629125504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629125504)

</details>
