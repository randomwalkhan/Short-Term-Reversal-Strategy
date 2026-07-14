# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 11:15:04 EDT`
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

- Cash: `$17,620.25`
- Equity: `$26,935.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-60.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9315.0        46.88          46.58      660.72         662.6          bid_ask_mid                      46.58                bid_ask_mid                    True           -60.0                  -0.64         81.82               22              1.27         53.38           52.93                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AAPL           96.43               28            0.53              1.17        316.81                35.57         0.572          pass              0.802             74.8                           0.720               12.03              1.130                  ok            True                  False
  PAYX          100.00               20            1.20              0.93        110.35                31.82         0.553          pass              0.728             68.7                           0.473                9.63              0.936                  ok            True                  False
  QCOM           86.11               36            0.56              0.72        183.67                63.33         0.550          pass              0.629             79.3                           0.685               -3.05              0.160                  ok            True                  False
  GILD           88.00               25            0.74              0.68        131.11                32.97         0.545          pass              0.520             50.6                           0.472                3.24              0.418                  ok            True                  False
  CTAS           88.00               25            1.01              1.30        183.19                31.28         0.528          pass              0.498             44.1                           0.360                7.58              0.645                  ok            True                  False
  AMGN           95.65               23            0.92              2.32        359.45                21.45         0.525          pass              0.662             41.0                           0.521               -0.95             -0.077                  ok            True                  False
  TMUS           87.50               32            0.66              0.87        188.04                37.13         0.525          pass              0.529             43.3                           0.486                7.58              1.029                  ok            True                  False
  PCAR           86.21               29            0.76              0.66        123.98                31.62         0.521          pass              0.466             40.5                           0.424                3.11              0.406                  ok            True                  False
  IDXX           87.50               16            2.22              8.77        560.45                34.15         0.504          pass              0.403             37.4                           0.675                2.94              0.530                  ok            True                  False
   KHC           88.89                9            1.01              0.18         25.15                36.18         0.660          pass              0.428             41.8                           0.516                3.25              0.328                  ok           False                  False
  MDLZ          100.00                4            1.55              0.65         59.58                31.17         0.644          pass              0.530             21.8                           0.359               -1.21              0.016                  ok           False                  False
   PEP           88.89                9            1.16              1.12        138.01                30.22         0.626          pass              0.358             19.3                           0.257               -1.29             -0.109                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-14T11:15:04.383318-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:10:01.445183-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:05:01.389220-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:00:04.389185-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:55:01.316217-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:50:01.398804-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "DASH260814C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "entry_ask": 13.75, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.525, "hypothetical_budget": 8810.13, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 19.56, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "matched_signals": 45, "recovery_stability_score": 0.826, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:45:05.382640-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:40:02.394699-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:35:01.379704-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:30:01.227428-04:00 early_entry_1030 early_entry_shadow                 {"contract_symbol": "DASH260821C00190000", "current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "entry_ask": 14.35, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 8810.13, "hypothetical_contracts": 6, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 268.0, "option_spread_pct": 20.35, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714111504)

</details>
