# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:25:04 EDT`
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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           81.25               16            1.56              0.62         56.30                61.55         0.660          pass              0.233             31.3                           0.448               23.49              2.788                  ok            True                  False
  META           86.11               36            0.66              3.00        644.72                53.08         0.559          pass              0.563             57.1                           0.540                6.90              0.870                  ok            True                  False
  PAYX          100.00               21            1.29              1.04        113.95                33.31         0.545          pass              0.583             18.2                           0.338                7.14              0.798                  ok            True                  False
   ROP           89.47               19            1.56              3.98        361.44                31.85         0.526          pass              0.455             30.0                           0.386               -1.62             -0.063                  ok            True                  False
   WBD           92.59               27            0.50              0.09         26.83                20.40         0.520          pass              0.666             55.0                           0.620                2.35              0.398                  ok            True                  False
   ADP           95.00               20            1.28              2.29        254.29                34.14         0.519          pass              0.588             23.3                           0.337                5.22              0.601                  ok            True                  False
  GILD           92.86               28            0.57              0.53        134.05                34.72         0.516          pass              0.607             30.9                           0.296                3.02              0.047                  ok            True                  False
   CSX           91.67               24            0.54              0.19         50.67                17.40         0.510          pass              0.575             39.7                           0.257                3.41              0.449                  ok            True                  False
  BKNG           85.71               21            1.81              2.30        180.69                41.44         0.508          pass              0.348             23.8                           0.257               -1.46              0.140                  ok            True                  False
  ORLY           83.87               31            1.09              0.65         85.77                41.23         0.507          pass              0.406             37.2                           0.435                1.04              0.005                  ok            True                  False
  AAPL          100.00                3            2.16              5.04        331.58                36.42         0.631          pass              0.467              1.4                           0.039                4.44              0.688                  ok           False                  False
  MDLZ          100.00                7            1.36              0.58         60.75                32.63         0.608          pass              0.509             16.2                           0.308                1.69              0.223                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-20T10:25:04.012806-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:20:01.111901-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "TXN260821C00290000", "fill_price": 23.275, "pnl": 2187.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.51, "ticker": "TXN"}
2026-07-20T10:05:02.132166-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:00:05.019489-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T03:00:02.156318-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-07-18T02:55:03.939140-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:50:01.103428-04:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720102504)

</details>
