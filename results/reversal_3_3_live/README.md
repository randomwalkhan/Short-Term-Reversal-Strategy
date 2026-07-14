# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 14:30:06 EDT`
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

- Cash: `$17,620.25`
- Equity: `$26,780.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-215.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9160.0        46.88           45.8      660.72        660.99          bid_ask_mid                       45.8                bid_ask_mid                    True          -215.0                  -2.29         81.82               22              1.27         53.38           52.28                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           81.82               11            0.61              0.11         25.18                36.18         0.662          pass              0.315             64.6                           0.676                3.66              0.346                                 ok            True                  False
  AAPL           95.83               24            0.66              1.47        316.68                35.57         0.589          pass              0.757             68.3                           0.648               11.88              1.123                                 ok            True                  False
  AMGN           94.12               17            1.12              2.81        359.24                21.45         0.551          pass              0.568             30.0                           0.355               -1.14             -0.086                                 ok            True                  False
  PYPL           80.95               21            1.05              0.35         47.50                33.27         0.544          pass              0.330             59.0                           0.605                6.24              0.673                                 ok            True                  False
  PAYX          100.00               27            0.69              0.54        110.52                31.82         0.539          pass              0.813             82.0                           0.700               10.19              0.959                                 ok            True                  False
  GILD           89.66               29            0.59              0.55        131.17                32.97         0.530          pass              0.619             60.6                           0.576                3.40              0.425                                 ok            True                  False
  TMUS           87.88               33            0.52              0.68        188.12                37.13         0.527          pass              0.584             55.8                           0.487                7.74              1.035                                 ok            True                  False
  PCAR           87.10               31            0.53              0.46        124.06                31.62         0.523          pass              0.557             58.5                           0.614                3.35              0.417                                 ok            True                  False
  CTAS           88.89               27            0.92              1.19        183.24                31.28         0.521          pass              0.549             48.8                           0.612                7.67              0.648                                 ok            True                  False
  MDLZ          100.00                6            1.45              0.61         59.60                31.17         0.637          pass              0.544             26.9                           0.399               -1.11              0.021                                 ok           False                  False
   KDP           80.00                5            2.19              0.48         31.04                34.17         0.588          pass              0.067              2.8                           0.225               -8.76             -0.815 downtrend_blocked_slope_and_streak           False                  False
   PEP           87.50                8            1.81              1.75        137.74                30.22         0.587          pass              0.288              9.7                           0.263               -1.94             -0.139                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-14T12:00:02.352813-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:55:01.322008-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:50:02.227286-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:45:01.430125-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:40:01.377381-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:35:04.197394-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:30:05.253585-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:25:01.317372-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:20:05.915369-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:15:04.383318-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714143006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714143006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714143006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714143006)

</details>
