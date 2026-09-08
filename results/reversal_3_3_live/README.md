# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 10:45:04 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$77,148.10`
- Equity: `$77,148.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           82.61               23            2.25              3.35        211.66                91.63         0.648          pass              0.334             37.7                           0.531                9.25              1.036                                 ok            True                  False
   KHC          100.00               13            0.51              0.09         24.81                29.15         0.622          pass              0.711             76.2                           0.767               -2.15              0.045                                 ok            True                  False
   WMT           88.24               17            1.23              0.92        106.75                40.24         0.607          pass              0.357              9.9                           0.257               -0.62              0.221                                 ok            True                  False
  MELI          100.00               15            2.06             28.50       1966.15                45.80         0.590          pass              0.540             15.8                           0.128               -0.53              0.067                                 ok            True                  False
  REGN          100.00               10            1.58              9.16        823.79                29.02         0.535          pass              0.615             53.7                           0.487               -1.67              0.122                                 ok            True                  False
  NVDA           89.29               28            1.32              2.13        229.45                44.80         0.526          pass              0.440              6.7                           0.121                9.04              0.882                                 ok            True                  False
  CHTR           90.00               20            2.79              2.97        150.72                60.37         0.512          pass              0.403              6.2                           0.202               -1.70             -0.116                                 ok            True                  False
  UPRO           85.71               21            1.32              1.41        151.28                24.27         0.500          pass              0.338             20.7                           0.387                0.87              0.080                                 ok            True                  False
  PYPL           80.00                5            3.04              1.17         54.46                57.43         0.597          pass              0.068              2.6                           0.121              -13.39             -1.563 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.00               25            3.75              3.75        141.19               102.15         0.566          pass              0.240             27.9                           0.308               12.09              1.175                                 ok           False                  False
  CPRT           87.50                8            2.80              0.66         33.44                42.28         0.550          pass              0.258              1.0                           0.196               -1.46              0.002                                 ok           False                  False
  PANW           86.05               43            0.67              1.57        332.59                70.93         0.549          pass              0.632             71.8                           0.775               -5.67             -0.699            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-09-08T10:45:04.455818-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:40:01.518522-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:35:01.536075-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:30:03.470274-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.61, "early_entry_score": 0.722, "early_reclaim_pct": 89.0, "entry_ask": 20.8, "entry_bid": 18.9, "entry_mode": "early", "entry_option_price": 19.85, "hypothetical_budget": 38574.05, "hypothetical_contracts": 19, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 9.57, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.722, "early_reclaim_pct": 89.0, "matched_signals": 36, "recovery_stability_score": 0.567, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:25:01.519959-04:00 early_entry_1025 early_entry_shadow      {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.61, "early_entry_score": 0.764, "early_reclaim_pct": 84.3, "entry_ask": 8.4, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 7.3, "hypothetical_budget": 38574.05, "hypothetical_contracts": 52, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 30.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.764, "early_reclaim_pct": 84.3, "matched_signals": 40, "recovery_stability_score": 0.605, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.44, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.739, "early_reclaim_pct": 90.0, "matched_signals": 37, "recovery_stability_score": 0.611, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:20:01.549867-04:00 early_entry_1020 early_entry_shadow   {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 81.0, "entry_ask": 8.5, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 7.35, "hypothetical_budget": 38574.05, "hypothetical_contracts": 52, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 31.29, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.624, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 81.0, "matched_signals": 40, "recovery_stability_score": 0.624, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.432, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 86.2, "matched_signals": 36, "recovery_stability_score": 0.629, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:15:05.512277-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:10:03.508736-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.56, "early_entry_score": 0.785, "early_reclaim_pct": 85.6, "entry_ask": 7.9, "entry_bid": 4.9, "entry_mode": "early", "entry_option_price": 6.4, "hypothetical_budget": 38574.05, "hypothetical_contracts": 60, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 46.88, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.851, "shadow_only": true, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.785, "early_reclaim_pct": 85.6, "matched_signals": 43, "recovery_stability_score": 0.851, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "trend_health_status": "ok"}, {"current_drop_pct": 0.94, "early_entry_score": 0.775, "early_reclaim_pct": 61.7, "matched_signals": 30, "recovery_stability_score": 0.739, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.567, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:05:01.504433-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "MELI261023C01970000", "current_drop_pct": 0.58, "early_entry_score": 0.839, "early_reclaim_pct": 76.1, "entry_ask": 104.9, "entry_bid": 84.2, "entry_mode": "early", "entry_option_price": 94.55, "hypothetical_budget": 38574.05, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.89, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.57, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.839, "early_reclaim_pct": 76.1, "matched_signals": 33, "recovery_stability_score": 0.768, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.57, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.796, "early_reclaim_pct": 85.9, "matched_signals": 45, "recovery_stability_score": 0.846, "success_rate": 91.11, "ticker": "INSM", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:00:06.216987-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908104504)

</details>
