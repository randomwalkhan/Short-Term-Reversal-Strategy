# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-04 15:00:02 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$22,561.75`
- Equity: `$34,601.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$30.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260717C00270000       2026-06-04                   0      2     12010.0                 12040.0        60.05           60.2      270.38        268.75          bid_ask_mid                       60.2                bid_ask_mid                    True            30.0                   0.25         94.74               19              3.62        161.75          165.16                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MELI           94.12               34            0.91             10.40       1634.08                61.24         0.594          pass              0.596              0.0                           0.230               -1.67             -0.060                      ok            True                  False
  CTSH           93.55               31            0.58              0.22         53.42                51.56         0.552          pass              0.624             22.5                           0.322                3.70              0.590                      ok            True                  False
   TXN           95.83               24            0.88              1.89        307.78                42.91         0.550          pass              0.751             67.6                           0.450                0.33             -0.093                      ok            True                  False
   ADI          100.00               17            1.81              5.54        435.30                44.48         0.538          pass              0.662             53.7                           0.573                8.26              0.943                      ok            True                  False
  TEAM           93.18               44            0.73              0.52        101.31                88.72         0.534          pass              0.817             70.8                           0.418               16.89              2.884                      ok            True                  False
  SOXL           94.44               18            4.20              8.25        277.00               141.59         0.531          pass              0.724             77.3                           0.648               55.17              4.592                      ok            True                  False
  PANW           90.32               31            1.15              2.26        279.46                59.60         0.523          pass              0.699             77.0                           0.785               12.38              1.664                      ok            True                   True
   WDC           96.55               29            1.59              6.59        591.28                59.52         0.512          pass              0.782             68.0                           0.501               27.21              2.306                      ok            True                  False
   APP           85.71               35            1.55              6.21        568.17                74.91         0.506          pass              0.509             46.6                           0.540               16.52              2.297                      ok            True                  False
  LRCX           90.62               32            0.65              1.58        343.03                54.10         0.502          pass              0.745             88.2                           0.808               16.90              1.392                      ok            True                   True
  SNPS           93.10               29            1.15              4.03        496.29                43.50         0.502          pass              0.694             55.8                           0.509               -1.33             -0.432                      ok            True                  False
  INTU           77.27               22            2.48              5.40        309.13               102.00         0.671          pass              0.224             25.7                           0.506              -20.89             -0.654 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-04T15:00:02.553545-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T14:55:06.549299-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-04T14:50:05.645592-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SOXL260717C00270000", "contracts": 2, "early_entry_score": 0.751, "entry_mode": "regular", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 5.33, "option_volume": 64.0, "success_rate": 94.74, "ticker": "SOXL", "timing_score": 0.565}
2026-06-04T14:50:05.645592-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.634, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 16.0, "option_spread_pct": 7.13, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.593}
2026-06-04T14:50:05.645592-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-04", "training_samples": 5195, "window": 5}
2026-06-04T11:33:58.038645-04:00 early_entry_1130      early_entry_shadow  {"contract_symbol": "SNPS260717C00510000", "current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "entry_ask": 29.4, "entry_bid": 27.7, "entry_mode": "early", "entry_option_price": 28.55, "hypothetical_budget": 17285.88, "hypothetical_contracts": 6, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 124.0, "option_spread_pct": 5.95, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "matched_signals": 34, "recovery_stability_score": 0.81, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:52:01.009972-04:00 early_entry_1050      early_entry_shadow {"contract_symbol": "ASML260717C01640000", "current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "entry_ask": 176.5, "entry_bid": 162.4, "entry_mode": "early", "entry_option_price": 169.45, "hypothetical_budget": 17285.88, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 116.0, "option_spread_pct": 8.32, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "matched_signals": 30, "recovery_stability_score": 0.7, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:07:26.962733-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "entry_ask": 19.1, "entry_bid": 17.1, "entry_mode": "early", "entry_option_price": 18.1, "hypothetical_budget": 17285.88, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1675.0, "option_spread_pct": 11.05, "option_volume": 84.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "top_candidates": [{"current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "matched_signals": 30, "recovery_stability_score": 0.831, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T09:22:28.092024-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-03T15:10:03.976623-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260604150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260604150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260604150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260604150002)

</details>
