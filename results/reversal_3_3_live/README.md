# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 15:35:05 EDT`
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

- Cash: `$38,003.30`
- Equity: `$73,803.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00160000       2026-09-25                   0     20     35550.0                 35800.0        17.77           17.9      158.68        159.51          bid_ask_mid                       17.9                bid_ask_mid                    True           250.0                    0.7          93.1               29              1.81         73.26           72.42                 109.71                2435.0         2824.0               0.01                      ok
```

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.75               32            1.32              1.49        160.97               109.71         0.722          pass              0.753             55.8                           0.646               21.76              2.843                                 ok            True                  False
  FTNT           81.82               11            3.11              3.90        177.00                58.17         0.557          pass              0.125              4.7                           0.085                8.97              1.036                                 ok            True                  False
   TRI           84.62               26            1.61              1.13         99.83                57.78         0.555          pass              0.485             66.7                           0.375                3.12             -0.144                                 ok            True                  False
  TEAM          100.00               27            1.98              2.67        191.46                57.21         0.544          pass              0.578              3.3                           0.105                5.13              0.576                                 ok            True                  False
  ADSK           81.08               37            0.58              0.85        210.98                55.76         0.523          pass              0.360             33.0                           0.252               -0.70             -0.270                                 ok            True                  False
  SHOP           82.61               23            2.07              2.11        144.26                62.63         0.514          pass              0.294             28.8                           0.270               10.37              1.290                                 ok            True                  False
  CRWD           77.78               18            2.98              5.42        257.35                96.70         0.683          pass              0.122              0.0                           0.150               20.62              2.015                                 ok           False                  False
  PANW           54.55               11            3.94             10.77        385.31                80.20         0.571          pass              0.072              2.7                           0.072               10.65              1.151                                 ok           False                  False
   KHC           92.31               13            1.28              0.21         23.77                23.05         0.529          pass              0.460             19.7                           0.403               -3.42             -0.362            downtrend_blocked_slope           False                  False
  WDAY           94.74               38            0.49              0.66        190.71                49.78         0.524          pass              0.884             84.0                           0.558                2.68              0.238                                 ok           False                  False
  NVDA           91.18               34            0.30              0.48        224.38                44.14         0.519          pass              0.669             53.0                           0.352                2.57              0.665                                 ok           False                  False
  PAYX           85.19               27            0.70              0.50        101.38                39.96         0.509          pass              0.469             55.3                           0.301              -12.42             -1.478 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-09-25T15:10:05.947782-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:05:07.061521-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:00:05.968673-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:55:06.191609-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:50:06.559632-04:00       entry_1500              entry {"allocated_cash": 35550.0, "asset_type": "option", "contract_symbol": "MSTR261120C00160000", "contracts": 20, "early_entry_score": 0.665, "entry_mode": "regular", "entry_option_price": 17.775, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 2435.0, "option_spread_pct": 1.41, "option_volume": 2824.0, "success_rate": 93.1, "ticker": "MSTR", "timing_score": 0.711}
2026-09-25T14:50:06.559632-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-25", "training_samples": 5827, "window": 5}
2026-09-25T12:00:04.925096-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:55:06.011160-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:50:06.515187-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:45:06.706431-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925153505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925153505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925153505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925153505)

</details>
