# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 14:25:06 EDT`
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
  SNPS           86.67               30            0.80              2.80        501.31                52.43         0.570            pass              0.578             70.1                           0.558               20.10              1.519                                 ok            True                  False
  SHOP           83.33               36            0.80              1.01        178.79                48.43         0.513            pass              0.534             73.4                           0.598               19.91              2.070                                 ok            True                  False
  MSTR           91.67               36            0.50              0.53        152.45                78.93         0.645            pass              0.574              8.4                           0.172               -1.78             -0.361            downtrend_blocked_slope           False                  False
  SOXL           86.21               29            2.03              1.83        127.62                96.52         0.571            pass              0.587             79.2                           0.908              -14.43             -1.763 downtrend_blocked_slope_and_streak           False                  False
  MPWR           91.67               36            0.39              3.57       1317.70                51.39         0.545            pass              0.796             85.6                           0.818               -2.94             -0.286            downtrend_blocked_slope           False                  False
  MDLZ           96.15               26            0.28              0.12         61.74                19.83         0.520            pass              0.770             70.4                           0.704                4.80              0.666                                 ok           False                  False
  AMGN           71.43               14            1.41              4.11        415.81                27.37         0.520            pass              0.109             10.1                           0.247               -2.82             -0.071           downtrend_blocked_streak           False                  False
   STX           85.71               28            2.28             12.02        748.10                70.16         0.515            pass              0.545             73.7                           0.765              -19.42             -2.484            downtrend_blocked_slope           False                  False
  CSCO           94.29               35            0.16              0.13        115.28                34.19         0.507            pass              0.876             92.6                           0.712                8.09              0.941                                 ok           False                  False
  UPRO           83.78               37            0.16              0.17        155.39                28.94         0.506            pass              0.575             81.1                           0.712                4.90              0.599                                 ok           False                  False
  GILD           90.00               10            1.64              1.72        149.69                19.66         0.504            pass              0.384             22.3                           0.347               -2.19              0.043           downtrend_blocked_streak           False                  False
   WDC           73.08               26            2.40              6.50        384.16                63.46         0.488 below_threshold              0.371             71.8                           0.711              -16.72             -2.008            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013142506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013142506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013142506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013142506)

</details>
