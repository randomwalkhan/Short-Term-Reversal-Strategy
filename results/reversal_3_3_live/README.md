# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 13:35:05 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$55,068.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$292.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27607.5        30.35          30.67      310.66        313.89          bid_ask_mid                      30.67                bid_ask_mid                    True           292.5                   1.07          87.5               32              1.06         63.04           61.46                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           87.50               16            1.23              0.42         48.55               552.32         1.000          pass              0.352              4.0                           0.212                4.68              0.574                                 ok            True                  False
  ABNB           96.30               27            1.08              1.44        189.88                61.60         0.661          pass              0.642             20.8                           0.427                4.63              0.488                                 ok            True                  False
  SHOP           91.18               34            1.42              1.53        153.23                72.08         0.613          pass              0.622             34.1                           0.387                0.86             -0.139                                 ok            True                  False
   TRI           88.89               27            1.56              1.14        103.89                66.28         0.608          pass              0.566             51.8                           0.599                0.79              0.324                                 ok            True                  False
  WDAY           82.14               28            2.32              3.16        193.07                76.21         0.593          pass              0.354             39.2                           0.460                8.34              0.266                                 ok            True                  False
  MELI           93.75               16            2.06             28.78       1984.67                47.50         0.562          pass              0.509             15.4                           0.337                6.98              0.979                                 ok            True                  False
  REGN          100.00               20            1.24              7.26        830.45                29.20         0.557          pass              0.642             40.0                           0.569                3.28              0.443                                 ok            True                  False
  CPRT           86.96               23            1.67              0.39         33.16                43.23         0.522          pass              0.356             10.5                           0.318               13.06              1.349                                 ok            True                  False
  BKNG           94.74               19            2.05              3.06        212.47                35.36         0.514          pass              0.575             23.5                           0.527               -1.35              0.012                                 ok            True                  False
  TMUS           94.29               35            0.67              0.85        181.25                29.92         0.502          pass              0.642             14.8                           0.158                1.85              0.070                                 ok            True                  False
  INSM           89.13               46            0.41              0.36        123.74               110.58         0.685          pass              0.783             90.2                           0.641               -6.73             -0.443            downtrend_blocked_slope           False                  False
  AMAT           88.57               35            0.40              1.33        479.47                76.53         0.659          pass              0.686             75.0                           0.654              -12.68             -1.309 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:55:03.284797-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261002C00062000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 2.68, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.465, "hypothetical_budget": 13730.3, "hypothetical_contracts": 55, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 610.0, "option_spread_pct": 17.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.702, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T11:50:01.099073-04:00 early_entry_1150 early_entry_shadow                                   {"contract_symbol": "PYPL261016C00065000", "current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "entry_ask": 1.6, "entry_bid": 1.5, "entry_mode": "early", "entry_option_price": 1.55, "hypothetical_budget": 13730.3, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 6048.0, "option_spread_pct": 6.45, "option_volume": 584.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.734, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "matched_signals": 35, "recovery_stability_score": 0.734, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:45:03.275607-04:00 early_entry_1145 early_entry_shadow                                    {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "matched_signals": 35, "recovery_stability_score": 0.706, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:40:01.100306-04:00 early_entry_1140 early_entry_shadow                                  {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.684, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:35:01.234662-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:30:01.097446-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:25:05.264548-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:20:05.287776-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:15:01.102404-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826133505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826133505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826133505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826133505)

</details>
