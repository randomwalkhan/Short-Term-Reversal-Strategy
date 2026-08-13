# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:30:06 EDT`
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
  INSM           81.82               22            1.95              1.81        131.50               107.72         0.767            pass              0.274             22.8                           0.333               27.79              3.809                       ok            True                  False
   BKR           84.62               13            1.79              0.80         63.94                33.24         0.553            pass              0.305             35.4                           0.592                5.78              0.756                       ok            True                  False
  MPWR           83.78               37            0.84              8.43       1421.40                55.33         0.544            pass              0.424             29.5                           0.277                7.35              0.597                       ok            True                  False
  PCAR           96.88               32            0.60              0.55        130.82                29.70         0.520            pass              0.785             62.3                           0.416               -2.61             -0.176                       ok            True                  False
  ISRG           86.49               37            0.34              0.97        400.86                69.94         0.673            pass              0.594             57.8                           0.473               13.29              1.337                       ok           False                  False
  MCHP           85.00               40            0.24              0.13         79.38                74.47         0.657            pass              0.595             65.5                           0.408                5.65              0.931                       ok           False                  False
   ROP           97.22               36            0.23              0.64        394.95                44.32         0.594            pass              0.863             76.6                           0.508                1.30              0.195                       ok           False                  False
  FAST          100.00               26            0.31              0.11         52.17                25.01         0.568            pass              0.781             72.4                           0.589               11.57              1.205                       ok           False                  False
   HON           89.29               28            0.77              1.27        234.79                35.57         0.542            pass              0.527             35.0                           0.338               -3.47             -0.607  downtrend_blocked_slope           False                  False
   MAR           93.02               43            0.03              0.07        354.55                36.15         0.530            pass              0.868             89.2                           0.494               -5.59             -0.445  downtrend_blocked_slope           False                  False
  ADSK           83.78               37            0.50              0.87        249.14                45.76         0.518            pass              0.583             83.5                           0.543                5.66              0.852                       ok           False                  False
  ROST           92.31               26            0.98              1.71        247.52                22.10         0.487 below_threshold              0.656             57.6                           0.494               -2.68             -0.106 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-08-13T10:30:06.616446-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:25:07.519899-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:20:10.643979-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:15:10.251023-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:10:10.565177-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:05:05.347522-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:00:40.571954-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813103006)

</details>
