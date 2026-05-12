# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 15:25:01 EDT`
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
   TXN           90.91               22            1.22              2.54        296.67                67.69         0.681          pass              0.631             64.1                           0.739               11.55              1.005                                 ok            True                  False
  TEAM           82.61               23            3.74              2.29         86.33               115.89         0.630          pass              0.268             16.3                           0.161               20.56              2.433                                 ok            True                  False
  FTNT           88.89               18            1.85              1.50        114.80                70.54         0.627          pass              0.359              1.8                           0.212               32.17              3.564                                 ok            True                  False
  GOOG           85.71               28            1.02              2.76        385.59                39.86         0.558          pass              0.460             44.0                           0.533               10.16              1.033                                 ok            True                  False
  MNST           80.00               25            0.88              0.53         86.18                49.64         0.551          pass              0.375             73.4                           0.481               10.96              1.196                                 ok            True                  False
  INTU           89.29               28            1.13              3.11        391.96                46.70         0.541          pass              0.549             42.3                           0.521               -2.88             -0.117                                 ok            True                  False
    ZS           80.77               26            1.76              1.84        148.08                59.15         0.538          pass              0.234             17.7                           0.366                7.48              1.240                                 ok            True                  False
  CDNS           95.24               21            2.12              5.40        361.89                37.36         0.524          pass              0.558             10.8                           0.242                9.58              1.132                                 ok            True                  False
   CSX           87.88               33            0.57              0.18         44.66                30.07         0.503          pass              0.565             50.5                           0.425               -1.65             -0.115                                 ok            True                  False
 CMCSA           94.74               38            0.06              0.01         25.03                62.25         0.650          pass              0.925             93.5                           0.760               -9.50             -0.963 downtrend_blocked_slope_and_streak           False                  False
  NXPI           75.00                4            3.96              8.49        302.35                87.21         0.642          pass              0.213             49.6                           0.438               27.55              1.311                                 ok           False                  False
  SHOP           85.71               21            2.56              1.84        101.75                84.99         0.624          pass              0.390             33.8                           0.494              -18.14             -2.187            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-12T15:10:04.189330-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:45:01.039711-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512152501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512152501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512152501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512152501)

</details>
