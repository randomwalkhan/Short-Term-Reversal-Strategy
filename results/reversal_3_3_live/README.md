# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 09:45:01 EDT`
Last processed slot: `manual`

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
- Equity: `$65,695.10`
- Realized PnL: `$63,430.10`
- Unrealized PnL: `$-7,735.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261009C00135000       2026-09-09                   1     34     36890.0                 29155.0        10.85           8.57      133.57         129.4          bid_ask_mid                       8.57                bid_ask_mid                    True         -7735.0                 -20.97         80.65               31              2.16         74.55           73.62                 103.38                 254.0           23.0               0.03                      ok
```

## Today's Closed Trades (2026-09-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           85.71               28            2.08             12.93        880.38                74.71         0.549          pass              0.456             42.9                           0.662                2.49              0.534                                 ok            True                  False
  ALNY           84.21               19            2.04              3.69        256.42                46.38         0.503          pass              0.283             20.2                           0.168                5.74              1.070                                 ok            True                  False
   KDP           84.62               26            0.98              0.22         31.99                29.72         0.502          pass              0.374             31.5                           0.253               -1.38              0.060                                 ok            True                  False
  MSTR           79.31               29            2.73              2.53        131.61               104.12         0.616          pass              0.301             37.5                           0.579                4.78              0.541                                 ok           False                  False
   KHC          100.00                9            0.98              0.17         24.54                28.60         0.611          pass              0.499             12.7                           0.212               -0.12             -0.113                                 ok           False                  False
  AMGN           96.88               32            0.19              0.51        391.05                44.45         0.586          pass              0.868             87.5                           0.715              -11.31             -1.164 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.06               34            0.83              1.48        254.23                48.69         0.537          pass              0.796             60.6                           0.639               -7.58             -1.330 downtrend_blocked_slope_and_streak           False                  False
  MRVL           76.47               34            2.05              3.37        233.56                80.25         0.535          pass              0.372             52.7                           0.639               -6.09             -0.183           downtrend_blocked_streak           False                  False
  INTU           97.56               41            0.18              0.41        313.77                48.73         0.526          pass              0.911             86.0                           0.629               -9.40             -1.280 downtrend_blocked_slope_and_streak           False                  False
  PYPL           94.12               34            0.41              0.15         52.11                58.54         0.523          pass              0.879             96.7                           0.840              -15.73             -1.228 downtrend_blocked_slope_and_streak           False                  False
  NFLX           89.66               29            1.08              0.57         75.78                38.30         0.512          pass              0.489             18.0                           0.206               -7.67             -0.754 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00               24            1.46             19.19       1868.10                42.66         0.509          pass              0.618             24.5                           0.206               -5.21             -0.351 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910094501)

</details>
