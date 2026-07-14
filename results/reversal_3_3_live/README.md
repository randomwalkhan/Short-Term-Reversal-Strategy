# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 10:05:01 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$26,160.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-835.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  8540.0        46.88           42.7      660.72        657.48          bid_ask_mid                       42.7                bid_ask_mid                    True          -835.0                  -8.91         81.82               22              1.27         53.38           51.28                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           94.44               18            1.07              2.37        316.29                35.57         0.603          pass              0.645             48.9                           0.550               11.42              1.105                                 ok            True                  False
  PAYX          100.00               24            0.95              0.74        110.43                31.82         0.543          pass              0.773             75.3                           0.728                9.91              0.948                                 ok            True                  False
  AMGN           95.83               24            0.79              2.00        359.59                21.45         0.526          pass              0.694             49.2                           0.547               -0.82             -0.072                                 ok            True                  False
  CTAS           90.62               32            0.73              0.94        183.35                31.28         0.502          pass              0.659             59.5                           0.550                7.88              0.657                                 ok            True                  False
  AMZN           83.87               31            0.89              1.55        246.65                34.41         0.502          pass              0.405             37.0                           0.294                2.07              0.309                                 ok            True                  False
  IDXX           90.48               21            1.78              7.02        561.20                34.15         0.500          pass              0.552             49.9                           0.481                3.41              0.550                                 ok            True                  False
   KHC           88.89                9            0.71              0.13         25.18                36.18         0.676          pass              0.481             58.9                           0.632                3.56              0.342                                 ok           False                  False
  MDLZ          100.00                8            1.13              0.47         59.66                31.17         0.647          pass              0.550             28.6                           0.282               -0.78              0.036                                 ok           False                  False
   KDP           81.82               11            1.22              0.27         31.14                34.17         0.612          pass              0.201             28.3                           0.215               -7.85             -0.770 downtrend_blocked_slope_and_streak           False                  False
   PEP           92.31               26            0.19              0.18        138.41                30.22         0.587          pass              0.705             70.5                           0.548               -0.32             -0.064                                 ok           False                  False
   ADP          100.00                6            2.07              3.63        249.49                31.20         0.584          pass              0.581             41.0                           0.529                9.29              0.824                                 ok           False                  False
 CMCSA           63.64               11            1.34              0.22         23.87                31.59         0.568          pass              0.117             17.9                           0.253               -1.02             -0.128                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-14T10:05:01.368977-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:00:02.374246-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "SNPS260814C00430000", "current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 30.45, "hypothetical_budget": 8810.13, "hypothetical_contracts": 2, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 3.0, "option_spread_pct": null, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "matched_signals": 39, "recovery_stability_score": 0.763, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T15:10:07.483451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:05:06.913203-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:00:09.058779-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T14:55:09.246495-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T14:50:06.804809-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 9375.0, "asset_type": "option", "contract_symbol": "META260821C00660000", "contracts": 2, "early_entry_score": 0.317, "entry_mode": "regular", "entry_option_price": 46.875, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 7322.0, "option_spread_pct": 2.03, "option_volume": 1343.0, "success_rate": 81.82, "ticker": "META", "timing_score": 0.583}
2026-07-13T14:50:06.804809-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-13", "training_samples": 5399, "window": 5}
2026-07-13T12:00:04.108537-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:55:01.971433-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714100501)

</details>
