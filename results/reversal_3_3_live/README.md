# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 12:10:06 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$73,431.80`
- Equity: `$145,231.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 71800.0        17.85          17.95      223.97         225.0          bid_ask_mid                      17.95                bid_ask_mid                    True           400.0                   0.56         100.0               38              0.68         80.16           79.26                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           95.45               22            0.75              0.19         35.11                27.06         0.539          pass              0.722             62.7                           0.710                9.97              0.929                                 ok            True                  False
 CMCSA           92.31               13            0.85              0.14         22.78                23.88         0.533          pass              0.569             55.7                           0.404                9.61              1.046                                 ok            True                  False
   WMT           83.33               18            0.88              0.75        120.80                23.20         0.530          pass              0.299             34.8                           0.307                7.81              0.755                                 ok            True                  False
   EXC           82.35               17            0.88              0.28         44.73                20.91         0.528          pass              0.281             39.7                           0.493                6.45              0.575                                 ok            True                  False
   KHC           85.71               21            1.26              0.22         25.00                34.71         0.523          pass              0.401             41.1                           0.535               11.25              1.100                                 ok            True                  False
  AMGN           80.95               21            1.06              3.30        445.86                28.21         0.521          pass              0.253             34.0                           0.321                6.67              0.742                                 ok            True                  False
   AEP           83.33               18            0.86              0.79        130.30                17.81         0.519          pass              0.241             15.7                           0.283                5.46              0.481                                 ok            True                  False
   ADP           90.91               22            0.83              1.80        307.17                23.94         0.511          pass              0.613             63.7                           0.339               12.73              1.233                                 ok            True                  False
  ORLY          100.00               13            1.73              1.11         91.52                17.78         0.505          pass              0.511             13.4                           0.271                4.58              0.595                                 ok            True                  False
  MDLZ          100.00                1            2.33              1.06         64.73                24.03         0.569          pass              0.477              6.7                           0.177                5.40              0.533                                 ok           False                  False
   XEL           71.43                7            1.39              0.77         78.64                16.59         0.532          pass              0.053              0.0                           0.239                5.54              0.579                                 ok           False                  False
   WDC           75.00               44            0.47              1.15        353.70                71.39         0.527          pass              0.524             90.4                           0.676              -11.26             -0.890 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-23T12:00:05.040170-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:55:05.962130-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:50:05.123171-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:45:05.133222-04:00 early_entry_1145 early_entry_shadow                               {"contract_symbol": "TRI261218C00125000", "current_drop_pct": 0.54, "early_entry_score": 0.773, "early_reclaim_pct": 72.9, "entry_ask": 8.6, "entry_bid": 7.7, "entry_mode": "early", "entry_option_price": 8.15, "hypothetical_budget": 36715.9, "hypothetical_contracts": 45, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 133.0, "option_spread_pct": 11.04, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.773, "early_reclaim_pct": 72.9, "matched_signals": 38, "recovery_stability_score": 0.645, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:40:06.240161-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:35:04.567844-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:30:06.325430-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:25:04.050092-04:00 early_entry_1125 early_entry_shadow           {"contract_symbol": "IDXX261218C00560000", "current_drop_pct": 0.53, "early_entry_score": 0.77, "early_reclaim_pct": 64.2, "entry_ask": 37.3, "entry_bid": 33.0, "entry_mode": "early", "entry_option_price": 35.15, "hypothetical_budget": 36715.9, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 12.0, "option_spread_pct": 12.23, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.77, "early_reclaim_pct": 64.2, "matched_signals": 40, "recovery_stability_score": 0.688, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:20:06.118477-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:15:05.326587-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "MAR261127C00395000", "current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 62.0, "entry_ask": 16.1, "entry_bid": 13.1, "entry_mode": "early", "entry_option_price": 14.6, "hypothetical_budget": 36715.9, "hypothetical_contracts": 25, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 20.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 91.67, "ticker": "MAR", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 62.0, "matched_signals": 36, "recovery_stability_score": 0.676, "success_rate": 91.67, "ticker": "MAR", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023121006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023121006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023121006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023121006)

</details>
