# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 11:50:02 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$47,718.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           88.89               18            1.00              0.32         45.78               551.67         1.000          pass              0.412              7.1                           0.143               -0.13             -0.132                      ok            True                  False
  TEAM           83.33               24            3.04              4.13        192.40               115.35         0.717          pass              0.298             14.7                           0.261               15.50              1.406                      ok            True                  False
  DRAM           82.86               35            0.51              0.20         56.81                66.99         0.609          pass              0.552             82.7                           0.867                2.74              0.161                      ok            True                  False
   TRI           93.94               33            0.69              0.52        107.10                60.77         0.598          pass              0.755             56.6                           0.622                8.29              0.536                      ok            True                  False
  SHOP           92.31               13            3.49              3.60        145.83                69.51         0.585          pass              0.441             11.5                           0.207               -4.33              0.025                      ok            True                  False
  PAYX          100.00               22            0.72              0.64        127.06                24.69         0.555          pass              0.657             40.6                           0.547                6.65              0.630                      ok            True                  False
  CSCO           83.87               31            1.08              0.83        110.13                40.87         0.539          pass              0.368             23.7                           0.394               -3.19             -0.099                      ok            True                  False
  CPRT           82.61               23            1.58              0.36         32.83                40.13         0.527          pass              0.283             24.6                           0.339                2.43              0.084                      ok            True                  False
  IDXX           87.50               16            1.77              6.91        553.73                29.41         0.512          pass              0.387             31.8                           0.556                0.13             -0.042                      ok            True                  False
  INSM           85.71               28            1.52              1.30        121.26               109.80         0.792          pass              0.354              0.8                           0.196               -6.51             -0.723 downtrend_blocked_slope           False                  False
  ABNB           95.00               40            0.15              0.19        183.14                62.80         0.634          pass              0.938             91.6                           0.725                2.04              0.107                      ok           False                  False
   STX           83.78               37            0.20              1.17        827.88                71.45         0.623          pass              0.624             93.6                           0.763              -16.90             -1.149 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-01T11:50:02.104495-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:45:02.019132-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                   {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "entry_ask": 12.75, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 12.225, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 39, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.59, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.718, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.718, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:40:05.886827-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                    {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "entry_ask": 12.6, "entry_bid": 11.55, "entry_mode": "early", "entry_option_price": 12.075, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.7, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "matched_signals": 40, "recovery_stability_score": 0.713, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:35:02.066939-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                        {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "entry_ask": 12.3, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 11.9, "hypothetical_budget": 23859.05, "hypothetical_contracts": 20, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 6.72, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "matched_signals": 38, "recovery_stability_score": 0.626, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:30:06.192762-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:25:02.972583-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:20:06.559055-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:15:02.069821-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:10:03.158617-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:46:36.373751-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "INTU261016C00370000", "current_drop_pct": 0.72, "early_entry_score": 0.75, "early_reclaim_pct": 76.7, "entry_ask": 16.9, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 16.35, "hypothetical_budget": 23859.05, "hypothetical_contracts": 14, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 595.0, "option_spread_pct": 6.73, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.882, "shadow_only": true, "success_rate": 91.43, "ticker": "INTU", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.75, "early_reclaim_pct": 76.7, "matched_signals": 35, "recovery_stability_score": 0.882, "success_rate": 91.43, "ticker": "INTU", "timing_score": 0.486, "trend_health_status": "ok"}, {"current_drop_pct": 1.04, "early_entry_score": 0.71, "early_reclaim_pct": 69.7, "matched_signals": 37, "recovery_stability_score": 0.783, "success_rate": 89.19, "ticker": "TEAM", "timing_score": 0.76, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901115002)

</details>
