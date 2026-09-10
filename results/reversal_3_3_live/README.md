# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 15:25:05 EDT`
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

- Cash: `$35,166.10`
- Equity: `$70,716.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$975.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00130000       2026-09-10                   0     30     34575.0                 35550.0        11.52          11.85      129.47        129.64          bid_ask_mid                      11.85                bid_ask_mid                    True           975.0                   2.82          80.0               30              2.43          70.7           73.01                 104.12               13089.0          181.0               0.03                      ok
```

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.28              2.11        131.79               104.12         0.636          pass              0.340             47.8                           0.483                5.27              0.562                                 ok            True                  False
   KHC          100.00               11            0.67              0.12         24.56                28.60         0.614          pass              0.634             55.4                           0.463                0.18             -0.099                                 ok            True                  False
   EXC          100.00               10            0.81              0.25         43.59                15.30         0.573          pass              0.477              6.6                           0.117               -1.54             -0.002                                 ok            True                  False
   STX           87.10               31            1.68             10.39        881.47                74.71         0.552          pass              0.566             60.6                           0.632                2.92              0.553                                 ok            True                  False
   AEP           86.67               15            0.83              0.72        124.36                16.58         0.527          pass              0.370             35.4                           0.224                0.23              0.180                                 ok            True                  False
  CPRT           85.71               14            2.44              0.55         31.80                45.10         0.516          pass              0.297             22.0                           0.240               -4.35             -0.246                                 ok            True                  False
  AMGN          100.00                1            2.24              6.13        388.64                44.45         0.644          pass              0.495             10.3                           0.271              -13.13             -1.258 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.18               34            0.94              1.22        185.53                77.13         0.636          pass              0.643             40.5                           0.354               -3.38             -0.535 downtrend_blocked_slope_and_streak           False                  False
   TRI           96.55               29            1.02              0.69         96.68                52.79         0.547          pass              0.596              4.8                           0.181               -6.31             -0.758 downtrend_blocked_slope_and_streak           False                  False
  INTU           97.14               35            0.52              1.13        313.45                48.73         0.536          pass              0.803             60.9                           0.516               -9.70             -1.296 downtrend_blocked_slope_and_streak           False                  False
    ZS           96.97               33            1.57              1.82        165.32                64.27         0.529          pass              0.713             35.5                           0.548               -4.00             -1.166            downtrend_blocked_slope           False                  False
  MRVL           75.00               32            2.44              4.01        233.29                80.25         0.523          pass              0.330             43.8                           0.330               -6.46             -0.201           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T15:00:04.389376-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T14:55:01.338809-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T14:50:04.321187-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 34575.0, "asset_type": "option", "contract_symbol": "MSTR261016C00130000", "contracts": 30, "early_entry_score": 0.329, "entry_mode": "regular", "entry_option_price": 11.525, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 13089.0, "option_spread_pct": 3.04, "option_volume": 181.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.627}
2026-09-10T14:50:04.321187-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-10", "training_samples": 5765, "window": 5}
2026-09-10T12:00:03.311742-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:55:04.274439-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "entry_ask": 5.8, "entry_bid": 4.7, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 20.95, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "matched_signals": 37, "recovery_stability_score": 0.651, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:50:01.152194-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "entry_ask": 5.7, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 17.14, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "matched_signals": 41, "recovery_stability_score": 0.674, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.576, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:45:04.259583-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "entry_ask": 5.9, "entry_bid": 4.4, "entry_mode": "early", "entry_option_price": 5.15, "hypothetical_budget": 34870.55, "hypothetical_contracts": 67, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 29.13, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910152505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910152505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910152505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910152505)

</details>
