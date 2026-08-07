# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 15:00:06 EDT`
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

- Cash: `$16,479.50`
- Equity: `$32,647.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$-47.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   0     94     16215.0                 16168.0         1.72           1.72       58.88         58.99          bid_ask_mid                       1.72                bid_ask_mid                    True           -47.0                  -0.29         94.12               17              1.51         27.86            27.0                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INSM           80.00               35            1.35              1.26        132.01               110.04         0.708          pass              0.449             70.6                           0.782               22.29              1.528                                 ok            True                  False
  PYPL           89.47               19            1.32              0.55         59.54                59.52         0.685          pass              0.429             16.0                           0.334                5.06              0.448                                 ok            True                  False
    MU           80.00               35            0.81              5.01        879.32               110.38         0.660          pass              0.470             79.2                           0.696               -5.06              0.214                                 ok            True                  False
  TMUS           87.50               16            1.73              2.18        179.03                57.01         0.642          pass              0.325              6.9                           0.244               -1.80             -0.187                                 ok            True                  False
  GOOG           80.56               36            0.89              2.21        355.67                50.46         0.532          pass              0.292             16.8                           0.302               10.77              1.305                                 ok            True                  False
   ADP           96.15               26            0.99              1.90        272.69                34.67         0.509          pass              0.756             66.2                           0.377                8.28              0.679                                 ok            True                  False
  DRAM           78.12               32            2.37              0.85         51.07               108.98         0.600          pass              0.369             54.3                           0.635               -5.60              0.336                                 ok           False                  False
  PAYX          100.00               24            0.47              0.40        119.96                34.54         0.575          pass              0.692             47.0                           0.307                6.39              0.407                                 ok           False                  False
   MAR           88.89               18            1.33              3.35        358.24                38.09         0.553          pass              0.358              4.2                           0.128               -5.22             -0.888 downtrend_blocked_slope_and_streak           False                  False
   CSX           92.00               25            0.66              0.23         50.60                29.04         0.545          pass              0.617             47.7                           0.273               -5.38             -0.311 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.91               33            0.02              0.01         62.75                30.17         0.537          pass              0.794             98.8                           0.480                3.67              0.189                                 ok           False                  False
 GOOGL           76.47               34            0.97              2.44        356.71                51.28         0.530          pass              0.250             12.3                           0.202               10.80              1.334                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-07T15:00:06.559995-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T14:55:06.579498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-07T14:50:05.673484-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 16215.0, "asset_type": "option", "contract_symbol": "PYPL260918C00060000", "contracts": 94, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 1.725, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 8843.0, "option_spread_pct": 2.9, "option_volume": 464.0, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.693}
2026-08-07T14:50:05.673484-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-07", "training_samples": 5596, "window": 5}
2026-08-07T12:00:04.348993-04:00 early_entry_1200 early_entry_shadow     {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "matched_signals": 36, "recovery_stability_score": 0.6, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:55:05.632607-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "matched_signals": 37, "recovery_stability_score": 0.603, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:50:01.513920-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:45:01.522063-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.616, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "matched_signals": 36, "recovery_stability_score": 0.616, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:40:01.565358-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:35:06.439574-04:00 early_entry_1135 early_entry_shadow  {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "matched_signals": 36, "recovery_stability_score": 0.658, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807150006)

</details>
