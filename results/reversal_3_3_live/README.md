# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-14 15:30:58 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$41,318.00`
- Realized PnL: `$31,228.00`
- Unrealized PnL: `$90.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260918C00140000       2026-08-14                   0      9     19620.0                 19710.0         21.8           21.9      141.95        143.34          bid_ask_mid                       21.9                bid_ask_mid                    True            90.0                   0.46         82.86               35              2.35        114.04          115.37                 164.53                 831.0          148.0               0.04                      ok
```

## Today's Closed Trades (2026-08-14)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   BKR     option         option BKR260918C00065000     98          2026-08-13         2026-08-14        1.925        2.25 3185.0   16.883117 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.78               37            1.39              1.42        144.75               164.53         0.842          pass              0.571             68.7                           0.834               24.94              1.851                  ok            True                  False
  TEAM           81.25               32            2.20              2.55        164.89               127.34         0.762          pass              0.292             11.8                           0.278               60.70              5.649                  ok            True                  False
  SHOP           95.65               23            2.24              2.48        157.47                83.25         0.669          pass              0.661             35.8                           0.366               32.29              3.068                  ok            True                  False
  LRCX           86.67               30            1.61              3.81        335.38                86.66         0.649          pass              0.519             47.7                           0.626               13.16              1.147                  ok            True                  False
  MRVL           80.00               35            0.95              1.47        221.55                86.88         0.622          pass              0.405             58.6                           0.591               17.34              1.208                  ok            True                  False
  TMUS           88.24               34            0.60              0.77        183.05                56.42         0.602          pass              0.635             65.1                           0.509                5.54              0.415                  ok            True                  False
  DXCM           81.82               22            1.70              1.09         91.01                54.70         0.591          pass              0.243             18.4                           0.377                7.76              0.822                  ok            True                  False
   TRI           84.21               19            2.84              2.11        105.17                75.25         0.583          pass              0.295             21.5                           0.212                5.02              0.359                  ok            True                  False
  INTC           86.11               36            1.54              1.13        104.08                80.36         0.576          pass              0.473             26.5                           0.490               14.14              1.026                  ok            True                  False
  UPRO           80.65               31            0.71              0.78        157.34                41.59         0.551          pass              0.296             27.8                           0.341               11.61              0.795                  ok            True                  False
  ASML           87.10               31            1.09             14.08       1841.87                47.59         0.544          pass              0.464             26.8                           0.497               12.20              1.246                  ok            True                  False
  FAST          100.00               19            0.84              0.30         51.21                25.38         0.542          pass              0.613             32.8                           0.241                6.71              0.774                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260814153058)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260814153058)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260814153058)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260814153058)

</details>
