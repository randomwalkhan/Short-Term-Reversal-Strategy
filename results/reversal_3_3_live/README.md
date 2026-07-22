# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 11:10:01 EDT`
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

- Cash: `$17,264.25`
- Equity: `$34,094.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$-82.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 16830.0         3.08           3.06       55.67         55.44          bid_ask_mid                       3.06                bid_ask_mid                    True           -82.5                  -0.49          80.0               10              2.03         42.85            47.9                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            0.84              0.35         58.70               115.77         0.723          pass              0.525             84.3                           0.749               -5.94             -1.368                                 ok            True                  False
  PYPL           86.67               30            0.73              0.28         55.73                62.33         0.652          pass              0.453             25.7                           0.389               24.51              2.789                                 ok            True                  False
  AAPL           95.83               24            0.94              2.15        326.82                37.60         0.593          pass              0.601             16.2                           0.336                3.60              0.530                                 ok            True                  False
   ADP           95.65               23            1.05              1.81        245.44                36.45         0.571          pass              0.575             10.6                           0.200                0.94              0.329                                 ok            True                  False
  PAYX          100.00               26            1.01              0.79        111.62                33.94         0.545          pass              0.610             16.3                           0.238                3.99              0.656                                 ok            True                  False
  ABNB           93.75               16            2.20              2.22        143.15                31.72         0.521          pass              0.482              7.7                           0.317               -1.42             -0.200                                 ok            True                  False
  PANW           90.00               20            2.46              5.90        339.62                60.47         0.511          pass              0.497             37.6                           0.275                4.10              0.560                                 ok            True                  False
  CTSH           87.18               39            0.74              0.23         43.53                49.89         0.506          pass              0.540             35.0                           0.411                2.06              0.298                                 ok            True                  False
  AMAT           90.62               32            0.74              2.92        563.30               100.84         0.715          pass              0.753             83.9                           0.714               -1.77             -0.811 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.32               31            0.62              1.41        321.40                94.63         0.686          pass              0.744             86.6                           0.723               -3.95             -1.044 downtrend_blocked_slope_and_streak           False                  False
  ISRG           70.83               24            1.37              3.37        348.62                68.15         0.627          pass              0.176              6.8                           0.176              -16.83             -2.057            downtrend_blocked_slope           False                  False
  META           72.73               11            2.28             10.29        639.40                51.99         0.607          pass              0.088              6.9                           0.215                4.31              0.140                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-07-22T11:10:01.815938-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:05:06.654140-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:00:03.703283-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:55:01.795388-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "ASML260821C01800000", "current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "entry_ask": 123.4, "entry_bid": 119.9, "entry_mode": "early", "entry_option_price": 121.65, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 224.0, "option_spread_pct": 2.88, "option_volume": 138.0, "reason": "shadow_insufficient_cash", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 34, "recovery_stability_score": 0.597, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T10:50:06.298041-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:45:04.805546-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:40:06.812850-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:35:07.269157-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PANW260821C00340000", "current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "entry_ask": 24.8, "entry_bid": 23.4, "entry_mode": "early", "entry_option_price": 24.1, "hypothetical_budget": 8632.13, "hypothetical_contracts": 3, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 923.0, "option_spread_pct": 5.81, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "top_candidates": [{"current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "matched_signals": 31, "recovery_stability_score": 0.611, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.712, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-22T10:30:05.882610-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                     {"contract_symbol": "CRWD260821C00190000", "current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "entry_ask": 14.05, "entry_bid": 13.05, "entry_mode": "early", "entry_option_price": 13.55, "hypothetical_budget": 8632.13, "hypothetical_contracts": 6, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1740.0, "option_spread_pct": 7.38, "option_volume": 66.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "matched_signals": 39, "recovery_stability_score": 0.712, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-22T10:25:01.797338-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                      {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.98, "early_entry_score": 0.749, "early_reclaim_pct": 63.4, "entry_ask": 121.7, "entry_bid": 103.0, "entry_mode": "early", "entry_option_price": 112.35, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 111.0, "option_spread_pct": 16.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.75, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.749, "early_reclaim_pct": 63.4, "matched_signals": 32, "recovery_stability_score": 0.662, "success_rate": 93.75, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722111001)

</details>
