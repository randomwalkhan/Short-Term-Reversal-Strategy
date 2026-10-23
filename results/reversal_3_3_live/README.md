# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 13:05:05 EDT`
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

- Cash: `$73,431.80`
- Equity: `$144,231.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 70800.0        17.85           17.7      223.97        224.97          bid_ask_mid                       17.7                bid_ask_mid                    True          -600.0                  -0.84         100.0               38              0.68         80.16           78.97                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.74               19            0.88              0.22         35.10                27.06         0.548          pass              0.677             56.3                           0.506                9.82              0.923                                 ok            True                  False
   KHC           81.25               16            1.61              0.28         24.97                34.71         0.527          pass              0.199             24.3                           0.250               10.84              1.083                                 ok            True                  False
   EXC           80.00               15            1.06              0.33         44.71                20.91         0.527          pass              0.168             27.5                           0.303                6.26              0.567                                 ok            True                  False
   MAR           88.24               17            1.12              3.11        395.47                21.06         0.525          pass              0.396             25.6                           0.210                7.24              0.940                                 ok            True                  False
 CMCSA           86.67               15            0.83              0.13         22.78                23.88         0.516          pass              0.433             56.8                           0.429                9.63              1.047                                 ok            True                  False
  COST           86.67               15            1.19              8.48       1014.58                17.03         0.512          pass              0.297             11.5                           0.333                6.25              0.653                                 ok            True                  False
  ORLY          100.00               13            1.63              1.05         91.55                17.78         0.510          pass              0.526             18.3                           0.417                4.68              0.599                                 ok            True                  False
   ADP           91.30               23            0.79              1.71        307.21                23.94         0.508          pass              0.635             65.4                           0.412               12.78              1.235                                 ok            True                  False
  SBUX           85.71               21            1.32              0.95        101.50                25.63         0.503          pass              0.283              2.2                           0.158               10.81              1.154                                 ok            True                  False
   CEG           85.00               40            0.28              0.50        255.00                65.49         0.583          pass              0.665             91.0                           0.599              -14.62             -1.653 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.59              1.18         64.68                24.03         0.553          pass              0.468              4.3                           0.206                5.12              0.521                                 ok           False                  False
   CSX           71.43                7            1.55              0.56         51.43                26.41         0.540          pass              0.189             45.0                           0.556                7.64              0.635                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023130505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023130505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023130505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023130505)

</details>
