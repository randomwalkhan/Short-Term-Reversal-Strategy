# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 14:50:06 EDT`
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
   KDP           89.66               29            0.75              0.15         28.79                34.80         0.520            pass              0.613             59.0                           0.434                0.26              0.122                                 ok            True                  False
  TEAM           91.30               46            0.30              0.18         86.54               114.61         0.640            pass              0.848             94.1                           0.755               -2.75             -0.468 downtrend_blocked_slope_and_streak           False                  False
   TXN           93.75               32            0.44              0.93        301.91                69.06         0.628            pass              0.842             88.8                           0.645                3.99              0.577                                 ok           False                  False
   WMT           85.71                7            2.00              1.88        133.40                20.68         0.512            pass              0.326             40.9                           0.279                1.30              0.305                                 ok           False                  False
   TRI           69.23               13            2.22              1.36         86.77                57.28         0.496 below_threshold              0.229             53.0                           0.587               -6.91             -0.883 downtrend_blocked_slope_and_streak           False                  False
  TMUS           82.61               23            1.51              2.05        192.54                36.70         0.491 below_threshold              0.317             37.2                           0.518               -1.38             -0.199                                 ok           False                  False
 GOOGL           90.70               43            0.10              0.27        387.54                41.27         0.482 below_threshold              0.809             91.8                           0.768               -2.71             -0.177                                 ok           False                  False
  SNPS           97.14               35            0.82              2.85        492.65                41.71         0.479 below_threshold              0.854             79.7                           0.560               -2.90             -0.368 downtrend_blocked_slope_and_streak           False                  False
   ADP           94.29               35            0.39              0.61        220.18                38.42         0.474 below_threshold              0.875             93.5                           0.709                5.97              0.495                                 ok           False                  False
  GOOG           90.24               41            0.35              0.94        384.50                41.08         0.467 below_threshold              0.738             72.6                           0.698               -2.93             -0.198           downtrend_blocked_streak           False                  False
  ADSK           91.18               34            0.83              1.42        243.55                38.52         0.463 below_threshold              0.749             81.5                           0.742               -0.39             -0.130                                 ok           False                   True
  CTAS           91.18               34            0.61              0.74        171.88                24.66         0.454 below_threshold              0.701             65.9                           0.701                1.33              0.291                                 ok           False                   True
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-20T14:50:06.419995-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T14:50:06.419995-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-20", "training_samples": 5043, "window": 5}
2026-05-20T12:00:03.589849-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:55:04.978899-04:00 early_entry_1155  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:50:01.042142-04:00 early_entry_1150  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00 early_entry_1140  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00      manage_1130           exit {"asset_type": "option", "contract_symbol": "FTNT260717C00125000", "fill_price": 10.15, "pnl": 1855.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.01, "ticker": "FTNT"}
2026-05-20T11:35:01.033169-04:00 early_entry_1135  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:30:01.977277-04:00 early_entry_1130  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520145006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520145006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520145006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520145006)

</details>
