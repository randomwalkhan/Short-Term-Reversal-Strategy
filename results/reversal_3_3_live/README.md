# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 12:00:04 EDT`
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

- Cash: `$67,953.30`
- Equity: `$67,953.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.50               24            1.10              0.40         52.34                57.12         0.635          pass              0.359              0.9                           0.083               -0.45             -0.198                  ok            True                  False
  NVDA           91.30               23            1.45              2.29        224.53                44.57         0.582          pass              0.524             26.0                           0.535               -0.53              0.382                  ok            True                  False
  ADSK           81.48               27            1.56              2.38        216.13                55.47         0.551          pass              0.319             37.1                           0.268                3.45              0.234                  ok            True                  False
  MPWR           85.19               27            1.74             16.46       1348.41                51.84         0.548          pass              0.440             44.5                           0.652               10.65              1.214                  ok            True                  False
    MU           84.85               33            1.43             10.74       1067.28                49.67         0.530          pass              0.491             51.7                           0.644                2.80              0.957                  ok            True                  False
  UPRO           85.00               20            1.57              1.65        149.59                31.44         0.519          pass              0.358             35.5                           0.393                0.51              0.375                  ok            True                  False
  MSFT          100.00               21            1.11              3.89        498.92                22.42         0.516          pass              0.647             40.8                           0.624                0.69              0.092                  ok            True                  False
   ADP           95.83               24            0.58              1.07        263.22                21.61         0.513          pass              0.651             35.4                           0.363               -0.53             -0.012                  ok            True                  False
  DRAM           82.14               28            2.34              1.01         61.47                51.34         0.513          pass              0.277             16.2                           0.436               -1.84              0.487                  ok            True                  False
  CTSH          100.00               11            2.85              1.18         58.63                40.91         0.503          pass              0.491             11.3                           0.298               -1.28             -0.197                  ok            True                  False
  MSTR           94.74               38            0.45              0.52        161.98               109.59         0.770          pass              0.921             88.2                           0.669               21.68              2.774                  ok           False                  False
  CRWD           88.64               44            0.42              0.78        262.16                96.70         0.705          pass              0.717             72.0                           0.595               25.78              2.249                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-09-24T12:00:04.840325-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:55:06.286422-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:50:04.896304-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:45:04.623722-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:40:06.370244-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:35:05.981561-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:30:04.769449-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "MSTR261030C00160000", "current_drop_pct": 1.05, "early_entry_score": 0.841, "early_reclaim_pct": 72.6, "entry_ask": 14.25, "entry_bid": 13.65, "entry_mode": "early", "entry_option_price": 13.95, "hypothetical_budget": 33976.65, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 590.0, "option_spread_pct": 4.3, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.758, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.841, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.604, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.758, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-24T11:25:06.367252-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "MSTR261030C00160000", "current_drop_pct": 0.89, "early_entry_score": 0.855, "early_reclaim_pct": 76.9, "entry_ask": 13.85, "entry_bid": 13.5, "entry_mode": "early", "entry_option_price": 13.675, "hypothetical_budget": 33976.65, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 590.0, "option_spread_pct": 2.56, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.764, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.855, "early_reclaim_pct": 76.9, "matched_signals": 35, "recovery_stability_score": 0.615, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.764, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-24T11:20:06.692131-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:15:04.671941-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924120004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924120004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924120004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924120004)

</details>
