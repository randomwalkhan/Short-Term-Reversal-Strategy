# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-20 11:31:08 EDT`
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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           97.44               39            0.67              0.69        146.29                84.09         0.674          pass              0.841             60.2                           0.573               -1.25             -0.359                                 ok            True                   True
   KHC           85.19               27            0.56              0.10         25.64                39.84         0.563          pass              0.490             60.8                           0.672                2.30              0.186                                 ok            True                  False
  UPRO           84.00               25            0.97              1.04        151.72                40.33         0.558          pass              0.410             49.1                           0.464               -1.15             -0.164                                 ok            True                  False
 CMCSA           91.67               24            0.77              0.14         26.53                43.42         0.548          pass              0.578             39.6                           0.466                4.83              0.512                                 ok            True                  False
   BKR           85.71               14            1.57              0.71         64.18                32.39         0.543          pass              0.311             25.7                           0.302                1.52              0.263                                 ok            True                  False
  BKNG           97.14               35            0.78              1.16        212.50                45.88         0.534          pass              0.722             33.9                           0.446                1.90             -0.070                                 ok            True                  False
  ISRG           80.95               21            1.27              3.54        396.20                37.69         0.534          pass              0.276             41.1                           0.565                5.07              0.321                                 ok            True                  False
   WBD           90.48               21            0.81              0.16         28.46                19.61         0.532          pass              0.480             24.6                           0.265                7.20              0.773                                 ok            True                  False
  TMUS           89.19               37            0.60              0.77        182.03                55.86         0.507          pass              0.578             34.0                           0.353                0.72              0.249                                 ok            True                  False
  ALNY           66.67                9            3.59              6.10        240.00               130.07         0.795          pass              0.108              9.4                           0.287                8.23              0.917                                 ok           False                  False
  INSM           73.33               15            2.40              2.19        129.72               109.27         0.774          pass              0.190             26.3                           0.550               -3.79             -0.438 downtrend_blocked_slope_and_streak           False                  False
  TEAM           85.00               40            0.11              0.13        174.17               121.79         0.771          pass              0.692             93.7                           0.695               57.97              2.928                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-20T11:31:08.330243-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "SHOP261016C00145000", "current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "entry_ask": 11.45, "entry_bid": 10.35, "entry_mode": "early", "entry_option_price": 10.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 617.0, "option_spread_pct": 10.09, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.573, "shadow_only": true, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "matched_signals": 39, "recovery_stability_score": 0.573, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 32, "recovery_stability_score": 0.782, "success_rate": 96.88, "ticker": "VRTX", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-20T10:57:29.950425-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "entry_ask": 14.4, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 13.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 215.0, "option_spread_pct": 7.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "matched_signals": 33, "recovery_stability_score": 0.636, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T10:38:39.121946-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-20T10:19:19.114673-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "entry_ask": 26.9, "entry_bid": 24.1, "entry_mode": "early", "entry_option_price": 25.5, "hypothetical_budget": 26569.0, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 92.0, "option_spread_pct": 10.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "matched_signals": 30, "recovery_stability_score": 0.605, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T09:18:16.446091-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-19T11:30:46.509801-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-19T10:58:16.376316-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                {"contract_symbol": "ZS260918C00185000", "current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "entry_ask": 15.8, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 26569.0, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1626.0, "option_spread_pct": 4.53, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "matched_signals": 41, "recovery_stability_score": 0.774, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-19T10:25:26.675121-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T12:30:08.738941-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260820113108)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260820113108)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260820113108)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260820113108)

</details>
