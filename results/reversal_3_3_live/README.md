# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 10:25:02 EDT`
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
- Equity: `$58,153.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$450.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 27765.0        30.35          30.85      310.66        310.28          bid_ask_mid                      30.85                bid_ask_mid                    True           450.0                   1.65          87.5               32              1.06         63.04           65.84                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               33            1.64              1.97        170.49               115.46         0.758          pass              0.408             43.6                           0.314                9.37              1.084                  ok            True                  False
  GEHC           96.77               31            0.78              0.40         74.02                49.18         0.600          pass              0.733             44.2                           0.656                1.19              0.223                  ok            True                  False
  DXCM           88.24               34            0.69              0.44         90.87                50.36         0.580          pass              0.580             47.4                           0.368                1.01              0.102                  ok            True                  False
   TRI           86.36               22            2.03              1.54        107.96                67.11         0.576          pass              0.425             39.2                           0.460                2.17              0.442                  ok            True                  False
  WDAY           80.00               30            2.07              2.89        197.91                78.88         0.567          pass              0.289             32.8                           0.272                7.59              0.731                  ok            True                  False
   KHC           86.36               22            1.09              0.20         25.59                37.91         0.560          pass              0.415             36.4                           0.583                3.00              0.359                  ok            True                  False
  FAST          100.00               20            0.99              0.36         51.13                22.00         0.542          pass              0.578             19.0                           0.319               -3.07             -0.221                  ok            True                  False
  PAYX          100.00               27            0.60              0.52        125.79                34.31         0.533          pass              0.752             61.9                           0.627                3.26              0.336                  ok            True                  False
  MDLZ           94.44               18            1.48              0.67         64.41                26.88         0.528          pass              0.553             20.4                           0.330                3.18              0.370                  ok            True                  False
  SBUX           89.47               19            0.69              0.52        107.27                20.57         0.520          pass              0.558             64.6                           0.646                0.66             -0.093                  ok            True                  False
   KDP           83.33               24            1.06              0.24         32.41                31.66         0.518          pass              0.293             19.8                           0.271               10.23              0.904                  ok            True                  False
   LIN           82.14               28            0.79              2.71        488.87                26.61         0.500          pass              0.338             36.9                           0.252               -0.89              0.099                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-25T10:25:02.779045-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:15:01.792883-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:10:01.860034-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:05:04.691112-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:00:02.656689-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T00:00:04.661538-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-24T15:10:01.417381-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-24T15:05:03.439109-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-24T15:00:02.474855-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825102502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825102502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825102502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825102502)

</details>
