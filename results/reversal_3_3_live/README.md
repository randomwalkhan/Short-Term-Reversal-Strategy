# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:15:06 EST`
Last processed slot: `early_entry_1015`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           72.73               22            1.60              1.68        148.58               127.24         0.763            pass              0.273             38.8                           0.405              -11.60             -0.949 downtrend_blocked_slope_and_streak           False                  False
   KDP           87.88               33            0.45              0.11         35.58                47.31         0.579            pass              0.513             30.4                           0.287                0.14             -0.020                                 ok           False                  False
   CEG           90.00               40            0.54              0.90        234.90                66.73         0.559            pass              0.594             23.8                           0.231              -17.01             -2.029 downtrend_blocked_slope_and_streak           False                  False
   AEP           96.30               27            0.14              0.13        127.54                16.32         0.521            pass              0.719             51.4                           0.322               -1.16             -0.134                                 ok           False                  False
  PAYX           74.19               31            0.01              0.01        118.49                28.65         0.520            pass              0.486             98.0                           0.492                2.87              0.119                                 ok           False                  False
  MDLZ           96.97               33            0.21              0.10         67.77                23.85         0.514            pass              0.821             72.0                           0.465                1.67              0.051                                 ok           False                  False
  DXCM           86.05               43            0.29              0.18         84.76                47.84         0.509            pass              0.622             69.9                           0.483                3.93              0.312                                 ok           False                  False
  ISRG           89.13               46            0.07              0.20        427.09                50.77         0.508            pass              0.772             92.7                           0.702               -2.96             -0.404           downtrend_blocked_streak           False                  False
  ALNY           73.53               34            1.28              1.48        164.10               117.72         0.504            pass              0.246             11.9                           0.187                3.81              0.204                                 ok           False                  False
  PANW           78.79               33            1.51              3.77        354.52                69.35         0.501            pass              0.412             69.4                           0.729                8.71              1.296                                 ok           False                  False
 GOOGL           80.00               30            0.59              1.12        272.62                60.73         0.481 below_threshold              0.325             47.9                           0.290               -9.11             -0.814            downtrend_blocked_slope           False                  False
  ORLY          100.00               25            1.01              0.68         96.40                21.83         0.478 below_threshold              0.584             12.2                           0.195                4.54              0.465                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:15:06.172355-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:10:04.653720-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:05:06.125532-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00      manage_1530      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:11:16.077658-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127101506)

</details>
