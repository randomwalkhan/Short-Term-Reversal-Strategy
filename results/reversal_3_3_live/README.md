# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 14:50:02 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           80.00               35            0.86              0.26         43.07                65.21         0.591          pass              0.287             20.4                           0.215               10.53              0.864                                 ok            True                  False
  MPWR           81.82               22            3.69             34.93       1337.69                84.79         0.577          pass              0.267             27.1                           0.341               -5.76             -0.017                                 ok            True                  False
  UPRO           89.47               19            1.55              1.58        145.19                41.96         0.572          pass              0.428             19.3                           0.311                1.28              0.247                                 ok            True                  False
   WBD           87.50               16            0.81              0.16         27.20                20.00         0.531          pass              0.521             76.0                           0.700                1.46              0.246                                 ok            True                  False
  FTNT           95.45               22            1.76              2.03        163.64                41.65         0.508          pass              0.671             46.7                           0.380                5.20              0.516                                 ok            True                  False
  KLAC           84.00               25            1.86              2.92        223.25               109.33         0.724          pass              0.445             55.2                           0.373              -26.97             -2.111 downtrend_blocked_slope_and_streak           False                  False
  AMAT           80.00               15            3.27             13.26        573.75                98.89         0.653          pass              0.179             26.8                           0.225              -22.48             -1.528 downtrend_blocked_slope_and_streak           False                  False
  MSTR           70.59               34            2.18              1.48         96.83               100.18         0.624          pass              0.364             47.3                           0.516                9.69              0.335                                 ok           False                  False
  META           78.57               14            1.98              9.45        677.26                54.55         0.611          pass              0.139             17.2                           0.216                8.96              1.318                                 ok           False                  False
  ASML           93.75               32            1.12             14.20       1809.19                66.00         0.602          pass              0.742             56.1                           0.366               -9.77             -0.659            downtrend_blocked_slope           False                  False
   TXN           77.78                9            3.39              7.14        298.13                65.52         0.584          pass              0.117             19.6                           0.321               -2.38              0.127                                 ok           False                  False
   ADI           78.57               14            2.75              7.53        387.73                55.85         0.579          pass              0.142             19.2                           0.299               -4.27             -0.014                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-16T14:50:02.142710-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"early_entry_score": 0.671, "option_liquidity_status": "low_volume", "option_open_interest": 761.0, "option_spread_pct": 4.13, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.508}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.521, "option_liquidity_status": "wide_spread", "option_open_interest": 3043.0, "option_spread_pct": 25.76, "option_volume": 343.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.531}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"early_entry_score": 0.267, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 84.0, "option_spread_pct": 8.5, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.577}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.287, "option_liquidity_status": "low_volume", "option_open_interest": 859.0, "option_spread_pct": 12.05, "option_volume": 16.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.591}
2026-07-16T14:50:02.142710-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-16", "training_samples": 5411, "window": 5}
2026-07-16T12:00:02.316099-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:55:05.282861-04:00 early_entry_1155      early_entry_shadow  {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "entry_ask": 16.9, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 16.5, "hypothetical_budget": 14612.13, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 4.85, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "matched_signals": 42, "recovery_stability_score": 0.646, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:50:01.317315-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "entry_ask": 16.7, "entry_bid": 15.75, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.86, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "matched_signals": 40, "recovery_stability_score": 0.61, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716145002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716145002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716145002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716145002)

</details>
