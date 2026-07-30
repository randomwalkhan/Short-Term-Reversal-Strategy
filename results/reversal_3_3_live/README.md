# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 10:10:02 EDT`
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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           83.33               18            1.51              0.62         58.09                61.52         0.679          pass              0.259             16.2                           0.255                3.51              0.214                  ok            True                  False
   KDP           85.00               20            0.86              0.19         31.37                34.46         0.594          pass              0.415             51.8                           0.546                3.04              0.045                  ok            True                  False
  AAPL           90.91               11            1.66              3.93        336.50                28.00         0.575          pass              0.440             28.3                           0.393                1.55              0.188                  ok            True                  False
  FAST          100.00               10            1.51              0.50         47.56                27.18         0.573          pass              0.537             26.5                           0.278                3.45              0.415                  ok            True                  False
   CSX           95.24               21            0.77              0.27         50.62                28.82         0.568          pass              0.634             34.5                           0.269                1.86              0.283                  ok            True                  False
  VRTX           84.62               13            1.70              5.75        480.87                33.19         0.567          pass              0.310             36.8                           0.278               -0.25             -0.023                  ok            True                  False
   MAR          100.00               17            1.32              3.53        379.61                28.18         0.560          pass              0.683             59.9                           0.577                3.55              0.351                  ok            True                  False
  AMGN           90.91               11            1.66              4.50        385.71                27.22         0.559          pass              0.419             21.8                           0.244                7.31              0.717                  ok            True                  False
   PEP           80.00               10            1.99              2.00        142.64                31.31         0.552          pass              0.126             23.7                           0.244                3.87              0.332                  ok            True                  False
  ABNB           95.24               21            1.58              1.69        152.28                40.20         0.551          pass              0.647             39.6                           0.249                2.76              0.083                  ok            True                  False
   HON           87.50               24            0.83              1.39        240.52                39.75         0.522          pass              0.475             43.1                           0.383                7.39              1.074                  ok            True                  False
  MNST           96.30               27            0.63              0.43         97.05                25.74         0.519          pass              0.807             80.6                           0.692               -1.42             -0.242                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-07-30T10:10:02.887573-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "matched_signals": 43, "recovery_stability_score": 0.729, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:05:01.868497-04:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "matched_signals": 40, "recovery_stability_score": 0.681, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:00:05.892455-04:00 early_entry_1000 early_entry_shadow                          {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "entry_ask": 18.65, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.975, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 379.0, "option_spread_pct": 7.51, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T09:55:02.964620-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "FAST260918C00045000", "fill_price": 3.465, "pnl": -1732.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "FAST"}
2026-07-29T15:10:04.505433-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-07-29T15:05:04.399519-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-07-29T15:00:04.380256-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-07-29T14:55:04.522646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-07-29T14:50:04.497983-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"allocated_cash": 17325.0, "asset_type": "option", "contract_symbol": "FAST260918C00045000", "contracts": 45, "early_entry_score": 0.745, "entry_mode": "regular", "entry_option_price": 3.85, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 324.0, "option_spread_pct": 7.79, "option_volume": 33.0, "success_rate": 100.0, "ticker": "FAST", "timing_score": 0.573}
2026-07-29T14:50:04.497983-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-29", "training_samples": 5497, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730101002)

</details>
