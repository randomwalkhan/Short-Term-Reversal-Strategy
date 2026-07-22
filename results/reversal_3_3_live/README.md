# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 15:55:01 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$989.25`
- Equity: `$34,461.75`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$285.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 17160.0         3.08           3.12       55.67         55.53          bid_ask_mid                       3.12                bid_ask_mid                    True           247.5                   1.46         80.00               10              2.03         42.85           46.90                  61.63                6395.0           68.0               0.05                      ok
  AAPL     option         option AAPL260821C00325000       2026-07-22                   0     15     16275.0                 16312.5        10.85          10.88      324.66        326.67          bid_ask_mid                      10.88                bid_ask_mid                    True            37.5                   0.23         95.83               24              0.94         29.64           27.42                  37.60               16822.0          985.0               0.01                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           80.65               31            0.92              6.26        968.14               110.72         0.671          pass              0.468             81.1                           0.505                1.38             -0.660                                 ok            True                  False
  PYPL           87.10               31            0.57              0.22         55.75                62.33         0.654          pass              0.539             48.0                           0.450               24.70              2.796                                 ok            True                  False
   ADP           94.44               18            1.45              2.51        245.15                36.45         0.566          pass              0.560             21.7                           0.350                0.53              0.311                                 ok            True                  False
  PAYX          100.00               21            1.29              1.01        111.53                33.94         0.554          pass              0.596             22.6                           0.322                3.70              0.643                                 ok            True                  False
  BKNG           91.18               34            0.65              0.82        179.05                40.68         0.542          pass              0.693             60.4                           0.353                2.26              0.306                                 ok            True                  False
  CTSH           85.71               35            1.02              0.31         43.50                49.89         0.505          pass              0.500             43.3                           0.314                1.78              0.286                                 ok            True                  False
  KLAC           85.71               28            1.31              2.00        216.70               102.77         0.709          pass              0.558             71.6                           0.393               -2.93             -0.751 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.89               27            0.97              2.19        321.06                94.63         0.686          pass              0.656             79.1                           0.457               -4.29             -1.060 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.00               25            1.85              7.30        561.42               100.84         0.686          pass              0.561             59.8                           0.350               -2.87             -0.862 downtrend_blocked_slope_and_streak           False                  False
  DRAM           80.77               26            1.92              0.79         58.51               115.77         0.673          pass              0.387             64.1                           0.548               -6.96             -1.418            downtrend_blocked_slope           False                  False
  ISRG           63.64               11            2.57              6.30        347.36                68.15         0.608          pass              0.078              3.6                           0.214              -17.84             -2.113            downtrend_blocked_slope           False                  False
  META           66.67                9            2.43             10.96        639.11                51.99         0.596          pass              0.123             21.0                           0.322                4.15              0.133                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-22T15:10:06.070612-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-22T15:05:02.089739-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-22T15:00:04.754101-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-22T14:55:01.833206-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-22T14:50:06.810797-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 16275.0, "asset_type": "option", "contract_symbol": "AAPL260821C00325000", "contracts": 15, "early_entry_score": 0.642, "entry_mode": "regular", "entry_option_price": 10.85, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 16822.0, "option_spread_pct": 0.92, "option_volume": 985.0, "success_rate": 95.83, "ticker": "AAPL", "timing_score": 0.59}
2026-07-22T14:50:06.810797-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-22", "training_samples": 5500, "window": 5}
2026-07-22T12:00:05.697705-04:00 early_entry_1200 early_entry_shadow     {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.584, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:55:06.689792-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "matched_signals": 33, "recovery_stability_score": 0.584, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:50:01.765013-04:00 early_entry_1150 early_entry_shadow     {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.646, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:45:06.236742-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.677, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "matched_signals": 33, "recovery_stability_score": 0.677, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722155501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722155501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722155501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722155501)

</details>
