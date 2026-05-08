# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 12:50:04 EDT`
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
  FAST           96.30               27            0.59              0.18         44.28                33.68         0.549          pass               -0.79             -0.065                                 ok            True
   ADP           88.89               27            0.74              1.11        213.62                38.09         0.508          pass                8.13              0.721                                 ok            True
  ADSK           87.50               16            1.98              3.49        249.55                40.37         0.501          pass                3.63              0.637                                 ok            True
  CHTR           80.00               20            2.17              2.44        159.20               119.32         0.786          pass              -12.97             -1.223            downtrend_blocked_slope           False
 CMCSA           83.33                6            2.12              0.39         26.07                61.43         0.684          pass               -6.80             -0.633 downtrend_blocked_slope_and_streak           False
  TEAM           75.00               12            5.14              3.32         90.95               115.49         0.585          pass               22.46              3.400                                 ok           False
  SHOP           93.75               16            3.78              2.95        110.47                82.33         0.575          pass              -14.55             -1.669 downtrend_blocked_slope_and_streak           False
  PYPL           92.59               27            0.96              0.31         46.09                42.03         0.548          pass               -9.32             -1.067 downtrend_blocked_slope_and_streak           False
  MSFT           79.17               24            1.03              3.04        419.62                34.38         0.530          pass               -1.90             -0.265                                 ok           False
  META           76.92               26            1.29              5.55        614.43                41.17         0.527          pass               -9.80             -1.250 downtrend_blocked_slope_and_streak           False
 GOOGL           90.91               44            0.03              0.07        397.96                37.55         0.518          pass               15.53              1.659                                 ok           False
  NFLX           90.70               43            0.49              0.30         88.13                43.15         0.511          pass               -4.99             -0.591            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T12:40:09.595901-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:35:05.338232-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:30:08.598241-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:25:05.406767-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:10:10.747163-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T12:05:08.430158-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T12:00:07.637390-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T11:55:02.097202-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T11:40:01.103440-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-08T11:35:02.020696-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508125004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508125004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508125004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508125004)

</details>
