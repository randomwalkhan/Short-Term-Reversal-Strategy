# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 14:55:02 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$15,258.50`
- Equity: `$30,553.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$570.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260618C00090000       2026-05-08                   0     19     14725.0                 15295.0         7.75           8.05       89.62         89.43           570.0                   3.87         83.33               30              2.98         65.54           68.69                 115.49                2469.0          138.0               0.04                      ok
```

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           82.14               28            3.19              2.06         91.49               115.49         0.619          pass               24.98              3.492                                 ok            True
  FAST           96.00               25            0.87              0.27         44.24                33.68         0.549          pass               -1.08             -0.078                                 ok            True
  ORLY           81.25               16            1.36              0.90         94.19                34.97         0.545          pass                0.18              0.217                                 ok            True
   XEL           95.24               21            0.83              0.47         80.23                27.43         0.536          pass                0.77              0.158                                 ok            True
   HON           83.33               18            1.38              2.09        215.18                24.51         0.505          pass               -0.04              0.085                                 ok            True
   ADP           89.29               28            0.71              1.07        213.63                38.09         0.504          pass                8.16              0.722                                 ok            True
    ZS           83.33               36            1.31              1.40        152.19                60.77         0.504          pass               11.29              1.179                                 ok            True
  TMUS           86.84               38            0.51              0.69        193.90                36.72         0.502          pass                1.80              0.354                                 ok            True
  CHTR           69.23               13            3.03              3.40        158.78               119.32         0.766          pass              -13.74             -1.263            downtrend_blocked_slope           False
 CMCSA           75.00                4            2.88              0.53         26.01                61.43         0.641          pass               -7.53             -0.668 downtrend_blocked_slope_and_streak           False
  SHOP           93.75               16            3.37              2.64        110.61                82.33         0.600          pass              -14.19             -1.650 downtrend_blocked_slope_and_streak           False
  NFLX           87.88               33            0.96              0.59         88.01                43.15         0.539          pass               -5.43             -0.612            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-08T14:55:02.174561-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:50:08.791874-04:00  entry_1500          entry {"allocated_cash": 14725.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 19, "entry_option_price": 7.75, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 2469.0, "option_spread_pct": 3.87, "option_volume": 138.0, "success_rate": 83.33, "ticker": "TEAM", "timing_score": 0.621}
2026-05-08T14:50:08.791874-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-08", "training_samples": 5000, "window": 5}
2026-05-08T14:40:05.233807-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:35:05.426480-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:30:08.223932-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:25:10.631446-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:10:04.922004-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:05:07.903857-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:00:06.476462-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508145502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508145502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508145502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508145502)

</details>
