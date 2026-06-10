# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 11:25:01 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$30,404.75`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$182.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 15147.5         2.05           2.08       52.68         52.57          bid_ask_mid                       2.08                bid_ask_mid                    True           182.5                   1.22         93.55               31              0.59         45.34           46.56                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               19            2.81              5.24        264.63               141.19         0.666          pass              0.665             46.0                           0.265               30.54              3.518                                 ok            True                  False
  CSCO           96.67               30            0.54              0.46        120.16                60.79         0.632          pass              0.799             67.5                           0.377                0.03              0.156                                 ok            True                  False
    MU           80.00               25            2.18             14.27        929.78               110.66         0.621          pass              0.329             55.8                           0.296               -1.39             -0.466                                 ok            True                  False
  TEAM           92.68               41            0.58              0.39         95.44                85.52         0.601          pass              0.860             87.2                           0.593                6.73             -0.217                                 ok            True                   True
  CTSH           90.32               31            0.81              0.30         52.81                47.83         0.554          pass              0.670             66.4                           0.399               -1.22             -0.416                                 ok            True                  False
  REGN           84.38               32            0.96              4.14        614.40                44.80         0.537          pass              0.421             34.7                           0.308               -2.78             -0.035                                 ok            True                  False
  ISRG           81.25               16            1.77              5.27        424.35                33.80         0.531          pass              0.177             16.8                           0.156                0.13              0.072                                 ok            True                  False
  VRTX           95.65               23            1.20              3.76        444.16                26.58         0.520          pass              0.601             20.7                           0.156                0.73              0.057                                 ok            True                  False
  CDNS           94.29               35            0.79              2.17        389.97                58.96         0.506          pass              0.836             79.2                           0.378                3.68              0.278                                 ok            True                  False
  DRAM          100.00               14            1.79              0.75         59.54               102.89         0.705          pass              0.696             66.4                           0.332               -3.19             -0.839            downtrend_blocked_slope           False                  False
  INTU           66.67               18            2.96              6.08        291.17               101.32         0.680          pass              0.174             17.4                           0.318               -7.36             -1.179 downtrend_blocked_slope_and_streak           False                  False
  WDAY           90.00               40            0.49              0.48        140.02                67.85         0.572          pass              0.791             89.0                           0.628               12.08              0.586                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-10T11:25:01.359589-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.2, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.86, "early_reclaim_pct": 87.2, "matched_signals": 41, "recovery_stability_score": 0.593, "success_rate": 92.68, "ticker": "TEAM", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:20:02.310347-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 79.7, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.588, "shadow_only": true, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 79.7, "matched_signals": 39, "recovery_stability_score": 0.588, "success_rate": 92.31, "ticker": "TEAM", "timing_score": 0.592, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.735, "early_reclaim_pct": 84.2, "matched_signals": 37, "recovery_stability_score": 0.627, "success_rate": 89.19, "ticker": "WDAY", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:15:04.333810-04:00 early_entry_1115 early_entry_shadow   {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "entry_ask": 9.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.95, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 16.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.79, "early_reclaim_pct": 77.7, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.599, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.73, "early_reclaim_pct": 82.5, "matched_signals": 37, "recovery_stability_score": 0.677, "success_rate": 89.19, "ticker": "WDAY", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T11:10:04.307912-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:05:01.212784-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:00:04.519159-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:55:01.275812-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:50:04.358355-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "ABNB260717C00135000", "current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "entry_ask": 4.45, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.325, "hypothetical_budget": 7628.63, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 490.0, "option_spread_pct": 5.78, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "matched_signals": 37, "recovery_stability_score": 0.608, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:45:02.614919-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:40:02.425306-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                      {"contract_symbol": "WDAY260717C00140000", "current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "entry_ask": 11.0, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.55, "hypothetical_budget": 7628.63, "hypothetical_contracts": 7, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 684.0, "option_spread_pct": 8.53, "option_volume": 78.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "matched_signals": 40, "recovery_stability_score": 0.625, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610112501)

</details>
