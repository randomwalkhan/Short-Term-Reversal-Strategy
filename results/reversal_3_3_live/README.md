# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 15:55:06 EDT`
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

- Cash: `$16,479.50`
- Equity: `$33,070.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$376.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   0     94     16215.0                 16591.0         1.72           1.76       58.88         59.17          bid_ask_mid                       1.76                bid_ask_mid                    True           376.0                   2.32         94.12               17              1.51         27.86           27.25                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           80.00               35            0.71              4.36        879.60               110.38         0.667            pass              0.479             81.9                           0.632               -4.96              0.219                                 ok            True                  False
  PYPL           92.86               28            1.01              0.42         59.60                59.52         0.654            pass              0.641             37.6                           0.485                5.39              0.463                                 ok            True                  False
  TMUS           89.47               19            1.51              1.90        179.16                57.01         0.640            pass              0.434             19.1                           0.342               -1.57             -0.177                                 ok            True                  False
   ADP           96.43               28            0.78              1.49        272.87                34.67         0.511            pass              0.792             73.5                           0.573                8.51              0.689                                 ok            True                  False
  INSM           78.95               38            1.16              1.08        132.09               110.04         0.701            pass              0.481             74.8                           0.647               22.53              1.537                                 ok           False                  False
  DRAM           78.12               32            1.98              0.71         51.13               108.98         0.627            pass              0.395             61.8                           0.586               -5.23              0.354                                 ok           False                  False
   MAR           84.62               13            1.63              4.11        357.91                38.09         0.556            pass              0.199              0.0                           0.237               -5.51             -0.902 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           89.29               28            0.22              0.09         62.71                30.17         0.555            pass              0.675             84.0                           0.473                3.46              0.180                                 ok           False                  False
   CSX           90.48               21            0.90              0.32         50.56                29.04         0.554            pass              0.495             28.9                           0.227               -5.61             -0.322 downtrend_blocked_slope_and_streak           False                  False
  GOOG           78.38               37            0.77              1.93        355.79                50.46         0.530            pass              0.316             27.6                           0.399               10.90              1.310                                 ok           False                  False
 GOOGL           75.00               36            0.79              1.99        356.90                51.28         0.526            pass              0.311             28.5                           0.353               11.00              1.342                                 ok           False                  False
   BKR           66.67               15            1.77              0.78         62.42                29.90         0.483 below_threshold              0.082              0.0                           0.160                7.67              0.714                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-07T15:10:06.531054-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T15:05:04.549865-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T15:00:06.559995-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T14:55:06.579498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T14:50:05.673484-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 16215.0, "asset_type": "option", "contract_symbol": "PYPL260918C00060000", "contracts": 94, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 1.725, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 8843.0, "option_spread_pct": 2.9, "option_volume": 464.0, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.693}
2026-08-07T14:50:05.673484-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-07", "training_samples": 5596, "window": 5}
2026-08-07T12:00:04.348993-04:00 early_entry_1200 early_entry_shadow     {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "matched_signals": 36, "recovery_stability_score": 0.6, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:55:05.632607-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "matched_signals": 37, "recovery_stability_score": 0.603, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:50:01.513920-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:45:01.522063-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.616, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "matched_signals": 36, "recovery_stability_score": 0.616, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807155506)

</details>
