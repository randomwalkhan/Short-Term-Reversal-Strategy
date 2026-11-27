# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:10:04 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           72.73               22            1.72              1.80        148.53               127.24         0.757          pass              0.259             34.4                           0.272              -11.71             -0.954 downtrend_blocked_slope_and_streak           False                  False
  AMAT           66.67               39            0.07              0.16        311.11               107.91         0.672          pass              0.541             93.5                           0.481              -18.25             -1.902            downtrend_blocked_slope           False                  False
  ASML           72.73               33            0.45              4.13       1301.31                72.71         0.597          pass              0.359             48.6                           0.259              -13.35             -1.380            downtrend_blocked_slope           False                  False
   KDP           88.24               34            0.35              0.09         35.59                47.31         0.580          pass              0.523             28.6                           0.239                0.24             -0.015                                 ok           False                  False
  REGN           89.36               47            0.01              0.10        981.83                56.75         0.561          pass              0.797             97.2                           0.463                3.32              0.300                                 ok           False                  False
   CEG           87.80               41            0.49              0.81        234.93                66.73         0.553          pass              0.551             29.1                           0.153              -16.97             -2.026 downtrend_blocked_slope_and_streak           False                  False
   AEP           96.43               28            0.04              0.03        127.58                16.32         0.522          pass              0.836             87.8                           0.578               -1.06             -0.129                                 ok           False                  False
  ISRG           89.13               46            0.02              0.05        427.16                50.77         0.511          pass              0.789             98.2                           0.667               -2.91             -0.402           downtrend_blocked_streak           False                  False
  MDLZ           97.22               36            0.00              0.00         67.81                23.85         0.508          pass              0.924            100.0                           0.735                1.88              0.060                                 ok           False                  False
  ROST           93.18               44            0.03              0.05        223.24                44.59         0.505          pass              0.892             96.7                           0.618               -5.92             -0.460                                 ok           False                  False
  DXCM           85.71               42            0.47              0.28         84.72                47.84         0.504          pass              0.558             51.8                           0.347                3.75              0.304                                 ok           False                  False
  ALNY           74.29               35            1.22              1.41        164.13               117.72         0.502          pass              0.255             12.8                           0.147                3.87              0.207                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:10:04.653720-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:05:06.125532-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00      manage_1530      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:11:16.077658-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T14:56:03.145316-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127101004)

</details>
