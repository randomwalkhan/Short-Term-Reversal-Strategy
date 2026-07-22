# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 11:15:05 EDT`
Last processed slot: `early_entry_1115`

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
- Equity: `$34,369.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$192.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 17105.0         3.08           3.11       55.67          55.5          bid_ask_mid                       3.11                bid_ask_mid                    True           192.5                   1.14          80.0               10              2.03         42.85           47.12                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            0.93              0.39         58.68               115.77         0.718          pass              0.520             82.5                           0.778               -6.03             -1.372                                 ok            True                  False
  PYPL           87.10               31            0.63              0.25         55.74                62.33         0.652          pass              0.502             35.8                           0.467               24.64              2.794                                 ok            True                  False
  AAPL           95.00               20            1.08              2.47        326.68                37.60         0.610          pass              0.539              3.8                           0.199                3.45              0.524                                 ok            True                  False
   ADP           95.24               21            1.24              2.14        245.30                36.45         0.569          pass              0.542              3.8                           0.172                0.74              0.320                                 ok            True                  False
  PAYX          100.00               24            1.13              0.89        111.58                33.94         0.550          pass              0.566              5.9                           0.154                3.86              0.650                                 ok            True                  False
  PANW           90.48               21            2.30              5.51        339.79                60.47         0.516          pass              0.530             41.7                           0.338                4.27              0.568                                 ok            True                  False
  AMZN           84.21               19            1.61              2.79        246.35                25.29         0.511          pass              0.231              2.4                           0.165               -0.02              0.066                                 ok            True                  False
  CTAS           91.43               35            0.64              0.90        200.03                36.86         0.507          pass              0.696             57.8                           0.281               10.52              1.506                                 ok            True                  False
  CTSH           87.18               39            0.78              0.24         43.53                49.89         0.504          pass              0.531             32.0                           0.375                2.03              0.297                                 ok            True                  False
  AMAT           90.32               31            0.82              3.22        563.17               100.84         0.715          pass              0.734             82.3                           0.755               -1.85             -0.814 downtrend_blocked_slope_and_streak           False                  False
  LRCX           89.66               29            0.75              1.69        321.27                94.63         0.689          pass              0.705             83.9                           0.775               -4.07             -1.050 downtrend_blocked_slope_and_streak           False                  False
  ISRG           74.07               27            1.22              2.98        348.78                68.15         0.622          pass              0.228             17.5                           0.222              -16.69             -2.050            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-07-22T11:15:05.770543-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:10:01.815938-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:05:06.654140-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:00:03.703283-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:55:01.795388-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "ASML260821C01800000", "current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "entry_ask": 123.4, "entry_bid": 119.9, "entry_mode": "early", "entry_option_price": 121.65, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 224.0, "option_spread_pct": 2.88, "option_volume": 138.0, "reason": "shadow_insufficient_cash", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 34, "recovery_stability_score": 0.597, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T10:50:06.298041-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:45:04.805546-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:40:06.812850-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:35:07.269157-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PANW260821C00340000", "current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "entry_ask": 24.8, "entry_bid": 23.4, "entry_mode": "early", "entry_option_price": 24.1, "hypothetical_budget": 8632.13, "hypothetical_contracts": 3, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 923.0, "option_spread_pct": 5.81, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "top_candidates": [{"current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "matched_signals": 31, "recovery_stability_score": 0.611, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.712, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-22T10:30:05.882610-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                     {"contract_symbol": "CRWD260821C00190000", "current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "entry_ask": 14.05, "entry_bid": 13.05, "entry_mode": "early", "entry_option_price": 13.55, "hypothetical_budget": 8632.13, "hypothetical_contracts": 6, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1740.0, "option_spread_pct": 7.38, "option_volume": 66.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "matched_signals": 39, "recovery_stability_score": 0.712, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722111505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722111505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722111505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722111505)

</details>
