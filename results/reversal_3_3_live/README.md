# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 09:55:01 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,264.25`
- Equity: `$35,964.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$1,787.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 18700.0         3.08            3.4       55.67         55.84          bid_ask_mid                        3.4                bid_ask_mid                    True          1787.5                  10.57          80.0               10              2.03         42.85           47.73                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           80.77               26            1.50              0.62         58.59               115.77         0.699          pass              0.413             72.1                           0.916               -6.56             -1.398                                 ok            True                  False
  AAPL           96.77               31            0.52              1.19        327.23                37.60         0.580          pass              0.649             17.1                           0.168                4.04              0.549                                 ok            True                  False
   ADP           96.30               27            0.74              1.27        245.67                36.45         0.571          pass              0.570              0.0                           0.203                1.26              0.343                                 ok            True                  False
  ABNB           93.75               16            2.10              2.11        143.19                31.72         0.528          pass              0.493             11.2                           0.220               -1.31             -0.195                                 ok            True                  False
   TRI           86.11               36            0.69              0.44         90.51                49.06         0.514          pass              0.472             28.2                           0.293                1.33              0.411                                 ok            True                  False
  DXCM           84.21               19            1.98              1.04         74.31                40.17         0.509          pass              0.267             14.4                           0.210               -1.07              0.116                                 ok            True                  False
  PANW           87.50               16            2.93              7.02        339.14                60.47         0.504          pass              0.368             25.7                           0.207                3.59              0.538                                 ok            True                  False
  AMAT           90.91               33            0.49              1.94        563.72               100.84         0.724          pass              0.785             89.3                           0.955               -1.53             -0.799 downtrend_blocked_slope_and_streak           False                  False
  KLAC           88.89               36            0.63              0.95        217.15               102.77         0.712          pass              0.741             86.5                           0.926               -2.25             -0.719 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.91               33            0.61              1.37        321.41                94.63         0.676          pass              0.773             86.9                           0.947               -3.94             -1.043 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.12               34            0.30              3.84       1799.86                63.30         0.613          pass              0.863             88.4                           0.905                1.55              0.002                                 ok           False                  False
  PYPL           88.89               45            0.02              0.01         55.85                62.33         0.607          pass              0.789             97.1                           0.525               25.40              2.821                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-07-22T00:00:04.624946-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-07-21T15:10:09.418772-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T15:05:04.539660-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T15:00:02.487183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T14:55:03.644573-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-21T14:50:05.500810-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 16912.5, "asset_type": "option", "contract_symbol": "PYPL260821C00055000", "contracts": 55, "early_entry_score": 0.165, "entry_mode": "regular", "entry_option_price": 3.075, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 6395.0, "option_spread_pct": 4.88, "option_volume": 68.0, "success_rate": 80.0, "ticker": "PYPL", "timing_score": 0.663}
2026-07-21T14:50:05.500810-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-21", "training_samples": 5488, "window": 5}
2026-07-21T11:17:25.409204-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:59:34.342189-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:16:24.427902-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "CTAS260821C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "entry_ask": 8.0, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 17088.38, "hypothetical_contracts": 22, "matched_signals": 34, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 548.0, "option_spread_pct": 14.77, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "matched_signals": 34, "recovery_stability_score": 0.727, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722095501)

</details>
