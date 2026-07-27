# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 10:25:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$17,668.00`
- Equity: `$36,293.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$2,250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 18625.0         6.55           7.45       129.9        132.46          bid_ask_mid                       7.45                bid_ask_mid                    True          2250.0                  13.74         91.67               24              0.73         32.92           31.78                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           83.33               36            0.91              8.50       1330.17                65.61         0.546            pass              0.441             41.5                           0.230                2.34              0.304                                 ok            True                  False
  CSCO           87.50               32            0.70              0.56        113.93                39.56         0.531            pass              0.444             14.9                           0.211               -4.93             -0.235                                 ok            True                  False
  AVGO           82.86               35            0.62              1.66        381.21                43.69         0.503            pass              0.324             10.4                           0.133               -1.17              0.051                                 ok            True                  False
  PYPL           90.00               40            0.17              0.07         56.12                61.92         0.632            pass              0.787             85.8                           0.808               17.64              1.305                                 ok           False                  False
  DRAM           77.78               27            2.44              0.91         52.81                97.77         0.614            pass              0.179              1.5                           0.041               -9.42             -0.541            downtrend_blocked_slope           False                  False
  KLAC           86.67               15            3.90              5.75        208.05                94.03         0.599            pass              0.291              6.6                           0.087               -8.98             -0.832 downtrend_blocked_slope_and_streak           False                  False
   CSX          100.00                5            1.79              0.67         52.94                24.65         0.585            pass              0.478              6.4                           0.127                5.31              0.570                                 ok           False                  False
  PANW           95.74               47            0.06              0.13        323.74                61.51         0.536            pass              0.915             87.1                           0.455               -2.03             -0.763 downtrend_blocked_slope_and_streak           False                  False
   TXN           89.47               38            0.37              0.73        279.27                50.69         0.534            pass              0.553             20.0                           0.217               -6.71             -0.706            downtrend_blocked_slope           False                  False
   STX           88.24               17            5.22             31.14        838.35               103.51         0.498 below_threshold              0.316              0.0                           0.150               -6.21              0.379                                 ok           False                  False
   ADI           82.14               28            1.35              3.51        370.36                41.03         0.492 below_threshold              0.237              3.7                           0.084               -4.96             -0.434 downtrend_blocked_slope_and_streak           False                  False
  AMAT           84.62               13            4.58             17.17        528.89                84.50         0.487 below_threshold              0.205              4.3                           0.056              -11.07             -0.937 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-27T10:25:04.556459-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:20:01.585305-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:15:03.558106-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:10:05.779963-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:05:02.641100-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:00:03.474876-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T09:35:01.555025-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:30:04.489033-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:25:02.551278-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:20:01.575598-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727102504)

</details>
