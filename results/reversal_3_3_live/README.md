# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-11 15:45:53 EDT`
Last processed slot: `manual`

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

- Cash: `$17,648.00`
- Equity: `$31,473.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   1      5     13425.0                 13825.0        26.85          27.65      307.66        311.71          bid_ask_mid                      27.65                bid_ask_mid                    True           400.0                   2.98          87.1               31              1.19         68.92           66.61                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           97.14               35            1.19              1.29        154.63                81.38         0.650          pass              0.779             49.2                           0.692               17.70              2.599                                 ok            True                  False
  MSFT           80.00               35            0.52              1.84        505.27                57.78         0.613          pass              0.407             59.5                           0.637               27.98              2.477                                 ok            True                  False
   ROP          100.00               26            1.04              2.94        402.63                46.36         0.601          pass              0.646             26.4                           0.394                2.24              0.181                                 ok            True                  False
  UPRO           85.71               28            1.03              1.11        154.50                41.60         0.560          pass              0.418             30.0                           0.484               11.72              1.634                                 ok            True                  False
  WDAY           80.00               30            1.57              2.02        183.32                68.85         0.544          pass              0.311             41.1                           0.475               13.53              1.399                                 ok            True                  False
  ROST           92.86               28            0.72              1.28        254.28                21.47         0.511          pass              0.656             47.3                           0.278                0.78              0.130                                 ok            True                  False
  AMGN          100.00               29            0.72              2.11        416.30                30.34         0.501          pass              0.695             39.4                           0.424                5.37              0.822                                 ok            True                  False
  INSM           75.00               28            1.67              1.57        134.08               107.27         0.736          pass              0.275             27.1                           0.407               27.25              3.310                                 ok           False                  False
  AMZN           73.68               19            1.72              3.36        276.65                61.51         0.636          pass              0.210             28.8                           0.494               18.38              1.896                                 ok           False                  False
  INTC           87.18               39            0.49              0.33         97.38                84.72         0.634          pass              0.683             78.1                           0.595               12.45              1.746                                 ok           False                  False
  AAPL           81.25               16            1.27              2.74        307.09                38.28         0.598          pass              0.219             28.5                           0.356              -10.43             -0.961 downtrend_blocked_slope_and_streak           False                  False
  MCHP           82.93               41            0.36              0.20         81.30                75.25         0.584          pass              0.515             59.5                           0.580                7.12              1.154                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-11T11:31:47.849981-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "PANW260918C00380000", "current_drop_pct": 0.6, "early_entry_score": 0.708, "early_reclaim_pct": 74.5, "entry_ask": 33.15, "entry_bid": 31.2, "entry_mode": "early", "entry_option_price": 32.175, "hypothetical_budget": 8824.0, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 3447.0, "option_spread_pct": 6.06, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.708, "early_reclaim_pct": 74.5, "matched_signals": 46, "recovery_stability_score": 0.556, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-11T11:13:53.163975-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "PANW260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "entry_ask": 33.25, "entry_bid": 31.95, "entry_mode": "early", "entry_option_price": 32.6, "hypothetical_budget": 8824.0, "hypothetical_contracts": 2, "matched_signals": 47, "option_liquidity_status": "ok", "option_open_interest": 3447.0, "option_spread_pct": 3.99, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "matched_signals": 47, "recovery_stability_score": 0.639, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-11T10:26:01.426396-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ROP260918C00400000", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "entry_ask": 20.4, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 17.9, "hypothetical_budget": 8824.0, "hypothetical_contracts": 4, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 27.93, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.555, "shadow_only": true, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "matched_signals": 32, "recovery_stability_score": 0.555, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.679, "early_reclaim_pct": 69.3, "matched_signals": 44, "recovery_stability_score": 0.579, "success_rate": 88.64, "ticker": "PANW", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-11T00:00:05.969366-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-08-10T15:10:01.692365-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:05:01.609183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:00:04.645498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:55:05.599659-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:50:01.766475-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 13425.0, "asset_type": "option", "contract_symbol": "LRCX260918C00310000", "contracts": 5, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 26.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 3.35, "option_volume": 93.0, "success_rate": 87.1, "ticker": "LRCX", "timing_score": 0.649}
2026-08-10T14:50:01.766475-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-10", "training_samples": 5614, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260811154553)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260811154553)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260811154553)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260811154553)

</details>
