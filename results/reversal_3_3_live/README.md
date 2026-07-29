# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 10:30:04 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               13            1.16              0.39         47.93                27.18         0.583          pass              0.594             38.5                           0.492                4.51              0.461                                 ok            True                  False
  GILD           89.66               29            0.54              0.51        134.10                34.28         0.513          pass              0.608             57.6                           0.463                2.73             -0.018                                 ok            True                  False
   MAR          100.00               31            0.68              1.83        382.73                28.18         0.509          pass              0.788             65.8                           0.642                4.88              0.409                                 ok            True                   True
   HON           80.00               15            1.77              3.06        245.74                39.75         0.506          pass              0.105              7.0                           0.220                8.98              1.141                                 ok            True                  False
  AVGO           81.48               27            1.37              3.66        379.34                41.80         0.503          pass              0.276             24.3                           0.229               -4.72             -0.046                                 ok            True                  False
  ISRG           75.00               20            1.55              3.93        360.12                72.57         0.651          pass              0.241             36.3                           0.275               -8.43             -0.893                                 ok           False                  False
  META           91.67               36            0.68              2.84        592.19                53.87         0.580          pass              0.669             42.2                           0.360              -13.50             -1.521 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.91               33            0.47              0.61        182.13                56.22         0.579          pass              0.691             63.0                           0.455               -3.25             -0.867            downtrend_blocked_slope           False                  False
  MSTR           77.78               45            0.23              0.15         96.09                69.55         0.553          pass              0.479             74.7                           0.373               -1.57             -0.049                                 ok           False                  False
   XEL          100.00               25            0.32              0.18         80.25                19.80         0.551          pass              0.662             35.8                           0.305               -0.12              0.132                                 ok           False                  False
  ASML           95.24               21            2.15             23.85       1572.73                55.40         0.514          pass              0.662             45.9                           0.296              -14.56             -1.255 downtrend_blocked_slope_and_streak           False                  False
  MPWR           84.21               38            0.70              6.25       1279.33                58.32         0.506          pass              0.568             72.7                           0.400               -7.51             -0.244           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-29T10:30:04.319629-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "entry_ask": 20.1, "entry_bid": 17.9, "entry_mode": "early", "entry_option_price": 19.0, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 11.58, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "matched_signals": 31, "recovery_stability_score": 0.642, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:25:04.635109-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "entry_ask": 20.1, "entry_bid": 17.5, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 13.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.655, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:20:02.632182-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "entry_ask": 20.3, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.8, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1134.0, "option_spread_pct": 15.96, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.814, "early_reclaim_pct": 72.0, "matched_signals": 32, "recovery_stability_score": 0.586, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.51, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.712, "early_reclaim_pct": 74.0, "matched_signals": 33, "recovery_stability_score": 0.574, "success_rate": 90.91, "ticker": "PCAR", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:15:01.489767-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:10:01.513835-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:05:02.493653-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:00:06.571588-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T09:50:04.461343-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-29T09:30:03.798822-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729103004)

</details>
