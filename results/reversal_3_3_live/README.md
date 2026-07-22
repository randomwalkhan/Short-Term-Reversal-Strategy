# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 15:00:04 EDT`
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

- Cash: `$989.25`
- Equity: `$34,336.75`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$160.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00325000       2026-07-22                   0     15     16275.0                 16462.5        10.85          10.98      324.66        324.39          bid_ask_mid                      10.98                bid_ask_mid                    True           187.5                   1.15         95.83               24              0.94         29.64           30.14                  37.60               16822.0          985.0               0.01                      ok
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 16885.0         3.08           3.07       55.67         55.42          bid_ask_mid                       3.07                bid_ask_mid                    True           -27.5                  -0.16         80.00               10              2.03         42.85           47.46                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            1.30              0.54         58.62               115.77         0.696          pass              0.497             75.7                           0.696               -6.37             -1.389                                 ok            True                  False
  PYPL           86.67               30            0.77              0.30         55.72                62.33         0.648          pass              0.466             30.1                           0.436               24.46              2.787                                 ok            True                  False
  AAPL           95.00               20            1.06              2.44        326.70                37.60         0.608          pass              0.590             20.9                           0.425                3.47              0.524                                 ok            True                  False
   ADP           93.75               16            1.58              2.72        245.05                36.45         0.575          pass              0.464              0.0                           0.198                0.40              0.305                                 ok            True                  False
  INTC           86.49               37            0.77              0.57        105.21                79.77         0.570          pass              0.660             83.2                           0.632               -5.08             -1.055                                 ok            True                  False
  PAYX          100.00               22            1.17              0.92        111.57                33.94         0.559          pass              0.568             10.8                           0.184                3.81              0.649                                 ok            True                  False
  SBUX           85.00               20            0.99              0.72        104.14                24.95         0.530          pass              0.294             13.5                           0.107               -0.43             -0.131                                 ok            True                  False
  CTSH           85.71               35            1.00              0.30         43.50                49.89         0.507          pass              0.503             44.6                           0.516                1.80              0.287                                 ok            True                  False
  PANW           92.00               25            2.11              5.06        339.98                60.47         0.504          pass              0.610             46.5                           0.484                4.47              0.577                                 ok            True                  False
  AMAT           90.62               32            0.68              2.69        563.40               100.84         0.718          pass              0.757             85.2                           0.680               -1.72             -0.808 downtrend_blocked_slope_and_streak           False                  False
  KLAC           88.89               36            0.51              0.77        217.23               102.77         0.715          pass              0.749             89.1                           0.764               -2.13             -0.714 downtrend_blocked_slope_and_streak           False                  False
    MU           81.82               33            0.09              0.59        970.57               110.72         0.713          pass              0.568             98.2                           0.715                2.23             -0.622                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-22T15:00:04.754101-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-22T14:55:01.833206-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-22T14:50:06.810797-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 16275.0, "asset_type": "option", "contract_symbol": "AAPL260821C00325000", "contracts": 15, "early_entry_score": 0.642, "entry_mode": "regular", "entry_option_price": 10.85, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 16822.0, "option_spread_pct": 0.92, "option_volume": 985.0, "success_rate": 95.83, "ticker": "AAPL", "timing_score": 0.59}
2026-07-22T14:50:06.810797-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-22", "training_samples": 5500, "window": 5}
2026-07-22T12:00:05.697705-04:00 early_entry_1200 early_entry_shadow      {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.584, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:55:06.689792-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "matched_signals": 33, "recovery_stability_score": 0.584, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:50:01.765013-04:00 early_entry_1150 early_entry_shadow      {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.646, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:45:06.236742-04:00 early_entry_1145 early_entry_shadow  {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.677, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "matched_signals": 33, "recovery_stability_score": 0.677, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:40:06.764688-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.0, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.0, "matched_signals": 34, "recovery_stability_score": 0.722, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:35:05.764580-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.72, "early_entry_score": 0.833, "early_reclaim_pct": 73.4, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.833, "early_reclaim_pct": 73.4, "matched_signals": 37, "recovery_stability_score": 0.753, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722150004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722150004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722150004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722150004)

</details>
