# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 15:55:04 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$46,978.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$80.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   0     16     22240.0                 22320.0         13.9          13.95      224.68         224.9          bid_ask_mid                      13.95                bid_ask_mid                    True            80.0                   0.36         84.62               26              1.73         43.62           45.88                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL260918C00140000      9          2026-08-14         2026-08-17         21.8        28.1 5670.0   28.899083 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           84.62               26            1.67              2.67        227.50               127.87         0.829          pass              0.437             41.5                           0.319                2.04              0.303                  ok            True                  False
  TEAM           80.00               30            2.65              3.01        160.93               128.53         0.758          pass              0.282             24.2                           0.345               52.28              5.008                  ok            True                  False
  SHOP           92.31               13            3.73              4.02        152.60                83.98         0.642          pass              0.432              6.7                           0.109               26.97              2.202                  ok            True                  False
  TMUS           92.59               27            1.16              1.48        181.97                56.43         0.621          pass              0.633             40.4                           0.585                1.92              0.325                  ok            True                  False
  GEHC           95.00               20            1.72              0.89         73.31                52.52         0.612          pass              0.584             18.6                           0.403                6.47              0.705                  ok            True                  False
 CMCSA           90.00               10            2.12              0.39         26.01                41.99         0.603          pass              0.381             18.1                           0.315                4.34              0.556                  ok            True                  False
  UPRO           85.00               20            1.46              1.60        155.95                39.51         0.573          pass              0.257              0.0                           0.222                5.49              0.394                  ok            True                  False
  DXCM           86.67               30            1.09              0.69         89.46                54.82         0.562          pass              0.572             68.1                           0.543                1.67              0.680                  ok            True                  False
  ISRG           81.48               27            0.97              2.69        393.36                39.79         0.547          pass              0.270             20.7                           0.245                4.06              0.796                  ok            True                  False
   ROP          100.00               10            2.36              6.61        396.51                41.77         0.541          pass              0.470              5.2                           0.148               -0.68              0.035                  ok            True                  False
  DASH          100.00               24            1.90              2.89        215.78                46.91         0.527          pass              0.598             17.4                           0.208                6.18              0.618                  ok            True                  False
  PYPL           90.91               11            1.94              0.84         61.30                23.56         0.501          pass              0.410             20.9                           0.295                4.48              0.492                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-17T15:10:04.417812-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T15:05:03.524564-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T15:00:04.559198-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T14:55:02.466127-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-17T14:50:04.353625-04:00       entry_1500              entry {"allocated_cash": 22240.0, "asset_type": "option", "contract_symbol": "ALNY260918C00220000", "contracts": 16, "early_entry_score": 0.43, "entry_mode": "regular", "entry_option_price": 13.9, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 332.0, "option_spread_pct": 5.76, "option_volume": 21.0, "success_rate": 84.62, "ticker": "ALNY", "timing_score": 0.827}
2026-08-17T14:50:04.353625-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-17", "training_samples": 5665, "window": 5}
2026-08-17T12:00:04.607418-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:55:01.576813-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:50:04.389347-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:45:01.690104-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817155504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817155504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817155504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817155504)

</details>
