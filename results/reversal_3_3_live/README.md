# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 11:10:05 EDT`
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

- Cash: `$30,858.00`
- Equity: `$30,858.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  AAPL     option         option AAPL260821C00325000     15          2026-07-22         2026-07-23       10.850      9.7650 -1627.50       -10.0 stop_loss_hit_at_scan
  PYPL     option         option PYPL260821C00055000     55          2026-07-21         2026-07-23        3.075      2.7675 -1691.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               15            0.86              0.37         60.70                31.72         0.630          pass              0.639             47.5                           0.658                3.49              0.359                                 ok            True                  False
  AAPL           92.31               13            1.37              3.14        324.55                37.45         0.626          pass              0.505             31.5                           0.399                1.64              0.366                                 ok            True                  False
   KHC           92.31               13            1.27              0.23         25.86                31.13         0.601          pass              0.478             23.3                           0.334                3.85              0.461                                 ok            True                  False
   PEP           86.36               22            0.66              0.62        135.38                30.61         0.582          pass              0.469             53.6                           0.663               -2.25             -0.207                                 ok            True                  False
   ADP           96.55               29            0.55              0.93        242.72                36.25         0.542          pass              0.721             46.8                           0.349                0.21              0.067                                 ok            True                  False
   MAR          100.00               14            1.52              3.94        368.11                21.19         0.539          pass              0.602             40.4                           0.600               -2.23             -0.115                                 ok            True                  False
  ROST           88.46               26            1.00              1.66        237.50                31.02         0.525          pass              0.514             43.0                           0.656                6.91              0.890                                 ok            True                  False
  MPWR           82.86               35            1.57             15.34       1391.87                64.79         0.510          pass              0.452             52.7                           0.288                0.17              0.224                                 ok            True                  False
  SOXL           84.62               26            4.21              4.75        158.96               181.21         0.728          pass              0.424             40.4                           0.226              -19.87             -2.414            downtrend_blocked_slope           False                  False
  ASML           94.44               36            0.11              1.40       1801.26                56.20         0.614          pass              0.902             94.2                           0.436               -0.24              0.042                                 ok           False                  False
  ISRG           85.71                7            3.25              7.76        337.37                68.45         0.605          pass              0.239              8.6                           0.230              -19.91             -2.304            downtrend_blocked_slope           False                  False
   KDP           90.48               21            0.75              0.16         30.13                36.78         0.601          pass              0.552             46.4                           0.480               -2.43             -0.347 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-23T11:10:05.049884-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:05:02.110750-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:00:02.056957-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:55:03.926277-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:50:05.067806-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:45:02.071891-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:40:02.096587-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:35:03.078129-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "REGN260821C00600000", "current_drop_pct": 0.71, "early_entry_score": 0.696, "early_reclaim_pct": 80.9, "entry_ask": 59.7, "entry_bid": 53.0, "entry_mode": "early", "entry_option_price": 56.35, "hypothetical_budget": 15429.0, "hypothetical_contracts": 2, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 549.0, "option_spread_pct": 11.89, "option_volume": 131.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.791, "shadow_only": true, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.696, "early_reclaim_pct": 80.9, "matched_signals": 36, "recovery_stability_score": 0.791, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-23T10:30:04.030785-04:00 early_entry_1030 early_entry_shadow  {"contract_symbol": "REGN260821C00600000", "current_drop_pct": 0.68, "early_entry_score": 0.699, "early_reclaim_pct": 81.8, "entry_ask": 58.3, "entry_bid": 53.0, "entry_mode": "early", "entry_option_price": 55.65, "hypothetical_budget": 15429.0, "hypothetical_contracts": 2, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 549.0, "option_spread_pct": 9.52, "option_volume": 131.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.772, "shadow_only": true, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.699, "early_reclaim_pct": 81.8, "matched_signals": 36, "recovery_stability_score": 0.772, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-23T10:25:02.098761-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723111005)

</details>
