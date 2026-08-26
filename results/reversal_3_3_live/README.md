# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 11:45:03 EDT`
Last processed slot: `early_entry_1145`

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

- Cash: `$27,460.60`
- Equity: `$55,023.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$247.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27562.5        30.35          30.62      310.66        312.72          bid_ask_mid                      30.62                bid_ask_mid                    True           247.5                   0.91          87.5               32              1.06         63.04           62.53                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.54              0.19         48.65               552.32         1.000          pass              0.729             50.8                           0.503                5.40              0.606                      ok            True                  False
  ABNB           93.55               31            0.83              1.11        190.03                61.60         0.651          pass              0.635             22.9                           0.329                4.90              0.499                      ok            True                  False
  SHOP           90.62               32            1.51              1.62        153.18                72.08         0.619          pass              0.582             29.9                           0.347                0.76             -0.144                      ok            True                  False
   TRI           88.46               26            1.84              1.34        103.80                66.28         0.597          pass              0.522             43.2                           0.306                0.51              0.311                      ok            True                  False
  REGN          100.00               10            1.70              9.93        829.30                29.20         0.594          pass              0.513             17.8                           0.328                2.80              0.422                      ok            True                  False
  AMGN          100.00               21            0.75              2.32        441.24                27.99         0.565          pass              0.581             17.0                           0.211                6.08              0.807                      ok            True                  False
  MELI           95.45               22            1.61             22.56       1987.33                47.50         0.560          pass              0.558              7.5                           0.164                7.46              1.000                      ok            True                  False
  DXCM           87.88               33            0.96              0.60         88.90                51.46         0.559          pass              0.563             47.9                           0.342               -2.75             -0.103                      ok            True                  False
  BKNG           96.00               25            1.52              2.28        212.80                35.36         0.515          pass              0.619             22.5                           0.354               -0.82              0.037                      ok            True                  False
  CPRT           84.85               33            0.98              0.23         33.23                43.23         0.502          pass              0.434             33.7                           0.544               13.85              1.380                      ok            True                  False
  INSM           87.50               32            1.48              1.28        123.34               110.58         0.700          pass              0.611             64.8                           0.348               -7.73             -0.492 downtrend_blocked_slope           False                  False
  LRCX           86.84               38            0.55              1.21        314.14                81.56         0.634          pass              0.654             73.8                           0.707               -4.04             -0.840 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-26T11:45:03.275607-04:00 early_entry_1145 early_entry_shadow                                       {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "matched_signals": 35, "recovery_stability_score": 0.706, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:40:01.100306-04:00 early_entry_1140 early_entry_shadow                                     {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.684, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:35:01.234662-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:30:01.097446-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:25:05.264548-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:20:05.287776-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:15:01.102404-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:10:05.253776-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:05:02.266288-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:00:04.246676-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "DXCM260925C00089000", "current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 13730.3, "hypothetical_contracts": 36, "matched_signals": 36, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 54.0, "option_spread_pct": 21.05, "option_volume": 54.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.684, "early_reclaim_pct": 72.1, "matched_signals": 36, "recovery_stability_score": 0.554, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.569, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826114503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826114503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826114503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826114503)

</details>
