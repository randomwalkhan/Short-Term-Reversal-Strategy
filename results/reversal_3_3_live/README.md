# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 14:40:05 EDT`
Last processed slot: `manage_1430`

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
  TEAM           82.76               29            3.11              2.01         91.51               115.49         0.618          pass               25.08              3.496                                 ok            True
  FAST           96.00               25            0.76              0.23         44.26                33.68         0.556          pass               -0.96             -0.073                                 ok            True
  ORLY           81.25               16            1.40              0.92         94.18                34.97         0.543          pass                0.14              0.216                                 ok            True
   XEL           92.00               25            0.65              0.37         80.27                27.43         0.518          pass                0.95              0.166                                 ok            True
    ZS           82.50               40            0.76              0.81        152.44                60.77         0.510          pass               11.91              1.204                                 ok            True
  ADSK           85.71               14            2.26              3.97        249.34                40.37         0.500          pass                3.34              0.624                                 ok            True
  CHTR           78.95               19            2.29              2.57        159.14               119.32         0.785          pass              -13.08             -1.228            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.44              0.45         26.05                61.43         0.668          pass               -7.11             -0.648 downtrend_blocked_slope_and_streak           False
  SHOP           86.36               22            2.84              2.22        110.79                82.33         0.582          pass              -13.72             -1.625 downtrend_blocked_slope_and_streak           False
  PYPL           92.59               27            0.96              0.31         46.09                42.03         0.550          pass               -9.32             -1.067 downtrend_blocked_slope_and_streak           False
  NFLX           88.57               35            0.89              0.55         88.03                43.15         0.532          pass               -5.37             -0.609            downtrend_blocked_slope           False
  META           77.78               27            1.13              4.89        614.72                41.17         0.532          pass               -9.66             -1.243 downtrend_blocked_slope_and_streak           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T14:40:05.233807-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-08T14:35:05.426480-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-08T14:30:08.223932-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-08T14:25:10.631446-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-08T14:10:04.922004-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T14:05:07.903857-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T14:00:06.476462-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T13:55:05.067818-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T13:40:04.672860-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:35:10.686912-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508144005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508144005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508144005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508144005)

</details>
