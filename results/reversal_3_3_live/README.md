# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 13:45:02 EDT`
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

- Cash: `$58,874.30`
- Equity: `$120,474.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$3,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 61600.0         3.65           3.85       59.31         59.96          bid_ask_mid                       3.85                bid_ask_mid                    True          3200.0                   5.48          93.1               29              1.17         50.42            51.0                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.43               35            0.91              0.98        153.92                79.86         0.628          pass              0.596             20.5                           0.141               -2.67             -0.217                                 ok            True                  False
    ZS           88.24               17            2.70              4.41        231.84                75.53         0.546          pass              0.360             13.0                           0.407               14.06              1.623                                 ok            True                  False
   CEG           83.33               18            2.01              4.19        296.27                62.49         0.531          pass              0.229             11.3                           0.300               12.15              1.675                                 ok            True                  False
  ABNB           82.61               23            1.38              1.61        165.18                38.25         0.528          pass              0.269             20.0                           0.325                4.80              0.448                                 ok            True                  False
  DASH           81.25               16            2.40              3.30        195.09                43.05         0.510          pass              0.228             34.6                           0.638                7.51              0.736                                 ok            True                  False
  SNPS           78.26               23            1.25              4.48        508.07                55.08         0.601          pass              0.251             34.8                           0.339               20.59              2.040                                 ok           False                  False
  QCOM           88.89               27            1.08              1.32        174.93                55.68         0.594          pass              0.540             43.4                           0.268               -7.40             -0.714 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.24               17            0.41              0.06         20.63                20.79         0.529          pass              0.460             46.9                           0.385               -4.11             -0.361            downtrend_blocked_slope           False                  False
   STX           85.71               21            3.27             17.93        775.31                69.65         0.529          pass              0.341             20.7                           0.403              -17.81             -2.262            downtrend_blocked_slope           False                  False
  CSCO           60.00                5            2.35              1.95        117.56                33.46         0.522          pass              0.156             34.7                           0.511                8.73              1.144                                 ok           False                  False
   WDC           73.08               26            2.49              6.93        394.31                64.73         0.514          pass              0.184              8.7                           0.211              -14.53             -1.838            downtrend_blocked_slope           False                  False
  INTC           77.78               18            3.44              2.52        103.62                69.66         0.505          pass              0.133              9.6                           0.217              -12.87             -1.474 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-12T12:00:04.227731-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:55:04.380745-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:50:05.333973-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:45:05.208038-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "TTWO261120C00210000", "current_drop_pct": 1.13, "early_entry_score": 0.683, "early_reclaim_pct": 65.0, "entry_ask": 15.4, "entry_bid": 14.6, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 29437.15, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 800.0, "option_spread_pct": 5.33, "option_volume": 56.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 1.13, "early_entry_score": 0.683, "early_reclaim_pct": 65.0, "matched_signals": 33, "recovery_stability_score": 0.749, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:40:06.329765-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "TTWO261120C00210000", "current_drop_pct": 1.11, "early_entry_score": 0.685, "early_reclaim_pct": 65.7, "entry_ask": 15.5, "entry_bid": 14.5, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 29437.15, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 800.0, "option_spread_pct": 6.67, "option_volume": 56.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.435, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.685, "early_reclaim_pct": 65.7, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:35:01.412553-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "TTWO261120C00210000", "current_drop_pct": 1.08, "early_entry_score": 0.688, "early_reclaim_pct": 66.6, "entry_ask": 15.2, "entry_bid": 14.4, "entry_mode": "early", "entry_option_price": 14.8, "hypothetical_budget": 29437.15, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 800.0, "option_spread_pct": 5.41, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.799, "shadow_only": true, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 1.08, "early_entry_score": 0.688, "early_reclaim_pct": 66.6, "matched_signals": 33, "recovery_stability_score": 0.799, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:30:04.482107-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "ADBE261120C00240000", "current_drop_pct": 0.97, "early_entry_score": 0.698, "early_reclaim_pct": 77.3, "entry_ask": 13.3, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.075, "hypothetical_budget": 29437.15, "hypothetical_contracts": 22, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1006.0, "option_spread_pct": 3.44, "option_volume": 28.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.408, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.698, "early_reclaim_pct": 77.3, "matched_signals": 37, "recovery_stability_score": 0.703, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.408, "trend_health_status": "ok"}, {"current_drop_pct": 1.1, "early_entry_score": 0.686, "early_reclaim_pct": 66.0, "matched_signals": 33, "recovery_stability_score": 0.805, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:25:06.247311-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.67, "early_entry_score": 0.681, "early_reclaim_pct": 71.4, "entry_ask": 18.5, "entry_bid": 17.35, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 6.42, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.558, "shadow_only": true, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.681, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.558, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:20:06.014837-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.63, "early_entry_score": 0.7, "early_reclaim_pct": 73.1, "entry_ask": 18.5, "entry_bid": 17.5, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 5.56, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.7, "early_reclaim_pct": 73.1, "matched_signals": 38, "recovery_stability_score": 0.58, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:15:05.356295-04:00 early_entry_1115 early_entry_shadow     {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.66, "early_entry_score": 0.684, "early_reclaim_pct": 72.2, "entry_ask": 18.55, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 18.275, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 3.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.684, "early_reclaim_pct": 72.2, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.419, "trend_health_status": "ok"}, {"current_drop_pct": 1.03, "early_entry_score": 0.68, "early_reclaim_pct": 76.0, "matched_signals": 36, "recovery_stability_score": 0.705, "success_rate": 88.89, "ticker": "ADBE", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012134502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012134502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012134502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012134502)

</details>
