# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 10:40:02 EDT`
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

- Cash: `$31,073.00`
- Equity: `$31,073.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.33               36            1.09              1.14        148.58               133.30         0.798          pass              0.522             60.0                           0.312               53.79              3.901                  ok            True                  False
  SOXL           80.00               35            2.39              2.35        139.24               179.06         0.763          pass              0.316             24.2                           0.228                6.83              2.627                  ok            True                  False
    MU           80.56               36            0.54              3.29        876.16               110.35         0.711          pass              0.498             79.6                           0.419               -3.04              0.697                  ok            True                  False
  AMAT           91.67               36            0.52              1.96        538.30                85.88         0.681          pass              0.633             27.0                           0.198                3.76              1.315                  ok            True                  False
  LRCX           88.24               34            0.70              1.54        310.69                90.05         0.668          pass              0.589             47.5                           0.307                6.02              1.445                  ok            True                  False
  PYPL           93.94               33            0.71              0.29         58.94                60.12         0.653          pass              0.742             50.6                           0.380                4.60              0.347                  ok            True                  False
  TMUS           88.89               18            1.68              2.08        176.30                55.81         0.643          pass              0.437             27.5                           0.359               -1.69             -0.181                  ok            True                  False
 CMCSA           92.31               13            1.60              0.28         25.24                44.15         0.629          pass              0.503             30.8                           0.478                9.45              0.761                  ok            True                  False
   STX           91.18               34            0.55              3.13        811.42                91.44         0.591          pass              0.767             83.3                           0.460               -1.06              0.514                  ok            True                  False
   ROP           96.88               32            0.63              1.77        401.49                46.43         0.578          pass              0.760             51.7                           0.363                6.59              0.346                  ok            True                  False
  KLAC           83.78               37            0.66              0.91        197.72                68.97         0.565          pass              0.412             24.9                           0.295               -3.22              0.516                  ok            True                  False
  MDLZ           92.31               13            1.52              0.67         62.32                30.17         0.563          pass              0.475             23.6                           0.399                1.63             -0.032                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-08-10T10:30:04.655219-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:25:03.677192-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:20:04.656698-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:15:05.996593-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:10:04.657796-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:05:05.873939-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "entry_ask": 21.95, "entry_bid": 19.4, "entry_mode": "early", "entry_option_price": 20.675, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 12.33, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "matched_signals": 41, "recovery_stability_score": 0.792, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:00:04.766738-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "entry_ask": 22.45, "entry_bid": 20.25, "entry_mode": "early", "entry_option_price": 21.35, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 10.3, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "matched_signals": 41, "recovery_stability_score": 0.847, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.772, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.761, "success_rate": 91.18, "ticker": "STX", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810104002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810104002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810104002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810104002)

</details>
