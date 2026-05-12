# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 14:55:01 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260618C00520000      5          2026-05-12         2026-05-12         35.0        31.5 -1750.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           85.71               14            1.63              3.40        296.30                67.69         0.696          pass              0.405             52.0                           0.643               11.09              0.986                                 ok            True                  False
  TEAM           86.11               36            1.64              1.00         86.88               115.89         0.694          pass              0.509             34.4                           0.273               23.20              2.531                                 ok            True                  False
  FTNT           92.00               25            1.52              1.22        114.92                70.54         0.613          pass              0.501              6.7                           0.139               32.63              3.580                                 ok            True                  False
  GOOG           86.96               23            1.37              3.72        385.18                39.86         0.571          pass              0.403             24.7                           0.264                9.77              1.017                                 ok            True                  False
  MNST           80.00               25            0.89              0.54         86.18                49.64         0.551          pass              0.374             73.0                           0.529               10.95              1.195                                 ok            True                  False
  INTU           88.89               27            1.21              3.32        391.87                46.70         0.542          pass              0.520             38.3                           0.486               -2.96             -0.121                                 ok            True                  False
  CDNS           95.65               23            1.91              4.87        362.11                37.36         0.523          pass              0.597             19.4                           0.346                9.82              1.141                                 ok            True                  False
 CMCSA           93.33               30            0.40              0.07         25.00                62.25         0.673          pass              0.726             56.5                           0.474               -9.80             -0.978 downtrend_blocked_slope_and_streak           False                  False
  NXPI           66.67                3            4.15              8.88        302.18                87.21         0.626          pass              0.205             47.3                           0.310               27.31              1.302                                 ok           False                  False
  SHOP           85.00               20            2.74              1.96        101.70                84.99         0.619          pass              0.350             29.4                           0.482              -18.28             -2.195            downtrend_blocked_slope           False                  False
    ZS           79.17               24            1.97              2.05        147.99                59.15         0.536          pass              0.171              8.2                           0.134                7.25              1.230                                 ok           False                  False
   ROP          100.00               18            1.34              3.09        327.47                23.40         0.507          pass              0.514              3.3                           0.192               -8.40             -0.821            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:45:01.039711-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:40:05.033124-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:35:01.042494-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:30:01.054285-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512145501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512145501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512145501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512145501)

</details>
