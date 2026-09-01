# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 11:15:02 EDT`
Last processed slot: `early_entry_1115`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           89.47               19            0.89              0.29         45.80               551.67         1.000          pass              0.464             17.2                           0.209               -0.02             -0.127                  ok            True                  False
  TEAM           85.19               27            2.77              3.76        192.56               115.35         0.719          pass              0.382             19.4                           0.183               15.83              1.419                  ok            True                  False
  SHOP           92.31               13            3.35              3.45        145.89                69.51         0.594          pass              0.453             15.2                           0.167               -4.18              0.032                  ok            True                  False
   TRI           92.31               26            1.47              1.11        106.85                60.77         0.591          pass              0.510              5.4                           0.099                7.44              0.500                  ok            True                  False
  PAYX          100.00               15            1.16              1.03        126.90                24.69         0.572          pass              0.505              4.8                           0.090                6.18              0.610                  ok            True                  False
  DRAM           83.87               31            1.64              0.65         56.62                66.99         0.565          pass              0.431             43.8                           0.566                1.57              0.109                  ok            True                  False
  CPRT           87.50               16            2.00              0.46         32.79                40.13         0.553          pass              0.308              4.3                           0.111                1.99              0.064                  ok            True                  False
  CSCO           83.33               30            1.10              0.85        110.12                40.87         0.542          pass              0.342             21.8                           0.420               -3.22             -0.100                  ok            True                  False
 CMCSA           92.31               26            0.57              0.11         26.57                24.41         0.534          pass              0.534             15.3                           0.146                3.51              0.257                  ok            True                  False
  NVDA           86.67               30            1.12              1.73        219.76                45.52         0.524          pass              0.526             54.3                           0.608               -0.78              0.141                  ok            True                  False
  UPRO           84.21               19            1.54              1.62        149.57                31.61         0.519          pass              0.319             31.6                           0.361               -4.18             -0.182                  ok            True                  False
  ALNY           85.71               35            0.66              1.12        240.21                49.87         0.512          pass              0.561             63.6                           0.303                6.45              0.493                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-01T11:15:02.069821-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:10:03.158617-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:46:36.373751-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "INTU261016C00370000", "current_drop_pct": 0.72, "early_entry_score": 0.75, "early_reclaim_pct": 76.7, "entry_ask": 16.9, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 16.35, "hypothetical_budget": 23859.05, "hypothetical_contracts": 14, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 595.0, "option_spread_pct": 6.73, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.882, "shadow_only": true, "success_rate": 91.43, "ticker": "INTU", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.75, "early_reclaim_pct": 76.7, "matched_signals": 35, "recovery_stability_score": 0.882, "success_rate": 91.43, "ticker": "INTU", "timing_score": 0.486, "trend_health_status": "ok"}, {"current_drop_pct": 1.04, "early_entry_score": 0.71, "early_reclaim_pct": 69.7, "matched_signals": 37, "recovery_stability_score": 0.783, "success_rate": 89.19, "ticker": "TEAM", "timing_score": 0.76, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:40:01.982224-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "INTU261016C00360000", "current_drop_pct": 0.77, "early_entry_score": 0.732, "early_reclaim_pct": 75.1, "entry_ask": 19.8, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 12, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 493.0, "option_spread_pct": 11.76, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.884, "shadow_only": true, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.732, "early_reclaim_pct": 75.1, "matched_signals": 34, "recovery_stability_score": 0.884, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:35:04.145370-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "INTU261016C00330000", "current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "entry_ask": 35.9, "entry_bid": 31.6, "entry_mode": "early", "entry_option_price": 33.75, "hypothetical_budget": 23859.05, "hypothetical_contracts": 7, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 179.0, "option_spread_pct": 12.74, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.853, "shadow_only": true, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "matched_signals": 34, "recovery_stability_score": 0.853, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:30:06.594545-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:25:01.815203-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:20:03.001967-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:15:02.023349-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:10:02.052599-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901111502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901111502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901111502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901111502)

</details>
