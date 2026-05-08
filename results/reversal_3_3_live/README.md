# Reversal 3.3.2 Live Paper Test

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

- Cash: `$15,258.50`
- Equity: `$32,263.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$2,280.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260618C00090000       2026-05-08                   0     19     14725.0                 17005.0         7.75           8.95       89.62         91.18          2280.0                  15.48         83.33               30              2.98         65.54           67.58                 115.49                2469.0          138.0               0.04                      ok
```

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           84.62               39            1.29              0.84         92.01               115.49         0.663          pass               27.43              3.580                                 ok            True
   XEL           90.91               11            1.32              0.74         80.11                27.43         0.557          pass                0.28              0.135                                 ok            True
  ORLY           81.82               11            1.72              1.14         94.09                34.97         0.554          pass               -0.19              0.200                                 ok            True
   ADP           88.46               26            0.76              1.13        213.60                38.09         0.513          pass                8.11              0.720                                 ok            True
   HON           81.25               16            1.50              2.27        215.10                24.51         0.505          pass               -0.16              0.080                                 ok            True
    ZS           84.09               44            0.52              0.55        152.55                60.77         0.503          pass               12.18              1.215                                 ok            True
  CHTR           63.64               11            3.20              3.58        158.70               119.32         0.759          pass              -13.88             -1.270            downtrend_blocked_slope           False
 CMCSA           75.00                4            3.22              0.59         25.99                61.43         0.626          pass               -7.86             -0.684 downtrend_blocked_slope_and_streak           False
  SHOP           90.62               32            1.66              1.30        111.18                82.33         0.600          pass              -12.68             -1.570 downtrend_blocked_slope_and_streak           False
  FAST           96.67               30            0.38              0.12         44.31                33.68         0.550          pass               -0.59             -0.056                                 ok           False
   AEP           93.33               15            1.06              0.98        131.34                20.97         0.536          pass               -3.24             -0.283            downtrend_blocked_slope           False
  NFLX           88.57               35            0.87              0.54         88.03                43.15         0.533          pass               -5.35             -0.608            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                       detail
2026-05-08T15:55:02.084715-04:00 manage_1600   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00 manage_1530   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00 manage_1530   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00 manage_1530   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00 manage_1530   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00  entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00  entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T15:00:03.172365-04:00  entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T14:55:02.174561-04:00  entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-08T14:50:08.791874-04:00  entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-08", "training_samples": 5000, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508155502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508155502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508155502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508155502)

</details>
