# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 10:20:03 EDT`
Last processed slot: `manage_1030`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           95.83               24            0.78              1.72        312.65                38.12         0.571            pass              0.709             53.0                           0.524                6.09              1.237                                 ok            True                  False
   ADP           95.83               24            0.83              1.40        240.77                32.32         0.524            pass              0.748             67.6                           0.764                8.87              1.227                                 ok            True                  False
  GILD           88.46               26            0.67              0.64        135.55                35.14         0.516            pass              0.627             80.9                           0.470                7.79              0.933                                 ok            True                  False
  CTAS           87.50               24            0.96              1.21        179.65                32.70         0.514            pass              0.511             55.5                           0.523                4.40              0.734                                 ok            True                  False
  AMGN           92.59               27            0.61              1.58        367.31                27.70         0.500 below_threshold              0.653             51.4                           0.538                4.07              0.467                                 ok            True                  False
  MDLZ          100.00               13            0.82              0.34         59.33                30.45         0.588            pass              0.652             57.8                           0.697               -3.65             -0.213           downtrend_blocked_streak           False                  False
   KDP          100.00               12            1.10              0.24         30.87                33.74         0.571            pass              0.602             43.8                           0.663               -1.76             -0.475 downtrend_blocked_slope_and_streak           False                  False
  META           73.33               15            1.76              7.45        599.93                51.28         0.545            pass              0.265             59.2                           0.660                6.24              1.113                                 ok           False                  False
   HON           73.91               23            0.84              1.30        219.80                46.53         0.530            pass              0.319             59.8                           0.308               -8.39             -0.911            downtrend_blocked_slope           False                  False
 CMCSA           50.00                8            1.23              0.20         23.10                30.42         0.524            pass              0.136             27.8                           0.352                2.55              0.252                                 ok           False                  False
  PAYX          100.00               32            0.27              0.20        106.49                32.56         0.523            pass              0.868             89.8                           0.854               10.37              1.187                                 ok           False                  False
  CPRT           78.95               19            1.52              0.30         28.46                44.46         0.519            pass              0.203             30.4                           0.276               -7.38             -0.517            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-09T10:20:03.107544-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "ROP260821C00350000", "current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "entry_ask": 22.0, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 14199.63, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 28.0, "option_spread_pct": 35.92, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.742, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.694, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:15:06.221157-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:10:04.085991-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:05:06.090866-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "entry_ask": 109.3, "entry_bid": 81.4, "entry_mode": "early", "entry_option_price": 95.35, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 29.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.823, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.825, "early_reclaim_pct": 70.4, "matched_signals": 37, "recovery_stability_score": 0.823, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:05:06.090866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PAYX260821C00110000", "fill_price": 2.2725, "pnl": -1262.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-07-09T10:00:05.048554-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "MELI260807C01795000", "current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 105.0, "hypothetical_budget": 8518.38, "hypothetical_contracts": 0, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.856, "early_reclaim_pct": 74.0, "matched_signals": 39, "recovery_stability_score": 0.819, "success_rate": 94.87, "ticker": "MELI", "timing_score": 0.447, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 31, "recovery_stability_score": 0.751, "success_rate": 93.55, "ticker": "ROP", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-09T10:00:05.048554-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "CSX260821C00047500", "fill_price": 3.075, "pnl": 3915.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 30.85, "ticker": "CSX"}
2026-07-09T00:00:06.857915-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-08T15:10:05.590905-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-08T15:05:01.586553-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709102003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709102003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709102003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709102003)

</details>
