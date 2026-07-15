# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 15:40:02 EDT`
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

- Cash: `$16,570.25`
- Equity: `$30,610.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$-20.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   ADI     option         option ADI260821C00380000       2026-07-15                   0      4     14060.0                 14040.0        35.15           35.1      388.76        391.05          bid_ask_mid                       35.1                bid_ask_mid                    True           -20.0                  -0.14         86.21               29              1.02          62.6           59.16                  55.85                 129.0           42.0               0.05                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               12            0.87              0.36         58.65                30.54         0.629          pass              0.610             44.6                           0.325                0.78             -0.100                                 ok            True                  False
   TXN           88.00               25            1.44              3.09        304.23                65.52         0.583          pass              0.540             56.0                           0.683                1.03              0.282                                 ok            True                  False
  NXPI           86.67               30            1.13              2.24        282.91                58.07         0.538          pass              0.563             66.1                           0.672               -0.13              0.266                                 ok            True                  False
   WBD           87.50               16            0.71              0.14         27.42                20.00         0.537          pass              0.466             57.6                           0.683                2.34              0.286                                 ok            True                  False
  MSTR           77.78               45            0.08              0.06         97.56               100.18         0.645          pass              0.545             93.4                           0.596               12.16              0.436                                 ok           False                  False
  SOXL           85.00               20            6.52              8.06        173.21               219.49         0.642          pass              0.435             56.8                           0.775              -38.08             -3.060            downtrend_blocked_slope           False                  False
  KLAC           80.95               21            2.96              4.77        228.33               109.33         0.614          pass              0.313             51.0                           0.654              -25.90             -2.045 downtrend_blocked_slope_and_streak           False                  False
   CSX          100.00                7            1.56              0.55         49.69                19.08         0.586          pass              0.527             22.8                           0.327                3.39              0.324                                 ok           False                  False
   ADI           87.88               33            0.50              1.37        392.16                55.85         0.579          pass              0.659             79.4                           0.742               -1.61              0.111                                 ok           False                  False
  MCHP           93.10               29            1.22              0.74         86.79                68.63         0.578          pass              0.744             70.0                           0.740               -5.65             -0.250            downtrend_blocked_slope           False                  False
   LIN          100.00                7            1.52              5.56        520.16                20.66         0.575          pass              0.497             13.1                           0.264               -0.84             -0.314                                 ok           False                  False
   KDP           92.31               26            0.25              0.05         30.24                36.34         0.574          pass              0.711             73.0                           0.331               -7.78             -0.940 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-15T15:10:01.366399-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:00:06.972520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T14:50:07.762689-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"allocated_cash": 14060.0, "asset_type": "option", "contract_symbol": "ADI260821C00380000", "contracts": 4, "early_entry_score": 0.523, "entry_mode": "regular", "entry_option_price": 35.15, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 129.0, "option_spread_pct": 5.41, "option_volume": 42.0, "success_rate": 86.21, "ticker": "ADI", "timing_score": 0.569}
2026-07-15T14:50:07.762689-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.633, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 14.0, "option_spread_pct": 5.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.636}
2026-07-15T14:50:07.762689-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-15", "training_samples": 5408, "window": 5}
2026-07-15T12:00:03.706415-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "CRWD260821C00210000", "current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "entry_ask": 14.6, "entry_bid": 14.25, "entry_mode": "early", "entry_option_price": 14.425, "hypothetical_budget": 15315.13, "hypothetical_contracts": 10, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1292.0, "option_spread_pct": 2.43, "option_volume": 518.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.726, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "matched_signals": 39, "recovery_stability_score": 0.726, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-15T11:55:06.679355-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:50:02.876804-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:45:04.888686-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715154002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715154002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715154002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715154002)

</details>
