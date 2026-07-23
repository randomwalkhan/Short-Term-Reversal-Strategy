# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 10:10:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$30,858.00`
- Equity: `$30,858.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  AAPL     option         option AAPL260821C00325000     15          2026-07-22         2026-07-23       10.850      9.7650 -1627.50       -10.0 stop_loss_hit_at_scan
  PYPL     option         option PYPL260821C00055000     55          2026-07-21         2026-07-23        3.075      2.7675 -1691.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.10               31            0.66              0.26         55.40                61.85         0.662          pass              0.505             36.5                           0.345               21.68              2.331                      ok            True                  False
   KHC           92.31               13            0.75              0.14         25.90                31.13         0.639          pass              0.529             39.1                           0.325                4.40              0.485                      ok            True                  False
  MDLZ          100.00               11            1.17              0.50         60.65                31.72         0.636          pass              0.557             29.0                           0.396                3.17              0.345                      ok            True                  False
  AAPL           91.67               12            1.56              3.56        324.37                37.45         0.620          pass              0.453             22.3                           0.281                1.45              0.357                      ok            True                  False
   PEP           84.62               13            1.17              1.11        135.17                30.61         0.605          pass              0.243             13.1                           0.189               -2.76             -0.231                      ok            True                  False
  GILD           94.74               19            1.33              1.21        129.82                35.55         0.553          pass              0.618             36.6                           0.443               -4.62             -0.163                      ok            True                  False
   ADP           96.15               26            0.76              1.30        242.56                36.25         0.547          pass              0.640             26.1                           0.146               -0.01              0.057                      ok            True                  False
   MAR          100.00               13            1.69              4.36        367.93                21.19         0.536          pass              0.576             34.1                           0.274               -2.39             -0.123                      ok            True                  False
  PAYX          100.00               29            0.73              0.56        110.50                34.17         0.534          pass              0.654             24.8                           0.228                3.46              0.418                      ok            True                  False
  ORLY           81.48               27            1.23              0.74         86.21                43.13         0.520          pass              0.244             13.1                           0.163                0.41              0.060                      ok            True                  False
  AMGN           96.15               26            0.78              1.99        365.20                23.29         0.509          pass              0.733             58.5                           0.523               -0.11              0.130                      ok            True                  False
  SOXL           85.71               35            0.36              0.41        160.82               181.21         0.870          pass              0.691             94.9                           0.733              -16.65             -2.235 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-07-23T10:10:06.093555-04:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260821C00055000", "fill_price": 2.7675, "pnl": -1691.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-07-23T10:00:05.051160-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T09:55:06.076284-04:00      manage_1000               exit   {"asset_type": "option", "contract_symbol": "AAPL260821C00325000", "fill_price": 9.765, "pnl": -1627.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AAPL"}
2026-07-23T00:00:02.907448-04:00     data_refresh       data_refresh                                                                                                                                                                       {'saved': 93}
2026-07-22T15:10:06.070612-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-07-22T15:05:02.089739-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-07-22T15:00:04.754101-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-07-22T14:55:01.833206-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723101006)

</details>
