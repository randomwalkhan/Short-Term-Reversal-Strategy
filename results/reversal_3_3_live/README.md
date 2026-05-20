# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 15:55:05 EDT`
Last processed slot: `manage_1600`

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
   KDP           90.00               30            0.66              0.13         28.79                34.80         0.520            pass              0.643             63.8                           0.459                0.35              0.126                                 ok            True                  False
  TEAM           90.91               44            0.46              0.28         86.50               114.61         0.643            pass              0.828             91.1                           0.661               -2.90             -0.475 downtrend_blocked_slope_and_streak           False                  False
   AEP           88.46               26            0.15              0.13        128.86                26.29         0.510            pass              0.662             92.9                           0.400               -2.18             -0.308                                 ok           False                  False
   WMT          100.00                3            2.85              2.67        133.05                20.68         0.504            pass              0.497             15.7                           0.244                0.42              0.265                                 ok           False                  False
   CSX           86.49               37            0.29              0.09         46.04                31.47         0.497 below_threshold              0.610             69.0                           0.325                0.76              0.311                                 ok           False                  False
   TRI           69.23               13            2.25              1.38         86.76                57.28         0.495 below_threshold              0.227             52.4                           0.540               -6.94             -0.884 downtrend_blocked_slope_and_streak           False                  False
  TMUS           80.95               21            1.63              2.21        192.47                36.70         0.494 below_threshold              0.245             32.2                           0.395               -1.50             -0.204                                 ok           False                  False
  NFLX           76.47               17            1.41              0.88         88.95                24.16         0.470 below_threshold              0.187             31.1                           0.327               -0.23              0.126                                 ok           False                  False
  GOOG           88.64               44            0.10              0.28        384.78                41.08         0.461 below_threshold              0.752             91.8                           0.775               -2.69             -0.187           downtrend_blocked_streak           False                  False
  COST           80.00                5            1.96             15.01       1087.89                18.86         0.455 below_threshold              0.282             78.7                           0.533                7.75              0.905                                 ok           False                  False
  CTAS           91.67               36            0.53              0.64        171.92                24.66         0.446 below_threshold              0.739             70.1                           0.642                1.41              0.295                                 ok           False                   True
  ADBE           85.00               40            0.68              1.21        254.47                43.10         0.431 below_threshold              0.617             80.3                           0.775                1.24              0.058                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520155505)

</details>
