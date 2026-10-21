# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:35:02 EDT`
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
   KHC           85.71               21            1.26              0.21         23.74                25.26         0.504            pass              0.299              7.7                           0.153                7.05              0.761                       ok            True                  False
  INTU           88.24               34            0.57              1.34        334.72                37.42         0.501            pass              0.592             54.0                           0.383               12.68              1.292                       ok            True                  False
  TMUS           55.56                9            2.81              3.10        156.42                56.37         0.563            pass              0.143             28.9                           0.217               -8.55             -0.468  downtrend_blocked_slope           False                  False
   KDP           96.88               32            0.12              0.03         34.62                29.04         0.539            pass              0.884             94.5                           0.729               13.26              1.303                       ok           False                  False
  GILD           87.50                8            1.97              2.16        155.58                26.70         0.527            pass              0.360             35.6                           0.530                4.47              0.583                       ok           False                  False
  MDLZ           50.00                2            1.84              0.83         63.64                19.17         0.516            pass              0.087             11.9                           0.187                5.78              0.662                       ok           False                  False
  MSFT           96.55               29            0.43              1.60        531.18                21.62         0.502            pass              0.777             66.6                           0.542               -0.03              0.007                       ok           False                  False
  DXCM          100.00                3            3.32              2.00         84.88                29.22         0.495 below_threshold              0.456              2.1                           0.053               -1.67              0.071 downtrend_blocked_streak           False                  False
  DASH           86.49               37            1.07              1.43        191.06                49.85         0.490 below_threshold              0.563             53.5                           0.652               -0.84             -0.129                       ok           False                  False
  AVGO           82.05               39            0.15              0.36        334.22                36.72         0.486 below_threshold              0.523             75.6                           0.473              -11.33             -1.200  downtrend_blocked_slope           False                  False
  SBUX           86.67               30            0.87              0.60         99.11                24.55         0.475 below_threshold              0.481             40.7                           0.483                5.27              0.819                       ok           False                  False
  GEHC           80.95               21            1.32              0.65         69.95                23.16         0.475 below_threshold              0.264             39.2                           0.442                7.16              0.870                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-21T10:35:02.510761-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:30:05.461967-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "ABNB261120C00175000", "current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "entry_ask": 11.05, "entry_bid": 8.8, "entry_mode": "early", "entry_option_price": 9.925, "hypothetical_budget": 72415.9, "hypothetical_contracts": 72, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 728.0, "option_spread_pct": 22.67, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:25:04.556585-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:20:05.382566-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:15:01.464955-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:10:06.281776-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:05:06.311663-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:00:05.535793-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021103502)

</details>
