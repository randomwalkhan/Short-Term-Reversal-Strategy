# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 11:24:55 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$16,667.25`
- Equity: `$34,082.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$860.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   1     86     16555.0                 17415.0         1.92           2.02       50.11         50.18          bid_ask_mid                       2.02                bid_ask_mid                    True           860.0                   5.19         92.31               13              1.24         25.34           26.32                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           84.62               13            1.64              0.66         57.37                60.55         0.697          pass              0.250             12.5                           0.198                0.26              0.275                      ok            True                  False
  ISRG           83.33               36            0.86              2.13        352.06                72.78         0.635          pass              0.403             25.7                           0.419                1.31              0.255                      ok            True                  False
   KHC           93.33               15            1.23              0.23         26.28                32.41         0.582          pass              0.570             40.9                           0.426                0.68              0.412                      ok            True                  False
  MDLZ           93.33               15            1.11              0.49         62.87                34.51         0.582          pass              0.566             39.7                           0.277                2.26              0.549                      ok            True                  False
  CTAS           90.91               22            1.14              1.64        206.09                40.09         0.580          pass              0.565             45.5                           0.564               -0.00              0.452                      ok            True                  False
  AMGN          100.00               17            1.22              3.30        386.22                28.18         0.550          pass              0.631             43.1                           0.610                4.54              0.725                      ok            True                  False
  MNST           88.89               18            1.07              0.73         97.34                23.72         0.537          pass              0.416             24.1                           0.415               -0.91              0.176                      ok            True                  False
  GILD           85.19               27            0.86              0.79        130.94                35.61         0.528          pass              0.500             65.2                           0.695               -3.08             -0.092                      ok            True                  False
  VRTX           85.71               14            1.82              6.14        479.07                32.97         0.514          pass              0.308             25.9                           0.495               -2.62             -0.025                      ok            True                  False
   TRI           86.11               36            1.20              0.83         98.47                65.88         0.510          pass              0.571             61.1                           0.597                1.50              1.054                      ok            True                  False
  DASH           96.43               28            1.74              2.41        196.50                49.74         0.505          pass              0.594              7.8                           0.167                5.40              0.726                      ok            True                  False
  ALNY           90.24               41            0.64              0.93        205.08               124.46         0.746          pass              0.751             67.8                           0.454              -23.67             -1.935 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731112455)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731112455)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731112455)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731112455)

</details>
