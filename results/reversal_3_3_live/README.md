# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 15:05:04 EDT`
Last processed slot: `entry_1500`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               10            1.37              0.23         24.27                22.03         0.526            pass              0.348              9.5                           0.261               -3.47             -0.165                                 ok            True                  False
  WDAY           93.55               31            1.13              1.52        191.27                50.40         0.511            pass              0.698             48.5                           0.327                1.87              0.421                                 ok            True                  False
  FTNT           90.00               40            0.81              0.99        174.81                58.27         0.503            pass              0.732             71.6                           0.472               10.38              1.217                                 ok            True                  False
  CRWD           88.64               44            0.41              0.71        249.05                96.94         0.668            pass              0.732             78.2                           0.488               18.25              2.114                                 ok           False                  False
   TRI           94.44               36            0.13              0.08         95.39                58.54         0.588            pass              0.896             93.0                           0.810               -3.54             -0.261 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               15            3.54              4.85        193.59                58.22         0.498 below_threshold              0.577             31.3                           0.327                6.98              0.953                                 ok           False                  False
  MSFT           96.30               27            0.64              2.25        500.65                22.55         0.494 below_threshold              0.742             59.6                           0.646                0.90              0.101                                 ok           False                  False
  VRSK           92.31               39            0.09              0.11        171.97                39.65         0.463 below_threshold              0.864             98.6                           0.629               -1.80             -0.212           downtrend_blocked_streak           False                  False
  ADBE           83.33                6            4.40              7.69        246.23                45.94         0.426 below_threshold              0.193             20.4                           0.194               -7.28             -0.469            downtrend_blocked_slope           False                  False
  AMZN           72.00               25            1.30              2.35        257.44                26.96         0.406 below_threshold              0.334             64.4                           0.441               -0.73              0.005                                 ok           False                  False
   BKR           83.33               12            1.66              0.67         57.54                31.14         0.405 below_threshold              0.214             23.8                           0.243              -11.03             -1.066 downtrend_blocked_slope_and_streak           False                  False
  TTWO           78.26               23            1.77              2.60        208.80                37.71         0.389 below_threshold              0.227             33.8                           0.458               -3.32             -0.411 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-22T15:05:04.283152-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.689, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 24.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.507}
2026-09-22T14:50:01.294026-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
2026-09-22T12:00:04.192622-04:00 early_entry_1200      early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.559, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:55:04.534124-04:00 early_entry_1155      early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:50:04.129679-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.25, "hypothetical_budget": 35735.4, "hypothetical_contracts": 25, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.23, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922150504)

</details>
