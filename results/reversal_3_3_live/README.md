# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:20:10 EDT`
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
  INSM           80.95               21            2.01              1.86        131.48               107.72         0.767              pass              0.237             20.6                           0.220               27.72              3.806                       ok            True                  False
  MPWR           84.21               38            0.62              6.15       1422.37                55.33         0.554              pass              0.465             36.8                           0.260                7.60              0.607                       ok            True                  False
   BKR           81.82               11            2.20              0.99         63.86                33.24         0.537              pass              0.170             20.5                           0.325                5.34              0.737                       ok            True                  False
  ISRG           87.50               40            0.15              0.41        401.09                69.94         0.669              pass              0.713             82.0                           0.737               13.52              1.346                       ok           False                  False
  FAST          100.00               27            0.28              0.10         52.18                25.01         0.563              pass              0.795             75.0                           0.708               11.61              1.206                       ok           False                  False
   HON           88.00               25            0.82              1.36        234.76                35.57         0.556              pass              0.461             30.7                           0.287               -3.52             -0.610  downtrend_blocked_slope           False                  False
  PCAR           96.97               33            0.50              0.46        130.86                29.70         0.519              pass              0.811             68.5                           0.509               -2.51             -0.172                       ok           False                  False
  ROST           93.10               29            0.67              1.16        247.75                22.10         0.487   below_threshold              0.738             71.2                           0.636               -2.37             -0.091 downtrend_blocked_streak           False                  False
  TTWO           85.37               41            0.37              0.64        242.73                36.12         0.443   below_threshold              0.560             57.4                           0.393               -2.16              0.191                       ok           False                  False
  IDXX           95.45               44            0.21              0.85        570.21                27.90         0.428   below_threshold              0.871             76.0                           0.542                1.89              0.318                       ok           False                  False
   WMT           78.95               38            0.52              0.42        115.83                19.91         0.420   below_threshold              0.357             42.9                           0.289                3.88              0.320                       ok           False                  False
  CSCO             NaN                0            7.08              6.14        121.25                27.02           NaN no_signal_history                NaN              NaN                           0.624                1.36              0.390                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-08-13T10:20:10.643979-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:10:10.565177-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:05:05.347522-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:00:40.571954-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813102010)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813102010)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813102010)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813102010)

</details>
