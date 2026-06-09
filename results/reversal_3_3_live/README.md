# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:50:02 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           84.21               19            0.99              0.57         82.93                69.62         0.702          pass              0.349             35.4                           0.273               -1.62             -0.105                                 ok            True                  False
  CTSH           92.59               27            1.04              0.39         52.82                51.28         0.574          pass              0.625             39.6                           0.210                1.22             -0.128                                 ok            True                  False
  CDNS           91.67               24            1.49              4.12        392.47                58.79         0.568          pass              0.478              5.7                           0.078                1.73              0.443                                 ok            True                  False
  TEAM           95.24               21            3.83              2.63         96.76                87.01         0.542          pass              0.557              9.9                           0.188               10.86              0.760                                 ok            True                  False
   WDC          100.00               19            2.91             10.75        522.32                73.41         0.522          pass              0.608             31.8                           0.323               -2.47             -0.017                                 ok            True                  False
    ZS           72.73               11            4.11              3.72        127.66               157.94         0.851          pass              0.111              6.3                           0.162              -32.86             -1.908            downtrend_blocked_slope           False                  False
  DRAM          100.00               12            2.62              1.11         60.04               103.58         0.715          pass              0.559             24.7                           0.205               -2.60             -0.352            downtrend_blocked_slope           False                  False
  INTU           70.59               17            3.15              6.73        302.62               100.92         0.679          pass              0.127              4.2                           0.149               -2.78             -0.585 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               24            0.20              0.14         98.86                34.09         0.625          pass              0.820             88.0                           0.469                4.14              0.503                                 ok           False                  False
  MSFT           75.00                4            2.18              6.29        409.05                36.13         0.606          pass              0.064              1.0                           0.045               -3.19             -0.382            downtrend_blocked_slope           False                  False
   CEG           78.12               32            0.63              1.11        250.20                55.25         0.592          pass              0.347             47.2                           0.406              -17.40             -1.847 downtrend_blocked_slope_and_streak           False                  False
    MU           76.92               13            4.39             29.19        936.77               111.98         0.577          pass              0.129             17.1                           0.197                1.31              0.042                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-09T11:50:02.014967-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:45:02.008648-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:40:06.401362-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:35:02.395564-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:10:02.019874-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "WDC260717C00520000", "current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "entry_ask": 61.05, "entry_bid": 54.7, "entry_mode": "early", "entry_option_price": 57.875, "hypothetical_budget": 15111.13, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 457.0, "option_spread_pct": 10.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "matched_signals": 32, "recovery_stability_score": 0.618, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-09T11:05:04.976190-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609115002)

</details>
