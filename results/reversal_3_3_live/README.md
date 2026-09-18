# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 15:45:04 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               40            0.75              1.26        240.22                74.50         0.576          pass              0.445             62.5                           0.607               14.43              0.795                                 ok            True                  False
   KHC           90.91               11            1.15              0.20         24.64                21.70         0.534          pass              0.504             50.9                           0.452               -2.30             -0.138                                 ok            True                  False
  CTSH          100.00               12            2.93              1.27         61.34                39.55         0.514          pass              0.509             14.6                           0.356               -7.07             -0.034                                 ok            True                  False
  PYPL           91.67               24            0.97              0.36         52.79                57.74         0.641          pass              0.545             25.4                           0.297               -7.51             -0.447            downtrend_blocked_slope           False                  False
  CRWD           77.78               18            2.99              5.14        243.50                97.92         0.636          pass              0.213             32.0                           0.240               10.88              1.756                                 ok           False                  False
   EXC          100.00                6            1.16              0.35         42.49                15.46         0.567          pass              0.505             16.1                           0.313               -4.45             -0.464 downtrend_blocked_slope_and_streak           False                  False
  ADSK           88.37               43            0.01              0.01        218.63                55.63         0.546          pass              0.776             99.2                           0.833               -7.96             -0.024           downtrend_blocked_streak           False                  False
  ADBE           96.15               26            1.31              2.31        251.68                46.08         0.546          pass              0.680             39.6                           0.389              -12.73             -0.806 downtrend_blocked_slope_and_streak           False                  False
  PANW           53.85               13            3.54              9.29        371.08                79.31         0.528          pass              0.164             30.4                           0.325                8.99              1.413                                 ok           False                  False
   AEP           66.67                6            1.34              1.14        121.13                17.28         0.519          pass              0.069              5.8                           0.160               -3.78             -0.435 downtrend_blocked_slope_and_streak           False                  False
  INTC           83.33               42            0.23              0.18        108.72                60.44         0.513          pass              0.608             89.4                           0.932               18.41              0.948                                 ok           False                  False
   ADP           96.67               30            0.20              0.38        272.08                22.18         0.512          pass              0.846             87.3                           0.672               -3.56             -0.018           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                       detail
2026-09-18T15:10:04.788288-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500           entry_skipped                                                                                                                                                                                                       {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                     {"early_entry_score": 0.508, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.515}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
2026-09-18T14:50:01.910301-04:00       entry_1500          timing_overlay                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-18", "training_samples": 5785, "window": 5}
2026-09-18T12:00:05.801546-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:55:06.730103-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918154504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918154504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918154504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918154504)

</details>
