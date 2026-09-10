# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 09:35:02 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$36,540.10`
- Equity: `$73,532.10`
- Realized PnL: `$63,430.10`
- Unrealized PnL: `$102.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261009C00135000       2026-09-09                   1     34     36890.0                 36992.0        10.85          10.88      133.57        128.81     last_price_stale                        NaN                unavailable                   False           102.0                   0.28         80.65               31              2.16         74.55            3.13                 103.38                 254.0           23.0               0.03                      ok
```

## Today's Closed Trades (2026-09-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           87.50               40            0.90              1.32        207.24                89.81         0.623          pass              0.720             85.7                           0.810                8.85             -0.205                                 ok            True                  False
   STX           84.00               25            2.95             18.29        878.08                74.71         0.514          pass              0.316             19.3                           0.436                1.59              0.494                                 ok            True                  False
  WDAY           91.67               36            0.62              0.81        185.70                77.13         0.647          pass              0.731             60.5                           0.348               -3.07             -0.520 downtrend_blocked_slope_and_streak           False                  False
  MSTR           79.31               29            2.87              2.66        131.56               104.12         0.608          pass              0.290             34.3                           0.497                4.63              0.534                                 ok           False                  False
  TEAM           94.87               39            0.31              0.38        177.58                63.97         0.582          pass              0.899             83.5                           0.612                5.18             -0.144                                 ok           False                  False
  AMGN           96.97               33            0.16              0.43        391.09                44.45         0.582          pass              0.880             89.6                           0.638              -11.28             -1.162 downtrend_blocked_slope_and_streak           False                  False
  PANW           83.33               42            0.59              1.38        334.51                67.49         0.564          pass              0.562             72.2                           0.739               -1.82             -1.162            downtrend_blocked_slope           False                  False
   TRI           97.06               34            0.44              0.30         96.85                52.79         0.561          pass              0.616              0.0                           0.165               -5.76             -0.731 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.00               25            1.55              2.76        253.68                48.69         0.548          pass              0.634             26.4                           0.381               -8.25             -1.363 downtrend_blocked_slope_and_streak           False                  False
  INTU           96.77               31            0.91              2.00        313.08                48.73         0.545          pass              0.595              0.0                           0.276              -10.06             -1.314 downtrend_blocked_slope_and_streak           False                  False
    ZS           97.14               35            1.38              1.60        165.41                64.27         0.541          pass              0.744             41.1                           0.396               -3.82             -1.157            downtrend_blocked_slope           False                  False
  MRVL           76.47               34            2.01              3.30        233.59                80.25         0.538          pass              0.375             53.7                           0.622               -6.05             -0.181           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-10T00:00:06.085098-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-09T16:05:01.918481-04:00      manage_1600               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "CRWD261016C00210000", "fill_price": 12.87, "pnl": -3718.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CRWD"}
2026-09-09T15:10:06.054053-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T15:05:04.869479-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T15:00:02.977003-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:55:04.050096-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:50:05.027114-04:00       entry_1500              entry {"allocated_cash": 36890.0, "asset_type": "option", "contract_symbol": "MSTR261009C00135000", "contracts": 34, "early_entry_score": 0.281, "entry_mode": "regular", "entry_option_price": 10.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 254.0, "option_spread_pct": 2.76, "option_volume": 23.0, "success_rate": 80.65, "ticker": "MSTR", "timing_score": 0.638}
2026-09-09T14:50:05.027114-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-09", "training_samples": 5753, "window": 5}
2026-09-09T12:00:03.976220-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:55:03.977367-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910093502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910093502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910093502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910093502)

</details>
