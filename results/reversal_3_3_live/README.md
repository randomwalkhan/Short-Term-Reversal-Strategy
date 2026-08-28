# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 10:55:06 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               18            0.82              2.51        435.91                27.65         0.588          pass              0.593             26.9                           0.320                4.99              0.539                      ok            True                  False
  FAST          100.00               12            1.30              0.47         50.94                21.07         0.551          pass              0.532             21.3                           0.326               -1.08             -0.091                      ok            True                  False
  REGN          100.00               11            1.53              8.65        804.00                24.94         0.537          pass              0.621             53.6                           0.281               -0.90             -0.027                      ok            True                  False
  CSCO           84.85               33            0.93              0.73        111.84                41.41         0.535          pass              0.449             37.7                           0.658               -0.51             -0.015                      ok            True                  False
  GILD          100.00               17            1.73              1.80        148.09                26.47         0.521          pass              0.514              5.2                           0.226                5.73              0.627                      ok            True                  False
  NVDA           88.89               36            0.50              0.80        227.64                42.92         0.520          pass              0.689             75.7                           0.819                0.74             -0.121                      ok            True                   True
  VRTX           96.97               33            0.69              2.65        546.41                32.96         0.518          pass              0.782             58.9                           0.382                7.52              0.660                      ok            True                  False
  MNST           94.12               34            0.39              0.13         46.65               551.83         1.000          pass              0.770             44.6                           0.421               -0.64              0.165                      ok           False                  False
  INSM           73.33               15            2.35              1.99        120.54               110.68         0.786          pass              0.210             32.8                           0.425               -4.20             -0.590 downtrend_blocked_slope           False                  False
  SOXL           78.79               33            2.99              2.58        121.94               111.92         0.615          pass              0.346             43.6                           0.572              -17.65             -2.082 downtrend_blocked_slope           False                  False
  MCHP           86.21               29            1.39              0.73         75.18                63.59         0.608          pass              0.447             31.4                           0.432               -5.41             -0.675 downtrend_blocked_slope           False                  False
   STX           86.11               36            0.50              2.94        845.94                71.05         0.601          pass              0.637             80.2                           0.461              -13.40             -1.502 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-08-28T10:55:06.098266-04:00 early_entry_1055 early_entry_shadow                               {"contract_symbol": "NVDA261016C00225000", "current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "entry_ask": 11.8, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.775, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 17410.0, "option_spread_pct": 0.42, "option_volume": 1301.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-28T10:50:01.894913-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:45:05.072825-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:40:06.289047-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "entry_ask": 27.4, "entry_bid": 25.5, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 7.18, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "matched_signals": 35, "recovery_stability_score": 0.642, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:35:02.085142-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:30:04.053969-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:25:02.074094-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:20:02.098332-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:15:03.828658-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:10:03.076583-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828105506)

</details>
