# Reversal 3.3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-08 15:55:02 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$32,833.50`
- Equity: `$32,833.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option  TXN260618C00290000     10          2026-05-07         2026-05-08        13.10       15.50 2400.0   18.320611 take_profit_day1_hit_at_scan
  TEAM     option         option TEAM260618C00090000     19          2026-05-08         2026-05-08         7.75        9.25 2850.0   19.354839 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           85.37               41            1.18              0.76         92.04               115.49         0.659          pass               27.58              3.586                                 ok            True
   XEL           90.91               11            1.29              0.73         80.12                27.43         0.559          pass                0.30              0.137                                 ok            True
   ADP           90.32               31            0.51              0.77        213.76                38.09         0.518          pass                8.38              0.731                                 ok            True
   HON           83.33               18            1.37              2.06        215.19                24.51         0.515          pass               -0.02              0.086                                 ok            True
   PEP           89.47               19            1.04              1.14        155.80                17.00         0.505          pass               -0.50             -0.003                                 ok            True
  ADSK           85.71               14            2.41              4.23        249.23                40.37         0.504          pass                3.18              0.617                                 ok            True
  CHTR           69.23               13            2.97              3.34        158.81               119.32         0.769          pass              -13.69             -1.260            downtrend_blocked_slope           False
 CMCSA           75.00                4            2.90              0.53         26.01                61.43         0.645          pass               -7.55             -0.669 downtrend_blocked_slope_and_streak           False
  SHOP           92.11               38            1.15              0.90        111.35                82.33         0.596          pass              -12.22             -1.547 downtrend_blocked_slope_and_streak           False
  FAST           96.43               28            0.43              0.13         44.30                33.68         0.568          pass               -0.64             -0.058                                 ok           False
   AEP           92.31               13            1.21              1.12        131.28                20.97         0.545          pass               -3.39             -0.290            downtrend_blocked_slope           False
  NFLX           89.19               37            0.75              0.46         88.06                43.15         0.529          pass               -5.24             -0.603            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-05-08T16:05:06.142170-04:00 manage_1600         exit {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00 manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00 manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:00:03.172365-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508155502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508155502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508155502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508155502)

</details>
