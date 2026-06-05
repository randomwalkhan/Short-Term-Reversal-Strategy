# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 15:45:02 EDT`
Last processed slot: `manual`

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

- Cash: `$17,610.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   0     16     15760.0                 15760.0         9.85           9.85       98.17          98.9          bid_ask_mid                       9.85                bid_ask_mid                    True            -0.0                   -0.0         95.65               23              3.29          79.1            76.0                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           93.75               16            1.43              2.33        232.06                43.36         0.578          pass              0.600             45.0                           0.277               -2.16             -0.128                                 ok            True                  False
  CTSH           93.55               31            0.58              0.22         53.31                51.38         0.550          pass              0.781             74.8                           0.435                0.64              0.172                                 ok            True                  False
  TEAM           96.43               28            2.56              1.82        100.72                86.36         0.542          pass              0.709             45.0                           0.624               15.79              1.856                                 ok            True                  False
  WDAY           83.33               24            2.42              2.50        146.84                69.97         0.540          pass              0.291             18.3                           0.166               12.64              1.906                                 ok            True                  False
    ZS           71.43               14            3.59              3.40        133.80               157.69         0.835          pass              0.178             22.6                           0.529              -28.50             -2.370            downtrend_blocked_slope           False                  False
  MELI           91.30               23            1.75             20.01       1626.20                60.42         0.610          pass              0.470              7.1                           0.300               -3.50             -0.360            downtrend_blocked_slope           False                  False
    EA          100.00               10            0.23              0.33        203.26                 3.35         0.610          pass              0.464              1.1                           0.188                1.07              0.150                                 ok           False                  False
 GOOGL           81.82               11            1.80              4.69        370.18                30.67         0.541          pass              0.160             17.0                           0.301               -4.56             -0.727 downtrend_blocked_slope_and_streak           False                  False
  PANW           76.92               13            2.81              5.48        276.90                60.15         0.537          pass              0.135             20.5                           0.421                7.31              1.254                                 ok           False                  False
  ADSK           89.47               19            1.81              2.97        232.37                42.86         0.535          pass              0.377              3.6                           0.141               -4.81             -0.389            downtrend_blocked_slope           False                  False
  GOOG           90.91               11            1.75              4.51        367.34                28.09         0.531          pass              0.510             53.1                           0.346               -5.38             -0.763 downtrend_blocked_slope_and_streak           False                  False
  TTWO           96.15               26            1.38              2.10        215.75                37.81         0.510          pass              0.623             21.7                           0.313               -6.11             -0.367            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-06-05T15:10:05.308059-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-06-05T15:05:02.923743-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-06-05T15:00:04.878764-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-06-05T14:55:02.045804-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-06-05T14:50:02.059586-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.774, "option_liquidity_status": "low_volume", "option_open_interest": 374.0, "option_spread_pct": 9.63, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "ROST", "timing_score": 0.527}
2026-06-05T14:50:02.059586-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"early_entry_score": 0.624, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 359.0, "option_spread_pct": 16.53, "option_volume": 18.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-06-05T14:50:02.059586-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-05", "training_samples": 5221, "window": 5}
2026-06-05T14:50:02.059586-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 15760.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 16, "early_entry_score": 0.627, "entry_mode": "regular", "entry_option_price": 9.85, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1414.0, "option_spread_pct": 11.17, "option_volume": 56.0, "success_rate": 95.65, "ticker": "TEAM", "timing_score": 0.524}
2026-06-05T12:00:02.830136-04:00 early_entry_1200      early_entry_shadow  {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "entry_ask": 17.4, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 3.81, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "matched_signals": 36, "recovery_stability_score": 0.673, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:55:06.016628-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "entry_ask": 17.15, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 16.575, "hypothetical_budget": 16685.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 6.94, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.624, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "matched_signals": 36, "recovery_stability_score": 0.624, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605154502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605154502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605154502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605154502)

</details>
