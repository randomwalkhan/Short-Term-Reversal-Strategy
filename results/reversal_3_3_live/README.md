# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 14:50:08 EDT`
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
- Equity: `$29,983.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260618C00090000       2026-05-08                   0     19     14725.0                 14725.0         7.75           7.75       89.62         89.62             0.0                    0.0         83.33               30              2.98         65.54           65.54                 115.49                2469.0          138.0               0.04                      ok
```

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           83.33               30            2.98              1.92         91.55               115.49         0.621          pass               25.26              3.502                                 ok            True
  FAST           96.00               25            0.86              0.27         44.25                33.68         0.550          pass               -1.06             -0.078                                 ok            True
   XEL           94.74               19            0.92              0.52         80.21                27.43         0.542          pass                0.68              0.154                                 ok            True
  ORLY           81.25               16            1.43              0.94         94.18                34.97         0.541          pass                0.11              0.214                                 ok            True
    ZS           83.78               37            1.18              1.26        152.25                60.77         0.506          pass               11.43              1.185                                 ok            True
  CHTR           75.00               16            2.57              2.89        159.00               119.32         0.781          pass              -13.33             -1.241            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.71              0.50         26.03                61.43         0.654          pass               -7.37             -0.660 downtrend_blocked_slope_and_streak           False
  SHOP           85.00               20            2.95              2.31        110.75                82.33         0.586          pass              -13.82             -1.630 downtrend_blocked_slope_and_streak           False
  NFLX           87.88               33            0.94              0.58         88.01                43.15         0.540          pass               -5.42             -0.611            downtrend_blocked_slope           False
  PYPL           92.00               25            1.41              0.46         46.02                42.03         0.535          pass               -9.73             -1.088 downtrend_blocked_slope_and_streak           False
  MSFT           81.82               22            1.30              3.84        419.28                34.38         0.531          pass               -2.16             -0.277            downtrend_blocked_slope           False
  META           75.00               28            1.12              4.83        614.74                41.17         0.522          pass               -9.65             -1.242 downtrend_blocked_slope_and_streak           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-08T14:50:08.791874-04:00  entry_1500          entry {"allocated_cash": 14725.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 19, "entry_option_price": 7.75, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 2469.0, "option_spread_pct": 3.87, "option_volume": 138.0, "success_rate": 83.33, "ticker": "TEAM", "timing_score": 0.621}
2026-05-08T14:50:08.791874-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-08", "training_samples": 5000, "window": 5}
2026-05-08T14:40:05.233807-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:35:05.426480-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:30:08.223932-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:25:10.631446-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:10:04.922004-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:05:07.903857-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:00:06.476462-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T13:55:05.067818-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508145008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508145008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508145008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508145008)

</details>
