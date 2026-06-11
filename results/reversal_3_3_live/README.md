# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-11 14:45:04 EDT`
Last processed slot: `manual`

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

- Cash: `$28,725.75`
- Equity: `$28,725.75`
- Realized PnL: `$18,725.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CTSH     option         option CTSH260717C00055000     73          2026-06-09         2026-06-11         2.05       1.845 -1496.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               22            0.59              0.42        100.92                34.22         0.576            pass              0.763             75.1                           0.624                5.22              0.310                                 ok            True                  False
  INTU           72.73               22            2.52              5.00        282.08               101.53         0.683            pass              0.252             34.6                           0.261              -11.48             -1.761 downtrend_blocked_slope_and_streak           False                  False
   TRI           80.00               20            1.12              0.64         81.68                68.04         0.658            pass              0.323             63.3                           0.515               -4.08             -0.786 downtrend_blocked_slope_and_streak           False                  False
  CDNS           94.87               39            0.19              0.52        384.91                58.86         0.545            pass              0.922             92.6                           0.749                2.82             -0.107                                 ok           False                  False
  CTSH           89.66               29            1.00              0.36         51.65                46.99         0.514            pass              0.663             75.7                           0.571               -4.75             -0.775 downtrend_blocked_slope_and_streak           False                  False
  MSFT           40.00                5            2.38              6.63        394.52                36.94         0.505            pass              0.138             29.1                           0.352               -9.16             -1.401 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.00               25            3.34              2.14         90.62                86.53         0.497 below_threshold              0.481             39.2                           0.401               -5.16             -1.571 downtrend_blocked_slope_and_streak           False                  False
  WDAY           87.50               16            3.70              3.56        135.95                67.65         0.491 below_threshold              0.379             30.1                           0.289                1.83             -0.533                                 ok           False                  False
   ADP           97.30               37            0.45              0.73        230.79                32.69         0.489 below_threshold              0.860             77.1                           0.609                4.64              0.325                                 ok           False                  False
  SNPS           84.00               25            1.53              4.94        458.42                48.54         0.483 below_threshold              0.419             54.6                           0.543               -5.65             -0.727            downtrend_blocked_slope           False                  False
  CPRT           92.11               38            0.49              0.11         31.31                31.19         0.459 below_threshold              0.760             68.4                           0.499               -6.23             -0.521 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           93.94               33            0.51              0.23         64.08                18.57         0.456 below_threshold              0.727             52.2                           0.445                2.35              0.389                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-11T11:58:26.585033-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-11T11:22:14.657857-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "KDP260717C00031000", "current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "entry_ask": 1.45, "entry_bid": 1.1, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 14362.88, "hypothetical_contracts": 112, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 2194.0, "option_spread_pct": 27.45, "option_volume": 80.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "matched_signals": 32, "recovery_stability_score": 0.703, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-11T10:46:23.679160-04:00 early_entry_1045 early_entry_shadow                         {"contract_symbol": "CSCO260717C00120000", "current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "entry_ask": 4.8, "entry_bid": 4.55, "entry_mode": "early", "entry_option_price": 4.675, "hypothetical_budget": 14362.88, "hypothetical_contracts": 30, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 11268.0, "option_spread_pct": 5.35, "option_volume": 155.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.795, "early_reclaim_pct": 72.8, "matched_signals": 30, "recovery_stability_score": 0.78, "success_rate": 96.67, "ticker": "KDP", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-11T10:10:05.812920-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "entry_ask": 8.7, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 14362.88, "hypothetical_contracts": 19, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 261.0, "option_spread_pct": 33.56, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.778, "early_reclaim_pct": 70.9, "matched_signals": 39, "recovery_stability_score": 0.672, "success_rate": 92.31, "ticker": "ROP", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-11T10:10:05.812920-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "CTSH260717C00055000", "fill_price": 1.845, "pnl": -1496.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CTSH"}
2026-06-11T05:50:04.507646-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:45:04.534672-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:43:14.603904-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:25:01.583807-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:20:01.619276-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260611144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260611144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260611144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260611144504)

</details>
