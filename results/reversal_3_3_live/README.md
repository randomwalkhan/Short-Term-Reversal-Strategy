# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 11:45:05 EDT`
Last processed slot: `early_entry_1145`

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

- Cash: `$13,363.25`
- Equity: `$27,090.75`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,105.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 13727.5         7.43           8.07       68.52         71.36          bid_ask_mid                       8.07                bid_ask_mid                    True          1105.0                   8.75         90.91               11              3.59         94.78           83.76                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT           95.24               21            1.69              1.74        146.27                47.06         0.525          pass              0.686             53.3                           0.398               -2.91             -0.260                                 ok            True                  False
    ZS           76.32               38            0.64              0.57        126.99               152.67         0.876          pass              0.491             72.4                           0.670               -5.92             -0.557 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                2            1.37              0.23         23.70                25.54         0.681          pass              0.505             12.2                           0.257                5.01              0.793                                 ok           False                  False
   PEP          100.00                5            1.26              1.29        145.57                20.43         0.641          pass              0.548             28.1                           0.418                2.67              0.388                                 ok           False                  False
   CSX          100.00                4            1.62              0.53         46.67                20.12         0.627          pass              0.467              1.3                           0.230                0.00              0.173                                 ok           False                  False
  MCHP           94.44               36            0.05              0.03         95.62                60.62         0.623          pass              0.903             93.9                           0.566               -1.42              0.149                                 ok           False                  False
   XEL          100.00               23            0.25              0.14         78.92                23.22         0.604          pass              0.750             67.8                           0.421                1.94              0.273                                 ok           False                  False
  PAYX          100.00               28            0.02              0.01        100.27                31.37         0.589          pass              0.875             98.9                           0.816               -0.53              0.117                                 ok           False                  False
   WMT           73.33               15            1.39              1.18        120.53                34.81         0.588          pass              0.124             10.6                           0.279                5.56              0.478                                 ok           False                  False
  WDAY           86.36               44            0.02              0.01        126.76                67.72         0.583          pass              0.727             99.5                           0.795              -13.72             -1.760 downtrend_blocked_slope_and_streak           False                  False
   TXN           93.94               33            0.47              1.01        305.28                52.85         0.578          pass              0.807             74.7                           0.358               -1.25              0.033                                 ok           False                  False
  MSTR           86.67               45            0.02              0.01        122.80                75.43         0.577          pass              0.733             99.1                           0.730               -9.77             -0.580            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-17T11:45:05.887848-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.57, "early_entry_score": 0.828, "early_reclaim_pct": 71.4, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.828, "early_reclaim_pct": 71.4, "matched_signals": 35, "recovery_stability_score": 0.69, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:40:04.886888-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.65, "early_entry_score": 0.804, "early_reclaim_pct": 67.4, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.667, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.48, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.804, "early_reclaim_pct": 67.4, "matched_signals": 33, "recovery_stability_score": 0.667, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.48, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:35:01.995528-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.63, "early_entry_score": 0.805, "early_reclaim_pct": 68.0, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.805, "early_reclaim_pct": 68.0, "matched_signals": 33, "recovery_stability_score": 0.674, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:30:04.966423-04:00 early_entry_1130 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.7, "early_entry_score": 0.783, "early_reclaim_pct": 64.7, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.783, "early_reclaim_pct": 64.7, "matched_signals": 31, "recovery_stability_score": 0.646, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:25:01.981601-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.74, "early_entry_score": 0.777, "early_reclaim_pct": 62.9, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.777, "early_reclaim_pct": 62.9, "matched_signals": 31, "recovery_stability_score": 0.62, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:20:05.975593-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.78, "early_entry_score": 0.765, "early_reclaim_pct": 60.9, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 96.67, "ticker": "CTAS", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.765, "early_reclaim_pct": 60.9, "matched_signals": 30, "recovery_stability_score": 0.593, "success_rate": 96.67, "ticker": "CTAS", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:15:01.940218-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:10:02.894138-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:05:03.233466-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:00:05.904410-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617114505)

</details>
