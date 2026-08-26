# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 15:40:01 EDT`
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

- Cash: `$160.60`
- Equity: `$55,630.60`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$855.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 28170.0        30.35          31.30      310.66        313.38          bid_ask_mid                      31.30                bid_ask_mid                    True           855.0                   3.13         87.50               32              1.06         63.04           63.28                  88.60                 214.0           30.0               0.05                      ok
  MNST     option         option MNST261016C00048000       2026-08-26                   0    140     27300.0                 27300.0         1.95           1.95       48.03         48.25          bid_ask_mid                       1.95                bid_ask_mid                    True             0.0                   0.00         85.71               14              1.44         27.42           25.90                 552.32                 249.0           74.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           89.47               19            0.99              0.34         48.59               552.32         1.000          pass              0.521             36.0                           0.566                4.94              0.586                  ok            True                  False
  ALNY           86.49               37            0.64              1.08        239.62               130.65         0.842          pass              0.606             56.2                           0.272                6.51              0.670                  ok            True                  False
  ABNB           95.65               23            1.21              1.61        189.81                61.60         0.676          pass              0.589             11.5                           0.149                4.50              0.482                  ok            True                  False
  SHOP           90.00               30            1.75              1.89        153.07                72.08         0.616          pass              0.517             18.6                           0.179                0.52             -0.155                  ok            True                  False
   TRI           88.89               27            1.66              1.21        103.86                66.28         0.602          pass              0.557             48.8                           0.280                0.69              0.320                  ok            True                  False
  WDAY           80.00               30            2.07              2.81        193.21                76.21         0.592          pass              0.330             45.8                           0.412                8.62              0.277                  ok            True                  False
  MELI           95.00               20            1.80             25.19       1986.20                47.50         0.554          pass              0.600             26.0                           0.444                7.26              0.991                  ok            True                  False
   KHC           86.67               15            1.90              0.34         25.18                34.81         0.532          pass              0.430             55.1                           0.705                1.26              0.153                  ok            True                  False
  BKNG           94.74               19            2.02              3.02        212.48                35.36         0.515          pass              0.578             24.5                           0.251               -1.32              0.013                  ok            True                  False
  VRTX           97.22               36            0.55              2.13        551.94                33.40         0.507          pass              0.767             47.8                           0.429                4.58              0.800                  ok            True                  False
  CPRT           81.48               27            1.38              0.32         33.19                43.23         0.506          pass              0.281             25.8                           0.310               13.38              1.362                  ok            True                  False
  VRSK           89.47               38            0.53              0.70        188.19                41.10         0.504          pass              0.696             68.7                           0.487                3.94              0.504                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-26T15:10:04.393572-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:05:01.392780-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:00:04.399840-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:55:02.427965-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:50:02.229559-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 27300.0, "asset_type": "option", "contract_symbol": "MNST261016C00048000", "contracts": 140, "early_entry_score": 0.298, "entry_mode": "regular", "entry_option_price": 1.95, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 5.13, "option_volume": 74.0, "success_rate": 85.71, "ticker": "MNST", "timing_score": 1.0}
2026-08-26T14:50:02.229559-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-26", "training_samples": 5704, "window": 5}
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:55:03.284797-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261002C00062000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 2.68, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.465, "hypothetical_budget": 13730.3, "hypothetical_contracts": 55, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 610.0, "option_spread_pct": 17.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.702, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T11:50:01.099073-04:00 early_entry_1150 early_entry_shadow                                   {"contract_symbol": "PYPL261016C00065000", "current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "entry_ask": 1.6, "entry_bid": 1.5, "entry_mode": "early", "entry_option_price": 1.55, "hypothetical_budget": 13730.3, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 6048.0, "option_spread_pct": 6.45, "option_volume": 584.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.734, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "matched_signals": 35, "recovery_stability_score": 0.734, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:45:03.275607-04:00 early_entry_1145 early_entry_shadow                                    {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "matched_signals": 35, "recovery_stability_score": 0.706, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826154001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826154001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826154001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826154001)

</details>
