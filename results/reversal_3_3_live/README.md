# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 10:30:05 EDT`
Last processed slot: `manage_1030`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  FAST           96.30               27            0.55              0.17         44.29                33.68         0.553            pass               -0.76             -0.064                                 ok            True
    ZS           83.33               24            2.12              2.27        151.82                60.77         0.521            pass               10.37              1.142                                 ok            True
   ADP           84.21               19            1.28              1.92        213.27                38.09         0.518            pass                7.54              0.696                                 ok            True
  CHTR           85.71               28            1.48              1.66        159.53               119.32         0.783            pass              -12.36             -1.191            downtrend_blocked_slope           False
 CMCSA           85.71                7            1.70              0.31         26.11                61.43         0.709            pass               -6.40             -0.613 downtrend_blocked_slope_and_streak           False
  SHOP           88.24               17            3.26              2.55        110.65                82.33         0.594            pass              -14.09             -1.644 downtrend_blocked_slope_and_streak           False
  MSFT           80.00               20            1.37              4.03        419.19                34.38         0.534            pass               -2.23             -0.280            downtrend_blocked_slope           False
  NFLX           88.57               35            0.82              0.51         88.04                43.15         0.530            pass               -5.31             -0.606            downtrend_blocked_slope           False
  META           77.14               35            0.71              3.07        615.49                41.17         0.519            pass               -9.28             -1.224 downtrend_blocked_slope_and_streak           False
  PYPL           95.12               41            0.22              0.07         46.19                42.03         0.511            pass               -8.64             -1.033 downtrend_blocked_slope_and_streak           False
  ADBE           69.23               13            2.66              4.77        254.46                45.47         0.485 below_threshold                1.73              0.524                                 ok           False
   ROP           87.50                8            2.22              5.49        350.09                22.08         0.482 below_threshold               -2.49             -0.141                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                               detail
2026-05-08T10:30:05.923430-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:25:01.121300-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:20:05.936337-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00290000", "fill_price": 15.5, "pnl": 2400.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.32, "ticker": "TXN"}
2026-05-08T10:10:01.121937-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:05:06.101764-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:00:06.094621-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:55:06.107419-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:40:05.918205-04:00 manage_0930 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:35:06.024595-04:00 manage_0930 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:30:04.090136-04:00 manage_0930 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508103005)

</details>
