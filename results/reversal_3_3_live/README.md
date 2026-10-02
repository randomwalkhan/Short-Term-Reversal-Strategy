# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:20:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           84.62               26            0.72              2.04        406.39                47.14         0.533            pass              0.402             39.8                           0.360                4.85              0.521                                 ok            True                  False
   TRI           88.89               36            0.61              0.42         99.18                57.35         0.522            pass              0.722             86.6                           0.440                4.62              0.331                                 ok            True                  False
    MU           92.31               26            1.99             15.32       1090.82                49.88         0.502            pass              0.485              0.0                           0.157                5.88              0.329                                 ok            True                  False
    ZS           95.74               47            0.07              0.09        198.74                77.30         0.642            pass              0.944             93.2                           0.464                0.68             -0.471                                 ok           False                  False
  MSTR           92.31               39            0.01              0.01        160.50                96.54         0.624            pass              0.880             98.6                           0.424                4.27             -0.341                                 ok           False                  False
  DRAM           79.31               29            1.19              0.52         61.81                54.09         0.565            pass              0.183              0.0                           0.150                2.82             -0.024                                 ok           False                  False
  TEAM          100.00               38            1.02              1.35        189.33                55.53         0.518            pass              0.738             33.3                           0.223               -2.11             -0.601           downtrend_blocked_streak           False                  False
  ADSK           82.61               46            0.08              0.11        211.26                48.72         0.504            pass              0.544             74.6                           0.410               -2.67             -0.525 downtrend_blocked_slope_and_streak           False                  False
  VRSK           76.47               17            2.01              2.37        167.37                37.65         0.502            pass              0.116              6.4                           0.114               -5.93             -0.489 downtrend_blocked_slope_and_streak           False                  False
  GILD           88.89                9            1.65              1.70        146.77                19.81         0.498 below_threshold              0.337             16.8                           0.277               -3.36             -0.281 downtrend_blocked_slope_and_streak           False                  False
  PAYX           69.57               23            1.42              1.00        100.41                39.54         0.497 below_threshold              0.153              5.6                           0.124              -14.41             -1.710 downtrend_blocked_slope_and_streak           False                  False
  CTSH           92.00               25            1.59              0.68         60.59                46.07         0.488 below_threshold              0.555             28.7                           0.266                0.07             -0.043                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-02T11:20:06.662983-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:15:03.733352-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:10:04.764942-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:05:01.135805-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "entry_ask": 26.3, "entry_bid": 23.2, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 40682.15, "hypothetical_contracts": 16, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 12.53, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.605, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:50:04.979298-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:45:02.843264-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:40:04.819800-04:00 early_entry_1040 early_entry_shadow                         {"contract_symbol": "CEG261120C00260000", "current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "entry_ask": 16.1, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 15.5, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 433.0, "option_spread_pct": 7.74, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.898, "shadow_only": true, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.898, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-02T10:35:05.826835-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002112006)

</details>
