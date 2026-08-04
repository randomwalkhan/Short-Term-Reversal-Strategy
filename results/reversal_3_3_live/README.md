# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 15:35:05 EDT`
Last processed slot: `manage_1530`

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
   PEP     option         option PEP260918C00140000       2026-08-04                   0     40     16400.0                 17000.0          4.1           4.25      138.68         139.0          bid_ask_mid                       4.25                bid_ask_mid                    True           600.0                   3.66         83.33               24              0.68          24.5           24.51                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-04)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00050000    106          2026-08-03         2026-08-04         1.65       1.485 -1749.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DXCM           88.89               36            0.64              0.39         87.14                57.42         0.558            pass              0.613             49.1                           0.297               16.05              1.964                                 ok            True                  False
   WBD           88.24               17            0.98              0.18         26.01                24.14         0.545            pass              0.511             63.3                           0.442                0.02              0.063                                 ok            True                  False
  ALNY           85.19               27            1.36              2.10        219.43               126.96         0.817            pass              0.462             42.7                           0.434              -19.91             -2.921            downtrend_blocked_slope           False                  False
  ISRG           69.23               13            2.09              5.49        373.06                72.79         0.668            pass              0.176             29.7                           0.668                5.00              0.816                                 ok           False                  False
  TMUS           89.47               38            0.16              0.20        177.00                55.96         0.608            pass              0.770             90.0                           0.782               -7.32             -0.631            downtrend_blocked_slope           False                  False
  AMZN           76.47               17            2.10              4.18        282.23                60.32         0.596            pass              0.216             36.6                           0.498               12.32              1.485                                 ok           False                  False
   ROP           91.67               36            0.23              0.64        392.30                47.45         0.566            pass              0.809             89.4                           0.833               11.68              1.512                                 ok           False                  False
   PEP           84.62               26            0.47              0.46        139.43                26.13         0.547            pass              0.506             74.0                           0.718                2.95              0.399                                 ok           False                  False
   MAR          100.00               30            0.67              1.62        346.13                34.81         0.543            pass              0.772             61.4                           0.690               -6.33             -0.468 downtrend_blocked_slope_and_streak           False                  False
  VRSK           94.44               36            0.61              0.83        192.76                44.31         0.519            pass              0.797             62.1                           0.565               -1.70             -0.020           downtrend_blocked_streak           False                  False
  CTAS           95.12               41            0.05              0.08        203.98                37.98         0.495 below_threshold              0.941             97.3                           0.670                1.74              0.176                                 ok           False                  False
  COST           78.57               28            0.61              4.06        952.34                24.00         0.487 below_threshold              0.367             66.0                           0.709                2.21              0.346                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-04T15:10:06.388254-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-04T15:05:01.446900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-04T15:00:05.343102-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-04T14:55:02.363501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-04T14:50:05.317970-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"allocated_cash": 16400.0, "asset_type": "option", "contract_symbol": "PEP260918C00140000", "contracts": 40, "early_entry_score": 0.423, "entry_mode": "regular", "entry_option_price": 4.1, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 3513.0, "option_spread_pct": 4.88, "option_volume": 30.0, "success_rate": 83.33, "ticker": "PEP", "timing_score": 0.544}
2026-08-04T14:50:05.317970-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"early_entry_score": 0.728, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "ROP", "timing_score": 0.567}
2026-08-04T14:50:05.317970-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-04", "training_samples": 5558, "window": 5}
2026-08-04T12:00:02.363319-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                 {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "matched_signals": 33, "recovery_stability_score": 0.74, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:55:01.364368-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                             {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.701, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:50:01.376014-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "entry_ask": 36.7, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.35, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 7.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.717, "early_reclaim_pct": 72.3, "matched_signals": 33, "recovery_stability_score": 0.747, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.56, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804153505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804153505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804153505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804153505)

</details>
