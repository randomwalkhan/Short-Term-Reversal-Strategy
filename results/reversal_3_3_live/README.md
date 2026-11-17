# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 15:25:04 EST`
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

- Cash: `$58,029.80`
- Equity: `$110,049.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$-1,190.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP261218C00400000       2026-11-17                   0     17     53210.0                 52020.0         31.3           30.6      402.79        400.58          bid_ask_mid                       30.6                bid_ask_mid                    True         -1190.0                  -2.24         94.12               17              2.99         63.29            64.1                  119.5                1252.0          197.0               0.01                      ok
```

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           95.65               23            1.39              6.82        697.73                77.90         0.728          pass              0.634             24.7                           0.434                2.81              0.323                  ok            True                  False
   ADI           90.62               32            0.84              2.26        382.20                67.56         0.611          pass              0.607             38.6                           0.320               -9.49             -0.152                  ok            True                  False
   TXN           93.75               32            0.61              1.26        293.67                59.80         0.592          pass              0.786             71.2                           0.488               -6.43             -0.012                  ok            True                  False
  MDLZ           93.75               16            1.00              0.47         67.34                29.55         0.592          pass              0.501             11.8                           0.189                2.68              0.176                  ok            True                  False
  SBUX           84.62               13            1.15              0.87        108.35                31.47         0.578          pass              0.279             26.0                           0.226                3.18              0.190                  ok            True                  False
   CSX           80.00               15            1.44              0.53         51.80                34.26         0.578          pass              0.157             21.9                           0.228                1.10              0.256                  ok            True                  False
  QCOM           84.00               25            1.73              2.04        167.65                68.75         0.576          pass              0.420             52.0                           0.442                0.72              0.345                  ok            True                  False
   CEG           84.62               13            2.78              5.41        275.50                60.48         0.575          pass              0.257             18.8                           0.317                2.70              1.217                  ok            True                  False
  TMUS           83.33               30            0.64              0.76        169.68                46.99         0.572          pass              0.299              6.4                           0.183                9.40              0.919                  ok            True                  False
  CTAS           95.00               20            0.97              1.52        223.51                28.21         0.553          pass              0.552             10.0                           0.226               -0.55             -0.033                  ok            True                  False
   EXC           83.33               18            0.97              0.32         46.32                21.89         0.545          pass              0.242             15.1                           0.290                1.12              0.051                  ok            True                  False
  INSM           81.08               37            1.24              1.06        122.42                61.88         0.540          pass              0.458             65.1                           0.550               16.20              1.473                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:50:06.628486-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 53210.0, "asset_type": "option", "contract_symbol": "APP261218C00400000", "contracts": 17, "early_entry_score": 0.66, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 1252.0, "option_spread_pct": 1.28, "option_volume": 197.0, "success_rate": 94.12, "ticker": "APP", "timing_score": 0.778}
2026-11-17T14:50:06.628486-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-17", "training_samples": 6239, "window": 5}
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:55:01.833366-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:50:06.047053-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:45:03.924491-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "entry_ask": 23.75, "entry_bid": 21.55, "entry_mode": "early", "entry_option_price": 22.65, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 9.71, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "matched_signals": 32, "recovery_stability_score": 0.589, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117152504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117152504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117152504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117152504)

</details>
