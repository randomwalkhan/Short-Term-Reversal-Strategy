# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 11:20:02 EDT`
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
  AMGN          100.00               20            0.72              2.20        436.05                27.65         0.579          pass              0.661             45.6                           0.550                5.10              0.544                      ok            True                  False
  FAST          100.00               12            1.30              0.47         50.94                21.07         0.551          pass              0.532             21.3                           0.315               -1.08             -0.091                      ok            True                  False
  REGN          100.00               11            1.50              8.48        804.08                24.94         0.539          pass              0.624             54.5                           0.320               -0.87             -0.026                      ok            True                  False
  VRTX           97.14               35            0.51              1.97        546.71                32.96         0.516          pass              0.827             69.5                           0.552                7.71              0.668                      ok            True                   True
  CSCO           87.18               39            0.66              0.52        111.93                41.41         0.516          pass              0.603             55.7                           0.710               -0.24             -0.002                      ok            True                  False
  NVDA           88.00               25            1.82              2.91        226.73                42.92         0.507          pass              0.400             12.1                           0.190               -0.60             -0.181                      ok            True                  False
  MNST           94.12               34            0.36              0.12         46.65               551.83         1.000          pass              0.780             47.7                           0.511               -0.62              0.166                      ok           False                  False
  INSM           71.43               14            2.87              2.44        120.34               110.68         0.766          pass              0.157             17.8                           0.207               -4.72             -0.614 downtrend_blocked_slope           False                  False
  DRAM           75.68               37            0.11              0.04         56.81                68.22         0.615          pass              0.533             97.1                           0.724               -0.96             -0.219                      ok           False                  False
  MCHP           88.89               27            1.58              0.83         75.13                63.59         0.613          pass              0.478             22.2                           0.235               -5.59             -0.684 downtrend_blocked_slope           False                  False
   STX           86.11               36            0.53              3.17        845.84                71.05         0.598          pass              0.632             78.7                           0.392              -13.43             -1.504 downtrend_blocked_slope           False                  False
  SOXL           78.12               32            3.88              3.34        121.62               111.92         0.566          pass              0.284             27.0                           0.235              -18.40             -2.123 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-08-28T11:20:02.016207-04:00 early_entry_1120 early_entry_shadow             {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "entry_ask": 18.4, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 5.3, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.815, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.815, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.827, "early_reclaim_pct": 69.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:15:03.127521-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "entry_ask": 18.3, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.875, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 4.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "matched_signals": 39, "recovery_stability_score": 0.826, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:10:06.058739-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:05:02.171965-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:00:04.200311-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "CDNS261016C00345000", "current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "entry_ask": 19.2, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 17.0, "option_spread_pct": 18.18, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.754, "shadow_only": true, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "matched_signals": 41, "recovery_stability_score": 0.754, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.68, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:55:06.098266-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NVDA261016C00225000", "current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "entry_ask": 11.8, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.775, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 17410.0, "option_spread_pct": 0.42, "option_volume": 1301.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-28T10:50:01.894913-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:45:05.072825-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:40:06.289047-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "entry_ask": 27.4, "entry_bid": 25.5, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 7.18, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "matched_signals": 35, "recovery_stability_score": 0.642, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:35:02.085142-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828112002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828112002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828112002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828112002)

</details>
