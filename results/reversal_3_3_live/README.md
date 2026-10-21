# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:30:05 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   KHC           85.71               21            1.30              0.22         23.74                25.26         0.502            pass              0.290              4.6                           0.143                7.01              0.759                       ok            True                  False
  TMUS           50.00                8            2.94              3.25        156.36                56.37         0.555            pass              0.132             25.5                           0.226               -8.67             -0.474  downtrend_blocked_slope           False                  False
   KDP           96.43               28            0.35              0.08         34.59                29.04         0.548            pass              0.826             83.6                           0.562               13.00              1.293                       ok           False                  False
  GILD           87.50                8            1.94              2.12        155.60                26.70         0.529            pass              0.364             36.9                           0.500                4.51              0.585                       ok           False                  False
  MDLZ           50.00                2            1.93              0.86         63.62                19.17         0.511            pass              0.075              7.8                           0.175                5.68              0.658                       ok           False                  False
  INTU           88.89               36            0.35              0.81        334.94                37.42         0.504            pass              0.677             72.1                           0.574               12.94              1.302                       ok           False                  False
  MSFT           96.55               29            0.44              1.66        531.16                21.62         0.501            pass              0.773             65.5                           0.525               -0.05              0.006                       ok           False                  False
  DXCM          100.00                3            3.28              1.97         84.90                29.22         0.498 below_threshold              0.454              1.4                           0.074               -1.63              0.073 downtrend_blocked_streak           False                  False
  AVGO           83.33               36            0.35              0.83        334.01                36.72         0.493 below_threshold              0.441             43.0                           0.277              -11.51             -1.209  downtrend_blocked_slope           False                  False
  DASH           86.49               37            1.05              1.41        191.07                49.85         0.491 below_threshold              0.565             54.2                           0.670               -0.83             -0.129                       ok           False                  False
  GEHC           76.47               17            1.49              0.73         69.92                23.16         0.484 below_threshold              0.190             31.5                           0.349                6.98              0.863                       ok           False                  False
 CMCSA          100.00                3            3.22              0.50         22.14                21.50         0.477 below_threshold              0.452              1.3                           0.176                3.34              0.643                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-21T10:30:05.461967-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "ABNB261120C00175000", "current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "entry_ask": 11.05, "entry_bid": 8.8, "entry_mode": "early", "entry_option_price": 9.925, "hypothetical_budget": 72415.9, "hypothetical_contracts": 72, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 728.0, "option_spread_pct": 22.67, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:25:04.556585-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:20:05.382566-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:15:01.464955-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:10:06.281776-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:05:06.311663-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:00:05.535793-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021103005)

</details>
