# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-26 15:35:01 EDT`
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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AVGO     option         option AVGO260821C00380000      4          2026-06-25         2026-06-26         31.3       28.17 -1252.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   WBD           90.91               11            0.70              0.13         26.92                20.23         0.621          pass              0.445             28.3                           0.361               -0.26              0.069                      ok            True                  False
  AMAT           91.67               12            3.41             15.95        661.17                87.16         0.614          pass              0.532             48.9                           0.559               16.75              1.439                      ok            True                  False
    MU           90.91               11            5.61             47.62       1193.15               127.35         0.609          pass              0.441             27.6                           0.292               15.03              1.497                      ok            True                  False
  INTC           91.30               23            3.15              2.93        131.61                97.28         0.573          pass              0.575             43.1                           0.605               10.02              1.109                      ok            True                  False
  PCAR           84.62               26            0.87              0.74        121.36                36.28         0.523          pass              0.496             71.2                           0.576                2.59              0.084                      ok            True                  False
  LRCX          100.00               10            5.04             14.16        395.75                86.42         0.517          pass              0.530             26.2                           0.453                5.33              0.564                      ok            True                  False
  MRVL          100.00               10            5.68             11.18        276.47               155.27         0.753          pass              0.524             16.2                           0.359               -5.49             -0.478 downtrend_blocked_slope           False                  False
  AVGO           75.00               12            2.86              7.60        375.65                76.91         0.660          pass              0.140             20.3                           0.325               -4.39             -0.289 downtrend_blocked_slope           False                  False
  DRAM           85.71                7            5.60              3.01         75.60               122.54         0.649          pass              0.287             23.3                           0.264               11.46              1.219                      ok           False                  False
  KLAC           85.71                7            4.67              8.47        255.17                93.32         0.605          pass              0.282             23.0                           0.395                2.30              0.152                      ok           False                  False
  UPRO           90.00               30            0.36              0.34        134.58                51.32         0.604          pass              0.720             86.5                           0.659               -2.00             -0.532 downtrend_blocked_slope           False                  False
  ASML           91.67               12            3.53             45.56       1821.66                66.48         0.588          pass              0.418             11.5                           0.246               -6.50             -0.539 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-26T15:10:04.394440-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T14:50:01.669190-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"budget": 14680.25, "entry_cost": 16617.5, "reason": "insufficient_cash", "ticker": "MU"}
2026-06-26T14:50:01.669190-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.416, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3233.0, "option_spread_pct": 43.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.62}
2026-06-26T14:50:01.669190-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-26", "training_samples": 5312, "window": 5}
2026-06-26T12:00:02.704488-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "entry_ask": 17.3, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.75, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 6.57, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "matched_signals": 35, "recovery_stability_score": 0.58, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-26T11:53:23.382476-04:00 early_entry_1150      early_entry_shadow  {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "entry_ask": 17.0, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.6, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 4.82, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.78, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "matched_signals": 35, "recovery_stability_score": 0.78, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-26T11:10:57.327815-04:00 early_entry_1110      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260626153501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260626153501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260626153501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260626153501)

</details>
