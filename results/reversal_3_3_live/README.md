# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 15:05:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           85.71               14            1.62              3.38        296.31                67.69         0.696            pass              0.406             52.3                           0.658               11.10              0.987                      ok            True                  False
  TEAM           86.67               30            2.80              1.71         86.58               115.89         0.665            pass              0.378              0.0                           0.203               21.74              2.477                      ok            True                  False
  FTNT           92.00               25            1.56              1.26        114.90                70.54         0.611            pass              0.498              5.8                           0.185               32.57              3.578                      ok            True                  False
  GOOG           86.96               23            1.37              3.70        385.19                39.86         0.572            pass              0.405             25.1                           0.263                9.78              1.018                      ok            True                  False
  INTU           88.89               27            1.14              3.15        391.94                46.70         0.546            pass              0.530             41.6                           0.583               -2.89             -0.118                      ok            True                  False
  MNST           80.00               25            0.99              0.60         86.15                49.64         0.545            pass              0.365             70.0                           0.467               10.84              1.191                      ok            True                  False
    ZS           80.77               26            1.83              1.91        148.05                59.15         0.534            pass              0.224             14.4                           0.228                7.40              1.237                      ok            True                  False
  CDNS           95.65               23            1.89              4.82        362.14                37.36         0.524            pass              0.600             20.4                           0.406                9.84              1.143                      ok            True                  False
  NXPI           66.67                3            4.02              8.60        302.30                87.21         0.633            pass              0.210             49.0                           0.313               27.48              1.309                      ok           False                  False
  SHOP           83.33               18            2.93              2.10        101.64                84.99         0.617            pass              0.277             24.4                           0.393              -18.45             -2.204 downtrend_blocked_slope           False                  False
  WDAY           83.87               31            1.92              1.63        120.72                61.87         0.489 below_threshold              0.333             13.5                           0.313               -1.72              0.025                      ok           False                  False
   ROP          100.00               24            1.07              2.46        327.75                23.40         0.487 below_threshold              0.612             23.2                           0.452               -8.14             -0.808 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:45:01.039711-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:40:05.033124-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512150501)

</details>
