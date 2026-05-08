# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 13:10:09 EDT`
Last processed slot: `manage_1300`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$29,983.50`
- Equity: `$29,983.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           83.33               18            4.45              2.88         91.14               115.49         0.601          pass               23.35              3.433                                 ok            True
  FAST           96.00               25            0.80              0.25         44.25                33.68         0.553          pass               -1.01             -0.075                                 ok            True
   XEL           95.24               21            0.85              0.48         80.23                27.43         0.536          pass                0.76              0.157                                 ok            True
  ORLY           88.00               25            1.16              0.77         94.25                34.97         0.516          pass                0.38              0.226                                 ok            True
   ADP           88.46               26            0.74              1.11        213.61                38.09         0.513          pass                8.13              0.720                                 ok            True
  ADSK           87.50               16            1.95              3.43        249.57                40.37         0.503          pass                3.66              0.638                                 ok            True
  CHTR           76.47               17            2.42              2.72        159.08               119.32         0.785          pass              -13.20             -1.234            downtrend_blocked_slope           False
 CMCSA           83.33                6            2.15              0.40         26.07                61.43         0.682          pass               -6.84             -0.634 downtrend_blocked_slope_and_streak           False
  SHOP           93.75               16            3.58              2.80        110.54                82.33         0.586          pass              -14.38             -1.660 downtrend_blocked_slope_and_streak           False
  PYPL           93.55               31            0.84              0.27         46.10                42.03         0.533          pass               -9.21             -1.062 downtrend_blocked_slope_and_streak           False
  MSFT           78.26               23            1.08              3.19        419.55                34.38         0.532          pass               -1.94             -0.267            downtrend_blocked_slope           False
  NFLX           89.19               37            0.76              0.47         88.06                43.15         0.529          pass               -5.24             -0.603            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T13:10:09.442593-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T13:05:05.272156-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T13:00:07.011484-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T12:55:09.634470-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T12:40:09.595901-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:35:05.338232-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:30:08.598241-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:25:05.406767-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:10:10.747163-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T12:05:08.430158-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508131009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508131009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508131009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508131009)

</details>
