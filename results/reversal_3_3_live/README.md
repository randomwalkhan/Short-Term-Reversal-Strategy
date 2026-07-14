# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 13:55:01 EDT`
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

- Cash: `$17,620.25`
- Equity: `$27,195.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9575.0        46.88          47.88      660.72        661.77          bid_ask_mid                      47.88                bid_ask_mid                    True           200.0                   2.13         81.82               22              1.27         53.38           54.47                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               10            0.69              0.12         25.18                36.18         0.672          pass              0.514             60.0                           0.603                3.58              0.343                                 ok            True                  False
  AAPL           95.65               23            0.75              1.66        316.60                35.57         0.591          pass              0.738             64.3                           0.661               11.78              1.120                                 ok            True                  False
  CSCO           91.67               12            1.73              1.44        118.63                35.64         0.559          pass              0.398              5.9                           0.270               -0.06              0.235                                 ok            True                  False
  PAYX          100.00               24            0.97              0.75        110.43                31.82         0.541          pass              0.772             74.7                           0.386                9.88              0.947                                 ok            True                  False
  PYPL           80.95               21            1.10              0.37         47.49                33.27         0.541          pass              0.324             57.0                           0.553                6.19              0.671                                 ok            True                  False
  CTAS           86.36               22            1.21              1.55        183.09                31.28         0.534          pass              0.402             33.1                           0.280                7.37              0.635                                 ok            True                  False
  AMGN           95.65               23            0.95              2.41        359.42                21.45         0.522          pass              0.659             40.1                           0.670               -0.98             -0.079                                 ok            True                  False
  PCAR           87.10               31            0.69              0.60        124.00                31.62         0.513          pass              0.517             45.6                           0.554                3.18              0.409                                 ok            True                  False
  MDLZ          100.00                6            1.37              0.57         59.61                31.17         0.642          pass              0.557             31.1                           0.644               -1.02              0.025                                 ok           False                  False
   KDP           80.00                5            2.06              0.45         31.06                34.17         0.596          pass              0.081              7.2                           0.282               -8.64             -0.809 downtrend_blocked_slope_and_streak           False                  False
   PEP           87.50                8            1.74              1.69        137.77                30.22         0.591          pass              0.298             12.8                           0.329               -1.88             -0.136                                 ok           False                  False
   ADP          100.00                7            1.96              3.44        249.57                31.20         0.584          pass              0.590             44.0                           0.301                9.41              0.829                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714135501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714135501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714135501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714135501)

</details>
