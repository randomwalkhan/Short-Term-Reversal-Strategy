# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 15:30:01 EDT`
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

- Cash: `$24,658.00`
- Equity: `$47,378.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   0     16     22240.0                 22720.0         13.9           14.2      224.68        225.35          bid_ask_mid                       14.2                bid_ask_mid                    True           480.0                   2.16         84.62               26              1.73         43.62           46.73                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL260918C00140000      9          2026-08-14         2026-08-17         21.8        28.1 5670.0   28.899083 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           82.76               29            1.44              2.31        227.66               127.87         0.825          pass              0.431             49.5                           0.628                2.28              0.313                  ok            True                  False
  TEAM           80.65               31            2.01              2.28        161.24               128.53         0.781          pass              0.363             42.5                           0.691               53.27              5.038                  ok            True                  False
  ABNB          100.00               13            2.11              2.72        182.89                64.74         0.676          pass              0.538             16.6                           0.432               19.61              2.436                  ok            True                  False
  SHOP           94.74               19            3.10              3.35        152.88                83.98         0.646          pass              0.584             22.2                           0.409               27.79              2.231                  ok            True                  False
  TMUS           91.30               23            1.55              1.98        181.76                56.43         0.620          pass              0.512             20.5                           0.436                1.52              0.308                  ok            True                  False
  GEHC           95.00               20            1.66              0.85         73.32                52.52         0.615          pass              0.594             21.8                           0.594                6.54              0.708                  ok            True                  False
 CMCSA           90.00               10            2.02              0.37         26.02                41.99         0.608          pass              0.393             21.8                           0.382                4.44              0.560                  ok            True                  False
  UPRO           85.71               21            1.30              1.42        156.02                39.51         0.579          pass              0.284              0.1                           0.223                5.66              0.401                  ok            True                  False
  DXCM           85.19               27            1.45              0.91         89.36                54.82         0.556          pass              0.480             57.5                           0.478                1.30              0.664                  ok            True                  False
   ROP          100.00               13            2.06              5.76        396.87                41.77         0.540          pass              0.526             17.4                           0.337               -0.37              0.049                  ok            True                  False
  DASH          100.00               27            1.63              2.47        215.96                46.91         0.531          pass              0.583              5.6                           0.165                6.48              0.631                  ok            True                  False
  ISRG           86.11               36            0.71              1.96        393.67                39.79         0.517          pass              0.514             42.0                           0.672                4.34              0.808                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817153001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817153001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817153001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817153001)

</details>
