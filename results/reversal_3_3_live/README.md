# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 10:15:06 EST`
Last processed slot: `early_entry_1015`

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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           90.91               11            1.34              0.35         36.74                35.93         0.581          pass              0.530             58.1                           0.728                4.95              0.587                                 ok            True                  False
 CMCSA           92.86               14            1.22              0.21         24.86                35.54         0.562          pass              0.631             68.6                           0.831                8.62              1.409                                 ok            True                  False
  ISRG           87.50               16            1.77              5.81        466.03                42.48         0.541          pass              0.395             33.7                           0.440                1.75              0.387                                 ok            True                  False
  COST           80.95               21            0.64              4.79       1063.54                23.23         0.531          pass              0.366             71.4                           0.820                5.68              0.728                                 ok            True                  False
   PEP           88.24               17            1.10              1.10        142.24                27.68         0.529          pass              0.517             65.8                           0.827                3.96              0.649                                 ok            True                  False
  ORLY          100.00               15            1.43              0.92         91.10                25.42         0.520          pass              0.645             53.4                           0.639                0.29              0.124                                 ok            True                  False
  CTAS           94.12               17            1.32              2.09        225.51                27.57         0.510          pass              0.637             54.1                           0.704               -0.30              0.288                                 ok            True                  False
  FTNT           87.50               48            0.05              0.04        122.49                92.45         0.652          pass              0.738             90.8                           0.415              -31.97             -4.838 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.78               45            0.13              0.63        670.44                77.01         0.628          pass              0.950             95.7                           0.911               19.53              2.460                                 ok           False                  False
  PAYX           75.00                4            2.00              1.67        118.78                35.22         0.562          pass              0.218             53.9                           0.610                0.22              0.524                                 ok           False                  False
  MSTR           88.24               34            0.94              0.85        128.93                81.05         0.560          pass              0.637             67.1                           0.418              -12.28             -1.054            downtrend_blocked_slope           False                  False
  MDLZ           95.45               22            0.42              0.20         66.74                30.66         0.559          pass              0.800             87.9                           0.950                4.29              0.766                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-11-06T10:15:06.200919-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:10:06.574666-05:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "entry_ask": 31.1, "entry_bid": 25.9, "entry_mode": "early", "entry_option_price": 28.5, "hypothetical_budget": 61581.4, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 18.25, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.847, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 82.4, "matched_signals": 37, "recovery_stability_score": 0.911, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:05:04.744572-05:00 early_entry_1005 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "entry_ask": 34.8, "entry_bid": 29.0, "entry_mode": "early", "entry_option_price": 31.9, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "matched_signals": 34, "recovery_stability_score": 0.776, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 72.0, "matched_signals": 39, "recovery_stability_score": 0.724, "success_rate": 89.74, "ticker": "TTWO", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:00:04.754305-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "entry_ask": 34.8, "entry_bid": 28.1, "entry_mode": "early", "entry_option_price": 31.45, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 21.3, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "matched_signals": 34, "recovery_stability_score": 0.777, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.696, "early_reclaim_pct": 81.0, "matched_signals": 36, "recovery_stability_score": 0.872, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.429, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T09:50:05.832497-05:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "ORLY261218C00095000", "fill_price": 1.6875, "pnl": -6468.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ORLY"}
2026-11-06T00:00:05.873156-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 91, 'empty': 2}
2026-11-05T15:10:05.513182-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T15:05:05.534747-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T15:00:06.437749-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T14:55:05.870253-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106101506)

</details>
