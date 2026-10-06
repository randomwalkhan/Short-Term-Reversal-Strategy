# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 09:40:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$44,576.80`
- Equity: `$88,262.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$-324.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MRVL     option         option MRVL261120C00270000       2026-10-05                   1     18     44010.0                 43686.0        24.45          24.27      269.79        293.46     last_price_stale                        NaN                unavailable                   False          -324.0                  -0.74         82.86               35              0.92         63.78             0.0                  54.74                2381.0          509.0               0.02                      ok
```

## Today's Closed Trades (2026-10-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           84.00               25            1.53              0.66         61.32                49.40         0.567            pass              0.345             27.3                           0.273               -4.66             -0.170                                 ok            True                  False
   BKR           88.89               18            1.41              0.57         57.14                33.54         0.532            pass              0.374             10.0                           0.228               -1.21             -0.265                                 ok            True                  False
  AMAT           83.78               37            1.24              4.69        540.27                48.32         0.500 below_threshold              0.395             21.5                           0.265               13.36              1.615                                 ok            True                  False
  QCOM           90.24               41            0.15              0.19        180.71                57.17         0.570            pass              0.535              1.5                           0.175               -8.95             -1.083 downtrend_blocked_slope_and_streak           False                  False
    MU           92.50               40            0.36              2.65       1062.82                46.96         0.518            pass              0.820             78.4                           0.472               -3.28             -0.158                                 ok           False                  False
  LRCX           76.67               30            1.91              4.63        343.82                55.68         0.515            pass              0.238             17.8                           0.252                9.19              1.344                                 ok           False                  False
  TMUS           89.19               37            0.22              0.25        164.53                30.04         0.508            pass              0.637             53.8                           0.472                1.15             -0.058                                 ok           False                  False
  PAYX           77.78               36            0.40              0.28         99.66                39.17         0.499 below_threshold              0.433             69.9                           0.494              -13.23             -0.902 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.10               29            0.18              0.03         21.84                16.80         0.471 below_threshold              0.690             55.6                           0.334               -9.13             -1.069 downtrend_blocked_slope_and_streak           False                  False
  KLAC           75.00               28            2.03              2.94        205.59                43.53         0.468 below_threshold              0.197             10.1                           0.235                7.61              1.101                                 ok           False                  False
  ADBE           90.91               44            0.07              0.12        238.73                36.84         0.465 below_threshold              0.775             79.3                           0.374                0.15              0.043                                 ok           False                  False
   APP           83.33               48            0.15              0.29        281.85                52.52         0.460 below_threshold              0.596             87.1                           0.410              -14.35             -1.761 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-06T00:00:06.226199-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-10-05T15:10:05.053706-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T15:05:06.249640-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T15:00:06.038960-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T14:55:02.074607-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T14:50:07.104378-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 44010.0, "asset_type": "option", "contract_symbol": "MRVL261120C00270000", "contracts": 18, "early_entry_score": 0.427, "entry_mode": "regular", "entry_option_price": 24.45, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2381.0, "option_spread_pct": 2.04, "option_volume": 509.0, "success_rate": 82.86, "ticker": "MRVL", "timing_score": 0.509}
2026-10-05T14:50:07.104378-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.457, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 29.3, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.53}
2026-10-05T14:50:07.104378-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-05", "training_samples": 5905, "window": 5}
2026-10-05T12:00:06.148315-04:00 early_entry_1200      early_entry_shadow   {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "matched_signals": 33, "recovery_stability_score": 0.669, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:55:05.965880-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.716, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "matched_signals": 34, "recovery_stability_score": 0.716, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006094001)

</details>
