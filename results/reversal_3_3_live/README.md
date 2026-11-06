# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 10:05:04 EST`
Last processed slot: `manage_1000`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.06               34            0.88              4.13        668.94                77.01         0.647          pass              0.839             71.5                           0.776               18.64              2.426                  ok            True                   True
  MDLZ           91.67               12            1.27              0.59         66.57                30.66         0.564          pass              0.571             63.4                           0.784                3.40              0.727                  ok            True                  False
  TMUS           80.77               26            0.81              0.91        160.20                69.87         0.563          pass              0.413             76.4                           0.822                8.70              1.075                  ok            True                  False
  COST           81.25               16            0.94              6.99       1062.59                23.23         0.543          pass              0.302             58.2                           0.757                5.37              0.715                  ok            True                  False
  MSFT          100.00               22            1.14              4.26        534.10                35.82         0.526          pass              0.718             61.7                           0.579                1.02              0.116                  ok            True                  False
  AAPL           95.83               24            0.67              1.62        343.48                25.86         0.511          pass              0.732             62.5                           0.703               -1.69             -0.148                  ok            True                  False
  ISRG           87.50                8            2.07              6.78        465.61                42.48         0.571          pass              0.325             22.6                           0.350                1.45              0.373                  ok           False                  False
   KDP           87.50                8            1.90              0.49         36.68                35.93         0.563          pass              0.378             40.7                           0.582                4.35              0.561                  ok           False                  False
   PEP           85.71                7            1.56              1.56        142.04                27.68         0.560          pass              0.363             51.4                           0.744                3.47              0.627                  ok           False                  False
   ADP          100.00                7            1.92              4.13        305.37                28.50         0.558          pass              0.599             47.6                           0.671               -0.96              0.230                  ok           False                  False
 CMCSA           83.33                6            1.98              0.35         24.80                35.54         0.558          pass              0.292             49.0                           0.730                7.78              1.374                  ok           False                  False
   CSX           77.78                9            1.53              0.55         50.60                30.62         0.551          pass              0.142             29.1                           0.486               -1.46             -0.168                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-11-06T10:05:04.744572-05:00 early_entry_1005 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "entry_ask": 34.8, "entry_bid": 29.0, "entry_mode": "early", "entry_option_price": 31.9, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "matched_signals": 34, "recovery_stability_score": 0.776, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 72.0, "matched_signals": 39, "recovery_stability_score": 0.724, "success_rate": 89.74, "ticker": "TTWO", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:00:04.754305-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "entry_ask": 34.8, "entry_bid": 28.1, "entry_mode": "early", "entry_option_price": 31.45, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 21.3, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "matched_signals": 34, "recovery_stability_score": 0.777, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.696, "early_reclaim_pct": 81.0, "matched_signals": 36, "recovery_stability_score": 0.872, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.429, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T09:50:05.832497-05:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "ORLY261218C00095000", "fill_price": 1.6875, "pnl": -6468.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ORLY"}
2026-11-06T00:00:05.873156-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 91, 'empty': 2}
2026-11-05T15:10:05.513182-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T15:05:05.534747-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T15:00:06.437749-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T14:55:05.870253-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-11-05T14:50:06.583825-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 64687.5, "asset_type": "option", "contract_symbol": "ORLY261218C00095000", "contracts": 345, "early_entry_score": 0.515, "entry_mode": "regular", "entry_option_price": 1.875, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 2285.0, "option_spread_pct": 13.33, "option_volume": 162.0, "success_rate": 100.0, "ticker": "ORLY", "timing_score": 0.528}
2026-11-05T14:50:06.583825-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-05", "training_samples": 6319, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106100504)

</details>
