# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:15:06 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.00               20            2.21              4.73        303.52                65.52         0.572          pass              0.461             23.5                           0.391                0.24              0.247                                 ok            True                  False
   ADI           84.00               25            1.46              4.02        391.03                55.85         0.566          pass              0.359             31.8                           0.447               -2.56              0.067                                 ok            True                  False
   CSX           84.62               13            1.13              0.40         49.75                19.08         0.561          pass              0.264             21.5                           0.291                3.84              0.343                                 ok            True                  False
   LIN          100.00               12            1.26              4.62        520.56                20.66         0.559          pass              0.538             22.8                           0.306               -0.58             -0.302                                 ok            True                  False
  NXPI           86.96               23            2.01              3.99        282.16                58.07         0.536          pass              0.380             18.0                           0.220               -1.02              0.225                                 ok            True                  False
   WBD           86.67               15            0.87              0.17         27.41                20.00         0.535          pass              0.373             36.0                           0.468                2.18              0.278                                 ok            True                  False
  MDLZ           95.83               24            0.17              0.07         58.77                30.54         0.589          pass              0.820             89.1                           0.549                1.49             -0.068                                 ok           False                  False
  ASML           94.12               34            0.41              5.12       1773.45                66.00         0.580          pass              0.782             62.4                           0.425              -11.11             -0.727            downtrend_blocked_slope           False                  False
  KLAC           75.00               12            4.55              7.34        227.23               109.33         0.574          pass              0.086              5.2                           0.183              -27.12             -2.120 downtrend_blocked_slope_and_streak           False                  False
  AMAT           78.57               14            3.82             15.94        588.87                98.89         0.561          pass              0.105              7.3                           0.173              -20.76             -1.428 downtrend_blocked_slope_and_streak           False                  False
  QCOM           82.14               28            1.61              2.01        177.24                61.79         0.558          pass              0.238              1.7                           0.248               -5.17             -0.117           downtrend_blocked_streak           False                  False
  MCHP           96.00               25            2.29              1.40         86.51                68.63         0.552          pass              0.590             11.7                           0.276               -6.67             -0.300            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-15T11:15:06.015471-04:00 early_entry_1115 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:10:02.751788-04:00 early_entry_1110 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00 early_entry_1105 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00      manage_1100               exit {"asset_type": "option", "contract_symbol": "META260821C00660000", "fill_price": 54.6, "pnl": 1545.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.48, "ticker": "META"}
2026-07-15T11:00:03.028836-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:55:06.408548-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:50:02.878047-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:45:02.900716-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715111506)

</details>
