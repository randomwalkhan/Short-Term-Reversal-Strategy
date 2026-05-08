# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 11:25:01 EDT`
Last processed slot: `manage_1130`

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
  FAST           96.00               25            0.79              0.25         44.25                33.68         0.548          pass               -1.00             -0.074                                 ok            True
   ADP           84.21               19            1.27              1.90        213.27                38.09         0.518          pass                7.55              0.696                                 ok            True
   XEL           92.31               26            0.60              0.34         80.29                27.43         0.516          pass                1.01              0.169                                 ok            True
    ZS           80.00               25            2.05              2.19        151.85                60.77         0.513          pass               10.45              1.145                                 ok            True
  ORLY           89.29               28            0.99              0.65         94.30                34.97         0.510          pass                0.55              0.234                                 ok            True
  CHTR           84.00               25            1.78              2.00        159.38               119.32         0.785          pass              -12.62             -1.204            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.44              0.45         26.05                61.43         0.670          pass               -7.11             -0.648 downtrend_blocked_slope_and_streak           False
  SHOP           90.62               32            1.77              1.39        111.15                82.33         0.593          pass              -12.77             -1.575 downtrend_blocked_slope_and_streak           False
  TEAM           62.50                8            5.88              3.80         90.74               115.49         0.547          pass               21.51              3.364                                 ok           False
  META           76.92               26            1.26              5.45        614.47                41.17         0.534          pass               -9.78             -1.249 downtrend_blocked_slope_and_streak           False
  PYPL           93.55               31            0.83              0.27         46.10                42.03         0.533          pass               -9.20             -1.061 downtrend_blocked_slope_and_streak           False
  MSFT           78.26               23            1.16              3.42        419.45                34.38         0.526          pass               -2.02             -0.271            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                               detail
2026-05-08T11:25:01.142010-04:00 manage_1130 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T11:10:05.551682-04:00 manage_1100 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T11:05:01.130220-04:00 manage_1100 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T11:00:02.141684-04:00 manage_1100 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:55:06.709413-04:00 manage_1100 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:40:01.112958-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:35:06.124944-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:30:05.923430-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:25:01.121300-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:20:05.936337-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00290000", "fill_price": 15.5, "pnl": 2400.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.32, "ticker": "TXN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508112501)

</details>
