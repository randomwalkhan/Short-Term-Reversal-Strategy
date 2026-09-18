# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 15:30:05 EDT`
Last processed slot: `manage_1530`

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
  CRWD           80.00               20            2.70              4.65        243.71                97.92         0.643          pass              0.247             38.5                           0.355               11.21              1.769                                 ok            True                  False
   KHC           92.31               13            0.95              0.16         24.66                21.70         0.536          pass              0.580             59.5                           0.579               -2.10             -0.128                                 ok            True                  False
  PYPL           91.30               23            1.08              0.40         52.77                57.74         0.640          pass              0.504             17.4                           0.167               -7.60             -0.451            downtrend_blocked_slope           False                  False
  MRVL           78.95               38            0.92              1.55        240.10                74.50         0.576          pass              0.406             54.0                           0.585               14.23              0.787                                 ok           False                  False
   EXC          100.00                7            1.08              0.32         42.50                15.46         0.566          pass              0.523             22.0                           0.405               -4.38             -0.461 downtrend_blocked_slope_and_streak           False                  False
  ADSK           87.80               41            0.17              0.27        218.53                55.63         0.547          pass              0.719             85.2                           0.736               -8.11             -0.031           downtrend_blocked_streak           False                  False
  ADBE           96.15               26            1.42              2.51        251.60                46.08         0.539          pass              0.664             34.4                           0.271              -12.83             -0.811 downtrend_blocked_slope_and_streak           False                  False
  PANW           57.14               14            3.40              8.93        371.23                79.31         0.534          pass              0.179             33.1                           0.380                9.15              1.419                                 ok           False                  False
   AEP           66.67                6            1.20              1.02        121.18                17.28         0.527          pass              0.100             15.6                           0.281               -3.65             -0.428 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00                9            3.22              1.39         61.28                39.55         0.516          pass              0.467              5.2                           0.136               -7.35             -0.048                                 ok           False                  False
   ADP           96.55               29            0.27              0.51        272.02                22.18         0.514          pass              0.827             82.9                           0.588               -3.62             -0.021           downtrend_blocked_streak           False                  False
  CHTR           83.33               18            3.17              2.96        132.10                63.68         0.506          pass              0.232             13.0                           0.393              -14.69             -1.292 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918153005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918153005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918153005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918153005)

</details>
