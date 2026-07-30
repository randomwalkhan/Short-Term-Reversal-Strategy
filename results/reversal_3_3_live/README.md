# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 11:00:04 EDT`
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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KDP           85.00               20            0.91              0.20         31.36                34.46         0.590          pass              0.410             50.4                           0.679                2.99              0.042                      ok            True                  False
  VRTX           80.00               10            2.21              7.46        480.13                33.19         0.548          pass              0.109             17.9                           0.292               -0.76             -0.046                      ok            True                  False
  AMGN           90.91               11            1.81              4.92        385.53                27.22         0.546          pass              0.428             25.4                           0.470                7.14              0.710                      ok            True                  False
  ABNB           95.24               21            1.68              1.80        152.24                40.20         0.545          pass              0.635             35.9                           0.266                2.66              0.078                      ok            True                  False
  DXCM           80.95               21            1.70              0.90         74.76                45.20         0.533          pass              0.239             28.9                           0.387               -0.35             -0.324                      ok            True                  False
   HON           82.35               17            1.35              2.27        240.15                39.75         0.527          pass              0.203             13.7                           0.217                6.82              1.050                      ok            True                  False
  ROST           85.71               21            1.13              1.99        251.11                27.49         0.524          pass              0.326             16.1                           0.206               12.76              1.032                      ok            True                  False
  PCAR           84.21               19            1.49              1.40        133.27                29.38         0.519          pass              0.245              7.0                           0.208                6.40              0.902                      ok            True                  False
  IDXX           81.82               11            2.58             10.30        565.35                36.22         0.506          pass              0.122              5.4                           0.207                2.66             -0.054                      ok            True                  False
  DASH           97.37               38            0.99              1.34        192.95                53.51         0.503          pass              0.812             58.4                           0.507                2.03             -0.022                      ok            True                  False
  ISRG           78.57               28            1.03              2.54        352.01                72.57         0.661          pass              0.322             45.4                           0.361              -10.16             -0.980 downtrend_blocked_slope           False                  False
  PYPL           77.78                9            2.49              1.02         57.91                61.52         0.659          pass              0.091              8.5                           0.159                2.48              0.168                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-30T11:00:04.904053-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:55:01.879209-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:50:01.107758-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:45:05.898000-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:40:01.919519-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:35:01.875503-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:30:03.673843-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:25:02.736575-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:20:02.940055-04:00 early_entry_1020 early_entry_shadow                               {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "entry_ask": 16.05, "entry_bid": 14.75, "entry_mode": "early", "entry_option_price": 15.4, "hypothetical_budget": 16611.13, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 8.44, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.757, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "matched_signals": 41, "recovery_stability_score": 0.757, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T10:15:03.914804-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "matched_signals": 43, "recovery_stability_score": 0.762, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730110004)

</details>
