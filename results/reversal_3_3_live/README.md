# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 15:20:01 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  FTNT     option         option FTNT260717C00125000     14          2026-05-20         2026-05-20        8.825       10.15 1855.0   15.014164 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           90.91               33            0.55              0.11         28.80                34.80         0.508            pass              0.704             69.5                           0.511                0.46              0.130                                 ok            True                  False
   TXN           93.94               33            0.11              0.22        302.21                69.06         0.644            pass              0.881             97.3                           0.788                4.34              0.592                                 ok           False                  False
  TEAM           90.91               44            0.63              0.39         86.45               114.61         0.631            pass              0.817             87.6                           0.633               -3.07             -0.483 downtrend_blocked_slope_and_streak           False                  False
  INSM           78.57               42            0.33              0.25        107.30               111.50         0.631            pass              0.546             94.3                           0.489              -21.91             -0.803            downtrend_blocked_slope           False                  False
   WMT           85.71                7            2.01              1.89        133.39                20.68         0.511            pass              0.325             40.4                           0.392                1.28              0.304                                 ok           False                  False
   TRI           69.23               13            2.18              1.33         86.78                57.28         0.500 below_threshold              0.232             53.9                           0.512               -6.87             -0.881 downtrend_blocked_slope_and_streak           False                  False
  TMUS           82.61               23            1.42              1.93        192.59                36.70         0.497 below_threshold              0.329             41.0                           0.566               -1.29             -0.195                                 ok           False                  False
  SNPS           97.30               37            0.47              1.63        493.17                41.71         0.490 below_threshold              0.894             88.4                           0.741               -2.55             -0.352 downtrend_blocked_slope_and_streak           False                  False
   ADP           93.94               33            0.51              0.78        220.10                38.42         0.479 below_threshold              0.848             91.6                           0.677                5.85              0.490                                 ok           False                   True
  ADSK           90.91               33            0.89              1.53        243.51                38.52         0.466 below_threshold              0.731             80.1                           0.625               -0.45             -0.133                                 ok           False                   True
  VRSK           83.33               42            0.06              0.08        170.68                45.61         0.462 below_threshold              0.628             97.5                           0.667               -0.20             -0.218                                 ok           False                  False
  GOOG           88.37               43            0.23              0.62        384.64                41.08         0.459 below_threshold              0.715             82.0                           0.668               -2.81             -0.192           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-20T15:10:05.258354-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-20T15:05:01.057777-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-20T15:00:06.267185-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-20T14:55:06.339368-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-20T14:50:06.419995-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-20T14:50:06.419995-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-20", "training_samples": 5043, "window": 5}
2026-05-20T12:00:03.589849-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-20T11:55:04.978899-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-20T11:50:01.042142-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520152001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520152001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520152001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520152001)

</details>
