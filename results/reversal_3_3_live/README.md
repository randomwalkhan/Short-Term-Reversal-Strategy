# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 11:00:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.19              1.29        153.53               126.50         0.789          pass              0.474             57.6                           0.339               45.99              5.172                  ok            True                  False
  PYPL           91.67               24            1.06              0.44         58.81                59.96         0.677          pass              0.633             53.7                           0.521                0.04              0.212                  ok            True                  False
  SHOP           97.06               34            1.28              1.37        152.02                81.89         0.651          pass              0.709             27.9                           0.358               16.63              2.908                  ok            True                  False
  ABNB          100.00               13            2.09              2.71        183.82                64.05         0.642          pass              0.572             29.4                           0.334               18.36              2.277                  ok            True                  False
  GEHC           91.30               23            1.26              0.64         72.47                54.33         0.621          pass              0.592             47.1                           0.521               -0.10              0.326                  ok            True                  False
 CMCSA           88.24               17            1.23              0.22         25.56                42.38         0.621          pass              0.398             23.2                           0.353                7.03              0.684                  ok            True                  False
   ROP          100.00               15            2.03              5.68        397.07                44.32         0.603          pass              0.546             17.3                           0.170                0.55              0.162                  ok            True                  False
  MCHP           85.00               40            0.52              0.29         80.89                74.47         0.592          pass              0.453             20.0                           0.191                7.45              1.008                  ok            True                  False
  FAST          100.00               18            0.88              0.32         52.24                25.01         0.574          pass              0.622             37.0                           0.345               11.27              1.192                  ok            True                  False
  PAYX          100.00               12            1.75              1.49        120.66                33.26         0.569          pass              0.543             24.1                           0.293                2.45              0.358                  ok            True                  False
   LIN           81.25               16            1.37              4.70        488.51                25.58         0.553          pass              0.142              4.5                           0.131               -4.88             -0.062                  ok            True                  False
   ADP           94.74               19            1.62              3.07        269.77                32.74         0.545          pass              0.553             15.3                           0.221                1.07              0.117                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-12T11:00:05.629703-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "entry_ask": 17.35, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.025, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 3.82, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "matched_signals": 40, "recovery_stability_score": 0.596, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.721, "early_reclaim_pct": 94.2, "matched_signals": 30, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:55:04.810521-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "entry_ask": 17.7, "entry_bid": 16.95, "entry_mode": "early", "entry_option_price": 17.325, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.33, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "matched_signals": 41, "recovery_stability_score": 0.696, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:50:01.775257-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "entry_ask": 17.55, "entry_bid": 16.45, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.47, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "matched_signals": 41, "recovery_stability_score": 0.789, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:45:05.750947-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:40:06.908628-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:30:06.810656-04:00 early_entry_1030 early_entry_shadow     {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "entry_ask": 16.5, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.25, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.838, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "matched_signals": 40, "recovery_stability_score": 0.838, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.72, "early_reclaim_pct": 94.1, "matched_signals": 30, "recovery_stability_score": 0.734, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.379, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:25:01.823569-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "entry_ask": 16.5, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.95, "hypothetical_budget": 17549.0, "hypothetical_contracts": 11, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.9, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.843, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "matched_signals": 41, "recovery_stability_score": 0.843, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.746, "early_reclaim_pct": 95.5, "matched_signals": 37, "recovery_stability_score": 0.717, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.347, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:20:04.811080-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "matched_signals": 34, "recovery_stability_score": 0.643, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T10:15:04.787408-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812110005)

</details>
