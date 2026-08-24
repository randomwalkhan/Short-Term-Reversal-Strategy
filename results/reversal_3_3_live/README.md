# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 15:40:01 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$57,635.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-67.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   0      9     27315.0                 27247.5        30.35          30.28      310.66         309.6          bid_ask_mid                      30.28                bid_ask_mid                    True           -67.5                  -0.25          87.5               32              1.06         63.04           64.38                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           87.50               32            1.40              3.08        312.68                88.60         0.647          pass              0.630             72.9                           0.629                1.04             -0.237                                 ok            True                  False
  GEHC           97.22               36            0.61              0.32         74.68                48.71         0.582          pass              0.767             45.2                           0.496                1.95              0.263                                 ok            True                  False
  DXCM           87.50               32            0.96              0.62         92.07                49.72         0.562          pass              0.445             14.1                           0.257                4.34              0.254                                 ok            True                  False
  ASML           87.88               33            0.83             10.22       1759.38                48.84         0.551          pass              0.603             61.3                           0.527                0.90             -0.241                                 ok            True                  False
  MRVL           80.00               30            3.12              5.18        234.82                96.35         0.521          pass              0.352             55.5                           0.481               10.11              1.329                                 ok            True                  False
  INSM           85.71               35            1.31              1.15        125.28               110.84         0.764          pass              0.525             43.1                           0.456               -7.89             -0.622 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.66               29            1.75              6.04        489.73                82.60         0.648          pass              0.610             53.8                           0.535               -7.26             -0.968            downtrend_blocked_slope           False                  False
  WDAY           82.93               41            0.08              0.12        199.96                82.42         0.639          pass              0.630             96.0                           0.627                8.50              0.942                                 ok           False                  False
   APP           66.67               36            1.99              4.26        303.94                90.15         0.608          pass              0.313             26.4                           0.272              -11.60             -0.701            downtrend_blocked_slope           False                  False
  KLAC           81.25               32            1.11              1.43        183.38                68.78         0.591          pass              0.458             72.9                           0.667               -5.49             -1.112 downtrend_blocked_slope_and_streak           False                  False
  MCHP           85.71               28            2.25              1.19         75.11                69.56         0.586          pass              0.452             40.4                           0.511               -9.18             -0.820            downtrend_blocked_slope           False                  False
  UPRO           76.67               30            0.77              0.81        149.53                39.04         0.559          pass              0.320             43.7                           0.367               -4.04             -0.481            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-24T15:10:01.417381-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:05:03.439109-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:00:02.474855-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:55:01.386568-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:50:01.463647-04:00       entry_1500              entry {"allocated_cash": 27315.0, "asset_type": "option", "contract_symbol": "LRCX261016C00310000", "contracts": 9, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 5.27, "option_volume": 30.0, "success_rate": 87.5, "ticker": "LRCX", "timing_score": 0.666}
2026-08-24T14:50:01.463647-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-24", "training_samples": 5698, "window": 5}
2026-08-24T12:00:04.404720-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:55:01.402592-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:50:02.380511-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:45:05.900318-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824154001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824154001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824154001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824154001)

</details>
