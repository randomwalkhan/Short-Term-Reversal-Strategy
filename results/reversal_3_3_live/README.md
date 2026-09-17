# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 14:00:03 EDT`
Last processed slot: `manage_1400`

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
   WMT           84.38               32            0.68              0.51        107.28                39.87         0.538            pass              0.454             45.6                           0.557                0.64              0.084                                 ok            True                  False
  PANW           82.22               45            0.27              0.70        375.35                80.65         0.580            pass              0.597             93.3                           0.697               14.06              1.547                                 ok           False                  False
   TRI           91.67               24            1.80              1.27        100.76                57.96         0.571            pass              0.534             24.2                           0.479               -6.03             -0.592 downtrend_blocked_slope_and_streak           False                  False
  ADSK           85.71               35            0.65              1.00        219.88                56.33         0.539            pass              0.563             63.3                           0.742               -9.45             -0.456 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00               38            0.06              0.02         61.84                43.69         0.519            pass              0.926             95.7                           0.817               -2.50             -0.083                                 ok           False                  False
   PEP           88.89               18            0.45              0.42        134.16                14.34         0.514            pass              0.514             57.4                           0.700               -3.81             -0.361            downtrend_blocked_slope           False                  False
   ADP           96.55               29            0.29              0.56        272.95                24.48         0.513            pass              0.823             81.7                           0.601               -2.50             -0.135                                 ok           False                  False
 CMCSA           91.67               12            2.28              0.38         23.57                34.54         0.495 below_threshold              0.411             12.2                           0.390              -13.50             -1.384 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               42            0.12              0.28        318.01                44.10         0.491 below_threshold              0.928             92.9                           0.817               -7.35             -0.529 downtrend_blocked_slope_and_streak           False                  False
  VRSK           80.00               10            2.80              3.57        180.22                41.00         0.489 below_threshold              0.104             18.3                           0.311               -5.86             -0.409            downtrend_blocked_slope           False                  False
  NFLX           87.10               31            0.84              0.45         76.22                36.27         0.487 below_threshold              0.493             38.5                           0.521               -8.41             -0.600 downtrend_blocked_slope_and_streak           False                  False
  PAYX           87.50               32            0.31              0.25        116.61                25.45         0.485 below_threshold              0.623             76.0                           0.665               -6.16             -0.585            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917140003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917140003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917140003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917140003)

</details>
