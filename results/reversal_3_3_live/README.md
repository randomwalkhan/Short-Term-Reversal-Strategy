# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 09:40:06 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$28,218.10`
- Equity: `$54,818.10`
- Realized PnL: `$45,518.10`
- Unrealized PnL: `$-700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MNST     option         option MNST261016C00048000       2026-08-26                   1    140     27300.0                 26600.0         1.95            1.9       48.03         46.47     last_price_stale                        NaN                unavailable                   False          -700.0                  -2.56         85.71               14              1.44         27.42            3.13                 552.32                 249.0           74.0               0.05                      ok
```

## Today's Closed Trades (2026-08-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               12            1.29              3.96        438.64                27.27         0.601          pass              0.600             42.1                           0.409                4.64              0.689                  ok            True                  False
  COST           94.12               17            1.01              6.76        953.22                18.65         0.539          pass              0.552             25.1                           0.274               -1.60             -0.064                  ok            True                  False
  AAPL           84.62               26            0.97              2.13        312.54                33.02         0.539          pass              0.358             24.8                           0.322                1.69              0.183                  ok            True                  False
  SBUX           94.74               19            0.71              0.54        108.26                22.90         0.538          pass              0.679             57.5                           0.484               -0.19              0.006                  ok            True                  False
  VRTX           96.97               33            0.67              2.55        546.20                33.08         0.537          pass              0.755             49.4                           0.556                5.27              0.770                  ok            True                  False
   KDP           82.61               23            1.16              0.26         32.09                31.04         0.534          pass              0.277             22.4                           0.274                2.28              0.455                  ok            True                  False
  FAST          100.00               19            0.94              0.34         51.01                23.31         0.526          pass              0.741             76.1                           0.580               -1.31             -0.103                  ok            True                  False
  BKNG           93.75               16            2.22              3.24        207.50                36.49         0.519          pass              0.459              0.0                           0.203               -4.26             -0.105                  ok            True                  False
  ALNY           85.71               35            0.96              1.61        238.31               130.65         0.516          pass              0.593             74.0                           0.782                4.22              0.564                  ok            True                  False
 CMCSA           94.12               17            1.62              0.31         27.07                26.47         0.514          pass              0.521             15.4                           0.181                2.22              0.462                  ok            True                  False
  MDLZ           92.31               26            0.77              0.34         62.86                22.77         0.509          pass              0.642             52.0                           0.585               -1.58             -0.009                  ok            True                  False
  GEHC           96.43               28            0.83              0.43         73.13                25.07         0.508          pass              0.730             53.1                           0.377               -1.48              0.012                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-27T00:00:06.493019-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-08-26T15:50:01.441295-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "LRCX261016C00310000", "fill_price": 31.175, "pnl": 742.5, "reason": "time_exit_at_4pm_scan", "return_pct": 2.72, "ticker": "LRCX"}
2026-08-26T15:10:04.393572-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:05:01.392780-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:00:04.399840-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:55:02.427965-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:50:02.229559-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 27300.0, "asset_type": "option", "contract_symbol": "MNST261016C00048000", "contracts": 140, "early_entry_score": 0.298, "entry_mode": "regular", "entry_option_price": 1.95, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 5.13, "option_volume": 74.0, "success_rate": 85.71, "ticker": "MNST", "timing_score": 1.0}
2026-08-26T14:50:02.229559-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-26", "training_samples": 5704, "window": 5}
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:55:03.284797-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261002C00062000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 2.68, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.465, "hypothetical_budget": 13730.3, "hypothetical_contracts": 55, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 610.0, "option_spread_pct": 17.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.702, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827094006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827094006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827094006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827094006)

</details>
