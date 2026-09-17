# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 13:35:01 EDT`
Last processed slot: `manage_1330`

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
  PANW           81.40               43            0.52              1.36        375.07                80.65         0.576            pass              0.556             87.1                           0.540               13.77              1.536                                 ok            True                  False
   WMT           83.33               30            0.70              0.53        107.27                39.87         0.548            pass              0.409             44.1                           0.588                0.62              0.084                                 ok            True                  False
   TRI           90.91               22            1.94              1.38        100.72                57.96         0.573            pass              0.483             18.1                           0.334               -6.16             -0.598 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.85               33            0.70              1.09        219.84                56.33         0.547            pass              0.518             60.4                           0.694               -9.50             -0.459 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               17            0.52              0.49        134.13                14.34         0.514            pass              0.468             50.0                           0.496               -3.88             -0.365            downtrend_blocked_slope           False                  False
   ADP           96.67               30            0.25              0.48        272.99                24.48         0.510            pass              0.838             84.5                           0.653               -2.46             -0.133                                 ok           False                  False
  CTSH          100.00               38            0.31              0.13         61.79                43.69         0.504            pass              0.868             76.8                           0.684               -2.74             -0.095                                 ok           False                  False
  NFLX           89.66               29            1.03              0.55         76.17                36.27         0.491 below_threshold              0.507             24.5                           0.289               -8.59             -0.608 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           92.31               13            2.25              0.37         23.57                34.54         0.491 below_threshold              0.436             13.0                           0.392              -13.48             -1.383 downtrend_blocked_slope_and_streak           False                  False
  VRSK           80.00               10            2.80              3.56        180.22                41.00         0.490 below_threshold              0.105             18.5                           0.273               -5.86             -0.409            downtrend_blocked_slope           False                  False
  INTU          100.00               40            0.36              0.80        317.79                44.10         0.489 below_threshold              0.887             79.3                           0.599               -7.57             -0.540 downtrend_blocked_slope_and_streak           False                  False
  PAYX           87.50               32            0.31              0.26        116.61                25.45         0.485 below_threshold              0.622             75.7                           0.685               -6.17             -0.586            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917133501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917133501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917133501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917133501)

</details>
