# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 12:25:04 EST`
Last processed slot: `manage_1230`

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
  IDXX           97.06               34            0.88              4.26        687.83                78.44         0.698          pass              0.630              0.2                           0.086                1.11             -0.060                                 ok            True                  False
  AAPL          100.00               19            0.96              2.34        348.21                27.12         0.553          pass              0.556             13.7                           0.278                1.10              0.047                                 ok            True                  False
   MAR           93.33               15            1.14              3.30        412.62                25.25         0.546          pass              0.469              8.3                           0.219               -1.55             -0.132                                 ok            True                  False
  INTC           63.64               11            5.01              1.95         54.88               141.91         0.722          pass              0.125             15.5                           0.157               -5.95             -0.993 downtrend_blocked_slope_and_streak           False                  False
   APP           85.71                7            4.85             12.86        373.51               122.37         0.719          pass              0.307             27.5                           0.512               -7.82             -0.665 downtrend_blocked_slope_and_streak           False                  False
  FTNT           50.00               10            3.65              3.36        130.02                96.17         0.626          pass              0.106             14.4                           0.323                6.58              0.627                                 ok           False                  False
  ABNB           90.70               43            0.08              0.09        172.75                57.19         0.542          pass              0.818             92.7                           0.477               -9.12             -0.862 downtrend_blocked_slope_and_streak           False                  False
  MSFT           90.00               10            1.94              6.75        495.41                37.07         0.539          pass              0.430             36.5                           0.339               -7.73             -0.877            downtrend_blocked_slope           False                  False
  FAST           85.71                7            1.74              0.64         52.41                22.02         0.532          pass              0.214              2.7                           0.180               -2.31             -0.324 downtrend_blocked_slope_and_streak           False                  False
  CHTR           76.74               43            0.56              0.52        132.96                64.90         0.518          pass              0.252              0.0                           0.247               12.17              1.038                                 ok           False                  False
  ROST           76.92               13            1.64              2.53        218.80                42.36         0.514          pass              0.294             74.0                           0.872               -6.41             -0.927 downtrend_blocked_slope_and_streak           False                  False
  CSCO           42.86                7            2.68              1.77         93.94                50.60         0.509          pass              0.103             17.4                           0.364               -1.80             -0.432            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120122504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120122504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120122504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120122504)

</details>
