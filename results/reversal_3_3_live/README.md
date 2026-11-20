# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 13:45:05 EST`
Last processed slot: `manual`

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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.06               34            0.88              4.27        687.82                78.44         0.696          pass              0.722             30.8                           0.393                1.11             -0.060                                 ok            True                  False
  AAPL          100.00               13            1.37              3.36        347.77                27.12         0.563          pass              0.476              0.0                           0.253                0.67              0.028                                 ok            True                  False
   MAR           93.33               15            1.05              3.04        412.74                25.25         0.550          pass              0.523             26.3                           0.424               -1.46             -0.128                                 ok            True                  False
  INSM           84.44               45            0.51              0.52        144.24                87.95         0.537          pass              0.582             69.9                           0.352               25.62              1.891                                 ok            True                  False
  ODFL           86.21               29            1.01              1.23        173.30                43.88         0.524          pass              0.345              0.0                           0.150                4.34              0.396                                 ok            True                  False
  ALNY           83.33               48            0.10              0.11        147.77               110.46         0.736          pass              0.430             22.5                           0.266               -5.31             -0.519 downtrend_blocked_slope_and_streak           False                  False
  INTC           58.33               12            4.95              1.93         54.89               141.91         0.714          pass              0.137             17.4                           0.465               -5.90             -0.991 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                2            6.99             18.55        371.07               122.37         0.645          pass              0.465              0.0                           0.183               -9.89             -0.769 downtrend_blocked_slope_and_streak           False                  False
  FTNT           50.00                8            4.26              3.92        129.78                96.17         0.600          pass              0.063              1.0                           0.125                5.91              0.598                                 ok           False                  False
  FAST           87.50                8            1.55              0.57         52.44                22.02         0.537          pass              0.322             22.9                           0.451               -2.12             -0.315 downtrend_blocked_slope_and_streak           False                  False
  MSFT           90.91               11            1.89              6.60        495.47                37.07         0.536          pass              0.465             37.9                           0.366               -7.69             -0.875            downtrend_blocked_slope           False                  False
  GOOG           84.38               32            0.52              0.99        270.59                53.33         0.535          pass              0.506             63.0                           0.370               -5.05             -0.614            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-20T12:00:03.900140-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:45:06.435631-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:40:06.030121-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:35:06.036427-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:30:06.242321-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:25:03.911005-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:20:05.063742-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:15:06.465652-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120134505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120134505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120134505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120134505)

</details>
