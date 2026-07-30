# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 10:15:03 EDT`
Last processed slot: `early_entry_1015`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           83.33               12            1.80              0.74         58.03                61.52         0.698          pass              0.172              0.0                           0.242                3.21              0.200                  ok            True                  False
   KDP           82.35               17            1.19              0.26         31.34                34.46         0.587          pass              0.267             33.0                           0.466                2.69              0.029                  ok            True                  False
   CSX           94.12               17            1.01              0.36         50.59                28.82         0.578          pass              0.524             14.3                           0.164                1.62              0.272                  ok            True                  False
   MAR          100.00               14            1.40              3.74        379.52                28.18         0.575          pass              0.657             57.6                           0.623                3.47              0.347                  ok            True                  False
  VRTX           81.82               11            2.10              7.09        480.29                33.19         0.551          pass              0.176             22.0                           0.201               -0.65             -0.041                  ok            True                  False
  ABNB           95.24               21            1.59              1.71        152.28                40.20         0.550          pass              0.646             39.1                           0.266                2.75              0.082                  ok            True                  False
  AMGN           90.00               10            1.92              5.20        385.41                27.22         0.549          pass              0.351              9.7                           0.157                7.03              0.705                  ok            True                  False
  MNST           95.65               23            0.72              0.49         97.02                25.74         0.540          pass              0.774             77.8                           0.706               -1.51             -0.246                  ok            True                  False
   HON           86.36               22            0.99              1.67        240.41                39.75         0.524          pass              0.398             31.9                           0.331                7.21              1.067                  ok            True                  False
  DXCM           84.62               26            1.52              0.80         74.80                45.20         0.517          pass              0.391             36.7                           0.539               -0.16             -0.316                  ok            True                  False
  ROST           88.46               26            0.81              1.43        251.35                27.49         0.515          pass              0.502             39.4                           0.357               13.12              1.046                  ok            True                  False
  IDXX           81.25               16            2.11              8.44        566.15                36.22         0.510          pass              0.128              1.3                           0.087                3.15             -0.032                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-30T10:15:03.914804-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "matched_signals": 43, "recovery_stability_score": 0.762, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:10:02.887573-04:00 early_entry_1010 early_entry_shadow           {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "matched_signals": 43, "recovery_stability_score": 0.729, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:05:01.868497-04:00 early_entry_1005 early_entry_shadow             {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "matched_signals": 40, "recovery_stability_score": 0.681, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:00:05.892455-04:00 early_entry_1000 early_entry_shadow                                    {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "entry_ask": 18.65, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.975, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 379.0, "option_spread_pct": 7.51, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T09:55:02.964620-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "FAST260918C00045000", "fill_price": 3.465, "pnl": -1732.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "FAST"}
2026-07-29T15:10:04.505433-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-29T15:05:04.399519-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-29T15:00:04.380256-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-29T14:55:04.522646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-29T14:50:04.497983-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 17325.0, "asset_type": "option", "contract_symbol": "FAST260918C00045000", "contracts": 45, "early_entry_score": 0.745, "entry_mode": "regular", "entry_option_price": 3.85, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 324.0, "option_spread_pct": 7.79, "option_volume": 33.0, "success_rate": 100.0, "ticker": "FAST", "timing_score": 0.573}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730101503)

</details>
