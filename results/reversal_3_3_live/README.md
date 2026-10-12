# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 12:45:06 EDT`
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
- Equity: `$118,874.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$1,600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 60000.0         3.65           3.75       59.31         59.78          bid_ask_mid                       3.75                bid_ask_mid                    True          1600.0                   2.74          93.1               29              1.17         50.42           50.73                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           88.24               17            2.66              4.35        231.86                75.53         0.551          pass              0.339              5.9                           0.278               14.10              1.624                                 ok            True                  False
   CEG           86.36               22            1.45              3.02        296.78                62.49         0.546          pass              0.372             22.5                           0.343               12.80              1.701                                 ok            True                  False
  ABNB           85.71               28            1.28              1.49        165.23                38.25         0.506          pass              0.400             25.8                           0.237                4.91              0.452                                 ok            True                  False
  MSTR           92.11               38            0.25              0.27        154.23                79.86         0.647          pass              0.809             78.4                           0.409               -2.02             -0.187                                 ok           False                  False
  SNPS           75.00               20            1.52              5.41        507.67                55.08         0.600          pass              0.191             21.3                           0.337               20.27              2.028                                 ok           False                  False
  QCOM           90.91               33            0.55              0.67        175.21                55.68         0.592          pass              0.717             71.3                           0.612               -6.90             -0.690 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           86.67               15            0.56              0.08         20.63                20.79         0.531          pass              0.349             28.1                           0.268               -4.25             -0.368            downtrend_blocked_slope           False                  False
   STX           85.71               21            3.27             17.94        775.31                69.65         0.529          pass              0.341             20.7                           0.429              -17.81             -2.262            downtrend_blocked_slope           False                  False
   WDC           74.07               27            2.37              6.60        394.45                64.73         0.516          pass              0.204             13.0                           0.236              -14.43             -1.832            downtrend_blocked_slope           False                  False
  TEAM          100.00               39            0.45              0.65        206.51                49.66         0.509          pass              0.739             31.6                           0.303               15.30              1.665                                 ok           False                  False
  INTC           77.78               18            3.42              2.51        103.63                69.66         0.507          pass              0.135             10.3                           0.195              -12.85             -1.473 downtrend_blocked_slope_and_streak           False                  False
  DASH           72.73               11            2.82              3.88        194.84                43.05         0.506          pass              0.126             23.1                           0.337                7.05              0.716                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012124506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012124506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012124506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012124506)

</details>
