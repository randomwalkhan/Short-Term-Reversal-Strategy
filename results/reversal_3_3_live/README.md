# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:35:02 EDT`
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
   TRI           83.33               18            1.18              0.69         82.89                69.62         0.696          pass              0.280             22.8                           0.135               -1.82             -0.114                                 ok            True                  False
  CDNS           91.67               24            1.46              4.03        392.51                58.79         0.571          pass              0.472              3.5                           0.227                1.77              0.444                                 ok            True                  False
  CTSH           93.33               30            0.81              0.30         52.86                51.28         0.568          pass              0.704             52.7                           0.253                1.45             -0.118                                 ok            True                  False
  TEAM           95.24               21            3.93              2.70         96.73                87.01         0.535          pass              0.549              7.4                           0.186               10.74              0.755                                 ok            True                  False
    ZS           72.73               11            4.25              3.84        127.60               157.94         0.846          pass              0.101              3.2                           0.213              -32.96             -1.914            downtrend_blocked_slope           False                  False
  DRAM          100.00                9            3.12              1.32         59.95               103.58         0.708          pass              0.471              0.0                           0.223               -3.11             -0.376            downtrend_blocked_slope           False                  False
  INTU           75.00               20            2.61              5.57        303.12               100.92         0.703          pass              0.155              6.1                           0.122               -2.23             -0.560 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                1            3.51              3.05        122.84                58.94         0.637          pass              0.468              1.4                           0.166                1.23              0.435                                 ok           False                  False
  PAYX          100.00               26            0.05              0.03         98.91                34.09         0.621          pass              0.860             97.0                           0.741                4.29              0.510                                 ok           False                  False
  MSFT           80.00                5            2.09              6.02        409.16                36.13         0.613          pass              0.066              1.6                           0.095               -3.10             -0.378            downtrend_blocked_slope           False                  False
   ADI          100.00               14            2.05              5.80        401.40                49.72         0.598          pass              0.503              5.6                           0.116               -5.54             -0.326            downtrend_blocked_slope           False                  False
   CEG           77.42               31            0.89              1.55        250.00                55.25         0.581          pass              0.275             25.7                           0.311              -17.61             -1.859 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-09T11:35:02.395564-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:10:02.019874-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "WDC260717C00520000", "current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "entry_ask": 61.05, "entry_bid": 54.7, "entry_mode": "early", "entry_option_price": 57.875, "hypothetical_budget": 15111.13, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 457.0, "option_spread_pct": 10.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "matched_signals": 32, "recovery_stability_score": 0.618, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-09T11:05:04.976190-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:00:04.007300-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:55:02.016087-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609113502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609113502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609113502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609113502)

</details>
