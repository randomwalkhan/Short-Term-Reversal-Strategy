# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 10:35:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$69,741.10`
- Equity: `$69,741.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           82.35               34            1.35              1.25        132.16               104.12         0.668            pass              0.497             69.1                           0.616                6.27              0.605                                 ok            True                  False
   STX           88.24               34            0.90              5.58        883.53                74.71         0.587            pass              0.664             75.4                           0.832                3.73              0.589                                 ok            True                  False
   KDP           86.67               30            0.64              0.14         32.02                29.72         0.500 below_threshold              0.531             56.5                           0.672               -1.04              0.075                                 ok            True                  False
  AMGN          100.00               14            1.19              3.26        389.87                44.45         0.636            pass              0.553             20.9                           0.202              -12.20             -1.210 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               15            0.35              0.06         24.58                28.60         0.610            pass              0.725             77.0                           0.697                0.51             -0.084                                 ok           False                  False
  MRVL           76.32               38            1.00              1.65        234.30                80.25         0.575            pass              0.475             76.9                           0.795               -5.08             -0.134           downtrend_blocked_streak           False                  False
  ADBE           96.88               32            0.97              1.74        254.12                48.69         0.541            pass              0.762             53.7                           0.598               -7.71             -1.337 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               14            1.45              8.22        804.13                27.92         0.536            pass              0.570             30.0                           0.196               -2.32              0.033           downtrend_blocked_streak           False                  False
   CEG           91.67               24            1.02              2.10        293.00                32.56         0.499 below_threshold              0.647             64.3                           0.653                4.07              0.706                                 ok           False                  False
  FAST           96.55               29            0.33              0.11         48.74                20.91         0.496 below_threshold              0.806             76.5                           0.773               -4.93             -0.403 downtrend_blocked_slope_and_streak           False                  False
   LIN           76.47               17            0.98              3.18        465.29                16.09         0.487 below_threshold              0.115              6.6                           0.216               -5.45             -0.542 downtrend_blocked_slope_and_streak           False                  False
  CSCO           87.50               40            0.37              0.28        109.31                35.88         0.479 below_threshold              0.642             64.6                           0.397               -2.96             -0.276            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-10T10:35:01.109260-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:30:01.098158-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.588, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.588, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:25:01.160051-04:00 early_entry_1025 early_entry_shadow     {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:20:01.150296-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:15:05.197385-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:10:04.284123-04:00 early_entry_1010 early_entry_shadow                               {"contract_symbol": "MSFT261016C00500000", "current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "entry_ask": 13.2, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 27, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 24351.0, "option_spread_pct": 4.65, "option_volume": 115.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.728, "shadow_only": true, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "matched_signals": 31, "recovery_stability_score": 0.728, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-10T10:05:04.263972-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.2, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.801, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.2, "matched_signals": 37, "recovery_stability_score": 0.801, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:00:02.289278-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T09:50:01.115358-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "MSTR261009C00135000", "fill_price": 9.765, "pnl": -3689.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-10T00:00:06.085098-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910103501)

</details>
