# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 15:30:04 EDT`
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

- Cash: `$167.25`
- Equity: `$34,644.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,422.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option  CSX260918C00050000       2026-07-30                   1     86     16555.0                 17845.0         1.92           2.08       50.11         50.51          bid_ask_mid                       2.08                bid_ask_mid                    True          1290.0                   7.79         92.31               13              1.24         25.34           26.22                  28.82                2759.0          136.0               0.03                      ok
  PYPL     option         option PYPL260918C00057500       2026-07-31                   0     66     16500.0                 16632.0         2.50           2.52       57.10         57.28          bid_ask_mid                       2.52                bid_ask_mid                    True           132.0                   0.80         86.21               29              0.95         31.54           32.76                  60.55                6425.0          263.0               0.05                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           88.24               34            0.64              0.26         57.54                60.55         0.631          pass              0.640             65.7                           0.624                1.27              0.321                                 ok            True                  False
  MDLZ           94.12               17            0.97              0.43         62.90                34.51         0.579          pass              0.623             47.4                           0.599                2.41              0.555                                 ok            True                  False
  CTAS           91.67               24            0.98              1.41        206.18                40.09         0.578          pass              0.622             53.2                           0.394                0.16              0.459                                 ok            True                  False
   KHC           90.91               11            1.69              0.31         26.25                32.41         0.575          pass              0.412             19.1                           0.272                0.21              0.391                                 ok            True                  False
   KDP           80.00               15            1.44              0.32         31.43                32.85         0.558          pass              0.188             33.1                           0.299                0.66              0.338                                 ok            True                  False
  GILD           85.19               27            0.66              0.60        131.02                35.61         0.541          pass              0.526             73.5                           0.594               -2.87             -0.083                                 ok            True                  False
  MNST           88.89               18            1.10              0.75         97.33                23.72         0.535          pass              0.410             21.9                           0.338               -0.94              0.175                                 ok            True                  False
  ALNY           90.00               40            0.70              1.00        205.05               124.46         0.743          pass              0.761             73.4                           0.715              -23.71             -1.937            downtrend_blocked_slope           False                  False
  LRCX           85.19               27            1.58              3.29        296.31                97.18         0.645          pass              0.316              0.0                             NaN               -6.47             -1.469 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.88               33            0.62              0.75        173.02                56.67         0.584          pass              0.634             70.8                           0.652              -10.48             -1.126            downtrend_blocked_slope           False                  False
  GEHC           87.50                8            2.73              1.34         69.37                56.76         0.567          pass              0.351             31.3                           0.369                7.93              1.209                                 ok           False                  False
  DRAM           77.78               27            2.71              0.99         51.91               113.92         0.556          pass              0.264             31.7                           0.277               -3.41             -1.391 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T15:05:50.400930-04:00       entry_1500              entry {"allocated_cash": 16500.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 66, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 2.5, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 6425.0, "option_spread_pct": 4.8, "option_volume": 263.0, "success_rate": 86.21, "ticker": "PYPL", "timing_score": 0.642}
2026-07-31T15:05:50.400930-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-31", "training_samples": 5549, "window": 5}
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731153004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731153004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731153004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731153004)

</details>
