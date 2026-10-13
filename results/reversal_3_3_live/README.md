# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 14:30:04 EDT`
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
  SNPS           86.67               30            0.81              2.86        501.28                52.43         0.569            pass              0.576             69.4                           0.566               20.08              1.518                                 ok            True                  False
  SHOP           83.33               36            0.74              0.92        178.82                48.43         0.517            pass              0.541             75.6                           0.571               19.99              2.073                                 ok            True                  False
  MSTR           91.67               36            0.37              0.39        152.51                78.93         0.651            pass              0.667             39.1                           0.323               -1.65             -0.355            downtrend_blocked_slope           False                  False
  SOXL           86.21               29            2.10              1.89        127.59                96.52         0.567            pass              0.584             78.5                           0.902              -14.49             -1.766 downtrend_blocked_slope_and_streak           False                  False
  MPWR           91.43               35            0.40              3.69       1317.65                51.39         0.550            pass              0.782             85.1                           0.806               -2.96             -0.287            downtrend_blocked_slope           False                  False
  MDLZ           96.15               26            0.28              0.12         61.74                19.83         0.520            pass              0.770             70.4                           0.654                4.80              0.666                                 ok           False                  False
  AMGN           73.33               15            1.36              3.96        415.87                27.37         0.518            pass              0.125             13.3                           0.321               -2.77             -0.069           downtrend_blocked_streak           False                  False
   STX           85.71               28            2.26             11.93        748.14                70.16         0.515            pass              0.546             73.9                           0.753              -19.40             -2.483            downtrend_blocked_slope           False                  False
  UPRO           83.78               37            0.09              0.10        155.42                28.94         0.511            pass              0.599             89.1                           0.763                4.97              0.603                                 ok           False                  False
  CSCO           94.29               35            0.16              0.13        115.28                34.19         0.507            pass              0.876             92.6                           0.727                8.09              0.941                                 ok           False                  False
  GILD           88.89                9            1.73              1.82        149.65                19.66         0.504            pass              0.341             17.9                           0.325               -2.28              0.039           downtrend_blocked_streak           False                  False
   WDC           73.08               26            2.36              6.40        384.20                63.46         0.490 below_threshold              0.372             72.2                           0.720              -16.69             -2.006            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013143004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013143004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013143004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013143004)

</details>
