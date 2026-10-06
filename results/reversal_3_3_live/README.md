# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 09:30:02 EDT`
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
  MRVL     option         option MRVL261120C00270000       2026-10-05                   1     18     44010.0                 43686.0        24.45          24.27      269.79        274.17     last_price_stale                        NaN                unavailable                   False          -324.0                  -0.74         82.86               35              0.92         63.78             0.0                  54.74                2381.0          509.0               0.02                      ok
```

## Today's Closed Trades (2026-10-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           83.87               31            0.89              0.39         61.43                49.40         0.572            pass              0.440             46.6                           0.379               -4.04             -0.140                                 ok            True                  False
  CTAS           94.12               17            1.42              1.94        194.57                21.51         0.503            pass              0.560             28.9                           0.303               -3.11             -0.209                                 ok            True                  False
  LRCX           81.40               43            0.01              0.03        345.79                55.68         0.564            pass              0.589             98.4                           0.521               11.31              1.431                                 ok           False                  False
   TRI           89.74               39            0.28              0.19         97.00                50.10         0.516            pass              0.736             77.1                           0.471                1.20             -0.064                                 ok           False                  False
  TEAM          100.00               42            0.13              0.18        196.57                55.00         0.514            pass              0.902             83.4                           0.499                4.11              0.169                                 ok           False                  False
  KLAC           78.95               38            0.56              0.81        206.50                43.53         0.511            pass              0.238              0.0                           0.270                9.23              1.169                                 ok           False                  False
  PAYX           80.00               35            0.55              0.38         99.62                39.17         0.499 below_threshold              0.394             59.0                           0.365              -13.35             -0.908 downtrend_blocked_slope_and_streak           False                  False
   STX           88.00               25            2.83             17.56        879.56                65.24         0.496 below_threshold              0.465             34.1                           0.372               -6.21             -0.556            downtrend_blocked_slope           False                  False
   WDC           76.92               26            2.95              9.11        437.73                62.33         0.471 below_threshold              0.214             20.0                           0.403               -7.74             -0.817            downtrend_blocked_slope           False                  False
  PYPL           92.31               39            0.40              0.15         54.34                29.69         0.454 below_threshold              0.756             62.9                           0.397                2.46              0.154                                 ok           False                  False
  WDAY           91.43               35            0.81              1.07        188.50                38.39         0.452 below_threshold              0.517              0.0                           0.257               -0.43             -0.172                                 ok           False                  False
  VRSK           85.71               42            0.13              0.15        163.22                37.15         0.450 below_threshold              0.677             93.1                           0.634               -5.16             -0.513            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006093002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006093002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006093002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006093002)

</details>
