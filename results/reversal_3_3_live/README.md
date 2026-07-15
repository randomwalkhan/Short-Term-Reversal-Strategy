# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 16:00:04 EDT`
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

- Cash: `$16,570.25`
- Equity: `$30,650.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$20.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   ADI     option         option ADI260821C00380000       2026-07-15                   0      4     14060.0                 14080.0        35.15           35.2      388.76         391.9          bid_ask_mid                       35.2                bid_ask_mid                    True            20.0                   0.14         86.21               29              1.02          62.6           59.33                  55.85                 129.0           42.0               0.05                      ok
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
   TXN           88.00               25            1.42              3.04        304.25                65.52         0.584          pass              0.542             56.7                           0.709                1.05              0.283                                 ok            True                  False
  MCHP           93.75               32            1.00              0.61         86.85                68.63         0.574          pass              0.797             75.4                           0.811               -5.44             -0.240                                 ok            True                   True
  MPWR           81.25               32            1.75             16.84       1369.19                84.79         0.563          pass              0.427             63.7                           0.780               -2.17              0.152                                 ok            True                  False
   CSX           86.67               15            0.98              0.34         49.77                19.08         0.553          pass              0.421             51.5                           0.655                4.00              0.350                                 ok            True                  False
   XEL          100.00               11            1.12              0.63         79.90                21.57         0.542          pass              0.548             29.1                           0.408               -1.28             -0.112                                 ok            True                  False
   WBD           87.50               16            0.76              0.15         27.42                20.00         0.533          pass              0.456             54.3                           0.602                2.29              0.283                                 ok            True                  False
  NXPI           84.00               25            1.69              3.36        282.43                58.07         0.530          pass              0.407             49.2                           0.397               -0.70              0.240                                 ok            True                  False
  SBUX           85.00               20            1.00              0.74        105.85                22.72         0.503          pass              0.333             27.6                           0.381                2.86              0.361                                 ok            True                  False
  SOXL           85.71               21            6.03              7.46        173.46               219.49         0.668          pass              0.473             60.0                           0.841              -37.76             -3.036            downtrend_blocked_slope           False                  False
  KLAC           81.82               22            2.23              3.60        228.83               109.33         0.655          pass              0.383             63.0                           0.776              -25.35             -2.011 downtrend_blocked_slope_and_streak           False                  False
  MSTR           77.78               45            0.11              0.08         97.55               100.18         0.643          pass              0.537             91.0                           0.691               12.12              0.435                                 ok           False                  False
  AMAT           83.33               18            2.73             11.38        590.82                98.89         0.586          pass              0.374             57.8                           0.738              -19.86             -1.377 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715160004)

</details>
