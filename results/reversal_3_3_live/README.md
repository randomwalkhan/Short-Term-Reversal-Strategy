# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 10:20:05 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PANW           80.49               41            0.70              1.83        370.98                79.39         0.581            pass              0.475             68.1                           0.712                9.55              1.220                       ok            True                  False
  TEAM          100.00               18            3.10              4.25        193.85                58.22         0.523            pass              0.532              8.9                           0.162                7.47              0.973                       ok            True                  False
  WDAY           93.55               31            1.16              1.56        191.25                50.40         0.516            pass              0.595             14.1                           0.121                1.83              0.419                       ok            True                  False
  FTNT           84.62               26            2.02              2.48        174.17                58.27         0.506            pass              0.367             29.1                           0.370                9.03              1.161                       ok            True                  False
  CRWD           88.64               44            0.28              0.48        249.14                96.94         0.675            pass              0.753             85.1                           0.824               18.40              2.119                       ok           False                  False
  PYPL           92.86               42            0.00              0.00         52.62                57.19         0.498 below_threshold              0.893            100.0                           0.598               -1.05             -0.112                       ok           False                  False
  MSFT           96.15               26            0.73              2.58        500.51                22.55         0.498 below_threshold              0.663             35.6                           0.379                0.81              0.097                       ok           False                  False
  ADBE           96.00               25            1.84              3.21        248.14                45.94         0.481 below_threshold              0.748             66.7                           0.323               -4.79             -0.349  downtrend_blocked_slope           False                  False
  VRSK           92.31               39            0.05              0.06        171.99                39.65         0.466 below_threshold              0.866             99.2                           0.562               -1.76             -0.211 downtrend_blocked_streak           False                  False
  MELI           87.10               31            0.85             10.81       1815.84                29.69         0.459 below_threshold              0.376              0.2                           0.015               -6.29             -0.681  downtrend_blocked_slope           False                  False
  DXCM           90.91               33            0.72              0.45         88.98                24.75         0.458 below_threshold              0.626             45.3                           0.259                4.73              0.717                       ok           False                  False
  ADSK           84.38               32            1.00              1.53        218.20                55.48         0.429 below_threshold              0.368             20.7                           0.123                2.10              0.389                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-22T10:20:05.273245-04:00 early_entry_1020 early_entry_shadow                      {"contract_symbol": "ZS261030C00205000", "current_drop_pct": 0.63, "early_entry_score": 0.921, "early_reclaim_pct": 97.5, "entry_ask": 16.2, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.975, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 259.0, "option_spread_pct": 16.36, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.796, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.921, "early_reclaim_pct": 97.5, "matched_signals": 38, "recovery_stability_score": 0.796, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:15:09.621740-04:00 early_entry_1015 early_entry_shadow                                {"contract_symbol": "ZS261030C00205000", "current_drop_pct": 0.98, "early_entry_score": 0.897, "early_reclaim_pct": 96.2, "entry_ask": 15.75, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 259.0, "option_spread_pct": 13.56, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.897, "early_reclaim_pct": 96.2, "matched_signals": 35, "recovery_stability_score": 0.637, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:10:05.106762-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "entry_ask": 7.35, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 6.375, "hypothetical_budget": 35735.4, "hypothetical_contracts": 56, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 30.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "matched_signals": 31, "recovery_stability_score": 0.747, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:05:08.595270-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:00:06.196250-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "entry_ask": 7.35, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 6.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 57, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 36.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "matched_signals": 31, "recovery_stability_score": 0.659, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T09:20:04.200203-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-21T15:10:05.959722-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922102005)

</details>
