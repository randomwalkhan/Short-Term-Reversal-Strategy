# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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
  CRWD           89.13               46            0.24              0.35        208.71                89.85         0.661          pass              0.751             80.6                           0.506               -8.60             -0.861            downtrend_blocked_slope           False                  False
  AMGN          100.00               21            0.78              2.09        381.57                44.93         0.630          pass              0.623             28.8                           0.244              -13.16             -1.553 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               13            0.43              0.07         24.36                28.75         0.620          pass              0.651             56.3                           0.412               -1.82             -0.364            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.37              0.37        140.40                68.52         0.540          pass              0.772             79.5                           0.386               -5.59             -0.985            downtrend_blocked_slope           False                  False
  SNPS           85.42               48            0.17              0.47        396.97                60.55         0.540          pass              0.640             80.4                           0.446              -14.71             -1.574            downtrend_blocked_slope           False                  False
  PANW           75.76               33            1.68              3.98        336.79                67.54         0.537          pass              0.238             10.4                           0.217              -13.07             -1.452            downtrend_blocked_slope           False                  False
  TEAM           93.94               33            1.38              1.73        178.83                63.98         0.536          pass              0.611             10.6                           0.242               -4.59             -0.759            downtrend_blocked_slope           False                  False
 CMCSA           93.55               31            0.30              0.05         25.15                36.51         0.528          pass              0.720             55.4                           0.313               -4.98             -0.721 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.83               24            0.06              0.02         43.38                15.10         0.526          pass              0.826             93.4                           0.402               -0.41              0.019                                 ok           False                  False
  ADSK           90.70               43            0.01              0.02        211.60                52.16         0.521          pass              0.834             98.8                           0.692              -21.81             -2.863 downtrend_blocked_slope_and_streak           False                  False
  WDAY           95.24               42            0.26              0.34        184.95                76.08         0.511          pass              0.803             50.7                           0.299               -4.63             -0.882 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.14               35            0.81              1.41        248.22                48.95         0.510          pass              0.864             82.2                           0.667              -14.64             -1.911 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
2026-09-11T10:00:03.674225-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T15:00:04.389376-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T14:55:01.338809-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911101501)

</details>
