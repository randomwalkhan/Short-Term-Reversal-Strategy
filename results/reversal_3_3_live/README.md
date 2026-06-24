# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 10:20:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           95.00               20            4.45              7.20        228.33               242.24         0.909          pass              0.581              7.9                           0.166                9.64              2.300                  ok            True                  False
    MU           89.29               28            1.82             13.41       1046.02               131.92         0.733          pass              0.450              3.1                           0.116               10.33              1.805                  ok            True                  False
  KLAC           90.48               21            1.93              3.30        243.07                93.06         0.708          pass              0.515             30.6                           0.357               12.08              1.280                  ok            True                  False
  MRVL          100.00               13            5.05              9.87        274.81               157.48         0.669          pass              0.487              0.0                           0.170               -0.73              0.712                  ok            True                  False
  LRCX           96.00               25            1.25              3.24        369.94                85.65         0.626          pass              0.825             87.4                           0.593               12.17              1.453                  ok            True                  False
  MCHP           96.43               28            1.09              0.71         92.95                72.77         0.622          pass              0.702             40.0                           0.410                0.84              0.552                  ok            True                  False
  ASML           95.24               21            2.29             28.48       1766.25                65.60         0.609          pass              0.581             15.5                           0.276               -2.25              0.082                  ok            True                  False
  INTC           93.75               32            1.27              1.18        131.77                97.89         0.575          pass              0.839             89.4                           0.535               21.01              2.229                  ok            True                  False
  PANW           87.50               24            2.15              4.37        289.04                56.69         0.545          pass              0.348              0.0                           0.177                9.27              0.878                  ok            True                  False
  AMAT           96.88               32            0.65              2.66        584.74                79.43         0.530          pass              0.888             96.1                           0.599               16.60              1.862                  ok            True                   True
  NXPI           91.30               23            1.78              3.74        298.34                63.85         0.517          pass              0.519             26.2                           0.172               -0.94              0.313                  ok            True                  False
  CDNS           91.30               23            1.75              4.64        377.07                55.93         0.517          pass              0.440              0.0                           0.217               -4.72             -0.240                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-24T10:20:01.164945-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                           {"contract_symbol": "AMAT260724C00580000", "current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "entry_ask": 54.55, "entry_bid": 49.75, "entry_mode": "early", "entry_option_price": 52.15, "hypothetical_budget": 15306.25, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 65.0, "option_spread_pct": 9.2, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.599, "shadow_only": true, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "matched_signals": 32, "recovery_stability_score": 0.599, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:15:01.116504-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:10:01.169006-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "entry_mode": "early", "error": "KLAC: no call expiries found in the 21-40 trading-day window.", "matched_signals": 33, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "matched_signals": 33, "recovery_stability_score": 0.751, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:05:01.111815-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:00:02.286958-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "entry_ask": 35.3, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 33.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 114.0, "option_spread_pct": 8.88, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "matched_signals": 33, "recovery_stability_score": 0.655, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-24T09:20:01.109273-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T11:20:02.932662-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "GOOG260731C00345000", "current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "entry_ask": 18.9, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 142.0, "option_spread_pct": 5.99, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T10:51:17.657217-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624102001)

</details>
