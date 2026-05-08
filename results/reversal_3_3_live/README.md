# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 12:05:08 EDT`
Last processed slot: `manage_1200`

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
  FAST           96.15               26            0.69              0.21         44.27                33.68         0.548          pass               -0.90             -0.070                                 ok            True
    ZS           83.33               24            2.22              2.37        151.77                60.77         0.515          pass               10.26              1.137                                 ok            True
   ADP           88.00               25            0.97              1.46        213.47                38.09         0.505          pass                7.88              0.710                                 ok            True
  CHTR           76.47               17            2.47              2.77        159.05               119.32         0.780          pass              -13.23             -1.236            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.38              0.44         26.05                61.43         0.671          pass               -7.06             -0.645 downtrend_blocked_slope_and_streak           False
  SHOP           88.24               17            3.21              2.51        110.66                82.33         0.596          pass              -14.05             -1.642 downtrend_blocked_slope_and_streak           False
  TEAM           62.50                8            5.79              3.74         90.77               115.49         0.553          pass               21.63              3.369                                 ok           False
  PYPL           93.55               31            0.74              0.24         46.12                42.03         0.539          pass               -9.11             -1.057 downtrend_blocked_slope_and_streak           False
  NFLX           88.57               35            0.82              0.51         88.05                43.15         0.536          pass               -5.30             -0.606            downtrend_blocked_slope           False
  META           76.92               26            1.28              5.52        614.44                41.17         0.527          pass               -9.79             -1.250 downtrend_blocked_slope_and_streak           False
  MSFT           78.26               23            1.20              3.54        419.40                34.38         0.525          pass               -2.06             -0.272            downtrend_blocked_slope           False
  ADBE           73.33               15            2.43              4.37        254.64                45.47         0.507          pass                1.97              0.534                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T12:05:08.430158-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T12:00:07.637390-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T11:55:02.097202-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-08T11:40:01.103440-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-08T11:35:02.020696-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-08T11:30:01.135082-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-08T11:25:01.142010-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-08T11:10:05.551682-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-08T11:05:01.130220-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-08T11:00:02.141684-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508120508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508120508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508120508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508120508)

</details>
