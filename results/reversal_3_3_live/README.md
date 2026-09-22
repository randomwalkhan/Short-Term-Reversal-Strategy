# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 10:10:05 EDT`
Last processed slot: `manage_1000`

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
  CRWD           88.37               43            0.65              1.13        248.86                96.94         0.660            pass              0.684             65.1                           0.533               17.96              2.102                       ok            True                  False
  PANW           80.49               41            0.98              2.55        370.67                79.39         0.564            pass              0.436             55.5                           0.533                9.24              1.208                       ok            True                  False
  WDAY           93.55               31            1.15              1.54        191.26                50.40         0.517            pass              0.599             15.2                           0.111                1.85              0.420                       ok            True                  False
  TEAM          100.00               18            3.26              4.47        193.75                58.22         0.514            pass              0.517              4.1                           0.092                7.29              0.966                       ok            True                  False
  FTNT           83.33               24            2.11              2.59        174.12                58.27         0.511            pass              0.311             25.9                           0.243                8.93              1.157                       ok            True                  False
   WBD           93.33               45            0.00              0.00         30.80                38.22         0.525            pass              0.908            100.0                           0.581                9.53              0.745                       ok           False                  False
  MSFT           96.30               27            0.71              2.48        500.55                22.55         0.494 below_threshold              0.677             38.0                           0.321                0.83              0.098                       ok           False                  False
  ADBE           96.15               26            1.67              2.92        248.27                45.94         0.486 below_threshold              0.765             69.8                           0.335               -4.63             -0.341  downtrend_blocked_slope           False                  False
  VRSK           92.31               39            0.10              0.12        171.97                39.65         0.463 below_threshold              0.863             98.4                           0.586               -1.81             -0.213 downtrend_blocked_streak           False                  False
  MELI           90.00               40            0.35              4.42       1818.57                29.69         0.446 below_threshold              0.562             16.9                           0.097               -5.82             -0.658  downtrend_blocked_slope           False                  False
  ADSK           83.87               31            1.08              1.66        218.14                55.48         0.429 below_threshold              0.328             13.8                           0.093                2.01              0.385                       ok           False                  False
  DXCM           91.11               45            0.09              0.06         89.15                24.75         0.427 below_threshold              0.818             93.2                           0.472                5.39              0.745                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-22T10:10:05.106762-04:00 early_entry_1010      early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "entry_ask": 7.35, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 6.375, "hypothetical_budget": 35735.4, "hypothetical_contracts": 56, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 30.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "matched_signals": 31, "recovery_stability_score": 0.747, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:05:08.595270-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:00:06.196250-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "entry_ask": 7.35, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 6.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 57, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 36.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "matched_signals": 31, "recovery_stability_score": 0.659, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T09:20:04.200203-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-21T15:10:05.959722-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
2026-09-21T14:50:06.827514-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-21", "training_samples": 5798, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922101005)

</details>
