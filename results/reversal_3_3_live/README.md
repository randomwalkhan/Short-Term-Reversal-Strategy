# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-20 13:55:10 EDT`
Last processed slot: `manage_1400`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  WDAY           83.33               36            0.99              1.37        197.83                85.33         0.619          pass              0.463             46.2                           0.365               15.40              1.317                  ok            True                  False
  UPRO           86.67               15            1.74              1.86        151.36                40.33         0.576          pass              0.296              8.9                           0.186               -1.92             -0.200                  ok            True                  False
  MCHP           87.18               39            0.88              0.47         76.88                71.63         0.573          pass              0.599             52.5                           0.441                2.75             -0.349                  ok            True                  False
   KHC           85.19               27            0.60              0.11         25.63                39.84         0.561          pass              0.482             58.1                           0.473                2.26              0.184                  ok            True                  False
 CMCSA           90.00               20            0.96              0.18         26.51                43.42         0.559          pass              0.464             25.0                           0.302                4.63              0.503                  ok            True                  False
  FAST          100.00               14            1.17              0.42         51.26                21.74         0.557          pass              0.493              3.4                           0.133                0.08             -0.133                  ok            True                  False
  BKNG           96.97               33            0.93              1.39        212.40                45.88         0.536          pass              0.669             20.7                           0.279                1.75             -0.077                  ok            True                  False
   WBD           90.00               20            0.82              0.16         28.46                19.61         0.535          pass              0.485             32.9                           0.527                7.18              0.772                  ok            True                  False
   MAR           92.86               28            0.90              2.27        358.98                36.48         0.533          pass              0.635             39.6                           0.394               -0.83              0.134                  ok            True                  False
  TMUS           93.33               30            1.03              1.31        181.80                55.86         0.527          pass              0.572             10.1                           0.305                0.29              0.230                  ok            True                  False
  VRTX           90.00               10            2.23              8.61        548.37                32.17         0.518          pass              0.409             30.1                           0.207               11.51              0.822                  ok            True                  False
   BKR           81.82               11            2.20              0.99         64.05                32.39         0.514          pass              0.156             16.5                           0.370                0.86              0.234                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-20T11:40:03.908797-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "SHOP261016C00145000", "current_drop_pct": 0.62, "early_entry_score": 0.855, "early_reclaim_pct": 62.8, "entry_ask": 11.35, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.05, "hypothetical_budget": 26569.0, "hypothetical_contracts": 24, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 617.0, "option_spread_pct": 5.43, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 97.56, "ticker": "SHOP", "timing_score": 0.666, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.855, "early_reclaim_pct": 62.8, "matched_signals": 41, "recovery_stability_score": 0.651, "success_rate": 97.56, "ticker": "SHOP", "timing_score": 0.666, "trend_health_status": "ok"}, {"current_drop_pct": 0.74, "early_entry_score": 0.831, "early_reclaim_pct": 76.8, "matched_signals": 33, "recovery_stability_score": 0.748, "success_rate": 96.97, "ticker": "VRTX", "timing_score": 0.476, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-20T11:31:08.330243-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "SHOP261016C00145000", "current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "entry_ask": 11.45, "entry_bid": 10.35, "entry_mode": "early", "entry_option_price": 10.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 617.0, "option_spread_pct": 10.09, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.573, "shadow_only": true, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "matched_signals": 39, "recovery_stability_score": 0.573, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 32, "recovery_stability_score": 0.782, "success_rate": 96.88, "ticker": "VRTX", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-20T10:57:29.950425-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "entry_ask": 14.4, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 13.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 215.0, "option_spread_pct": 7.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "matched_signals": 33, "recovery_stability_score": 0.636, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T10:38:39.121946-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-20T10:19:19.114673-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "entry_ask": 26.9, "entry_bid": 24.1, "entry_mode": "early", "entry_option_price": 25.5, "hypothetical_budget": 26569.0, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 92.0, "option_spread_pct": 10.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "matched_signals": 30, "recovery_stability_score": 0.605, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T09:18:16.446091-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-19T11:30:46.509801-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-19T10:58:16.376316-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                {"contract_symbol": "ZS260918C00185000", "current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "entry_ask": 15.8, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 26569.0, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1626.0, "option_spread_pct": 4.53, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "matched_signals": 41, "recovery_stability_score": 0.774, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-19T10:25:26.675121-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T12:30:08.738941-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260820135510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260820135510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260820135510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260820135510)

</details>
