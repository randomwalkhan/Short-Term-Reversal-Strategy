# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 10:10:04 EDT`
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

- Cash: `$28,399.25`
- Equity: `$28,399.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   CSX     option         option  CSX260821C00047500     54          2026-07-07         2026-07-09        2.350      3.0750  3915.0   30.851064 take_profit_day2_hit_at_scan
  PAYX     option         option PAYX260821C00110000     50          2026-07-08         2026-07-09        2.525      2.2725 -1262.5  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           95.83               24            0.69              1.51        312.74                38.12         0.577          pass              0.727             58.7                           0.561                6.19              1.241                                 ok            True                  False
  GILD           88.89               18            1.10              1.05        135.37                35.14         0.538          pass              0.550             68.5                           0.428                7.32              0.913                                 ok            True                  False
  AMGN           94.12               17            1.08              2.77        366.80                27.70         0.533          pass              0.520             14.7                           0.216                3.59              0.446                                 ok            True                  False
   ADP           95.00               20            1.06              1.79        240.60                32.32         0.532          pass              0.696             58.6                           0.706                8.62              1.216                                 ok            True                  False
  GOOG           81.82               11            2.14              5.36        356.41                34.51         0.517          pass              0.138             10.5                           0.167                1.74              0.553                                 ok            True                  False
  CTAS           86.36               22            1.13              1.42        179.56                32.70         0.513          pass              0.444             47.6                           0.452                4.22              0.726                                 ok            True                  False
  MDLZ          100.00                8            1.19              0.49         59.27                30.45         0.595          pass              0.577             39.2                           0.521               -4.00             -0.230           downtrend_blocked_streak           False                  False
   KDP          100.00               10            1.29              0.28         30.85                33.74         0.571          pass              0.559             33.9                           0.518               -1.95             -0.484 downtrend_blocked_slope_and_streak           False                  False
  META           73.33               15            1.74              7.33        599.98                51.28         0.546          pass              0.267             59.8                           0.813                6.27              1.114                                 ok           False                  False
  PAYX          100.00               28            0.49              0.36        106.42                32.56         0.533          pass              0.818             81.7                           0.833               10.13              1.178                                 ok           False                  False
  CPRT           82.35               17            1.64              0.33         28.45                44.46         0.527          pass              0.237             24.8                           0.282               -7.50             -0.523            downtrend_blocked_slope           False                  False
   XEL          100.00               22            0.60              0.34         79.48                21.16         0.525          pass              0.618             28.4                           0.283               -2.86             -0.298            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-09T10:10:04.085991-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:05:06.090866-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "entry_ask": 109.3, "entry_bid": 81.4, "entry_mode": "early", "entry_option_price": 95.35, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 29.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "matched_signals": 37, "recovery_stability_score": 0.823, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:05:06.090866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PAYX260821C00110000", "fill_price": 2.2725, "pnl": -1262.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-07-09T10:00:05.048554-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 105.0, "hypothetical_budget": 8518.38, "hypothetical_contracts": 0, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "matched_signals": 39, "recovery_stability_score": 0.819, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 31, "recovery_stability_score": 0.751, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:00:05.048554-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "CSX260821C00047500", "fill_price": 3.075, "pnl": 3915.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 30.85, "ticker": "CSX"}
2026-07-09T00:00:06.857915-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-08T15:10:05.590905-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-08T15:05:01.586553-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-08T15:00:04.551542-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-08T14:55:01.624651-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709101004)

</details>
