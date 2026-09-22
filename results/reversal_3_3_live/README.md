# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 10:15:09 EDT`
Last processed slot: `early_entry_1015`

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
  PANW           80.49               41            0.86              2.23        370.81                79.39         0.572            pass              0.454             61.1                           0.581                9.38              1.213                       ok            True                  False
  TEAM          100.00               18            3.02              4.13        193.90                58.22         0.528            pass              0.540             11.3                           0.192                7.56              0.977                       ok            True                  False
  WDAY           93.55               31            1.00              1.34        191.35                50.40         0.527            pass              0.633             26.2                           0.187                2.00              0.427                       ok            True                  False
  FTNT           84.00               25            2.04              2.50        174.16                58.27         0.510            pass              0.343             28.5                           0.326                9.01              1.160                       ok            True                  False
  CRWD           88.64               44            0.39              0.69        249.06                96.94         0.669            pass              0.734             78.9                           0.748               18.26              2.114                       ok           False                  False
  ADBE           96.15               26            1.63              2.84        248.30                45.94         0.489 below_threshold              0.767             70.6                           0.339               -4.59             -0.339  downtrend_blocked_slope           False                  False
  MSFT           93.75               32            0.40              1.41        501.01                22.55         0.480 below_threshold              0.756             64.8                           0.493                1.14              0.112                       ok           False                  False
  VRSK           92.31               39            0.07              0.08        171.99                39.65         0.465 below_threshold              0.865             98.9                           0.569               -1.78             -0.212 downtrend_blocked_streak           False                  False
  MELI           89.74               39            0.44              5.58       1818.08                29.69         0.445 below_threshold              0.515              5.9                           0.116               -5.91             -0.662  downtrend_blocked_slope           False                  False
  ADSK           84.38               32            0.94              1.43        218.24                55.48         0.432 below_threshold              0.383             25.5                           0.129                2.16              0.392                       ok           False                  False
  DXCM           91.11               45            0.11              0.07         89.14                24.75         0.425 below_threshold              0.813             91.5                           0.461                5.37              0.744                       ok           False                  False
  GILD           95.00               20            0.90              0.95        150.15                21.02         0.419 below_threshold              0.785             92.2                           0.603                2.32              0.470                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-22T10:15:09.621740-04:00 early_entry_1015      early_entry_shadow                                {"contract_symbol": "ZS261030C00205000", "current_drop_pct": 0.98, "early_entry_score": 0.897, "early_reclaim_pct": 96.2, "entry_ask": 15.75, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 259.0, "option_spread_pct": 13.56, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.897, "early_reclaim_pct": 96.2, "matched_signals": 35, "recovery_stability_score": 0.637, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:10:05.106762-04:00 early_entry_1010      early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "entry_ask": 7.35, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 6.375, "hypothetical_budget": 35735.4, "hypothetical_contracts": 56, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 30.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.825, "early_reclaim_pct": 95.5, "matched_signals": 31, "recovery_stability_score": 0.747, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.375, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:05:08.595270-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:00:06.196250-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "GILD261030C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "entry_ask": 7.35, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 6.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 57, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 36.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.825, "early_reclaim_pct": 95.3, "matched_signals": 31, "recovery_stability_score": 0.659, "success_rate": 93.55, "ticker": "GILD", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T09:20:04.200203-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-21T15:10:05.959722-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922101509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922101509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922101509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922101509)

</details>
