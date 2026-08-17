# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 15:05:03 EDT`
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

- Cash: `$24,658.00`
- Equity: `$46,498.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$-400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   0     16     22240.0                 21840.0         13.9          13.65      224.68        225.52          bid_ask_mid                      13.65                bid_ask_mid                    True          -400.0                   -1.8         84.62               26              1.73         43.62           42.62                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL260918C00140000      9          2026-08-14         2026-08-17         21.8        28.1 5670.0   28.899083 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           83.33               30            1.36              2.17        227.72               127.87         0.825          pass              0.462             52.5                           0.649                2.37              0.317                  ok            True                  False
  TEAM           80.00               30            2.63              2.98        160.94               128.53         0.759          pass              0.284             24.9                           0.377               52.31              5.009                  ok            True                  False
  ABNB          100.00               13            2.24              2.88        182.83                64.74         0.670          pass              0.522             11.7                           0.410               19.45              2.430                  ok            True                  False
  SHOP           94.74               19            3.06              3.30        152.91                83.98         0.648          pass              0.588             23.5                           0.500               27.86              2.233                  ok            True                  False
  TMUS           87.50               16            1.88              2.41        181.58                56.43         0.635          pass              0.309              1.7                           0.190                1.17              0.292                  ok            True                  False
  GEHC           94.44               18            1.83              0.95         73.28                52.52         0.616          pass              0.541             13.5                           0.269                6.35              0.700                  ok            True                  False
 CMCSA           90.00               10            2.16              0.40         26.01                41.99         0.601          pass              0.377             16.6                           0.285                4.30              0.554                  ok            True                  False
  UPRO           84.00               25            1.16              1.27        156.08                39.51         0.561          pass              0.280              5.7                           0.253                5.80              0.408                  ok            True                  False
  DXCM           84.00               25            1.63              1.02         89.31                54.82         0.556          pass              0.420             52.4                           0.361                1.12              0.656                  ok            True                  False
  ISRG           81.48               27            1.00              2.76        393.33                39.79         0.545          pass              0.263             18.5                           0.291                4.04              0.795                  ok            True                  False
   ROP          100.00               13            2.07              5.78        396.86                41.77         0.540          pass              0.525             17.1                           0.252               -0.38              0.049                  ok            True                  False
  DASH          100.00               28            1.52              2.30        216.03                46.91         0.531          pass              0.609             12.0                           0.191                6.60              0.636                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-17T15:05:03.524564-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T15:00:04.559198-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T14:55:02.466127-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T14:50:04.353625-04:00       entry_1500              entry {"allocated_cash": 22240.0, "asset_type": "option", "contract_symbol": "ALNY260918C00220000", "contracts": 16, "early_entry_score": 0.43, "entry_mode": "regular", "entry_option_price": 13.9, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 332.0, "option_spread_pct": 5.76, "option_volume": 21.0, "success_rate": 84.62, "ticker": "ALNY", "timing_score": 0.827}
2026-08-17T14:50:04.353625-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-17", "training_samples": 5665, "window": 5}
2026-08-17T12:00:04.607418-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:55:01.576813-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:50:04.389347-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:45:01.690104-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:40:05.536828-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817150503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817150503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817150503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817150503)

</details>
