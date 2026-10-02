# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:10:04 EDT`
Last processed slot: `manage_1100`

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
  DRAM           80.65               31            0.76              0.33         61.89                54.09         0.584            pass              0.264             16.1                           0.208                3.27             -0.004                                 ok            True                  False
  AMGN           85.71               21            1.03              2.93        406.01                47.14         0.543            pass              0.321             13.6                           0.222                4.52              0.507                                 ok            True                  False
    MU           89.66               29            1.51             11.61       1092.41                49.88         0.514            pass              0.463              9.2                           0.104                6.40              0.351                                 ok            True                  False
    ZS           95.74               47            0.06              0.08        198.75                77.30         0.642            pass              0.947             94.2                           0.516                0.69             -0.471                                 ok           False                  False
  MSTR           91.89               37            0.22              0.25        160.39                96.54         0.622            pass              0.712             50.8                           0.244                4.05             -0.351                                 ok           False                  False
  TEAM          100.00               39            0.57              0.76        189.58                55.53         0.540            pass              0.835             62.6                           0.350               -1.66             -0.580           downtrend_blocked_streak           False                  False
  SNPS           81.40               43            0.23              0.78        490.21                58.70         0.535            pass              0.506             71.8                           0.528               27.13              1.976                                 ok           False                  False
   TRI           89.19               37            0.34              0.24         99.26                57.35         0.533            pass              0.756             92.4                           0.475                4.90              0.343                                 ok           False                  False
  PAYX           69.57               23            1.39              0.98        100.42                39.54         0.500            pass              0.137              0.0                           0.203              -14.38             -1.708 downtrend_blocked_slope_and_streak           False                  False
  VRSK           78.95               19            1.92              2.26        167.41                37.65         0.500            pass              0.110              0.0                           0.150               -5.85             -0.485 downtrend_blocked_slope_and_streak           False                  False
  GILD           85.71                7            1.90              1.96        146.66                19.81         0.491 below_threshold              0.213              3.9                           0.095               -3.61             -0.293 downtrend_blocked_slope_and_streak           False                  False
  CTSH           91.67               24            1.71              0.73         60.57                46.07         0.487 below_threshold              0.524             23.5                           0.272               -0.05             -0.049                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-02T11:10:04.764942-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:05:01.135805-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "entry_ask": 26.3, "entry_bid": 23.2, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 40682.15, "hypothetical_contracts": 16, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 12.53, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.605, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:50:04.979298-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:45:02.843264-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:40:04.819800-04:00 early_entry_1040 early_entry_shadow                         {"contract_symbol": "CEG261120C00260000", "current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "entry_ask": 16.1, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 15.5, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 433.0, "option_spread_pct": 7.74, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.898, "shadow_only": true, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.898, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-02T10:35:05.826835-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:30:04.822821-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:25:06.818366-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002111004)

</details>
