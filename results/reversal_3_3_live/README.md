# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 11:25:02 EDT`
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
  AMGN          100.00               20            0.71              2.18        436.06                27.65         0.580          pass              0.663             46.1                           0.588                5.11              0.544                      ok            True                  False
  FAST          100.00               12            1.36              0.49         50.93                21.07         0.548          pass              0.521             17.8                           0.302               -1.14             -0.094                      ok            True                  False
  REGN          100.00               10            1.56              8.85        803.92                24.94         0.541          pass              0.612             52.5                           0.351               -0.93             -0.029                      ok            True                  False
  CSCO           86.11               36            0.73              0.57        111.90                41.41         0.529          pass              0.542             50.9                           0.685               -0.31             -0.006                      ok            True                  False
  GILD          100.00               18            1.69              1.76        148.11                26.47         0.515          pass              0.547             14.0                           0.286                5.77              0.629                      ok            True                  False
  VRTX           97.14               35            0.62              2.39        546.52                32.96         0.509          pass              0.806             62.9                           0.460                7.59              0.663                      ok            True                  False
  NVDA           88.00               25            1.79              2.86        226.75                42.92         0.509          pass              0.405             13.5                           0.164               -0.56             -0.180                      ok            True                  False
    ZS           95.24               42            0.54              0.71        187.00                58.32         0.502          pass              0.897             82.2                           0.888                1.47             -0.275                      ok            True                   True
  MNST           91.67               36            0.33              0.11         46.65               551.83         1.000          pass              0.741             52.3                           0.543               -0.59              0.167                      ok           False                  False
  INSM           71.43               14            2.88              2.45        120.34               110.68         0.765          pass              0.156             17.5                           0.192               -4.73             -0.615 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.23              0.09         56.79                68.22         0.616          pass              0.516             93.7                           0.699               -1.08             -0.225                      ok           False                  False
  MCHP           88.89               27            1.68              0.89         75.11                63.59         0.607          pass              0.462             17.0                           0.210               -5.69             -0.689 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-08-28T11:25:02.223727-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ZS261002C00187500", "current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "entry_ask": 15.85, "entry_bid": 13.5, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 26394.05, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 16.01, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.888, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "matched_signals": 42, "recovery_stability_score": 0.888, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:20:02.016207-04:00 early_entry_1120 early_entry_shadow             {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "entry_ask": 18.4, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 5.3, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.815, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.815, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.827, "early_reclaim_pct": 69.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:15:03.127521-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "entry_ask": 18.3, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.875, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 4.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "matched_signals": 39, "recovery_stability_score": 0.826, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:10:06.058739-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:05:02.171965-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:00:04.200311-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "CDNS261016C00345000", "current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "entry_ask": 19.2, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 17.0, "option_spread_pct": 18.18, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.754, "shadow_only": true, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "matched_signals": 41, "recovery_stability_score": 0.754, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.68, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:55:06.098266-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NVDA261016C00225000", "current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "entry_ask": 11.8, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.775, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 17410.0, "option_spread_pct": 0.42, "option_volume": 1301.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-28T10:50:01.894913-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:45:05.072825-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:40:06.289047-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "entry_ask": 27.4, "entry_bid": 25.5, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 7.18, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "matched_signals": 35, "recovery_stability_score": 0.642, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828112502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828112502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828112502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828112502)

</details>
