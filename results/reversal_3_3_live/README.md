# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:25:07 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INSM           80.00               20            2.15              1.99        131.43               107.72         0.765            pass              0.189             15.2                           0.188               27.54              3.800                       ok            True                  False
  MPWR           84.21               38            0.70              6.99       1422.02                55.33         0.549            pass              0.439             28.3                           0.211                7.51              0.603                       ok            True                  False
   BKR           84.62               13            1.93              0.87         63.91                33.24         0.545            pass              0.289             30.3                           0.439                5.63              0.749                       ok            True                  False
  ISRG           86.84               38            0.30              0.85        400.91                69.94         0.671            pass              0.625             63.0                           0.641               13.34              1.339                       ok           False                  False
   ROP           97.14               35            0.30              0.83        394.87                44.32         0.596            pass              0.836             69.8                           0.530                1.23              0.192                       ok           False                  False
  FAST          100.00               26            0.34              0.12         52.17                25.01         0.566            pass              0.773             69.8                           0.631               11.54              1.203                       ok           False                  False
   HON           90.91               33            0.66              1.09        234.87                35.57         0.520            pass              0.630             44.5                           0.367               -3.36             -0.602  downtrend_blocked_slope           False                  False
  PCAR           97.14               35            0.48              0.44        130.87                29.70         0.508            pass              0.827             69.7                           0.484               -2.49             -0.171                       ok           False                  False
  ROST           92.31               26            0.90              1.56        247.58                22.10         0.491 below_threshold              0.667             61.1                           0.539               -2.60             -0.102 downtrend_blocked_streak           False                  False
  VRTX           97.83               46            0.06              0.21        525.64                27.73         0.446 below_threshold              0.916             90.5                           0.597                9.08              1.246                       ok           False                  False
  TTWO           84.21               38            0.66              1.13        242.52                36.12         0.443 below_threshold              0.417             24.6                           0.233               -2.44              0.178                       ok           False                  False
  IDXX           95.45               44            0.13              0.52        570.36                27.90         0.433 below_threshold              0.899             85.3                           0.569                1.97              0.322                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-08-13T10:25:07.519899-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:20:10.643979-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:10:10.565177-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:05:05.347522-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:00:40.571954-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813102507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813102507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813102507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813102507)

</details>
