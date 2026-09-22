# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 12:55:09 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           93.55               31            0.96              1.29        191.37                50.40         0.521            pass              0.721             56.0                           0.580                2.03              0.429                                 ok            True                  False
  MSFT           95.45               22            0.98              3.44        500.14                22.55         0.502            pass              0.645             38.3                           0.561                0.56              0.086                                 ok            True                  False
  FTNT           89.19               37            1.10              1.35        174.65                58.27         0.501            pass              0.659             61.2                           0.789               10.05              1.203                                 ok            True                  False
  CRWD           88.64               44            0.43              0.76        249.03                96.94         0.667            pass              0.727             76.7                           0.826               18.21              2.112                                 ok           False                  False
  PANW           81.82               44            0.36              0.92        371.36                79.39         0.586            pass              0.559             83.9                           0.843                9.93              1.236                                 ok           False                  False
   TRI           93.94               33            0.47              0.31         95.30                58.54         0.584            pass              0.805             73.7                           0.817               -3.88             -0.276 downtrend_blocked_slope_and_streak           False                  False
  INTC           82.93               41            0.36              0.31        121.65                69.88         0.570            pass              0.584             82.9                           0.462               16.15              1.529                                 ok           False                  False
   KHC           94.44               18            0.43              0.07         24.34                22.03         0.547            pass              0.636             47.5                           0.475               -2.55             -0.122                                 ok           False                  False
  UPRO           84.21               38            0.03              0.03        154.06                31.53         0.508            pass              0.639             96.5                           0.582                3.17              0.320                                 ok           False                  False
  TEAM          100.00               15            3.53              4.84        193.60                58.22         0.499 below_threshold              0.578             31.5                           0.626                6.99              0.953                                 ok           False                  False
  ADBE           88.89                9            3.63              6.33        246.81                45.94         0.460 below_threshold              0.386             34.4                           0.368               -6.53             -0.433            downtrend_blocked_slope           False                  False
  AMZN           68.42               19            1.45              2.62        257.33                26.96         0.429 below_threshold              0.284             60.3                           0.416               -0.88             -0.002                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-22T12:00:04.192622-04:00 early_entry_1200 early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.559, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:55:04.534124-04:00 early_entry_1155 early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:50:04.129679-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.25, "hypothetical_budget": 35735.4, "hypothetical_contracts": 25, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.23, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:45:05.185045-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:40:04.072289-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:35:05.251125-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:30:06.235648-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:25:05.068681-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                               {"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "matched_signals": 31, "recovery_stability_score": 0.684, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:20:05.152954-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                 {"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "matched_signals": 31, "recovery_stability_score": 0.652, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:14:41.644035-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922125509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922125509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922125509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922125509)

</details>
