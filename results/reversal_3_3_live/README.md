# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 10:20:01 EDT`
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
- Equity: `$58,198.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$495.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 27810.0        30.35           30.9      310.66        311.26          bid_ask_mid                       30.9                bid_ask_mid                    True           495.0                   1.81          87.5               32              1.06         63.04           64.48                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               33            1.69              2.03        170.46               115.46         0.756          pass              0.403             41.9                           0.340                9.32              1.082                  ok            True                  False
  GEHC           96.77               31            0.80              0.41         74.01                49.18         0.599          pass              0.728             42.7                           0.625                1.17              0.222                  ok            True                  False
  DXCM           88.24               34            0.68              0.43         90.88                50.36         0.581          pass              0.584             48.7                           0.369                1.02              0.103                  ok            True                  False
  WDAY           80.00               30            2.07              2.89        197.91                78.88         0.567          pass              0.289             32.9                           0.258                7.59              0.731                  ok            True                  False
   TRI           88.46               26            1.90              1.44        108.00                67.11         0.562          pass              0.518             43.1                           0.477                2.30              0.448                  ok            True                  False
   KHC           86.96               23            0.97              0.17         25.60                37.91         0.562          pass              0.458             43.2                           0.602                3.12              0.364                  ok            True                  False
  FAST          100.00               22            0.72              0.26         51.17                22.00         0.545          pass              0.658             41.3                           0.458               -2.81             -0.209                  ok            True                  False
  MDLZ           94.74               19            1.31              0.60         64.44                26.88         0.532          pass              0.594             29.2                           0.458                3.35              0.377                  ok            True                  False
  PAYX          100.00               29            0.51              0.45        125.82                34.31         0.526          pass              0.782             67.5                           0.631                3.36              0.340                  ok            True                  False
  SBUX           88.89               18            0.79              0.60        107.23                20.57         0.519          pass              0.520             59.3                           0.606                0.56             -0.098                  ok            True                  False
   KDP           83.33               24            1.08              0.25         32.40                31.66         0.517          pass              0.290             18.6                           0.261               10.21              0.903                  ok            True                  False
   LIN           81.48               27            0.81              2.77        488.84                26.61         0.504          pass              0.309             35.4                           0.229               -0.91              0.098                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:15:01.792883-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:10:01.860034-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:05:04.691112-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:00:02.656689-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T00:00:04.661538-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-24T15:10:01.417381-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-24T15:05:03.439109-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-24T15:00:02.474855-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-24T14:55:01.386568-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825102001)

</details>
