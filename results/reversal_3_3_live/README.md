# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:40:06 EDT`
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

- Cash: `$73,431.80`
- Equity: `$139,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-5,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 66400.0        17.85           16.6      223.97        222.68          bid_ask_mid                       16.6                bid_ask_mid                    True         -5000.0                   -7.0         100.0               38              0.68         80.16           78.44                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.22              0.30         35.06                27.06         0.552          pass              0.562             39.4                           0.353                9.45              0.907                                 ok            True                  False
   KHC           83.33               12            1.93              0.34         24.94                34.71         0.536          pass              0.168              4.0                           0.135               10.48              1.069                                 ok            True                  False
 CMCSA           92.31               13            0.85              0.14         22.78                23.88         0.533          pass              0.569             55.7                           0.307                9.61              1.046                                 ok            True                  False
   MAR           87.50               16            1.24              3.44        395.32                21.06         0.524          pass              0.345             17.6                           0.189                7.11              0.934                                 ok            True                  False
   AEP           82.35               17            0.91              0.83        130.28                17.81         0.522          pass              0.178              5.6                           0.234                5.41              0.479                                 ok            True                  False
  COST           86.67               15            1.19              8.51       1014.56                17.03         0.513          pass              0.282              6.6                           0.170                6.24              0.653                                 ok            True                  False
  ORLY          100.00               13            1.66              1.07         91.54                17.78         0.512          pass              0.475              1.3                           0.086                4.65              0.598                                 ok            True                  False
   ADP           90.00               20            1.04              2.25        306.98                23.94         0.510          pass              0.548             54.5                           0.281               12.49              1.224                                 ok            True                  False
  GILD           90.00               30            0.71              0.78        156.85                28.18         0.502          pass              0.515             21.7                           0.232                3.24              0.417                                 ok            True                  False
   CEG           85.29               34            0.71              1.26        254.67                65.49         0.593          pass              0.593             77.4                           0.759              -14.98             -1.672 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.24              1.02         64.75                24.03         0.574          pass              0.488             10.4                           0.231                5.49              0.538                                 ok           False                  False
  REGN           87.50                8            2.18             12.48        813.74                31.70         0.554          pass              0.256              0.3                           0.020                7.33              0.815                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-23T10:40:06.544410-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:35:06.665286-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:00:04.565947-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T00:00:06.660227-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023104006)

</details>
