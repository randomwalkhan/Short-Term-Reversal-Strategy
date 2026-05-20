# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 15:15:06 EDT`
Last processed slot: `manual`

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
   KDP           88.24               34            0.50              0.10         28.81                34.80         0.501            pass              0.647             72.4                           0.548                0.51              0.133                                 ok            True                  False
  TEAM           90.91               44            0.48              0.29         86.49               114.61         0.641            pass              0.826             90.5                           0.594               -2.93             -0.476 downtrend_blocked_slope_and_streak           False                  False
   TXN           93.94               33            0.16              0.33        302.17                69.06         0.640            pass              0.877             96.1                           0.764                4.28              0.590                                 ok           False                  False
  INSM           79.55               44            0.18              0.13        107.35               111.50         0.630            pass              0.554             97.0                           0.468              -21.79             -0.796            downtrend_blocked_slope           False                  False
   WMT          100.00                5            2.09              1.96        133.36                20.68         0.540            pass              0.569             38.2                           0.376                1.21              0.300                                 ok           False                  False
   TRI           75.00               12            2.42              1.48         86.72                57.28         0.498 below_threshold              0.210             48.8                           0.461               -7.10             -0.892 downtrend_blocked_slope_and_streak           False                  False
  SNPS           97.14               35            0.60              2.08        492.98                41.71         0.495 below_threshold              0.872             85.2                           0.669               -2.68             -0.358 downtrend_blocked_slope_and_streak           False                  False
  TMUS           82.61               23            1.51              2.04        192.54                36.70         0.491 below_threshold              0.317             37.3                           0.455               -1.38             -0.199                                 ok           False                  False
  ADSK           89.66               29            1.00              1.71        243.43                38.52         0.484 below_threshold              0.666             77.7                           0.574               -0.56             -0.138                                 ok           False                  False
 GOOGL           90.70               43            0.10              0.28        387.54                41.27         0.482 below_threshold              0.808             91.6                           0.694               -2.71             -0.177                                 ok           False                  False
    EA           92.86               28            0.22              0.31        201.57                 2.97         0.482 below_threshold              0.679             56.0                           0.444                0.23              0.041                                 ok           False                  False
   ADP           93.94               33            0.51              0.78        220.10                38.42         0.479 below_threshold              0.848             91.6                           0.651                5.85              0.490                                 ok           False                   True
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520151506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520151506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520151506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520151506)

</details>
