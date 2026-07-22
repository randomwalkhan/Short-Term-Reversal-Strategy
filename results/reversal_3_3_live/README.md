# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 11:20:03 EDT`
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

- Cash: `$17,264.25`
- Equity: `$34,589.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$412.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 17325.0         3.08           3.15       55.67         55.63          bid_ask_mid                       3.15                bid_ask_mid                    True           412.5                   2.44          80.0               10              2.03         42.85           46.07                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            0.72              0.30         58.72               115.77         0.730          pass              0.533             86.5                           0.829               -5.83             -1.362                                 ok            True                  False
  AAPL           95.24               21            0.99              2.28        326.76                37.60         0.609          pass              0.569             11.4                           0.209                3.54              0.528                                 ok            True                  False
   ADP           95.24               21            1.22              2.11        245.32                36.45         0.568          pass              0.577             15.7                           0.250                0.76              0.321                                 ok            True                  False
  PAYX          100.00               22            1.20              0.94        111.56                33.94         0.558          pass              0.562              8.8                           0.181                3.79              0.647                                 ok            True                  False
  ABNB           93.75               16            2.21              2.23        143.14                31.72         0.520          pass              0.483              8.1                           0.271               -1.43             -0.200                                 ok            True                  False
  AMZN           82.35               17            1.67              2.89        246.31                25.29         0.518          pass              0.171              3.4                           0.207               -0.08              0.063                                 ok            True                  False
  CTAS           90.91               33            0.71              0.99        199.98                36.86         0.515          pass              0.655             53.2                           0.263               10.45              1.503                                 ok            True                  False
  PANW           90.91               22            2.28              5.47        339.81                60.47         0.511          pass              0.549             42.2                           0.370                4.29              0.569                                 ok            True                  False
  CTSH           87.18               39            0.80              0.25         43.52                49.89         0.502          pass              0.525             30.0                           0.342                2.00              0.296                                 ok            True                  False
  AMAT           90.62               32            0.70              2.77        563.36               100.84         0.717          pass              0.756             84.8                           0.778               -1.74             -0.809 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.32               31            0.63              1.42        321.39                94.63         0.686          pass              0.743             86.5                           0.833               -3.96             -1.044 downtrend_blocked_slope_and_streak           False                  False
  PYPL           89.19               37            0.38              0.15         55.79                62.33         0.632          pass              0.670             60.6                           0.577               24.94              2.805                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-07-22T11:20:03.697647-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                   {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.97, "early_entry_score": 0.762, "early_reclaim_pct": 63.9, "entry_ask": 111.6, "entry_bid": 99.4, "entry_mode": "early", "entry_option_price": 105.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 111.0, "option_spread_pct": 11.56, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.614, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.762, "early_reclaim_pct": 63.9, "matched_signals": 33, "recovery_stability_score": 0.614, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:15:05.770543-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:10:01.815938-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:05:06.654140-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:00:03.703283-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:55:01.795388-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "ASML260821C01800000", "current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "entry_ask": 123.4, "entry_bid": 119.9, "entry_mode": "early", "entry_option_price": 121.65, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 224.0, "option_spread_pct": 2.88, "option_volume": 138.0, "reason": "shadow_insufficient_cash", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 34, "recovery_stability_score": 0.597, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T10:50:06.298041-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:45:04.805546-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:40:06.812850-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:35:07.269157-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PANW260821C00340000", "current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "entry_ask": 24.8, "entry_bid": 23.4, "entry_mode": "early", "entry_option_price": 24.1, "hypothetical_budget": 8632.13, "hypothetical_contracts": 3, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 923.0, "option_spread_pct": 5.81, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "top_candidates": [{"current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "matched_signals": 31, "recovery_stability_score": 0.611, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.712, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722112003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722112003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722112003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722112003)

</details>
