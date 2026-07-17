# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 09:40:05 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.10               31            0.78              0.31         56.60                63.95         0.626          pass              0.602             70.0                           0.546               23.78              2.497                      ok            True                  False
  ASML           95.65               23            2.62             32.68       1770.87                64.12         0.556          pass              0.575             10.9                           0.225               -1.76             -0.091                      ok            True                  False
  AVGO           80.95               21            2.18              5.71        372.00                50.81         0.510          pass              0.254             34.7                           0.344                1.62              0.208                      ok            True                  False
  BKNG           86.67               30            1.14              1.48        183.98                41.98         0.508          pass              0.415             17.6                           0.210               -1.12              0.040                      ok            True                  False
  DRAM           82.35               17            4.10              1.51         51.77               117.20         0.643          pass              0.295             40.4                           0.408              -17.10             -1.904 downtrend_blocked_slope           False                  False
   TXN           85.71                7            3.61              7.36        288.06                64.46         0.589          pass              0.233              7.4                           0.231               -4.22             -0.278 downtrend_blocked_slope           False                  False
    MU           83.33               18            4.18             24.99        842.49               110.15         0.588          pass              0.278             25.8                           0.259              -16.19             -1.412 downtrend_blocked_slope           False                  False
  KLAC           72.73               11            4.97              7.63        216.10               106.93         0.580          pass              0.116             17.1                           0.207              -11.49             -0.635 downtrend_blocked_slope           False                  False
  META           70.00               10            2.51             11.68        659.53                56.28         0.571          pass              0.107             16.7                           0.353               11.14              1.329                      ok           False                  False
   ADI           72.73               11            3.04              8.10        377.06                54.65         0.554          pass              0.105             14.4                           0.227               -2.18             -0.077                      ok           False                  False
   STX           87.50               16            3.42             17.86        737.83                93.61         0.534          pass              0.432             46.2                           0.507              -12.22             -1.137 downtrend_blocked_slope           False                  False
  AAPL           97.14               35            0.43              1.00        332.83                36.90         0.533          pass              0.791             57.1                           0.381                7.52              0.717                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-17T09:20:02.076532-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-16T15:10:05.118265-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:50:02.142710-04:00   entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-16T14:50:02.142710-04:00   entry_1500 entry_candidate_skipped                              {"early_entry_score": 0.671, "option_liquidity_status": "low_volume", "option_open_interest": 761.0, "option_spread_pct": 4.13, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.508}
2026-07-16T14:50:02.142710-04:00   entry_1500 entry_candidate_skipped                          {"early_entry_score": 0.521, "option_liquidity_status": "wide_spread", "option_open_interest": 3043.0, "option_spread_pct": 25.76, "option_volume": 343.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.531}
2026-07-16T14:50:02.142710-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00   entry_1500 entry_candidate_skipped              {"early_entry_score": 0.267, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 84.0, "option_spread_pct": 8.5, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.577}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717094005)

</details>
