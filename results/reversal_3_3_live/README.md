# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:00:06 EDT`
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
  AMGN           83.33               24            0.94              2.68        406.12                47.14         0.529            pass              0.272             12.2                           0.231                4.61              0.511                                 ok            True                  False
    MU           89.66               29            1.36             10.42       1092.92                49.88         0.523            pass              0.492             18.5                           0.180                6.57              0.358                                 ok            True                  False
  DRAM           79.41               34            0.56              0.24         61.93                54.09         0.578            pass              0.315             32.4                           0.228                3.48              0.005                                 ok           False                  False
  TEAM          100.00               42            0.01              0.01        189.91                55.53         0.557            pass              0.955             99.7                           0.485               -1.10             -0.554                                 ok           False                  False
  SNPS           81.40               43            0.28              0.97        490.12                58.70         0.532            pass              0.485             64.7                           0.392               27.06              1.973                                 ok           False                  False
   TRI           88.89               36            0.50              0.35         99.21                57.35         0.529            pass              0.730             89.0                           0.539                4.74              0.336                                 ok           False                  False
  PAYX           76.67               30            0.88              0.62        100.57                39.54         0.503            pass              0.247             21.2                           0.257              -13.94             -1.685 downtrend_blocked_slope_and_streak           False                  False
  VRSK           79.17               24            1.47              1.74        167.64                37.65         0.503            pass              0.170              8.8                           0.185               -5.42             -0.465 downtrend_blocked_slope_and_streak           False                  False
  ADBE           87.10               31            1.16              1.96        240.44                44.30         0.502            pass              0.436             19.0                           0.318               -4.20             -0.386            downtrend_blocked_slope           False                  False
  GILD           87.50                8            1.80              1.85        146.71                19.81         0.493 below_threshold              0.266              5.7                           0.184               -3.50             -0.288 downtrend_blocked_slope_and_streak           False                  False
   ADP           87.50                8            1.78              3.28        262.55                23.86         0.489 below_threshold              0.252              1.1                           0.188               -4.41             -0.424 downtrend_blocked_slope_and_streak           False                  False
  CTSH           92.00               25            1.59              0.68         60.59                46.07         0.488 below_threshold              0.555             28.7                           0.344                0.07             -0.043                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:50:04.979298-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:45:02.843264-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:40:04.819800-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "CEG261120C00260000", "current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "entry_ask": 16.1, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 15.5, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 433.0, "option_spread_pct": 7.74, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.898, "shadow_only": true, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.898, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-02T10:35:05.826835-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:30:04.822821-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:25:06.818366-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:20:07.304982-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:15:06.003196-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002110006)

</details>
