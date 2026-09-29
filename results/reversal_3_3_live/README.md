# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 10:20:06 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.29               35            0.99              1.09        156.67                99.69         0.702            pass              0.668             16.6                           0.114               20.05              2.178                      ok            True                  False
    ZS           97.62               42            0.47              0.65        199.11                81.58         0.601            pass              0.895             78.3                           0.732                2.36              0.374                      ok           False                  False
   WBD           95.00               40            0.11              0.02         30.89                38.06         0.578            pass              0.868             70.1                           0.587               10.11              1.217                      ok           False                  False
   TRI           87.50               32            1.09              0.75         97.01                56.59         0.567            pass              0.540             45.4                           0.453               -6.18             -0.310 downtrend_blocked_slope           False                  False
  AMGN           87.80               41            0.10              0.29        418.01                46.33         0.562            pass              0.738             91.1                           0.617               11.20              1.228                      ok           False                  False
  TMUS           82.61               23            1.06              1.24        165.92                33.31         0.531            pass              0.320             37.0                           0.568               -8.75             -0.670 downtrend_blocked_slope           False                  False
  PANW           69.23               26            2.48              6.80        389.18                69.78         0.527            pass              0.253             31.3                           0.369                1.94              0.419                      ok           False                  False
  CDNS           54.55               11            2.69              6.14        324.07                46.51         0.510            pass              0.150             30.9                           0.322               16.05              1.925                      ok           False                  False
   KDP           95.45               22            0.81              0.18         31.38                25.35         0.499 below_threshold              0.749             73.1                           0.497               -0.19              0.052                      ok           False                  False
  AAPL           75.00               12            1.61              3.81        336.77                22.11         0.494 below_threshold              0.105             14.0                           0.214                0.49              0.113                      ok           False                  False
   BKR           92.31               26            0.89              0.36         56.97                32.18         0.490 below_threshold              0.711             75.7                           0.655               -0.19              0.107                      ok           False                  False
  SNPS           70.83               24            1.39              4.07        415.87                42.94         0.490 below_threshold              0.320             59.3                           0.643               11.99              1.379                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-09-29T10:20:06.606039-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:15:06.005082-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:10:04.385907-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:05:05.319599-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 18.05, "pnl": 8760.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.35, "ticker": "CEG"}
2026-09-29T00:00:05.209830-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-28T15:10:04.000540-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-09-28T15:05:05.114052-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-09-28T15:00:06.099119-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929102006)

</details>
