# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 15:25:01 EDT`
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

- Cash: `$17,648.00`
- Equity: `$31,135.50`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$62.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   0      5     13425.0                 13487.5        26.85          26.98      307.66        308.58          bid_ask_mid                      26.98                bid_ask_mid                    True            62.5                   0.47          87.1               31              1.19         68.92           67.35                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.65               31            3.56              3.49        138.75               179.06         0.700            pass              0.321             31.2                           0.553                5.55              2.572                       ok            True                  False
  LRCX           87.88               33            0.88              1.92        310.53                90.05         0.658            pass              0.589             53.2                           0.561                5.83              1.437                       ok            True                  False
  PYPL           93.94               33            0.78              0.32         58.93                60.12         0.648            pass              0.726             45.5                           0.457                4.52              0.343                       ok            True                  False
  AMAT           89.29               28            1.62              6.10        536.52                85.88         0.641            pass              0.515             27.8                           0.429                2.62              1.265                       ok            True                  False
 CMCSA           88.24               17            1.01              0.18         25.28                44.15         0.634            pass              0.498             56.2                           0.680               10.10              0.788                       ok            True                  False
  BKNG           95.65               23            1.43              2.15        213.50                46.72         0.562            pass              0.666             41.1                           0.483               13.15              1.040                       ok            True                  False
  MCHP           84.62               26            2.55              1.51         84.04                76.06         0.507            pass              0.398             39.2                           0.655                5.94              0.923                       ok            True                  False
   HON           85.71               21            1.30              2.24        245.25                29.28         0.500 below_threshold              0.399             40.9                           0.412               -1.11             -0.000                       ok            True                  False
  ALNY           83.33               30            1.25              1.91        218.38               128.37         0.810            pass              0.342             12.8                           0.203              -22.24             -2.659  downtrend_blocked_slope           False                  False
    MU           80.56               36            0.00              0.01        877.56               110.35         0.742            pass              0.562             99.9                           0.609               -2.52              0.721                       ok           False                  False
  DRAM           77.14               35            0.93              0.33         50.46               108.94         0.695            pass              0.438             67.1                           0.567               -4.39              0.505 downtrend_blocked_streak           False                  False
   STX           88.89               36            0.20              1.13        812.28                91.44         0.599            pass              0.752             94.0                           0.522               -0.71              0.530                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-10T15:10:01.692365-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T15:05:01.609183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T15:00:04.645498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T14:55:05.599659-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-10T14:50:01.766475-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 13425.0, "asset_type": "option", "contract_symbol": "LRCX260918C00310000", "contracts": 5, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 26.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 3.35, "option_volume": 93.0, "success_rate": 87.1, "ticker": "LRCX", "timing_score": 0.649}
2026-08-10T14:50:01.766475-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-10", "training_samples": 5614, "window": 5}
2026-08-10T12:00:04.535713-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "LRCX260918C00310000", "current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "entry_ask": 28.45, "entry_bid": 26.4, "entry_mode": "early", "entry_option_price": 27.425, "hypothetical_budget": 15536.5, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 7.47, "option_volume": 47.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "matched_signals": 37, "recovery_stability_score": 0.687, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T11:55:01.643754-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:50:01.638195-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:45:06.232412-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810152501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810152501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810152501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810152501)

</details>
