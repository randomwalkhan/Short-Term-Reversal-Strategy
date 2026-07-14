# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 11:20:05 EDT`
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

- Cash: `$17,620.25`
- Equity: `$26,860.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9240.0        46.88           46.2      660.72        661.22          bid_ask_mid                       46.2                bid_ask_mid                    True          -135.0                  -1.44         81.82               22              1.27         53.38            53.0                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AAPL           96.30               27            0.54              1.20        316.79                35.57         0.577          pass              0.793             74.1                           0.733               12.01              1.129                  ok            True                  False
  QCOM           84.38               32            0.66              0.85        183.61                63.33         0.568          pass              0.546             75.4                           0.645               -3.16              0.155                  ok            True                  False
  PAYX          100.00               19            1.28              0.99        110.32                31.82         0.555          pass              0.715             66.6                           0.423                9.54              0.932                  ok            True                  False
  GILD           86.36               22            0.87              0.80        131.06                32.97         0.555          pass              0.432             42.4                           0.343                3.11              0.413                  ok            True                  False
  CTAS           86.96               23            1.17              1.50        183.11                31.28         0.530          pass              0.430             35.0                           0.311                7.40              0.637                  ok            True                  False
  TMUS           87.10               31            0.73              0.96        188.00                37.13         0.527          pass              0.496             37.9                           0.465                7.51              1.026                  ok            True                  False
  PCAR           85.19               27            0.89              0.78        123.93                31.62         0.525          pass              0.393             29.7                           0.377                2.97              0.400                  ok            True                  False
  AMGN           95.65               23            0.99              2.49        359.38                21.45         0.521          pass              0.649             36.8                           0.514               -1.02             -0.081                  ok            True                  False
  IDXX           90.00               10            2.76             10.90        559.54                34.15         0.516          pass              0.385             22.2                           0.428                2.37              0.504                  ok            True                  False
   KHC           88.89                9            1.21              0.21         25.14                36.18         0.649          pass              0.393             30.4                           0.313                3.04              0.319                  ok           False                  False
  MDLZ          100.00                4            1.70              0.71         59.55                31.17         0.636          pass              0.506             14.3                           0.277               -1.36              0.009                  ok           False                  False
   PEP           87.50                8            1.43              1.39        137.90                30.22         0.614          pass              0.276              4.8                           0.203               -1.56             -0.121                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-14T11:20:05.915369-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:15:04.383318-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:10:01.445183-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:05:01.389220-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:00:04.389185-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:55:01.316217-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:50:01.398804-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "DASH260814C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "entry_ask": 13.75, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.525, "hypothetical_budget": 8810.13, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 19.56, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "matched_signals": 45, "recovery_stability_score": 0.826, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:45:05.382640-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:40:02.394699-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:35:01.379704-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714112005)

</details>
