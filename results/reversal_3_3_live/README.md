# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 15:15:05 EDT`
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

- Cash: `$16,083.25`
- Equity: `$31,868.25`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$27.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   0     55     15757.5                 15785.0         2.86           2.87       58.15         58.03          bid_ask_mid                       2.87                bid_ask_mid                    True            27.5                   0.17         91.18               34              0.66         31.86           32.89                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.12               34            0.62              0.30         70.13                58.11         0.629          pass              0.658             19.4                           0.346               13.77              1.701                       ok            True                  False
  PYPL           90.62               32            0.88              0.36         58.39                60.15         0.612          pass              0.702             70.2                           0.410                4.53              0.471                       ok            True                  False
  MRVL           80.00               35            1.67              2.55        217.50               100.52         0.589          pass              0.389             54.4                           0.477                1.87              0.265                       ok            True                  False
  PAYX          100.00               17            0.72              0.60        118.40                35.13         0.583          pass              0.734             76.5                           0.607                7.48              0.765                       ok            True                  False
  CTAS           90.48               21            1.27              1.81        202.87                37.77         0.580          pass              0.514             34.4                           0.508               -0.15             -0.115                       ok            True                  False
   PEP           84.00               25            0.58              0.56        138.86                25.68         0.547          pass              0.358             32.2                           0.234                1.95              0.237                       ok            True                  False
  CPRT           83.33               18            2.07              0.43         29.22                38.86         0.503          pass              0.273             26.9                           0.459                5.96              0.605                       ok            True                  False
  SOXL           80.00               35            2.14              2.09        139.00               182.46         0.772          pass              0.453             69.8                           0.798              -14.96             -1.760 downtrend_blocked_streak           False                  False
   WDC           82.14               28            1.64              6.31        545.85                99.34         0.663          pass              0.270              8.7                           0.236               -3.08              0.123 downtrend_blocked_streak           False                  False
  AMAT           91.43               35            0.85              3.25        545.23                87.24         0.657          pass              0.750             71.1                           0.699               -2.16             -0.284 downtrend_blocked_streak           False                  False
  TMUS           87.50                8            2.57              3.19        175.84                55.59         0.638          pass              0.337             24.4                           0.281               -9.58             -0.454  downtrend_blocked_slope           False                  False
  LRCX           86.67               30            1.40              3.11        316.41                92.33         0.633          pass              0.567             64.1                           0.596               -1.88             -0.107 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-05T15:10:01.218994-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T15:05:03.750105-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T15:00:02.739208-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:55:01.792293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:50:06.241655-04:00       entry_1500                   entry {"allocated_cash": 15757.5, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 55, "early_entry_score": 0.753, "entry_mode": "regular", "entry_option_price": 2.865, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7033.0, "option_spread_pct": 3.84, "option_volume": 38.0, "success_rate": 91.18, "ticker": "PYPL", "timing_score": 0.614}
2026-08-05T14:50:06.241655-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.655, "option_liquidity_status": "low_volume", "option_open_interest": 2148.0, "option_spread_pct": 6.06, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "GEHC", "timing_score": 0.628}
2026-08-05T14:50:06.241655-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-05", "training_samples": 5567, "window": 5}
2026-08-05T12:00:04.693066-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805151505)

</details>
