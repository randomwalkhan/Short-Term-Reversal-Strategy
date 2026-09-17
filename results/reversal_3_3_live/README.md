# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 13:20:06 EDT`
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
   WMT           83.33               30            0.72              0.54        107.27                39.87         0.546            pass              0.405             42.6                           0.572                0.60              0.083                                 ok            True                  False
  CTSH          100.00               35            0.57              0.25         61.74                43.69         0.507            pass              0.789             57.1                           0.477               -3.00             -0.106                                 ok            True                  False
  PANW           82.22               45            0.26              0.68        375.36                80.65         0.581            pass              0.598             93.5                           0.603               14.06              1.548                                 ok           False                  False
   TRI           88.89               18            2.31              1.64        100.61                57.96         0.573            pass              0.355              2.5                           0.169               -6.52             -0.616 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.12              0.21        250.41                47.92         0.538            pass              0.923             94.1                           0.751              -10.58             -1.029 downtrend_blocked_slope_and_streak           False                  False
  SNPS           85.42               48            0.18              0.47        378.27                63.01         0.535            pass              0.471             24.4                           0.213               -9.17             -1.012            downtrend_blocked_slope           False                  False
  ADSK           84.38               32            1.03              1.58        219.63                56.33         0.533            pass              0.443             42.2                           0.472               -9.80             -0.474 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.67               30            0.20              0.38        273.03                24.48         0.513            pass              0.848             87.7                           0.727               -2.41             -0.130                                 ok           False                  False
   PEP           88.24               17            0.60              0.56        134.10                14.34         0.509            pass              0.446             42.9                           0.407               -3.96             -0.368            downtrend_blocked_slope           False                  False
  INTU          100.00               34            0.75              1.67        317.42                44.10         0.502            pass              0.782             57.1                           0.500               -7.93             -0.558 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.89                9            2.44              0.41         23.56                34.54         0.499 below_threshold              0.304              5.7                           0.273              -13.65             -1.392 downtrend_blocked_slope_and_streak           False                  False
  VRSK           80.00               10            2.69              3.42        180.29                41.00         0.496 below_threshold              0.115             21.8                           0.410               -5.75             -0.403            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917132006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917132006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917132006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917132006)

</details>
