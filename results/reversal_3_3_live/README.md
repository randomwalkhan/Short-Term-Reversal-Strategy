# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 14:25:01 EDT`
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
  MNST           80.00               10            1.68              0.54         45.69               551.67         1.000          pass              0.131             10.5                           0.384               -0.81             -0.163                      ok            True                  False
  TEAM           82.61               23            3.27              4.44        192.27               115.35         0.701          pass              0.308             27.3                           0.430               15.23              1.395                      ok            True                  False
   TRI           93.55               31            0.91              0.69        107.03                60.77         0.596          pass              0.688             42.5                           0.254                8.05              0.526                      ok            True                  False
  PAYX          100.00               12            1.58              1.41        126.74                24.69         0.562          pass              0.492              7.6                           0.126                5.73              0.591                      ok            True                  False
  CPRT           88.89               18            1.86              0.43         32.81                40.13         0.551          pass              0.378             10.9                           0.142                2.13              0.071                      ok            True                  False
  CSCO           85.29               34            0.90              0.69        110.19                40.87         0.533          pass              0.464             36.5                           0.608               -3.01             -0.091                      ok            True                  False
 CMCSA           92.00               25            0.69              0.13         26.56                24.41         0.531          pass              0.515             14.0                           0.209                3.38              0.252                      ok            True                  False
  NVDA           86.21               29            1.28              1.97        219.66                45.52         0.520          pass              0.488             47.9                           0.344               -0.94              0.134                      ok            True                  False
  UPRO           87.50               16            2.12              2.23        149.32                31.61         0.507          pass              0.325             11.4                           0.276               -4.73             -0.208                      ok            True                  False
  IDXX           86.67               15            2.02              7.85        553.32                29.41         0.501          pass              0.338             25.6                           0.448               -0.11             -0.054                      ok            True                  False
  INSM           87.18               39            0.71              0.61        121.56               109.80         0.779          pass              0.649             62.2                           0.717               -5.74             -0.686 downtrend_blocked_slope           False                  False
   STX           83.87               31            1.40              8.14        824.89                71.45         0.584          pass              0.469             55.7                           0.480              -17.90             -1.204 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-01T12:00:06.980016-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:55:07.200979-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:50:02.104495-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:45:02.019132-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "entry_ask": 12.75, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 12.225, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 39, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.59, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.718, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.718, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:40:05.886827-04:00 early_entry_1140 early_entry_shadow  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "entry_ask": 12.6, "entry_bid": 11.55, "entry_mode": "early", "entry_option_price": 12.075, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.7, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "matched_signals": 40, "recovery_stability_score": 0.713, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:35:02.066939-04:00 early_entry_1135 early_entry_shadow      {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "entry_ask": 12.3, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 11.9, "hypothetical_budget": 23859.05, "hypothetical_contracts": 20, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 6.72, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "matched_signals": 38, "recovery_stability_score": 0.626, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:30:06.192762-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:25:02.972583-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:20:06.559055-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:15:02.069821-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901142501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901142501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901142501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901142501)

</details>
