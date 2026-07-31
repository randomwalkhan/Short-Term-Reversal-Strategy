# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 12:02:50 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$16,667.25`
- Equity: `$33,867.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$645.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   1     86     16555.0                 17200.0         1.92            2.0       50.11         50.28          bid_ask_mid                        2.0                bid_ask_mid                    True           645.0                    3.9         92.31               13              1.24         25.34           25.81                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.95               21            1.25              0.50         57.43                60.55         0.666          pass              0.265             33.3                           0.468                0.65              0.293                      ok            True                  False
   KHC           93.33               15            1.04              0.19         26.30                32.41         0.594          pass              0.598             50.0                           0.596                0.87              0.421                      ok            True                  False
  MDLZ           92.86               14            1.22              0.54         62.85                34.51         0.581          pass              0.528             33.6                           0.279                2.15              0.544                      ok            True                  False
   KDP           82.61               23            0.71              0.16         31.50                32.85         0.555          pass              0.412             66.9                           0.655                1.41              0.372                      ok            True                  False
  MNST           88.89               18            1.12              0.76         97.32                23.72         0.534          pass              0.405             20.4                           0.316               -0.96              0.174                      ok            True                  False
  GILD           85.19               27            0.85              0.78        130.95                35.61         0.529          pass              0.502             65.8                           0.552               -3.06             -0.091                      ok            True                  False
  VRTX           85.71               14            1.68              5.68        479.27                32.97         0.523          pass              0.326             31.4                           0.551               -2.48             -0.019                      ok            True                  False
  AMGN          100.00               24            0.95              2.57        386.54                28.18         0.520          pass              0.713             55.8                           0.724                4.83              0.737                      ok            True                  False
  VRSK           84.62               13            2.43              3.41        198.89                43.45         0.501          pass              0.271             25.9                           0.506               -2.59              0.335                      ok            True                  False
  ALNY           87.50               32            1.04              1.49        204.84               124.46         0.767          pass              0.568             48.3                           0.294              -23.97             -1.953 downtrend_blocked_slope           False                  False
  ISRG           85.71               42            0.26              0.64        352.70                72.78         0.639          pass              0.649             77.8                           0.770                1.92              0.283                      ok           False                  False
  TMUS           88.89               36            0.40              0.49        173.13                56.67         0.580          pass              0.711             81.0                           0.780              -10.28             -1.117 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731120250)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731120250)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731120250)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731120250)

</details>
