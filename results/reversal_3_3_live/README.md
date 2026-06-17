# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 10:55:04 EDT`
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

- Cash: `$13,363.25`
- Equity: `$27,515.75`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,530.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 14152.5         7.43           8.32       68.52         70.76          bid_ask_mid                       8.32                bid_ask_mid                    True          1530.0                  12.12         90.91               11              3.59         94.78           91.55                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               21            0.71              0.50        100.07                31.37         0.594          pass              0.713             60.1                           0.429               -1.21              0.086                                 ok            True                  False
   WMT           80.00               20            1.12              0.95        120.62                34.81         0.580          pass              0.174             16.4                           0.224                5.85              0.490                                 ok            True                  False
  MDLZ           95.24               21            0.95              0.41         61.97                20.23         0.536          pass              0.630             34.4                           0.512                0.80              0.226                                 ok            True                  False
  SHOP           82.93               41            0.58              0.46        113.03                54.75         0.504          pass              0.547             72.8                           0.367               -0.33             -0.097                                 ok            True                  False
  CTAS           96.43               28            0.84              1.04        176.27                29.79         0.503          pass              0.743             57.7                           0.382                1.11              0.060                                 ok            True                  False
    ZS           76.47               34            1.30              1.15        126.74               152.67         0.867          pass              0.378             43.7                           0.280               -6.54             -0.587 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.92              0.15         23.73                25.54         0.704          pass              0.539             22.8                           0.321                5.48              0.813                                 ok           False                  False
  INTU           79.49               39            0.90              1.76        280.23                99.11         0.698          pass              0.458             65.1                           0.325              -13.56             -1.479 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                5            1.28              1.31        145.56                20.43         0.640          pass              0.545             27.0                           0.451                2.65              0.387                                 ok           False                  False
   CSX           80.00                5            1.48              0.49         46.69                20.12         0.607          pass              0.090              9.7                           0.198                0.14              0.180                                 ok           False                  False
  UPRO           94.12               34            0.24              0.24        144.04                48.01         0.588          pass              0.821             75.4                           0.410               -4.69             -0.481                                 ok           False                  False
   ADP           95.83               24            0.55              0.86        221.63                31.58         0.581          pass              0.736             61.6                           0.363               -3.78             -0.289            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-06-17T10:55:04.940733-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:50:01.959639-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:45:01.979292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:40:01.956283-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:35:06.928976-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:30:05.890992-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:25:01.204897-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:20:02.964904-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "entry_mode": "early", "error": "IDXX: no call expiries found in the 21-40 trading-day window.", "matched_signals": 45, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.794, "early_reclaim_pct": 66.4, "matched_signals": 45, "recovery_stability_score": 0.602, "success_rate": 93.33, "ticker": "IDXX", "timing_score": 0.392, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:15:03.936200-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "entry_mode": "early", "error": "CPRT: no call expiries found in the 21-40 trading-day window.", "matched_signals": 37, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.751, "early_reclaim_pct": 71.6, "matched_signals": 37, "recovery_stability_score": 0.622, "success_rate": 91.89, "ticker": "CPRT", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T10:10:04.940623-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "entry_ask": 7.5, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 5.6, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 67.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.638, "shadow_only": true, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.832, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.638, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.701, "early_reclaim_pct": 63.3, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 91.43, "ticker": "CPRT", "timing_score": 0.397, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617105504)

</details>
