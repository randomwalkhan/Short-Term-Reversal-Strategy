# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 10:40:03 EDT`
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

- Cash: `$30,388.00`
- Equity: `$57,298.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-405.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 26910.0        30.35           29.9      310.66        311.31          bid_ask_mid                       29.9                bid_ask_mid                    True          -405.0                  -1.48          87.5               32              1.06         63.04           62.24                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               33            1.62              1.95        170.50               115.46         0.758          pass              0.410             44.2                           0.339                9.39              1.085                      ok            True                  False
   TRI           90.91               11            2.80              2.13        107.71                67.11         0.603          pass              0.406             16.0                           0.190                1.36              0.406                      ok            True                  False
  GEHC           96.67               30            0.90              0.47         73.99                49.18         0.599          pass              0.698             35.0                           0.562                1.06              0.217                      ok            True                  False
  DXCM           88.57               35            0.64              0.41         90.89                50.36         0.578          pass              0.608             51.6                           0.425                1.06              0.105                      ok            True                  False
  WDAY           82.14               28            2.29              3.20        197.78                78.88         0.570          pass              0.311             25.8                           0.216                7.35              0.721                      ok            True                  False
   KHC           86.36               22            1.17              0.21         25.58                37.91         0.556          pass              0.401             31.8                           0.408                2.92              0.355                      ok            True                  False
  FAST          100.00               20            0.95              0.34         51.13                22.00         0.543          pass              0.616             31.7                           0.345               -3.03             -0.219                      ok            True                  False
  MDLZ           94.74               19            1.35              0.61         64.44                26.88         0.529          pass              0.587             27.1                           0.454                3.31              0.375                      ok            True                  False
  SBUX           87.50               16            0.89              0.67        107.20                20.57         0.524          pass              0.455             54.1                           0.571                0.45             -0.103                      ok            True                  False
   KDP           82.61               23            1.37              0.31         32.38                31.66         0.503          pass              0.234              9.2                           0.244                9.89              0.890                      ok            True                  False
  MCHP           87.88               33            0.70              0.36         74.05                69.73         0.640          pass              0.583             51.9                           0.390               -8.50             -0.802 downtrend_blocked_slope           False                  False
  ABNB           94.59               37            0.30              0.40        190.04                62.43         0.638          pass              0.756             41.0                           0.337                2.52              0.388                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-25T10:40:03.785417-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:35:02.544392-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:30:01.796364-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:25:02.779045-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:15:01.792883-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:10:01.860034-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:05:04.691112-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:00:02.656689-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T00:00:04.661538-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825104003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825104003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825104003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825104003)

</details>
