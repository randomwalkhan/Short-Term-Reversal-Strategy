# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 15:30:06 EDT`
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
   KDP           89.66               29            0.71              0.14         28.79                34.80         0.523            pass              0.619             61.0                           0.439                0.30              0.123                                 ok            True                  False
  INSM           80.85               47            0.07              0.05        107.39               111.50         0.619            pass              0.581             98.9                           0.553              -21.70             -0.791            downtrend_blocked_slope           False                  False
   WMT          100.00                3            2.30              2.16        133.27                20.68         0.540            pass              0.549             31.8                           0.320                0.98              0.290                                 ok           False                  False
   TRI           69.23               13            2.01              1.23         86.82                57.28         0.510            pass              0.243             57.3                           0.624               -6.71             -0.873 downtrend_blocked_slope_and_streak           False                  False
  TMUS           77.78               18            1.69              2.29        192.44                36.70         0.506            pass              0.193             29.8                           0.350               -1.56             -0.207                                 ok           False                  False
   CSX           86.84               38            0.21              0.07         46.05                31.47         0.497 below_threshold              0.653             78.2                           0.369                0.84              0.315                                 ok           False                  False
   ADP           94.29               35            0.39              0.60        220.18                38.42         0.474 below_threshold              0.876             93.6                           0.735                5.98              0.495                                 ok           False                  False
  COST           83.33                6            1.72             13.19       1088.67                18.86         0.467 below_threshold              0.380             81.3                           0.531                8.01              0.916                                 ok           False                  False
  ADSK           91.18               34            0.79              1.35        243.58                38.52         0.466 below_threshold              0.752             82.4                           0.742               -0.35             -0.128                                 ok           False                   True
  GOOG           88.64               44            0.22              0.60        384.64                41.08         0.453 below_threshold              0.723             82.6                           0.701               -2.81             -0.192           downtrend_blocked_streak           False                  False
    EA           94.44               36            0.15              0.22        201.61                 2.97         0.435 below_threshold              0.809             69.0                           0.525                0.30              0.044                                 ok           False                  False
  CTAS           92.31               39            0.44              0.53        171.97                24.66         0.433 below_threshold              0.792             75.6                           0.715                1.51              0.299                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520153006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520153006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520153006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520153006)

</details>
