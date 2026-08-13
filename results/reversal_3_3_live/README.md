# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:05:05 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INSM           81.82               22            1.96              1.81        131.50               107.72         0.768              pass              0.251             15.1                           0.190               27.79              3.809                       ok            True                  False
   BKR           84.62               13            1.87              0.84         63.92                33.24         0.549              pass              0.296             32.6                           0.274                5.70              0.752                       ok            True                  False
  ISRG           87.50               40            0.20              0.55        401.03                69.94         0.666              pass              0.694             75.8                           0.646               13.46              1.344                       ok           False                  False
   ROP           97.44               39            0.06              0.17        395.16                44.32         0.586              pass              0.934             93.9                           0.580                1.47              0.203                       ok           False                  False
   HON           91.89               37            0.36              0.59        235.09                35.57         0.519              pass              0.736             62.4                           0.411               -3.07             -0.589  downtrend_blocked_slope           False                  False
  PCAR           97.56               41            0.11              0.10        131.02                29.70         0.492   below_threshold              0.929             93.3                           0.612               -2.12             -0.154                       ok           False                  False
  ROST           93.55               31            0.63              1.10        247.78                22.10         0.477   below_threshold              0.767             72.8                           0.804               -2.33             -0.090 downtrend_blocked_streak           False                  False
  TTWO           85.37               41            0.31              0.53        242.77                36.12         0.447   below_threshold              0.581             64.4                           0.364               -2.10              0.194                       ok           False                  False
   WMT           78.05               41            0.32              0.26        115.90                19.91         0.414   below_threshold              0.436             64.8                           0.390                4.09              0.329                       ok           False                  False
  CSCO             NaN                0            7.82              6.78        120.97                27.02           NaN no_signal_history                NaN              NaN                           0.551                0.55              0.354                       ok           False                  False
  AAPL             NaN                0            0.00              0.00        304.46                35.20           NaN no_signal_history                NaN              NaN                           0.803               -8.61             -0.458  downtrend_blocked_slope           False                  False
  ABNB             NaN                0            0.00              0.00        182.74                64.05           NaN no_signal_history                NaN              NaN                           0.915               19.43              2.318                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-13T10:05:05.347522-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:00:40.571954-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600                    exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:50:05.779182-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.604, "option_liquidity_status": "low_volume", "option_open_interest": 178.0, "option_spread_pct": 8.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.806}
2026-08-12T14:50:05.779182-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-12", "training_samples": 5645, "window": 5}
2026-08-12T14:50:05.779182-04:00       entry_1500                   entry {"allocated_cash": 17360.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 62, "early_entry_score": 0.819, "entry_mode": "regular", "entry_option_price": 2.8, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7246.0, "option_spread_pct": 5.71, "option_volume": 86.0, "success_rate": 93.94, "ticker": "PYPL", "timing_score": 0.657}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813100505)

</details>
