# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 15:00:06 EDT`
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

- Cash: `$35,513.30`
- Equity: `$68,353.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL261030C00145000       2026-09-24                   0     16     32440.0                 32840.0        20.27          20.52      145.35        146.13          bid_ask_mid                      20.52                bid_ask_mid                    True           400.0                   1.23         83.33               36              0.62         109.9          108.74                 119.42                 341.0           51.0               0.08                      ok
```

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.43               35            0.50              0.19         52.43                57.12         0.616          pass              0.714             60.4                           0.659                0.14             -0.171                                 ok            True                   True
  NVDA           90.32               31            0.60              0.94        225.11                44.57         0.585          pass              0.682             69.5                           0.712                0.33              0.421                                 ok            True                   True
  TEAM          100.00               38            0.73              0.99        194.65                58.95         0.569          pass              0.859             71.7                           0.510                8.96              0.864                                 ok            True                  False
  MPWR           88.57               35            0.92              8.71       1351.74                51.84         0.551          pass              0.662             70.6                           0.699               11.57              1.252                                 ok            True                  False
  DRAM           82.14               28            1.92              0.83         61.54                51.34         0.537          pass              0.324             31.2                           0.494               -1.41              0.506                                 ok            True                  False
  AMAT           82.50               40            0.51              1.68        473.66                51.05         0.536          pass              0.569             82.9                           0.780                0.67              0.290                                 ok            True                  False
  MSFT           96.43               28            0.65              2.27        499.62                22.42         0.502          pass              0.766             65.4                           0.730                1.16              0.113                                 ok            True                  False
  SOXL           84.62               39            0.08              0.08        146.21               119.42         0.773          pass              0.690             98.9                           0.944               16.17              2.486                                 ok           False                  False
  PANW           82.61               46            0.11              0.29        393.17                79.07         0.638          pass              0.618             94.9                           0.803               17.24              1.383                                 ok           False                  False
   PEP          100.00                5            1.33              1.21        129.66                15.28         0.557          pass              0.456              0.0                           0.212               -6.03             -0.676 downtrend_blocked_slope_and_streak           False                  False
  ADBE           92.59               27            1.35              2.28        239.71                47.75         0.540          pass              0.549             15.3                           0.389               -6.84             -0.634            downtrend_blocked_slope           False                  False
  LRCX           74.36               39            0.87              1.88        306.48                60.60         0.538          pass              0.469             73.9                           0.725               -3.56              0.076                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-24T15:00:06.644624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T14:55:04.772794-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T14:50:06.859646-04:00       entry_1500              entry {"allocated_cash": 32440.0, "asset_type": "option", "contract_symbol": "SOXL261030C00145000", "contracts": 16, "early_entry_score": 0.614, "entry_mode": "regular", "entry_option_price": 20.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 341.0, "option_spread_pct": 7.64, "option_volume": 51.0, "success_rate": 83.33, "ticker": "SOXL", "timing_score": 0.762}
2026-09-24T14:50:06.859646-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-24", "training_samples": 5815, "window": 5}
2026-09-24T12:00:04.840325-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:55:06.286422-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:50:04.896304-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:45:04.623722-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:40:06.370244-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:35:05.981561-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924150006)

</details>
