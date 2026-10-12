# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 11:25:06 EDT`
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

- Cash: `$58,874.30`
- Equity: `$117,274.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 58400.0         3.65           3.65       59.31         59.56          bid_ask_mid                       3.65                bid_ask_mid                    True             0.0                    0.0          93.1               29              1.17         50.42           50.93                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.96               23            1.33              2.77        296.88                62.49         0.550          pass              0.376             16.1                           0.193               12.93              1.706                                 ok            True                  False
    ZS           91.67               36            1.16              1.89        232.92                75.53         0.527          pass              0.692             51.8                           0.474               15.87              1.694                                 ok            True                  False
  ABNB           85.71               28            1.27              1.47        165.24                38.25         0.508          pass              0.404             26.8                           0.248                4.93              0.453                                 ok            True                  False
  MSTR           92.31               39            0.17              0.18        154.26                79.86         0.646          pass              0.842             85.2                           0.462               -1.95             -0.183                                 ok           False                  False
  SNPS           72.22               18            1.71              6.09        507.38                55.08         0.599          pass              0.147             11.4                           0.253               20.04              2.019                                 ok           False                  False
  QCOM           88.89               27            1.12              1.38        174.91                55.68         0.592          pass              0.533             41.0                           0.580               -7.44             -0.716 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.24               17            0.36              0.05         20.64                20.79         0.533          pass              0.479             53.1                           0.456               -4.06             -0.359            downtrend_blocked_slope           False                  False
  DASH           76.92               13            2.54              3.49        195.00                43.05         0.515          pass              0.164             30.7                           0.415                7.35              0.729                                 ok           False                  False
   WDC           74.07               27            2.46              6.85        394.34                64.73         0.511          pass              0.193              9.7                           0.212              -14.50             -1.837            downtrend_blocked_slope           False                  False
   STX           84.21               19            3.87             21.22        773.90                69.65         0.508          pass              0.225              0.6                           0.219              -18.32             -2.290            downtrend_blocked_slope           False                  False
  INTC           77.78               18            3.40              2.49        103.63                69.66         0.508          pass              0.137             10.9                           0.305              -12.83             -1.471 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               43            0.14              0.21        206.70                49.66         0.507          pass              0.774             41.0                           0.238               15.66              1.679                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-10-12T11:25:06.247311-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.67, "early_entry_score": 0.681, "early_reclaim_pct": 71.4, "entry_ask": 18.5, "entry_bid": 17.35, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 6.42, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.558, "shadow_only": true, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.681, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.558, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:20:06.014837-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                   {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.63, "early_entry_score": 0.7, "early_reclaim_pct": 73.1, "entry_ask": 18.5, "entry_bid": 17.5, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 5.56, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.7, "early_reclaim_pct": 73.1, "matched_signals": 38, "recovery_stability_score": 0.58, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:15:05.356295-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.66, "early_entry_score": 0.684, "early_reclaim_pct": 72.2, "entry_ask": 18.55, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 18.275, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 3.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.684, "early_reclaim_pct": 72.2, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 89.19, "ticker": "TXN", "timing_score": 0.419, "trend_health_status": "ok"}, {"current_drop_pct": 1.03, "early_entry_score": 0.68, "early_reclaim_pct": 76.0, "matched_signals": 36, "recovery_stability_score": 0.705, "success_rate": 88.89, "ticker": "ADBE", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T11:10:06.283022-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:05:41.766229-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.58, "early_entry_score": 0.708, "early_reclaim_pct": 75.5, "entry_ask": 18.3, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.8, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 5.62, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.708, "early_reclaim_pct": 75.5, "matched_signals": 38, "recovery_stability_score": 0.783, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:55:05.736003-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:50:05.423702-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:45:04.583763-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:40:05.705407-04:00 early_entry_1040 early_entry_shadow  {"contract_symbol": "ADI261120C00420000", "current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "entry_ask": 14.3, "entry_bid": 12.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 29437.15, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 271.0, "option_spread_pct": 10.29, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.782, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.677, "early_reclaim_pct": 67.4, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ABNB", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:35:03.248275-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012112506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012112506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012112506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012112506)

</details>
