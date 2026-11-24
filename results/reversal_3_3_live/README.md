# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:30:05 EST`
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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           57.14                7            7.59              3.17         58.30               154.63         0.635          pass              0.082              6.2                           0.148               -5.16             -1.030 downtrend_blocked_slope_and_streak           False                  False
  UPRO           62.50                8            3.12              2.62        118.62                94.72         0.629          pass              0.159             32.0                           0.265              -14.94             -2.457 downtrend_blocked_slope_and_streak           False                  False
  QCOM           77.78               27            1.76              2.04        164.51                82.33         0.623          pass              0.323             49.1                           0.368               -6.37             -1.154 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.68               19            1.47              2.90        280.86                61.35         0.597          pass              0.174             18.1                           0.225               -3.28             -0.771            downtrend_blocked_slope           False                  False
   BKR           73.68               19            1.39              0.45         45.85                56.59         0.588          pass              0.182             21.0                           0.190               -4.96             -0.841 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.24               17            2.43              4.28        249.88                65.44         0.578          pass              0.416             30.7                           0.242               -8.14             -1.408 downtrend_blocked_slope_and_streak           False                  False
  GOOG           72.73               22            1.31              2.56        278.43                58.63         0.577          pass              0.211             24.4                           0.267               -3.18             -0.740            downtrend_blocked_slope           False                  False
  ASML           66.67                9            3.58             34.64       1368.94                73.86         0.574          pass              0.086              9.6                           0.188              -11.51             -1.573 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.74               19            0.75              2.19        414.69                26.32         0.566          pass              0.522              4.1                           0.185               -3.51             -0.423            downtrend_blocked_slope           False                  False
  AVGO           70.00               10            3.78              8.29        310.00                86.52         0.539          pass              0.119             21.7                           0.240               -9.12             -1.222            downtrend_blocked_slope           False                  False
  DASH           81.25               48            0.21              0.23        161.25                67.28         0.536          pass              0.550             87.7                           0.434               -9.67             -1.336 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               21            0.88              0.32         51.92                27.50         0.533          pass              0.575             16.2                           0.209               -5.90             -0.866 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:00:05.622595-05:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124103005)

</details>
