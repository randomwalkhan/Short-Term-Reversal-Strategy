# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 15:20:01 EDT`
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

- Cash: `$17,648.00`
- Equity: `$31,110.50`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$37.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   0      5     13425.0                 13462.5        26.85          26.92      307.66        308.27          bid_ask_mid                      26.92                bid_ask_mid                    True            37.5                   0.28          87.1               31              1.19         68.92           68.08                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               30            3.93              3.86        138.60               179.06         0.681          pass              0.273             23.9                           0.521                5.14              2.555                                 ok            True                  False
  LRCX           87.50               32            0.99              2.15        310.43                90.05         0.656          pass              0.555             47.5                           0.523                5.72              1.432                                 ok            True                  False
  PYPL           93.94               33            0.74              0.31         58.94                60.12         0.650          pass              0.735             48.2                           0.564                4.57              0.345                                 ok            True                  False
 CMCSA           88.89               18            0.89              0.16         25.29                44.15         0.637          pass              0.539             61.5                           0.734               10.24              0.794                                 ok            True                  False
  AMAT           89.29               28            1.85              6.98        536.15                85.88         0.626          pass              0.483             17.5                           0.350                2.38              1.254                                 ok            True                  False
  BKNG           95.65               23            1.46              2.20        213.48                46.72         0.559          pass              0.662             39.7                           0.479               13.11              1.039                                 ok            True                  False
  ORLY           82.35               17            1.79              1.17         93.03                35.75         0.538          pass              0.215             17.3                           0.343                1.40              0.385                                 ok            True                  False
  ALNY           83.33               30            1.26              1.94        218.37               128.37         0.809          pass              0.332              9.5                           0.227              -22.26             -2.660            downtrend_blocked_slope           False                  False
  DRAM           77.14               35            0.85              0.30         50.47               108.94         0.700          pass              0.446             69.9                           0.612               -4.31              0.509           downtrend_blocked_streak           False                  False
   STX           88.89               36            0.17              0.96        812.35                91.44         0.601          pass              0.755             94.9                           0.552               -0.69              0.531                                 ok           False                  False
  TMUS           90.00               40            0.27              0.33        177.05                55.81         0.594          pass              0.792             88.5                           0.760               -0.28             -0.117                                 ok           False                  False
  AAPL           70.00               10            1.77              3.88        311.40                38.00         0.580          pass              0.160             34.2                           0.655               -8.73             -1.054 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-10T15:10:01.692365-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T15:05:01.609183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T15:00:04.645498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T14:55:05.599659-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T14:50:01.766475-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 13425.0, "asset_type": "option", "contract_symbol": "LRCX260918C00310000", "contracts": 5, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 26.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 3.35, "option_volume": 93.0, "success_rate": 87.1, "ticker": "LRCX", "timing_score": 0.649}
2026-08-10T14:50:01.766475-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-10", "training_samples": 5614, "window": 5}
2026-08-10T12:00:04.535713-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "LRCX260918C00310000", "current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "entry_ask": 28.45, "entry_bid": 26.4, "entry_mode": "early", "entry_option_price": 27.425, "hypothetical_budget": 15536.5, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 7.47, "option_volume": 47.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "matched_signals": 37, "recovery_stability_score": 0.687, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T11:55:01.643754-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:50:01.638195-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:45:06.232412-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810152001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810152001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810152001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810152001)

</details>
