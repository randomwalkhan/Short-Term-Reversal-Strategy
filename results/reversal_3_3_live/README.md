# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 10:20:02 EDT`
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
- Equity: `$27,430.75`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,445.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 14067.5         7.43           8.28       68.52         70.92          bid_ask_mid                       8.28                bid_ask_mid                    True          1445.0                  11.45         90.91               11              3.59         94.78           90.58                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.00               20            1.05              0.89        120.65                34.81         0.585          pass              0.191             21.9                           0.212                5.93              0.493                                 ok            True                  False
  MDLZ           91.67               12            1.30              0.56         61.91                20.23         0.574          pass              0.414             10.6                           0.160                0.45              0.210                                 ok            True                  False
   LIN           96.15               26            0.73              2.64        517.04                19.32         0.520          pass              0.691             44.2                           0.526                4.06              0.415                                 ok            True                  False
  SBUX           85.19               27            0.59              0.42        101.50                25.47         0.520          pass              0.495             63.9                           0.419                5.83              0.904                                 ok            True                  False
  GOOG           84.21               19            1.43              3.71        369.51                27.92         0.518          pass              0.328             34.6                           0.455                2.91              0.097                                 ok            True                  False
  CTAS           96.00               25            1.05              1.29        176.16                29.79         0.509          pass              0.692             47.1                           0.327                0.89              0.050                                 ok            True                  False
    ZS           78.05               41            0.37              0.33        127.09               152.67         0.876          pass              0.539             84.0                           0.603               -5.66             -0.544 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.09              0.18         23.72                25.54         0.695          pass              0.486              5.5                           0.085                5.30              0.805                                 ok           False                  False
   PEP          100.00                3            1.75              1.78        145.36                20.43         0.626          pass              0.463              0.0                           0.162                2.17              0.366                                 ok           False                  False
   CSX           83.33                6            1.34              0.44         46.71                20.12         0.614          pass              0.180             10.0                           0.212                0.28              0.186                                 ok           False                  False
  TEAM           88.10               42            0.36              0.22         87.85                81.06         0.598          pass              0.752             92.1                           0.864              -13.69             -1.591 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               25            0.16              0.09         78.94                23.22         0.595          pass              0.796             78.7                           0.553                2.02              0.277                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-06-17T10:20:02.964904-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "entry_mode": "early", "error": "IDXX: no call expiries found in the 21-40 trading-day window.", "matched_signals": 45, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "matched_signals": 45, "recovery_stability_score": 0.602, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:15:03.936200-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:10:04.940623-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "entry_ask": 7.5, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 5.6, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 67.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.638, "shadow_only": true, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.638, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.701, "early_reclaim_pct": 63.3, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 91.43, "ticker": "CPRT", "timing_score": 0.397, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:05:01.950296-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"current_drop_pct": 0.55, "early_entry_score": 0.743, "early_reclaim_pct": 68.8, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.39, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.743, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.693, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.39, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:00:05.066819-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T15:10:02.062608-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T15:05:05.056304-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T15:00:03.019624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T14:55:06.031514-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-06-16T14:50:02.059942-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-16", "training_samples": 5231, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617102002)

</details>
