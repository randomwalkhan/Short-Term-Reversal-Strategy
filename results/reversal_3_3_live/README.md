# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-11 15:50:06 EDT`
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

- Cash: `$14,550.75`
- Equity: `$27,780.75`
- Realized PnL: `$18,725.75`
- Unrealized PnL: `$-945.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PAYX     option         option PAYX260717C00100000       2026-06-11                   0     27     14175.0                 13230.0         5.25            4.9      100.46         99.84          bid_ask_mid                        4.9                bid_ask_mid                    True          -945.0                  -6.67         100.0               22              0.63         41.79            41.0                  34.22                 685.0          131.0                0.1                      ok
```

## Today's Closed Trades (2026-06-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CTSH     option         option CTSH260717C00055000     73          2026-06-09         2026-06-11         2.05       1.845 -1496.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               13            1.25              0.88        100.72                34.22         0.596            pass              0.623             47.7                           0.324                4.53              0.280                                 ok            True                  False
  CDNS           94.44               36            0.51              1.38        384.54                58.86         0.544            pass              0.854             80.5                           0.527                2.49             -0.121                                 ok            True                  False
   ADP           95.00               20            1.58              2.56        230.00                32.69         0.532            pass              0.578             19.4                           0.147                3.45              0.273                                 ok            True                  False
  MDLZ           95.45               22            0.89              0.40         64.01                18.57         0.511            pass              0.580             16.2                           0.154                1.96              0.372                                 ok            True                  False
  INTU           68.42               19            2.98              5.93        281.68               101.53         0.667            pass              0.194             22.5                           0.286              -11.90             -1.783 downtrend_blocked_slope_and_streak           False                  False
   TRI           80.00               20            1.46              0.84         81.60                68.04         0.637            pass              0.287             52.4                           0.618               -4.41             -0.802 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               20            0.19              0.20        144.24                19.86         0.588            pass              0.723             65.9                           0.308               -0.50              0.079                                 ok           False                  False
  MSFT           50.00               10            1.79              4.99        395.22                36.94         0.524            pass              0.192             46.6                           0.713               -8.61             -1.374 downtrend_blocked_slope_and_streak           False                  False
  CTSH           89.66               29            1.00              0.36         51.65                46.99         0.514            pass              0.663             75.7                           0.678               -4.75             -0.775 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.89               27            3.01              1.93         90.71                86.53         0.507            pass              0.537             45.2                           0.649               -4.83             -1.555 downtrend_blocked_slope_and_streak           False                  False
  SNPS           82.61               23            1.66              5.34        458.25                48.54         0.487 below_threshold              0.358             50.9                           0.459               -5.77             -0.733            downtrend_blocked_slope           False                  False
   WMT           88.10               42            0.15              0.13        120.54                35.20         0.486 below_threshold              0.717             84.1                           0.481                1.27              0.427                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-11T15:10:05.901456-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-06-11T15:05:01.637462-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-06-11T15:00:05.308604-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-06-11T14:55:01.789795-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-06-11T14:50:01.795515-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 14175.0, "asset_type": "option", "contract_symbol": "PAYX260717C00100000", "contracts": 27, "early_entry_score": 0.758, "entry_mode": "regular", "entry_option_price": 5.25, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 685.0, "option_spread_pct": 9.52, "option_volume": 131.0, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.573}
2026-06-11T14:50:01.795515-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-11", "training_samples": 5237, "window": 5}
2026-06-11T11:58:26.585033-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-11T11:22:14.657857-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "KDP260717C00031000", "current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "entry_ask": 1.45, "entry_bid": 1.1, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 14362.88, "hypothetical_contracts": 112, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 2194.0, "option_spread_pct": 27.45, "option_volume": 80.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "matched_signals": 32, "recovery_stability_score": 0.703, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-11T10:46:23.679160-04:00 early_entry_1045 early_entry_shadow                         {"contract_symbol": "CSCO260717C00120000", "current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "entry_ask": 4.8, "entry_bid": 4.55, "entry_mode": "early", "entry_option_price": 4.675, "hypothetical_budget": 14362.88, "hypothetical_contracts": 30, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 11268.0, "option_spread_pct": 5.35, "option_volume": 155.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.795, "early_reclaim_pct": 72.8, "matched_signals": 30, "recovery_stability_score": 0.78, "success_rate": 96.67, "ticker": "KDP", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-11T10:10:05.812920-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "entry_ask": 8.7, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 14362.88, "hypothetical_contracts": 19, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 261.0, "option_spread_pct": 33.56, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.778, "early_reclaim_pct": 70.9, "matched_signals": 39, "recovery_stability_score": 0.672, "success_rate": 92.31, "ticker": "ROP", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260611155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260611155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260611155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260611155006)

</details>
