# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 13:30:06 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$27,185.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$190.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9565.0        46.88          47.82      660.72        663.97          bid_ask_mid                      47.82                bid_ask_mid                    True           190.0                   2.03         81.82               22              1.27         53.38           52.83                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AAPL           95.65               23            0.78              1.73        316.57                35.57         0.589          pass              0.734             62.7                           0.717               11.75              1.118                  ok            True                  False
   EXC           94.12               17            0.68              0.22         46.99                22.01         0.570          pass              0.683             67.7                           0.356               -0.81             -0.007                  ok            True                  False
  CSCO           93.33               15            1.46              1.22        118.73                35.64         0.560          pass              0.489             14.7                           0.377                0.21              0.248                  ok            True                  False
   ADP           93.75               16            1.45              2.56        249.95                31.20         0.549          pass              0.637             58.5                           0.583                9.97              0.852                  ok            True                  False
  AMGN           94.44               18            1.06              2.68        359.30                21.45         0.548          pass              0.593             33.2                           0.646               -1.09             -0.084                  ok            True                  False
  GILD           89.66               29            0.50              0.46        131.20                32.97         0.536          pass              0.638             66.7                           0.734                3.49              0.430                  ok            True                  False
  PCAR           85.19               27            0.83              0.72        123.95                31.62         0.529          pass              0.409             34.8                           0.474                3.04              0.403                  ok            True                  False
  TMUS           87.10               31            0.75              0.99        187.98                37.13         0.525          pass              0.489             35.6                           0.273                7.48              1.025                  ok            True                  False
  CTAS           89.29               28            0.84              1.09        183.28                31.28         0.520          pass              0.579             53.2                           0.635                7.76              0.652                  ok            True                  False
  IDXX           91.67               12            2.50              9.88        559.98                34.15         0.520          pass              0.465             29.5                           0.529                2.64              0.516                  ok            True                  False
  PYPL           86.67               30            0.75              0.25         47.54                33.27         0.511          pass              0.575             70.9                           0.767                6.57              0.687                  ok            True                  False
  CTSH           81.58               38            0.72              0.22         44.06                65.60         0.503          pass              0.554             91.7                           0.737               13.16              1.205                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714133006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714133006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714133006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714133006)

</details>
