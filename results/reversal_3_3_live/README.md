# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 12:55:05 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$1,421.80`
- Equity: `$134,769.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-2,922.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 62720.0         20.0          19.60      220.60        220.24          bid_ask_mid                      19.60                bid_ask_mid                    True         -1280.0                  -2.00         100.0               12              3.08         70.90           70.73                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 70627.5          1.1           1.08       44.42         44.22          bid_ask_mid                       1.08                bid_ask_mid                    True         -1642.5                  -2.27          80.0               15              0.97         20.09           24.46                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
 CMCSA           87.50               16            0.77              0.12         22.00                26.02         0.557          pass              0.383             29.2                           0.324                4.79              0.578                  ok            True                  False
   KDP           95.65               23            0.63              0.15         34.92                25.67         0.543          pass              0.748             69.0                           0.551                6.46              0.554                  ok            True                  False
  COST           81.82               11            1.24              8.69       1001.43                16.36         0.542          pass              0.152             14.3                           0.437                3.99              0.388                  ok            True                  False
   EXC           86.96               23            0.71              0.22         44.45                21.50         0.526          pass              0.386             20.3                           0.400                4.45              0.552                  ok            True                  False
  ORLY          100.00               12            1.70              1.08         90.58                20.34         0.519          pass              0.465              0.0                           0.187                4.03              0.458                  ok            True                  False
  TEAM          100.00               31            1.42              2.23        222.46                43.78         0.510          pass              0.700             36.2                           0.475                5.86              0.880                  ok            True                  False
  ABNB           84.21               19            1.55              1.86        170.25                25.32         0.501          pass              0.312             29.9                           0.367                1.70              0.139                  ok            True                  False
  MDLZ           87.50                8            1.29              0.57         62.73                25.86         0.595          pass              0.262              0.7                           0.197                1.07              0.132                  ok           False                  False
   PEP           80.00                5            1.57              1.49        134.82                25.06         0.583          pass              0.058              0.0                           0.168                4.74              0.640                  ok           False                  False
   KHC           87.50                8            2.24              0.39         24.56                34.80         0.568          pass              0.265              2.6                           0.235                7.78              0.943                  ok           False                  False
   ROP           76.92               13            1.58              4.88        439.56                39.00         0.563          pass              0.193             38.8                           0.492               17.99              2.011                  ok           False                  False
   WMT           78.57               14            1.12              0.94        119.89                23.89         0.546          pass              0.107              8.5                           0.302                5.94              0.464                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-27T12:00:05.676478-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "matched_signals": 42, "recovery_stability_score": 0.692, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T11:55:06.030396-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:50:05.158961-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:45:04.083038-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:40:06.585395-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:35:05.021467-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.823, "early_reclaim_pct": 78.9, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.823, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.774, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T11:30:06.374042-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:25:06.123076-04:00 early_entry_1125 early_entry_shadow                                                {"contract_symbol": "GILD261218C00160000", "current_drop_pct": 0.66, "early_entry_score": 0.687, "early_reclaim_pct": 64.5, "entry_ask": 7.15, "entry_bid": 6.75, "entry_mode": "early", "entry_option_price": 6.95, "hypothetical_budget": 1421.8, "hypothetical_contracts": 2, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1422.0, "option_spread_pct": 5.76, "option_volume": 48.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.497, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.687, "early_reclaim_pct": 64.5, "matched_signals": 33, "recovery_stability_score": 0.641, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.497, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-27T11:20:06.377760-04:00 early_entry_1120 early_entry_shadow                                                {"contract_symbol": "GILD261218C00160000", "current_drop_pct": 0.61, "early_entry_score": 0.721, "early_reclaim_pct": 66.9, "entry_ask": 7.2, "entry_bid": 6.85, "entry_mode": "early", "entry_option_price": 7.025, "hypothetical_budget": 1421.8, "hypothetical_contracts": 2, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1422.0, "option_spread_pct": 4.98, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 91.43, "ticker": "GILD", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.721, "early_reclaim_pct": 66.9, "matched_signals": 35, "recovery_stability_score": 0.658, "success_rate": 91.43, "ticker": "GILD", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-27T11:15:02.025902-04:00 early_entry_1115 early_entry_shadow   {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.87, "early_entry_score": 0.741, "early_reclaim_pct": 66.5, "entry_ask": 13.6, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 17.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.708, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.741, "early_reclaim_pct": 66.5, "matched_signals": 37, "recovery_stability_score": 0.708, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027125505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027125505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027125505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027125505)

</details>
