# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 12:40:01 EDT`
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

- Cash: `$31,840.75`
- Equity: `$31,840.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            1.03              1.58        217.91               100.52         0.633          pass              0.445             71.7                           0.531                2.53              0.294                       ok            True                  False
  CTAS           87.50               16            1.58              2.25        202.69                37.77         0.589          pass              0.355             18.6                           0.332               -0.46             -0.130                       ok            True                  False
 CMCSA           81.82               11            1.70              0.30         24.80                44.00         0.583          pass              0.199             28.6                           0.293                4.19              0.988                       ok            True                  False
  PAYX          100.00               10            1.47              1.22        118.14                35.13         0.582          pass              0.616             52.5                           0.468                6.68              0.731                       ok            True                  False
   KDP           80.00               20            0.69              0.15         31.04                28.75         0.557          pass              0.272             50.0                           0.421                2.27              0.457                       ok            True                  False
  MSFT           80.00               35            0.87              3.01        491.52                57.86         0.549          pass              0.291             23.2                           0.317               25.15              3.065                       ok            True                  False
  WDAY           82.86               35            1.18              1.41        170.68                70.04         0.524          pass              0.344             16.4                           0.247               27.82              2.862                       ok            True                  False
  CPRT           85.71               14            2.33              0.48         29.19                38.86         0.518          pass              0.285             18.0                           0.320                5.69              0.593                       ok            True                  False
   ADP           96.30               27            0.74              1.41        270.02                35.53         0.515          pass              0.728             54.3                           0.400               10.48              1.132                       ok            True                  False
  SOXL           80.00               35            1.80              1.76        139.14               182.46         0.789          pass              0.469             74.5                           0.894              -14.67             -1.744 downtrend_blocked_streak           False                  False
  AMAT           91.43               35            0.56              2.15        545.70                87.24         0.675          pass              0.782             80.9                           0.777               -1.87             -0.271 downtrend_blocked_streak           False                  False
  LRCX           86.67               30            1.19              2.65        316.60                92.33         0.646          pass              0.584             69.4                           0.620               -1.67             -0.097 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                         detail
2026-08-05T12:00:04.693066-04:00 early_entry_1200 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805124001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805124001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805124001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805124001)

</details>
