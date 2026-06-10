# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 11:55:01 EDT`
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

- Cash: `$15,257.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 14965.0         2.05           2.05       52.68         52.66          bid_ask_mid                       2.05                bid_ask_mid                    True             0.0                    0.0         93.55               31              0.59         45.34           45.24                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           96.55               29            0.67              0.57        120.12                60.79         0.630          pass              0.768             59.5                           0.406               -0.10              0.150                                 ok            True                  False
  MRVL          100.00               15            3.78              7.06        263.86               141.19         0.629          pass              0.578             27.4                           0.222               29.24              3.473                                 ok            True                  False
  CTSH           90.32               31            0.57              0.21         52.85                47.83         0.569          pass              0.702             76.6                           0.571               -0.98             -0.405                                 ok            True                   True
   MAR           92.31               13            1.42              3.92        391.93                22.12         0.550          pass              0.431              9.4                           0.086                0.56              0.312                                 ok            True                  False
  REGN           84.85               33            0.91              3.91        614.51                44.80         0.534          pass              0.451             38.5                           0.342               -2.73             -0.032                                 ok            True                  False
  CDNS           92.86               28            1.16              3.18        389.54                58.96         0.530          pass              0.724             69.6                           0.400                3.29              0.261                                 ok            True                  False
  VRTX           94.74               19            1.49              4.64        443.78                26.58         0.530          pass              0.521              5.2                           0.130                0.44              0.044                                 ok            True                  False
  INTU           71.43               21            2.57              5.29        291.51               101.32         0.690          pass              0.227             28.1                           0.512               -6.99             -1.161 downtrend_blocked_slope_and_streak           False                  False
  DRAM          100.00               11            2.76              1.16         59.36               102.89         0.666          pass              0.618             48.1                           0.285               -4.15             -0.884            downtrend_blocked_slope           False                  False
  TEAM           93.02               43            0.12              0.08         95.58                85.52         0.618          pass              0.901             97.4                           0.799                7.22             -0.196                                 ok           False                  False
   WBD           92.86               14            0.62              0.12         26.51                13.67         0.577          pass              0.476             16.2                           0.259               -2.75             -0.321            downtrend_blocked_slope           False                  False
    MU           72.22               18            3.41             22.32        926.32               110.66         0.576          pass              0.203             30.8                           0.208               -2.63             -0.524            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-10T11:55:01.302337-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:50:05.519116-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:45:05.407070-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "ABNB260717C00130000", "current_drop_pct": 0.75, "early_entry_score": 0.701, "early_reclaim_pct": 66.6, "entry_ask": 6.35, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.175, "hypothetical_budget": 7628.63, "hypothetical_contracts": 12, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 698.0, "option_spread_pct": 5.67, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 91.18, "ticker": "ABNB", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.75, "early_entry_score": 0.701, "early_reclaim_pct": 66.6, "matched_signals": 34, "recovery_stability_score": 0.664, "success_rate": 91.18, "ticker": "ABNB", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:40:04.221259-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:35:01.384925-04:00 early_entry_1135 early_entry_shadow            {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.85, "early_entry_score": 0.824, "early_reclaim_pct": 81.1, "entry_ask": 10.0, "entry_bid": 8.9, "entry_mode": "early", "entry_option_price": 9.45, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 39, "option_liquidity_status": "low_volume", "option_open_interest": 627.0, "option_spread_pct": 11.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.596, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.824, "early_reclaim_pct": 81.1, "matched_signals": 39, "recovery_stability_score": 0.55, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.596, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.785, "early_reclaim_pct": 87.3, "matched_signals": 40, "recovery_stability_score": 0.624, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.567, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:30:03.299935-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.6, "early_entry_score": 0.858, "early_reclaim_pct": 86.6, "entry_ask": 9.9, "entry_bid": 8.6, "entry_mode": "early", "entry_option_price": 9.25, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 14.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.599, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.858, "early_reclaim_pct": 86.6, "matched_signals": 41, "recovery_stability_score": 0.604, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.599, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:25:01.359589-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.2, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.2, "matched_signals": 41, "recovery_stability_score": 0.593, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:20:02.310347-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 79.7, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.588, "shadow_only": true, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 79.7, "matched_signals": 39, "recovery_stability_score": 0.588, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.592, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.735, "early_reclaim_pct": 84.2, "matched_signals": 37, "recovery_stability_score": 0.627, "success_rate": 89.19, "ticker": "WDAY", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:15:04.333810-04:00 early_entry_1115 early_entry_shadow   {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.73, "early_reclaim_pct": 82.5, "matched_signals": 37, "recovery_stability_score": 0.677, "success_rate": 89.19, "ticker": "WDAY", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:10:04.307912-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610115501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610115501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610115501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610115501)

</details>
