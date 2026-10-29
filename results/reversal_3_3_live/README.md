# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 15:10:05 EDT`
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

- Cash: `$61,734.30`
- Equity: `$125,079.30`
- Realized PnL: `$113,336.80`
- Unrealized PnL: `$1,742.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261218C00140000       2026-10-29                   0     41     61602.5                 63345.0        15.02          15.45      141.06        141.03          bid_ask_mid                      15.45                bid_ask_mid                    True          1742.5                   2.83         86.96               23              2.82         69.46           71.33                  71.12                1665.0           96.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261218C00110000     90          2026-10-28         2026-10-29        7.275      6.5475 -6547.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           92.31               13            1.84              1.94        150.31                30.20         0.553          pass              0.461             19.1                           0.471               -2.08             -0.037                                 ok            True                  False
  MSTR           86.96               23            2.87              2.91        143.91                71.12         0.552          pass              0.429             33.8                           0.413               -6.80             -0.082                                 ok            True                  False
  ADBE           86.21               29            1.27              2.21        248.81                41.65         0.510          pass              0.535             63.8                           0.453               -2.01              0.033                                 ok            True                  False
  TMUS           80.77               26            0.82              0.85        147.72                64.00         0.651          pass              0.192              0.0                           0.229               -6.47             -0.905            downtrend_blocked_slope           False                  False
  CSCO           69.23               13            1.70              1.32        109.73                35.33         0.551          pass              0.090              4.8                           0.245               -1.31              0.212                                 ok           False                  False
   WDC           73.17               41            0.90              2.51        395.35                80.12         0.548          pass              0.491             78.7                           0.455               10.21              1.171                                 ok           False                  False
  MPWR           57.89               19            2.37             20.10       1202.61                59.53         0.547          pass              0.233             39.4                           0.415               -5.34             -0.571            downtrend_blocked_slope           False                  False
  NVDA           78.95               19            1.24              1.87        214.58                30.56         0.546          pass              0.172             19.1                           0.332               -2.08             -0.114                                 ok           False                  False
  AVGO           54.55               11            2.42              5.95        349.26                43.15         0.533          pass              0.164             34.7                           0.386               -0.30              0.222                                 ok           False                  False
  MELI           77.42               31            1.25             14.66       1666.81                48.85         0.529          pass              0.357             54.5                           0.698              -11.03             -1.351 downtrend_blocked_slope_and_streak           False                  False
   LIN           77.78                9            1.20              4.26        506.34                14.48         0.519          pass              0.165             37.7                           0.346                1.80              0.215                                 ok           False                  False
   STX           72.97               37            0.89              4.37        696.10                77.70         0.511          pass              0.469             79.1                           0.459                0.13              0.180                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-29T15:10:05.741220-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T15:05:04.728633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T15:00:04.604775-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T14:55:06.721591-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T14:50:05.643869-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 61602.5, "asset_type": "option", "contract_symbol": "MSTR261218C00140000", "contracts": 41, "early_entry_score": 0.432, "entry_mode": "regular", "entry_option_price": 15.025, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1665.0, "option_spread_pct": 2.33, "option_volume": 96.0, "success_rate": 86.96, "ticker": "MSTR", "timing_score": 0.554}
2026-10-29T14:50:05.643869-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-29", "training_samples": 6227, "window": 5}
2026-10-29T12:00:05.637930-04:00 early_entry_1200 early_entry_shadow    {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "entry_ask": 14.7, "entry_bid": 14.3, "entry_mode": "early", "entry_option_price": 14.5, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.76, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "matched_signals": 34, "recovery_stability_score": 0.658, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:55:05.739980-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "entry_ask": 14.8, "entry_bid": 14.35, "entry_mode": "early", "entry_option_price": 14.575, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.09, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.667, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "matched_signals": 34, "recovery_stability_score": 0.667, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:50:04.572626-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "entry_ask": 14.95, "entry_bid": 14.55, "entry_mode": "early", "entry_option_price": 14.75, "hypothetical_budget": 61668.4, "hypothetical_contracts": 41, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.71, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "matched_signals": 33, "recovery_stability_score": 0.703, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:45:01.204806-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "entry_ask": 14.45, "entry_bid": 14.0, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 61668.4, "hypothetical_contracts": 43, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.16, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.738, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029151005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029151005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029151005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029151005)

</details>
