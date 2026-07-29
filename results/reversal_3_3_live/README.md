# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:25:04 EDT`
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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               15            0.98              0.33         47.96                27.18         0.583            pass              0.637             48.4                           0.532                4.70              0.470                                 ok            True                  False
  GILD           88.00               25            0.77              0.72        134.01                34.28         0.522            pass              0.486             40.1                           0.325                2.50             -0.028                                 ok            True                  False
   HON           80.00               15            1.57              2.71        245.89                39.75         0.521            pass              0.124             12.8                           0.217                9.21              1.150                                 ok            True                  False
   MAR          100.00               34            0.51              1.37        382.93                28.18         0.500 below_threshold              0.833             74.4                           0.655                5.06              0.417                                 ok            True                   True
  ISRG           72.73               22            1.40              3.55        360.28                72.57         0.645            pass              0.272             42.5                           0.308               -8.29             -0.887                                 ok           False                  False
  META           90.00               30            0.91              3.79        591.79                53.87         0.603            pass              0.505             14.9                           0.228              -13.70             -1.531 downtrend_blocked_slope_and_streak           False                  False
   WDC           84.85               33            0.23              0.74        463.19                95.99         0.594            pass              0.632             96.7                           0.540              -10.00             -0.131           downtrend_blocked_streak           False                  False
  TMUS           90.91               33            0.45              0.58        182.14                56.22         0.580            pass              0.697             64.7                           0.406               -3.23             -0.866            downtrend_blocked_slope           False                  False
  MPWR           84.21               38            0.31              2.77       1280.82                58.32         0.532            pass              0.616             87.9                           0.529               -7.15             -0.226           downtrend_blocked_streak           False                  False
   XEL          100.00               30            0.12              0.07         80.30                19.80         0.530            pass              0.812             75.3                           0.479                0.07              0.141                                 ok           False                  False
  DRAM           77.78               27            2.47              0.83         47.42               100.66         0.517            pass              0.398             77.6                           0.451              -18.83             -1.253 downtrend_blocked_slope_and_streak           False                  False
  AVGO           79.31               29            1.18              3.15        379.56                41.80         0.499 below_threshold              0.281             34.9                           0.290               -4.53             -0.037                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-29T10:25:04.635109-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "entry_ask": 20.1, "entry_bid": 17.5, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 13.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.655, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:20:02.632182-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "entry_ask": 20.3, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1134.0, "option_spread_pct": 15.96, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "matched_signals": 32, "recovery_stability_score": 0.586, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.712, "early_reclaim_pct": 74.0, "matched_signals": 33, "recovery_stability_score": 0.574, "success_rate": 90.91, "ticker": "PCAR", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:15:01.489767-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:10:01.513835-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:05:02.493653-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T09:50:04.461343-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-29T09:30:03.798822-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-29T09:25:01.530149-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729102504)

</details>
