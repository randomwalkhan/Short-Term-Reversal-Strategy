# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 09:30:05 EDT`
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
  MSTR     option         option MSTR261009C00135000       2026-09-09                   1     34     36890.0                 36992.0        10.85          10.88      133.57        128.04     last_price_stale                        NaN                unavailable                   False           102.0                   0.28         80.65               31              2.16         74.55            3.13                 103.38                 254.0           23.0               0.03                      ok
```

## Today's Closed Trades (2026-09-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           87.80               41            0.87              1.26        207.26                89.81         0.620          pass              0.729             86.3                           0.677                8.89             -0.203                                 ok            True                  False
  CPRT           86.36               22            1.75              0.40         32.43                45.10         0.522          pass              0.403             33.7                           0.317               -1.96             -0.134                                 ok            True                  False
   CEG           88.89               18            1.27              2.61        292.79                32.56         0.519          pass              0.510             55.8                           0.408                3.81              0.695                                 ok            True                  False
   STX           85.71               21            3.32             20.60        877.09                74.71         0.518          pass              0.301              7.8                           0.184                1.20              0.476                                 ok            True                  False
  FTNT           90.00               40            0.81              0.89        156.84                53.44         0.504          pass              0.683             55.2                           0.374               -1.01             -0.727                                 ok            True                  False
  AMGN          100.00               19            0.91              2.49        390.20                44.45         0.626          pass              0.573             16.6                           0.223              -11.95             -1.197 downtrend_blocked_slope_and_streak           False                  False
  MSTR           77.78               27            3.32              3.08        131.38               104.12         0.595          pass              0.219             15.2                           0.341                4.15              0.513                                 ok           False                  False
  MRVL           75.00               36            1.26              2.07        234.12                80.25         0.570          pass              0.444             71.1                           0.597               -5.32             -0.146           downtrend_blocked_streak           False                  False
  PYPL           95.45               22            0.99              0.36         52.02                58.54         0.562          pass              0.812             92.1                           0.535              -16.22             -1.254 downtrend_blocked_slope_and_streak           False                  False
    ZS           97.50               40            0.64              0.74        165.78                64.27         0.561          pass              0.853             65.8                           0.632               -3.09             -1.123            downtrend_blocked_slope           False                  False
  PANW           82.50               40            1.11              2.61        333.98                67.49         0.543          pass              0.463             47.5                           0.474               -2.34             -1.186            downtrend_blocked_slope           False                  False
  MELI          100.00               29            1.03             13.49       1870.55                42.66         0.511          pass              0.607              9.7                           0.135               -4.79             -0.331 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910093005)

</details>
