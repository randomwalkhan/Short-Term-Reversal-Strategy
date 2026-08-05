# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 09:30:01 EDT`
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

- Cash: `$17,080.75`
- Equity: `$34,080.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 17000.0          4.1           4.25      138.68        139.39     last_price_stale                        NaN                unavailable                   False           600.0                   3.66         83.33               24              0.68          24.5            0.39                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            0.97              1.48        217.95               100.52         0.637          pass              0.451             73.5                           0.511                2.60              0.297                       ok            True                  False
   KHC           94.12               17            0.79              0.15         26.58                32.24         0.604          pass              0.640             52.3                           0.522                1.81              0.282                       ok            True                  False
  DXCM           83.33               24            1.66              1.01         86.51                57.55         0.578          pass              0.240              0.0                           0.217               19.70              2.354                       ok            True                  False
   WBD           88.24               17            1.15              0.21         26.00                24.48         0.526          pass              0.489             56.8                           0.438               -0.23              0.068                       ok            True                  False
  ALNY           92.31               39            0.60              0.93        219.93               125.97         0.812          pass              0.826             74.6                           0.747              -17.97             -3.077  downtrend_blocked_slope           False                  False
  SOXL           79.41               34            2.84              2.79        139.00               182.46         0.751          pass              0.399             54.5                           0.489              -15.39             -1.783 downtrend_blocked_streak           False                  False
    MU           80.00               35            0.32              2.02        891.80               111.85         0.723          pass              0.505             88.8                           0.597               -7.26             -1.110 downtrend_blocked_streak           False                  False
  AMAT           91.67               36            0.33              1.27        546.07                87.24         0.694          pass              0.802             82.9                           0.469               -1.65             -0.261 downtrend_blocked_streak           False                  False
  LRCX           89.74               39            0.02              0.05        317.72                92.33         0.687          pass              0.819             99.0                           0.597               -0.51             -0.044                       ok           False                  False
  DRAM           77.42               31            2.09              0.80         54.51               109.93         0.657          pass              0.346             46.6                           0.454               -7.03             -0.648 downtrend_blocked_streak           False                  False
 CMCSA           85.71               21            0.26              0.05         24.91                44.00         0.651          pass              0.469             59.4                           0.405                5.72              1.054                       ok           False                  False
  TMUS           88.24               34            0.55              0.69        176.92                55.59         0.617          pass              0.643             67.1                           0.502               -7.70             -0.361  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-05T00:00:04.689271-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-04T15:10:06.388254-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:05:01.446900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:00:05.343102-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:55:02.363501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:50:05.317970-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 16400.0, "asset_type": "option", "contract_symbol": "PEP260918C00140000", "contracts": 40, "early_entry_score": 0.423, "entry_mode": "regular", "entry_option_price": 4.1, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 3513.0, "option_spread_pct": 4.88, "option_volume": 30.0, "success_rate": 83.33, "ticker": "PEP", "timing_score": 0.544}
2026-08-04T14:50:05.317970-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.728, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "ROP", "timing_score": 0.567}
2026-08-04T14:50:05.317970-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-04", "training_samples": 5558, "window": 5}
2026-08-04T12:00:02.363319-04:00 early_entry_1200      early_entry_shadow     {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "matched_signals": 33, "recovery_stability_score": 0.74, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:55:01.364368-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.701, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805093001)

</details>
