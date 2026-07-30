# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 10:30:03 EDT`
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
  PYPL           81.82               11            2.18              0.89         57.97                61.52         0.676          pass              0.134              3.8                           0.203                2.81              0.183                      ok            True                  False
   CSX          100.00               11            1.29              0.46         50.54                28.82         0.604          pass              0.486              6.4                           0.188                1.33              0.259                      ok            True                  False
   KDP           82.35               17            1.24              0.27         31.33                34.46         0.584          pass              0.264             32.2                           0.446                2.64              0.027                      ok            True                  False
  MNST           94.12               17            0.95              0.64         96.95                25.74         0.563          pass              0.692             70.7                           0.467               -1.73             -0.257                      ok            True                  False
  ABNB           93.75               16            1.91              2.04        152.13                40.20         0.561          pass              0.544             27.2                           0.214                2.42              0.068                      ok            True                  False
  VRTX           80.00               10            2.22              7.52        480.11                33.19         0.547          pass              0.107             17.3                           0.157               -0.78             -0.047                      ok            True                  False
   HON           84.21               19            1.05              1.77        240.36                39.75         0.537          pass              0.309             27.6                           0.257                7.14              1.064                      ok            True                  False
  IDXX           84.62               13            2.36              9.40        565.74                36.22         0.512          pass              0.235             13.7                           0.226                2.90             -0.044                      ok            True                  False
  DASH           96.97               33            1.42              1.92        192.71                53.51         0.508          pass              0.726             40.7                           0.381                1.60             -0.041                      ok            True                  False
  PCAR           90.62               32            0.57              0.53        133.64                29.38         0.504          pass              0.626             48.6                           0.590                7.40              0.944                      ok            True                  False
  ROST           88.46               26            0.99              1.75        251.21                27.49         0.503          pass              0.461             26.1                           0.248               12.91              1.038                      ok            True                  False
  ISRG           76.00               25            1.22              3.02        351.81                72.57         0.664          pass              0.272             35.1                           0.199              -10.33             -0.989 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-30T10:30:03.673843-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:25:02.736575-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:20:02.940055-04:00 early_entry_1020 early_entry_shadow                               {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "entry_ask": 16.05, "entry_bid": 14.75, "entry_mode": "early", "entry_option_price": 15.4, "hypothetical_budget": 16611.13, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 8.44, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.757, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "matched_signals": 41, "recovery_stability_score": 0.757, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T10:15:03.914804-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "matched_signals": 43, "recovery_stability_score": 0.762, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:10:02.887573-04:00 early_entry_1010 early_entry_shadow           {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "matched_signals": 43, "recovery_stability_score": 0.729, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:05:01.868497-04:00 early_entry_1005 early_entry_shadow             {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "matched_signals": 40, "recovery_stability_score": 0.681, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:00:05.892455-04:00 early_entry_1000 early_entry_shadow                                    {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "entry_ask": 18.65, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.975, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 379.0, "option_spread_pct": 7.51, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T09:55:02.964620-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "FAST260918C00045000", "fill_price": 3.465, "pnl": -1732.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "FAST"}
2026-07-29T15:10:04.505433-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-29T15:05:04.399519-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730103003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730103003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730103003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730103003)

</details>
