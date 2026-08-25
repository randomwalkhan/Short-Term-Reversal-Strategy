# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 11:00:02 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$30,388.00`
- Equity: `$57,860.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$157.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 27472.5        30.35          30.52      310.66        309.78          bid_ask_mid                      30.52                bid_ask_mid                    True           157.5                   0.58          87.5               32              1.06         63.04           64.72                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.86               35            1.08              1.30        170.77               115.46         0.774          pass              0.509             62.9                           0.581                9.99              1.110                  ok            True                  False
  ABNB           94.12               34            0.57              0.76        189.88                62.43         0.639          pass              0.612              4.0                           0.183                2.24              0.376                  ok            True                  False
   TRI           90.00               10            3.05              2.32        107.63                67.11         0.593          pass              0.351              8.5                           0.114                1.10              0.394                  ok            True                  False
  DXCM           87.88               33            0.77              0.49         90.85                50.36         0.582          pass              0.546             41.6                           0.348                0.93              0.099                  ok            True                  False
  GEHC           97.37               38            0.53              0.27         74.07                49.18         0.573          pass              0.830             62.1                           0.642                1.44              0.235                  ok            True                   True
  WDAY           80.00               30            2.09              2.91        197.90                78.88         0.566          pass              0.287             32.4                           0.329                7.57              0.731                  ok            True                  False
   KHC           86.96               23            1.01              0.18         25.59                37.91         0.559          pass              0.451             40.9                           0.557                3.08              0.362                  ok            True                  False
  PAYX          100.00               24            0.67              0.59        125.76                34.31         0.547          pass              0.719             56.9                           0.504                3.18              0.332                  ok            True                  False
  FAST          100.00               22            0.77              0.28         51.16                22.00         0.540          pass              0.667             44.4                           0.621               -2.85             -0.211                  ok            True                  False
  SBUX           81.82               11            1.26              0.95        107.08                20.57         0.526          pass              0.214             35.4                           0.250                0.08             -0.119                  ok            True                  False
  MDLZ           90.91               22            1.22              0.55         64.46                26.88         0.513          pass              0.525             34.2                           0.612                3.45              0.381                  ok            True                  False
   KDP           86.36               22            1.40              0.32         32.37                31.66         0.513          pass              0.322              7.1                           0.138                9.85              0.888                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-25T11:00:02.779478-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "entry_ask": 3.5, "entry_bid": 2.3, "entry_mode": "early", "entry_option_price": 2.9, "hypothetical_budget": 15194.0, "hypothetical_contracts": 52, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 41.38, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "matched_signals": 38, "recovery_stability_score": 0.642, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.809, "early_reclaim_pct": 75.9, "matched_signals": 30, "recovery_stability_score": 0.568, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:55:04.743815-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:50:06.625543-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:45:01.788012-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "DXCM261002C00091000", "current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "entry_ask": 5.0, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 4.15, "hypothetical_budget": 15194.0, "hypothetical_contracts": 36, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 40.96, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:40:03.785417-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:35:02.544392-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:30:01.796364-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:25:02.779045-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:15:01.792883-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825110002)

</details>
