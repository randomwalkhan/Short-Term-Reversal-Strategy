# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-11 15:25:06 EDT`
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

- Cash: `$14,550.75`
- Equity: `$28,590.75`
- Realized PnL: `$18,725.75`
- Unrealized PnL: `$-135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PAYX     option         option PAYX260717C00100000       2026-06-11                   0     27     14175.0                 14040.0         5.25            5.2      100.46         99.78          bid_ask_mid                        5.2                bid_ask_mid                    True          -135.0                  -0.95         100.0               22              0.63         41.79           44.23                  34.22                 685.0          131.0                0.1                      ok
```

## Today's Closed Trades (2026-06-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CTSH     option         option CTSH260717C00055000     73          2026-06-09         2026-06-11         2.05       1.845 -1496.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               13            1.31              0.92        100.70                34.22         0.592            pass              0.615             45.2                           0.278                4.47              0.277                                 ok            True                  False
   ADP           95.83               24            1.16              1.88        230.29                32.69         0.532            pass              0.669             40.7                           0.243                3.89              0.292                                 ok            True                  False
  INTU           72.73               22            2.84              5.65        281.80               101.53         0.663            pass              0.225             26.2                           0.240              -11.77             -1.776 downtrend_blocked_slope_and_streak           False                  False
   TRI           80.00               20            1.80              1.03         81.52                68.04         0.615            pass              0.252             41.2                           0.283               -4.74             -0.817 downtrend_blocked_slope_and_streak           False                  False
  CDNS           94.74               38            0.29              0.77        384.80                58.86         0.546            pass              0.902             89.1                           0.605                2.72             -0.111                                 ok           False                  False
  CTSH           85.71               21            1.41              0.51         51.59                46.99         0.537            pass              0.477             65.9                           0.475               -5.14             -0.794 downtrend_blocked_slope_and_streak           False                  False
  MSFT           40.00                5            2.45              6.82        394.44                36.94         0.500            pass              0.131             27.1                           0.339               -9.22             -1.404 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.00               25            3.50              2.24         90.58                86.53         0.486 below_threshold              0.471             36.4                           0.347               -5.31             -1.578 downtrend_blocked_slope_and_streak           False                  False
  CPRT           89.29               28            1.10              0.24         31.26                31.19         0.485 below_threshold              0.505             29.6                           0.196               -6.81             -0.549 downtrend_blocked_slope_and_streak           False                  False
  SNPS           82.61               23            1.72              5.56        458.16                48.54         0.482 below_threshold              0.351             48.9                           0.364               -5.83             -0.736            downtrend_blocked_slope           False                  False
  WDAY           84.62               13            4.27              4.11        135.71                67.65         0.470 below_threshold              0.248             19.3                           0.186                1.22             -0.560                                 ok           False                  False
  MDLZ           94.12               34            0.50              0.22         64.08                18.57         0.450 below_threshold              0.740             52.9                           0.421                2.36              0.390                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260611152506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260611152506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260611152506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260611152506)

</details>
