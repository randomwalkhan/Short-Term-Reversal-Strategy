# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 11:25:05 EDT`
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.75               32            1.47              1.63        157.91               104.19         0.707            pass              0.742             52.6                           0.447               14.13              2.457                                 ok            True                  False
   CEG           82.35               17            1.77              3.27        261.87                41.90         0.535            pass              0.225             20.7                           0.278               -2.26              0.003                                 ok            True                  False
  SHOP           85.71               35            1.18              1.18        141.74                62.03         0.522            pass              0.583             70.7                           0.884                4.99              1.166                                 ok            True                  False
  PYPL           86.67               15            1.67              0.64         54.76                60.08         0.515            pass              0.431             56.2                           0.598                0.17              0.078                                 ok            True                  False
   ADI           87.50               24            1.06              2.91        392.35                35.26         0.506            pass              0.530             62.1                           0.414                7.87              0.951                                 ok            True                  False
  MSFT          100.00               17            1.39              5.02        514.02                25.07         0.504            pass              0.643             48.6                           0.718                0.71              0.229                                 ok            True                  False
   TRI           87.88               33            0.93              0.64         98.71                56.74         0.584            pass              0.611             63.1                           0.658               -7.32             -0.510 downtrend_blocked_slope_and_streak           False                  False
  ASML           84.21               38            0.10              1.17       1743.44                41.71         0.532            pass              0.639             95.7                           0.525               10.61              1.148                                 ok           False                  False
  UPRO          100.00                8            2.54              2.71        151.04                32.02         0.515            pass              0.494             14.3                           0.311                1.78              0.527                                 ok           False                  False
   KHC           96.00               25            0.15              0.02         23.62                20.56         0.498 below_threshold              0.791             80.4                           0.395               -2.78             -0.478 downtrend_blocked_slope_and_streak           False                  False
  LRCX           72.00               25            2.56              5.66        312.79                61.39         0.498 below_threshold              0.259             36.4                           0.290               12.42              1.761                                 ok           False                  False
  PAYX           82.61               23            1.08              0.76        101.04                37.87         0.494 below_threshold              0.373             55.7                           0.580              -15.38             -1.910 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T11:25:05.958568-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:20:06.180521-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:15:05.555577-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:10:06.397628-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:05:04.918839-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:00:06.419831-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:55:05.016465-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:50:06.030235-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:45:06.952611-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928112505)

</details>
