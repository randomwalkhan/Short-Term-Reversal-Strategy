# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 12:45:05 EDT`
Last processed slot: `manual`

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
  FAST           96.30               27            0.54              0.17         44.29                33.68         0.551          pass               -0.75             -0.063                                 ok            True
    ZS           83.33               30            1.51              1.62        152.10                60.77         0.519          pass               11.06              1.170                                 ok            True
   ADP           88.46               26            0.86              1.28        213.54                38.09         0.507          pass                8.00              0.715                                 ok            True
  CHTR           76.47               17            2.49              2.80        159.04               119.32         0.782          pass              -13.26             -1.238            downtrend_blocked_slope           False
 CMCSA           83.33                6            2.15              0.40         26.07                61.43         0.682          pass               -6.84             -0.634 downtrend_blocked_slope_and_streak           False
  TEAM           76.92               13            5.02              3.25         90.98               115.49         0.588          pass               22.61              3.405                                 ok           False
  SHOP           93.75               16            3.64              2.85        110.52                82.33         0.583          pass              -14.43             -1.663 downtrend_blocked_slope_and_streak           False
  PYPL           92.59               27            1.03              0.33         46.08                42.03         0.545          pass               -9.38             -1.070 downtrend_blocked_slope_and_streak           False
  META           80.00               25            1.41              6.10        614.19                41.17         0.530          pass               -9.92             -1.256 downtrend_blocked_slope_and_streak           False
  MSFT           78.26               23            1.17              3.44        419.45                34.38         0.527          pass               -2.03             -0.271            downtrend_blocked_slope           False
 GOOGL           90.91               44            0.07              0.20        397.90                37.55         0.515          pass               15.48              1.656                                 ok           False
  NFLX           90.91               44            0.42              0.26         88.15                43.15         0.510          pass               -4.92             -0.587            downtrend_blocked_slope           False
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

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508124505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508124505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508124505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508124505)

</details>
