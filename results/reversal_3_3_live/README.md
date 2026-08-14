# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-14 15:08:52 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$21,608.00`
- Equity: `$41,228.00`
- Realized PnL: `$31,228.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260918C00140000       2026-08-14                   0      9     19620.0                 19620.0         21.8           21.8      141.95        141.95          bid_ask_mid                       21.8                bid_ask_mid                    True             0.0                    0.0         82.86               35              2.35        114.04          114.04                 164.53                 831.0          148.0               0.04                      ok
```

## Today's Closed Trades (2026-08-14)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   BKR     option         option BKR260918C00065000     98          2026-08-13         2026-08-14        1.925        2.25 3185.0   16.883117 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.86               35            2.35              2.39        144.34               164.53         0.813          pass              0.466             47.2                           0.529               23.74              1.807                  ok            True                  False
  TEAM           81.25               32            2.14              2.49        164.91               127.34         0.765          pass              0.288             10.6                           0.369               60.79              5.651                  ok            True                  False
  SHOP           95.65               23            2.42              2.68        157.38                83.25         0.659          pass              0.645             30.7                           0.319               32.05              3.059                  ok            True                  False
  LRCX           86.67               30            2.02              4.77        334.96                86.66         0.625          pass              0.477             34.4                           0.573               12.69              1.128                  ok            True                  False
  MRVL           80.00               35            1.26              1.95        221.34                86.88         0.603          pass              0.362             45.1                           0.393               16.97              1.193                  ok            True                  False
  TMUS           88.57               35            0.58              0.75        183.06                56.42         0.598          pass              0.654             66.2                           0.541                5.56              0.415                  ok            True                  False
  DXCM           80.00               20            1.77              1.13         90.99                54.70         0.596          pass              0.171             15.0                           0.421                7.68              0.819                  ok            True                  False
   TRI           82.61               23            2.62              1.95        105.24                75.25         0.569          pass              0.296             27.6                           0.340                5.26              0.369                  ok            True                  False
  INTC           86.11               36            1.83              1.34        103.99                80.36         0.558          pass              0.430             12.6                           0.301               13.80              1.013                  ok            True                  False
  UPRO           80.00               30            0.73              0.81        157.33                41.59         0.555          pass              0.266             25.8                           0.382               11.58              0.794                  ok            True                  False
  ISRG           82.76               29            0.92              2.59        400.16                68.90         0.546          pass              0.286             10.4                           0.250               12.52              1.181                  ok            True                  False
  FAST          100.00               20            0.71              0.26         51.23                25.38         0.543          pass              0.650             43.0                           0.506                6.84              0.780                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-14T15:08:52.029676-04:00       entry_1500              entry {"allocated_cash": 19620.0, "asset_type": "option", "contract_symbol": "SOXL260918C00140000", "contracts": 9, "early_entry_score": 0.466, "entry_mode": "regular", "entry_option_price": 21.8, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 831.0, "option_spread_pct": 4.13, "option_volume": 148.0, "success_rate": 82.86, "ticker": "SOXL", "timing_score": 0.813}
2026-08-14T15:08:52.029676-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-14", "training_samples": 5684, "window": 5}
2026-08-14T11:37:55.972745-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-14T10:55:04.531949-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-14T10:55:04.531949-04:00      manage_1100               exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "BKR260918C00065000", "fill_price": 2.25, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.88, "ticker": "BKR"}
2026-08-14T00:00:04.633795-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-13T15:10:04.909039-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:05:06.030850-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:00:02.921317-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T14:55:04.897309-04:00       entry_1500              entry {"allocated_cash": 18865.0, "asset_type": "option", "contract_symbol": "BKR260918C00065000", "contracts": 98, "early_entry_score": 0.39, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2279.0, "option_spread_pct": 12.99, "option_volume": 49.0, "success_rate": 84.21, "ticker": "BKR", "timing_score": 0.546}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260814150852)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260814150852)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260814150852)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260814150852)

</details>
