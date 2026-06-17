# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 10:30:05 EDT`
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

- Cash: `$13,363.25`
- Equity: `$26,538.25`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$552.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 13175.0         7.43           7.75       68.52         70.85          bid_ask_mid                       7.75                bid_ask_mid                    True           552.5                   4.38         90.91               11              3.59         94.78           84.62                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            0.98              0.83        120.67                34.81         0.583          pass              0.237             26.5                           0.223                6.00              0.496                                 ok            True                  False
  MDLZ           94.12               17            1.09              0.48         61.95                20.23         0.554          pass              0.552             24.4                           0.282                0.65              0.219                                 ok            True                  False
  GOOG           81.25               16            1.66              4.31        369.25                27.92         0.521          pass              0.197             24.0                           0.421                2.67              0.087                                 ok            True                  False
  SBUX           84.62               26            0.72              0.51        101.46                25.47         0.518          pass              0.449             55.7                           0.334                5.69              0.898                                 ok            True                  False
 GOOGL           84.62               13            1.76              4.60        371.28                28.01         0.509          pass              0.260             22.2                           0.394                1.40              0.007                                 ok            True                  False
  CTAS           96.30               27            0.93              1.16        176.21                29.79         0.503          pass              0.722             52.9                           0.298                1.01              0.055                                 ok            True                  False
    ZS           76.92               39            0.46              0.41        127.05               152.67         0.878          pass              0.521             79.9                           0.601               -5.75             -0.549 downtrend_blocked_slope_and_streak           False                  False
  INTU           80.00               45            0.14              0.27        280.87                99.11         0.709          pass              0.555             94.6                           0.639              -12.90             -1.445 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.86              0.14         23.74                25.54         0.707          pass              0.555             28.1                           0.234                5.55              0.816                                 ok           False                  False
   PEP          100.00                4            1.50              1.53        145.46                20.43         0.634          pass              0.507             14.6                           0.250                2.43              0.377                                 ok           False                  False
  MCHP           94.44               36            0.07              0.05         95.61                60.62         0.625          pass              0.884             87.5                           0.489               -1.44              0.148                                 ok           False                  False
   CSX           87.50                8            1.23              0.40         46.73                20.12         0.610          pass              0.323             20.7                           0.302                0.40              0.191                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-06-17T10:30:05.890992-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:25:01.204897-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:20:02.964904-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "entry_mode": "early", "error": "IDXX: no call expiries found in the 21-40 trading-day window.", "matched_signals": 45, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "matched_signals": 45, "recovery_stability_score": 0.602, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:15:03.936200-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:10:04.940623-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "entry_ask": 7.5, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 5.6, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 67.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.638, "shadow_only": true, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.638, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.701, "early_reclaim_pct": 63.3, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 91.43, "ticker": "CPRT", "timing_score": 0.397, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:05:01.950296-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"current_drop_pct": 0.55, "early_entry_score": 0.743, "early_reclaim_pct": 68.8, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.39, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.743, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.693, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.39, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:00:05.066819-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T15:10:02.062608-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T15:05:05.056304-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T15:00:03.019624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617103005)

</details>
