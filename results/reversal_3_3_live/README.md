# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 11:05:08 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   HON           85.71               21            0.51              0.87        243.04               250.29         0.999          pass              0.598             90.7                           0.432                9.92              6.162                      ok            True                  False
  DRAM           91.67               12            4.83              2.43         70.84               125.47         0.690          pass              0.501             35.9                           0.600                5.23              0.509                      ok            True                  False
    MU           90.91               11            5.25             41.58       1114.51               130.58         0.602          pass              0.494             45.3                           0.789                9.30              0.962                      ok            True                  False
   XEL          100.00               17            0.80              0.46         82.03                23.26         0.595          pass              0.533              9.0                           0.162                3.74              0.516                      ok            True                  False
   EXC           84.62               13            0.91              0.30         47.27                19.58         0.581          pass              0.238             12.2                           0.167                1.64              0.247                      ok            True                  False
  GILD           90.00               10            1.68              1.50        127.24                29.34         0.572          pass              0.354             10.0                           0.218                0.77              0.070                      ok            True                  False
  SBUX           83.33               18            0.98              0.71        104.29                26.41         0.553          pass              0.219              7.3                           0.169                0.52              0.239                      ok            True                  False
  PCAR           81.25               16            1.59              1.34        120.10                36.52         0.551          pass              0.142              4.5                           0.147                0.20              0.002                      ok            True                  False
  INTC           90.91               22            3.43              3.08        127.00                98.20         0.537          pass              0.590             55.2                           0.846               -0.52              0.475                      ok            True                  False
  MRVL          100.00               24            1.74              3.25        265.38               157.15         0.868          pass              0.794             71.4                           0.872               -6.28             -0.983 downtrend_blocked_slope           False                  False
  MPWR           91.18               34            0.20              1.88       1312.52                89.21         0.669          pass              0.803             92.8                           0.786              -16.91             -1.891 downtrend_blocked_slope           False                  False
   TXN           92.86               28            0.82              1.64        284.72                70.58         0.634          pass              0.753             75.7                           0.742               -5.99             -0.612 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T11:05:08.784584-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:00:08.009230-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:39:22.639470-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:20:14.360345-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:12.530028-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629110508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629110508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629110508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629110508)

</details>
