# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:40:04 EDT`
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
  AMGN           84.62               26            0.72              2.06        406.39                47.14         0.533            pass              0.291              2.8                           0.061                4.84              0.521                                 ok            True                  False
    MU           92.11               38            0.51              3.93       1095.71                49.88         0.528            pass              0.750             62.7                           0.502                7.48              0.397                                 ok            True                  False
  TEAM          100.00               42            0.11              0.14        189.85                55.53         0.551            pass              0.934             93.1                           0.484               -1.20             -0.559                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.319               11.31              0.523                                 ok           False                  False
  SNPS           80.95               42            0.33              1.14        490.05                58.70         0.535            pass              0.446             55.8                           0.262               27.00              1.971                                 ok           False                  False
   TRI           89.74               39            0.16              0.11         99.31                57.35         0.534            pass              0.796             96.6                           0.478                5.10              0.351                                 ok           False                  False
  PAYX           79.41               34            0.56              0.39        100.67                39.54         0.504            pass              0.362             50.4                           0.406              -13.66             -1.670 downtrend_blocked_slope_and_streak           False                  False
  CTSH           90.91               22            1.84              0.78         60.54                46.07         0.490 below_threshold              0.473             17.6                           0.229               -0.18             -0.055                                 ok           False                  False
  ADBE           88.89               36            0.93              1.57        240.61                44.30         0.489 below_threshold              0.565             35.2                           0.314               -3.97             -0.375                                 ok           False                  False
  GILD           94.44               18            1.12              1.15        147.01                19.81         0.485 below_threshold              0.517              9.9                           0.152               -2.83             -0.257 downtrend_blocked_slope_and_streak           False                  False
   ADP           80.00               10            1.55              2.86        262.73                23.86         0.485 below_threshold              0.065              5.5                           0.133               -4.18             -0.413 downtrend_blocked_slope_and_streak           False                  False
  VRSK           83.33               30            1.33              1.57        167.71                37.65         0.482 below_threshold              0.282              3.8                           0.123               -5.29             -0.458 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-02T10:40:04.819800-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "CEG261120C00260000", "current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "entry_ask": 16.1, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 15.5, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 433.0, "option_spread_pct": 7.74, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.898, "shadow_only": true, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.898, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-02T10:35:05.826835-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:30:04.822821-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:25:06.818366-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:20:07.304982-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:15:06.003196-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:10:02.761986-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002104004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002104004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002104004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002104004)

</details>
