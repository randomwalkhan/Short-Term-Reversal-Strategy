# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 10:15:02 EDT`
Last processed slot: `early_entry_1015`

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
- Equity: `$31,813.25`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$-27.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   1     55     15757.5                 15730.0         2.86           2.86       58.15         57.55     last_price_stale                        NaN                unavailable                   False           -27.5                  -0.17         91.18               34              0.66         31.86             0.0                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.67               12            1.69              0.69         58.24                59.18         0.687          pass              0.521             42.8                           0.351                2.77              0.323                       ok            True                  False
   STX           90.32               31            0.87              5.15        843.14                91.18         0.645          pass              0.629             49.6                           0.219               -8.25             -0.063                       ok            True                  False
  TMUS           83.33               12            2.12              2.62        176.09                55.40         0.626          pass              0.278             37.8                           0.618                1.78             -0.155                       ok            True                  False
 CMCSA           88.89               18            0.72              0.13         24.88                43.92         0.618          pass              0.561             69.7                           0.761               12.91              1.178                       ok            True                  False
  CTAS           90.48               21            1.10              1.57        202.97                37.87         0.580          pass              0.540             43.0                           0.588               -0.91             -0.364                       ok            True                  False
  DRAM           78.12               32            1.80              0.69         54.59               109.54         0.680          pass              0.378             54.6                           0.281               -7.55              0.034 downtrend_blocked_streak           False                  False
  GEHC           95.12               41            0.03              0.01         70.25                58.07         0.630          pass              0.952             96.3                           0.868               13.37              1.591                       ok           False                  False
  AMAT           88.46               26            2.49              9.53        542.53                86.87         0.604          pass              0.438             15.1                           0.149               -5.29              0.182 downtrend_blocked_streak           False                  False
  AMZN           75.00               20            1.85              3.58        275.88                61.64         0.589          pass              0.196             23.4                           0.463               16.54              2.317                       ok           False                  False
  LRCX           86.21               29            2.06              4.58        315.78                92.58         0.587          pass              0.492             47.1                           0.298               -2.69              0.434 downtrend_blocked_streak           False                  False
  WDAY           84.62               39            0.38              0.45        171.09                67.74         0.577          pass              0.594             73.2                           0.553               33.44              2.579                       ok           False                  False
  MSFT           78.12               32            1.11              3.83        491.17                57.67         0.559          pass              0.272             23.3                           0.261               27.72              3.195                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-06T10:15:02.220237-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:10:03.068587-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:05:03.941894-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T10:00:03.225302-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 25.4, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 0.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.595, "shadow_only": true, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.808, "early_reclaim_pct": 65.3, "matched_signals": 37, "recovery_stability_score": 0.595, "success_rate": 94.59, "ticker": "IDXX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T00:00:02.830410-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-05T15:10:01.218994-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-05T15:05:03.750105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-05T15:00:02.739208-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-05T14:55:01.792293-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-05T14:50:06.241655-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 15757.5, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 55, "early_entry_score": 0.753, "entry_mode": "regular", "entry_option_price": 2.865, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7033.0, "option_spread_pct": 3.84, "option_volume": 38.0, "success_rate": 91.18, "ticker": "PYPL", "timing_score": 0.614}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806101502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806101502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806101502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806101502)

</details>
