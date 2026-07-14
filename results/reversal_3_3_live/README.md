# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 14:15:05 EDT`
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

- Cash: `$17,620.25`
- Equity: `$27,065.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$70.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9445.0        46.88          47.22      660.72        661.82          bid_ask_mid                      47.22                bid_ask_mid                    True            70.0                   0.75         81.82               22              1.27         53.38            54.1                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               10            0.69              0.12         25.18                36.18         0.672          pass              0.514             60.0                           0.636                3.58              0.343                                 ok            True                  False
  AAPL           96.00               25            0.65              1.43        316.70                35.57         0.584          pass              0.766             69.1                           0.725               11.90              1.124                                 ok            True                  False
  CSCO           90.00               10            1.87              1.56        118.58                35.64         0.561          pass              0.331              2.8                           0.176               -0.21              0.229                                 ok            True                  False
   EXC           95.00               20            0.53              0.17         47.02                22.01         0.560          pass              0.747             74.7                           0.510               -0.66             -0.000                                 ok            True                  False
  PAYX          100.00               25            0.85              0.66        110.47                31.82         0.542          pass              0.788             77.9                           0.603               10.02              0.952                                 ok            True                  False
  PYPL           84.00               25            0.98              0.33         47.51                33.27         0.526          pass              0.445             61.9                           0.544                6.32              0.677                                 ok            True                  False
  AMGN           95.65               23            0.94              2.36        359.44                21.45         0.523          pass              0.663             41.2                           0.636               -0.96             -0.078                                 ok            True                  False
  CTAS           89.29               28            0.84              1.08        183.29                31.28         0.520          pass              0.580             53.5                           0.551                7.77              0.652                                 ok            True                  False
  PCAR           87.10               31            0.58              0.50        124.04                31.62         0.519          pass              0.544             54.4                           0.614                3.29              0.415                                 ok            True                  False
  MDLZ          100.00                5            1.50              0.63         59.59                31.17         0.641          pass              0.538             24.8                           0.439               -1.15              0.019                                 ok           False                  False
   KDP           80.00                5            2.11              0.46         31.05                34.17         0.593          pass              0.074              5.0                           0.272               -8.69             -0.811 downtrend_blocked_slope_and_streak           False                  False
   PEP           85.71                7            1.91              1.85        137.70                30.22         0.586          pass              0.225              4.7                           0.236               -2.04             -0.143                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714141505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714141505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714141505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714141505)

</details>
