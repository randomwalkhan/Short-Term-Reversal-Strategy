# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 12:15:01 EDT`
Last processed slot: `manual`

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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            1.04              0.78        107.16                39.87         0.577            pass              0.208             17.0                           0.338                0.27              0.068                                 ok            True                  False
   TRI           92.00               25            1.63              1.15        100.82                57.96         0.577            pass              0.543             21.8                           0.364               -5.87             -0.584 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.11              0.20        250.41                47.92         0.539            pass              0.924             94.4                           0.571              -10.57             -1.029 downtrend_blocked_slope_and_streak           False                  False
  ADSK           83.33               30            1.17              1.81        219.54                56.33         0.535            pass              0.378             34.0                           0.266               -9.93             -0.480 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.88               32            0.05              0.09        273.15                24.48         0.511            pass              0.889             97.0                           0.713               -2.26             -0.123                                 ok           False                  False
   PEP           88.24               17            0.65              0.61        134.08                14.34         0.506            pass              0.432             38.3                           0.512               -4.00             -0.371            downtrend_blocked_slope           False                  False
  CTSH          100.00               37            0.44              0.19         61.77                43.69         0.503            pass              0.831             67.1                           0.599               -2.87             -0.100                                 ok           False                  False
 CMCSA           92.31               13            2.25              0.37         23.57                34.54         0.493 below_threshold              0.397              0.0                           0.175              -13.48             -1.383 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               42            0.17              0.38        317.97                44.10         0.491 below_threshold              0.914             88.4                           0.509               -7.39             -0.531 downtrend_blocked_slope_and_streak           False                  False
  VRSK           77.78                9            2.90              3.69        180.17                41.00         0.487 below_threshold              0.096             15.6                           0.397               -5.95             -0.413            downtrend_blocked_slope           False                  False
  PAYX           87.10               31            0.39              0.32        116.58                25.45         0.486 below_threshold              0.588             70.0                           0.592               -6.23             -0.589            downtrend_blocked_slope           False                  False
  NFLX           86.67               30            1.00              0.54         76.18                36.27         0.482 below_threshold              0.439             26.4                           0.356               -8.56             -0.607 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-17T12:00:02.509358-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:55:04.328741-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:50:05.315984-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:45:05.877889-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:40:01.171788-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:35:02.981434-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:30:02.332975-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "CTSH261016C00060000", "current_drop_pct": 0.52, "early_entry_score": 0.801, "early_reclaim_pct": 61.0, "entry_ask": 3.9, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.7, "hypothetical_budget": 32655.65, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 756.0, "option_spread_pct": 10.81, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.801, "early_reclaim_pct": 61.0, "matched_signals": 35, "recovery_stability_score": 0.604, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-17T11:25:02.294340-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:20:05.657470-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:15:04.369387-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917121501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917121501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917121501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917121501)

</details>
