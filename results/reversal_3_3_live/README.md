# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:25:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           84.62               26            2.60             15.71        855.60                71.44         0.501          pass              0.410             43.5                           0.479               -0.86              0.514                                 ok            True                  False
  CRWD           89.13               46            0.44              0.64        208.58                89.85         0.649          pass              0.701             64.3                           0.354               -8.78             -0.870            downtrend_blocked_slope           False                  False
  AMGN          100.00               18            0.97              2.60        381.36                44.93         0.637          pass              0.552             11.7                           0.119              -13.33             -1.561 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               19            0.12              0.02         24.38                28.75         0.602          pass              0.783             87.5                           0.675               -1.51             -0.350            downtrend_blocked_slope           False                  False
  PANW           76.47               34            1.43              3.38        337.04                67.54         0.545          pass              0.307             31.0                           0.283              -12.85             -1.440            downtrend_blocked_slope           False                  False
   EXC           95.24               21            0.16              0.05         43.37                15.10         0.538          pass              0.772             81.6                           0.353               -0.52              0.014                                 ok           False                  False
  TEAM           93.94               33            1.42              1.78        178.81                63.98         0.534          pass              0.603              8.1                           0.104               -4.63             -0.761            downtrend_blocked_slope           False                  False
 CMCSA           93.94               33            0.06              0.01         25.17                36.51         0.531          pass              0.852             91.2                           0.529               -4.75             -0.710 downtrend_blocked_slope_and_streak           False                  False
   WDC           81.25               32            1.50              4.85        458.85                66.80         0.511          pass              0.361             43.4                           0.418               -1.70              0.264           downtrend_blocked_streak           False                  False
  WDAY           95.45               44            0.11              0.14        185.03                76.08         0.508          pass              0.891             80.0                           0.343               -4.48             -0.875 downtrend_blocked_slope_and_streak           False                  False
   BKR           92.31               13            1.57              0.65         59.12                30.11         0.504          pass              0.428              9.7                           0.152               -5.86             -0.459            downtrend_blocked_slope           False                  False
  ADBE           97.30               37            0.73              1.27        248.28                48.95         0.502          pass              0.882             83.9                           0.621              -14.57             -1.907 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:25:04.822765-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
2026-09-11T10:00:03.674225-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911102504)

</details>
