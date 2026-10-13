# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 14:45:06 EDT`
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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           86.67               30            0.85              2.98        501.23                52.43         0.567            pass              0.572             68.1                           0.599               20.03              1.516                                 ok            True                  False
  SHOP           84.62               39            0.57              0.71        178.91                48.43         0.509            pass              0.611             81.1                           0.650               20.19              2.081                                 ok            True                  False
  MSTR           91.67               36            0.46              0.49        152.47                78.93         0.646            pass              0.635             28.6                           0.259               -1.74             -0.359            downtrend_blocked_slope           False                  False
  MPWR           91.67               36            0.38              3.50       1317.73                51.39         0.546            pass              0.797             85.9                           0.733               -2.94             -0.286            downtrend_blocked_slope           False                  False
  CSCO           92.59               27            0.36              0.29        115.22                34.19         0.542            pass              0.756             84.1                           0.631                7.89              0.932                                 ok           False                  False
  SOXL           84.62               26            3.08              2.77        127.21                96.52         0.529            pass              0.488             68.5                           0.613              -15.35             -1.812 downtrend_blocked_slope_and_streak           False                  False
   STX           84.62               26            2.37             12.50        747.89                70.16         0.520            pass              0.500             72.6                           0.610              -19.49             -2.488            downtrend_blocked_slope           False                  False
  UPRO           86.11               36            0.19              0.21        155.37                28.94         0.512            pass              0.618             76.8                           0.692                4.87              0.598                                 ok           False                  False
  AMGN           80.00               20            1.06              3.09        416.25                27.37         0.512            pass              0.215             32.5                           0.519               -2.47             -0.055           downtrend_blocked_streak           False                  False
  GILD           90.00               10            1.56              1.64        149.73                19.66         0.508            pass              0.395             26.0                           0.469               -2.11              0.047           downtrend_blocked_streak           False                  False
  MDLZ           93.10               29            0.22              0.09         61.75                19.83         0.503            pass              0.756             76.5                           0.638                4.86              0.669                                 ok           False                  False
  MELI           81.40               43            0.38              5.03       1890.29                42.28         0.490 below_threshold              0.481             64.9                           0.352                9.30              1.216                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-13T12:00:04.609468-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "MRVL261120C00260000", "current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "entry_ask": 20.5, "entry_bid": 20.05, "entry_mode": "early", "entry_option_price": 20.275, "hypothetical_budget": 71287.15, "hypothetical_contracts": 35, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 3428.0, "option_spread_pct": 2.22, "option_volume": 501.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.919, "shadow_only": true, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "matched_signals": 35, "recovery_stability_score": 0.919, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "matched_signals": 41, "recovery_stability_score": 0.623, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-13T11:55:06.360057-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "matched_signals": 41, "recovery_stability_score": 0.631, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:50:05.756508-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:45:05.731226-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:40:02.593298-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                   {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 65.0, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 65.0, "matched_signals": 42, "recovery_stability_score": 0.738, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:35:06.355807-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:30:05.585101-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.64, "early_entry_score": 0.706, "early_reclaim_pct": 62.5, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.706, "early_reclaim_pct": 62.5, "matched_signals": 42, "recovery_stability_score": 0.736, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:25:04.515865-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                  {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "entry_ask": 29.3, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.75, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "matched_signals": 41, "recovery_stability_score": 0.74, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:20:02.638996-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                    {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.752, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "matched_signals": 42, "recovery_stability_score": 0.752, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:15:05.483725-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                  {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "matched_signals": 42, "recovery_stability_score": 0.736, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013144506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013144506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013144506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013144506)

</details>
