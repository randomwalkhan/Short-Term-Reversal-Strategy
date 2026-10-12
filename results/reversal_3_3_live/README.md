# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 14:30:05 EDT`
Last processed slot: `manage_1430`

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
- Equity: `$122,074.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$4,800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 63200.0         3.65           3.95       59.31         59.85          bid_ask_mid                       3.95                bid_ask_mid                    True          4800.0                   8.22          93.1               29              1.17         50.42           50.98                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.43               35            1.05              1.13        153.85                79.86         0.620          pass              0.573             13.4                           0.237               -2.81             -0.224                                 ok            True                  False
   CEG           82.35               17            2.03              4.24        296.25                62.49         0.535          pass              0.194             10.3                           0.293               12.13              1.674                                 ok            True                  False
  ABNB           80.95               21            1.62              1.88        165.07                38.25         0.521          pass              0.209             19.3                           0.378                4.56              0.437                                 ok            True                  False
    ZS           81.82               11            3.71              6.08        231.13                75.53         0.513          pass              0.114              2.4                           0.170               12.87              1.575                                 ok            True                  False
  SNPS           77.27               22            1.45              5.16        507.78                55.08         0.595          pass              0.214             24.9                           0.261               20.36              2.031                                 ok           False                  False
  QCOM           89.29               28            1.00              1.23        174.97                55.68         0.593          pass              0.569             47.3                           0.462               -7.33             -0.711 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.24               17            0.41              0.06         20.63                20.79         0.529          pass              0.460             46.9                           0.448               -4.11             -0.361            downtrend_blocked_slope           False                  False
  CSCO           60.00                5            2.34              1.94        117.56                33.46         0.523          pass              0.157             35.0                           0.518                8.74              1.145                                 ok           False                  False
   STX           83.33               24            3.08             16.91        775.75                69.65         0.519          pass              0.310             25.3                           0.505              -17.65             -2.253            downtrend_blocked_slope           False                  False
  TEAM          100.00               43            0.01              0.02        206.78                49.66         0.510          pass              0.944             97.8                           0.705               15.81              1.685                                 ok           False                  False
   WDC           74.07               27            2.46              6.85        394.34                64.73         0.510          pass              0.199             11.6                           0.374              -14.50             -1.837            downtrend_blocked_slope           False                  False
  INTC           77.78               18            3.52              2.58        103.59                69.66         0.501          pass              0.126              7.5                           0.239              -12.94             -1.477 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012143005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012143005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012143005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012143005)

</details>
