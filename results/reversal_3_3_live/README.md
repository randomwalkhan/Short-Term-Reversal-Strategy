# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 15:05:01 EDT`
Last processed slot: `entry_1500`

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
   KDP           90.91               33            0.54              0.11         28.80                34.80         0.509            pass              0.707             70.5                           0.548                0.47              0.131                                 ok            True                  False
  TEAM           90.48               42            0.76              0.46         86.42               114.61         0.636            pass              0.798             85.1                           0.591               -3.20             -0.489 downtrend_blocked_slope_and_streak           False                  False
   TXN           93.94               33            0.39              0.82        301.96                69.06         0.625            pass              0.858             90.2                           0.640                4.04              0.580                                 ok           False                  False
  PAYX           95.45               22            0.13              0.08         94.44                29.36         0.566            pass              0.825             96.0                           0.627                4.59              0.250                                 ok           False                  False
   WMT           85.71                7            1.96              1.84        133.41                20.68         0.515            pass              0.329             41.8                           0.426                1.33              0.306                                 ok           False                  False
  TMUS           82.61               23            1.41              1.90        192.60                36.70         0.498 below_threshold              0.331             41.6                           0.630               -1.27             -0.194                                 ok           False                  False
  ADSK           88.46               26            1.09              1.86        243.36                38.52         0.497 below_threshold              0.609             75.7                           0.608               -0.65             -0.142                                 ok           False                  False
   TRI           69.23               13            2.39              1.46         86.72                57.28         0.485 below_threshold              0.216             49.3                           0.467               -7.07             -0.891 downtrend_blocked_slope_and_streak           False                  False
  SNPS           97.06               34            0.88              3.05        492.56                41.71         0.482 below_threshold              0.843             78.3                           0.549               -2.95             -0.371 downtrend_blocked_slope_and_streak           False                  False
   ADP           93.55               31            0.67              1.03        220.00                38.42         0.482 below_threshold              0.816             89.0                           0.609                5.68              0.482                                 ok           False                   True
 GOOGL           90.70               43            0.14              0.39        387.49                41.27         0.479 below_threshold              0.798             88.2                           0.741               -2.75             -0.179                                 ok           False                  False
  GOOG           90.00               40            0.38              1.02        384.46                41.08         0.471 below_threshold              0.724             70.1                           0.698               -2.96             -0.199           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-20T15:05:01.057777-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T15:00:06.267185-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T14:55:06.339368-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T14:50:06.419995-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T14:50:06.419995-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-20", "training_samples": 5043, "window": 5}
2026-05-20T12:00:03.589849-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:55:04.978899-04:00 early_entry_1155  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:50:01.042142-04:00 early_entry_1150  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00      manage_1130           exit {"asset_type": "option", "contract_symbol": "FTNT260717C00125000", "fill_price": 10.15, "pnl": 1855.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.01, "ticker": "FTNT"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520150501)

</details>
