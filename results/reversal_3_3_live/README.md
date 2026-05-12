# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 15:15:01 EDT`
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
   TXN           91.67               24            1.01              2.11        296.86                67.69         0.681            pass              0.683             70.3                           0.800               11.79              1.015                      ok            True                  False
  TEAM           82.61               23            3.76              2.30         86.33               115.89         0.635            pass              0.237              5.9                           0.223               20.54              2.432                      ok            True                  False
  FTNT           92.00               25            1.59              1.28        114.89                70.54         0.608            pass              0.508              9.2                           0.212               32.53              3.577                      ok            True                  False
  GOOG           84.00               25            1.15              3.12        385.43                39.86         0.566            pass              0.374             36.8                           0.410               10.02              1.027                      ok            True                  False
  MNST           80.00               25            0.92              0.56         86.17                49.64         0.549            pass              0.371             72.1                           0.431               10.91              1.194                      ok            True                  False
    ZS           80.77               26            1.67              1.74        148.13                59.15         0.543            pass              0.248             22.3                           0.396                7.58              1.244                      ok            True                  False
  INTU           88.89               27            1.24              3.41        391.83                46.70         0.540            pass              0.514             36.7                           0.504               -2.99             -0.122                      ok            True                  False
  CDNS           95.65               23            1.94              4.95        362.08                37.36         0.521            pass              0.593             18.2                           0.362                9.78              1.140                      ok            True                  False
  NXPI           80.00                5            3.78              8.09        302.52                87.21         0.652            pass              0.221             52.0                           0.542               27.80              1.320                      ok           False                  False
  SHOP           85.71               21            2.59              1.86        101.74                84.99         0.622            pass              0.387             33.1                           0.470              -18.16             -2.188 downtrend_blocked_slope           False                  False
   ROP          100.00               19            1.18              2.73        327.63                23.40         0.510            pass              0.555             14.8                           0.385               -8.25             -0.813 downtrend_blocked_slope           False                  False
  ADSK           95.00               40            0.39              0.64        235.79                40.78         0.496 below_threshold              0.763             37.8                           0.258                0.13              0.115                      ok           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512151501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512151501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512151501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512151501)

</details>
