# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 11:40:06 EST`
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
  AAPL           95.65               23            0.76              1.86        348.41                27.12         0.536          pass              0.561              7.0                           0.221                1.30              0.056                                 ok            True                  False
   MAR           90.91               22            0.64              1.85        413.25                25.25         0.532          pass              0.488             21.2                           0.286               -1.05             -0.109                                 ok            True                  False
  INTC           57.14               21            3.43              1.34         55.15               141.91         0.746          pass              0.274             42.1                           0.259               -4.39             -0.918 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.92             15.70        372.29               122.37         0.700          pass              0.504             11.5                           0.220               -8.85             -0.717 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.50               40            0.41              1.99        688.80                78.44         0.696          pass              0.686              5.3                           0.236                1.59             -0.038                                 ok           False                  False
  FTNT           68.42               19            2.73              2.51        130.38                96.17         0.656          pass              0.181             18.5                           0.249                7.60              0.670                                 ok           False                  False
  QCOM           71.43                7            3.46              3.92        160.33                69.46         0.559          pass              0.089             11.0                           0.144               -5.44             -0.836 downtrend_blocked_slope_and_streak           False                  False
  FAST           91.67               12            1.12              0.41         52.50                22.02         0.549          pass              0.389              3.3                           0.160               -1.70             -0.295 downtrend_blocked_slope_and_streak           False                  False
  MCHP           66.67               12            3.61              1.48         57.84                78.21         0.543          pass              0.110             14.2                           0.217               -3.41             -0.504            downtrend_blocked_slope           False                  False
  CSCO           55.56                9            2.32              1.54         94.04                50.60         0.542          pass              0.058              1.3                           0.167               -1.44             -0.416                                 ok           False                  False
  CHTR           77.27               44            0.31              0.29        133.06                64.90         0.529          pass              0.327             24.5                           0.183               12.45              1.049                                 ok           False                  False
  MSFT           94.44               18            1.47              5.11        496.11                37.07         0.522          pass              0.646             51.9                           0.304               -7.29             -0.856            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-20T11:40:06.030121-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:35:06.036427-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:30:06.242321-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:25:03.911005-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:20:05.063742-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:15:06.465652-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:10:05.768872-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:05:06.071133-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:00:06.033769-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:55:04.962322-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120114006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120114006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120114006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120114006)

</details>
