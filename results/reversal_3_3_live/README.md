# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-07 15:50:04 EDT`
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

- Cash: `$14,483.50`
- Equity: `$27,308.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$-275.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00290000       2026-05-07                   0     10     13100.0                 12825.0         13.1          12.82      283.62        285.23          -275.0                   -2.1         91.67               12              2.01         41.87           38.86                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CRWD     option         option CRWD260618C00470000      3          2026-05-06         2026-05-07       33.025       51.55 5557.5   56.093868 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  INTC          100.00               26            2.00              1.59        112.33                95.68         0.680          pass               65.84              4.372                                 ok            True
   TXN           89.47               19            1.46              2.95        288.18                67.07         0.678          pass                1.57              0.520                                 ok            True
  FAST           96.00               25            0.84              0.26         44.60                34.69         0.553          pass               -1.93             -0.078                                 ok            True
  ASML           81.48               27            1.36             14.66       1538.46                46.11         0.527          pass                7.71              0.600                                 ok            True
  MDLZ           83.33               24            0.70              0.30         61.74                24.46         0.517          pass                6.45              0.816                                 ok            True
  SBUX           90.48               21            1.40              1.04        105.99                31.94         0.515          pass                5.43              0.848                                 ok            True
   ADI           80.00               25            1.30              3.79        414.03                34.89         0.504          pass                1.57              0.381                                 ok            True
 CMCSA           88.46               26            0.62              0.12         26.39                61.67         0.677          pass              -16.96             -1.125 downtrend_blocked_slope_and_streak           False
  NXPI           75.00                4            3.93              8.35        299.97                84.51         0.666          pass               20.92              2.673                                 ok           False
  GEHC           73.68               38            0.62              0.27         61.62                55.11         0.555          pass              -12.22             -1.568            downtrend_blocked_slope           False
   CSX           71.43                7            2.13              0.68         45.29                28.34         0.535          pass               -3.41             -0.181                                 ok           False
  ROST          100.00                6            2.05              3.29        227.50                15.20         0.515          pass               -1.19              0.020                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                         detail
2026-05-07T15:40:04.301487-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:35:09.139839-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:30:09.012076-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:25:04.977816-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:10:07.636776-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:05:07.086274-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T15:00:07.624219-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T14:55:04.902714-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-07T14:50:57.198065-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-07", "training_samples": 4977, "window": 5}
2026-05-07T14:50:57.198065-04:00  entry_1500          entry {"allocated_cash": 13100.0, "asset_type": "option", "contract_symbol": "TXN260618C00290000", "contracts": 10, "entry_option_price": 13.1, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 1293.0, "option_spread_pct": 4.58, "option_volume": 214.0, "success_rate": 91.67, "ticker": "TXN", "timing_score": 0.69}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507155004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507155004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507155004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507155004)

</details>
