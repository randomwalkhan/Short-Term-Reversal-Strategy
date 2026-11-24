# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:35:04 EST`
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
  INTC           57.14                7            7.02              2.93         58.40               154.63         0.669          pass              0.107             13.3                           0.195               -4.58             -1.002 downtrend_blocked_slope_and_streak           False                  False
  UPRO           75.00               12            2.71              2.28        118.76                94.72         0.644          pass              0.200             40.9                           0.302              -14.58             -2.438 downtrend_blocked_slope_and_streak           False                  False
  QCOM           77.78               27            1.50              1.74        164.63                82.33         0.639          pass              0.347             56.6                           0.560               -6.13             -1.142 downtrend_blocked_slope_and_streak           False                  False
   BKR           75.00               20            1.19              0.38         45.88                56.59         0.596          pass              0.223             32.1                           0.246               -4.77             -0.832 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67                9            3.41             32.98       1369.64                73.86         0.584          pass              0.100             14.0                           0.244              -11.35             -1.565 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            1.06              2.09        281.20                61.35         0.578          pass              0.294             41.1                           0.311               -2.88             -0.752            downtrend_blocked_slope           False                  False
  GOOG           79.31               29            0.89              1.75        278.78                58.63         0.568          pass              0.328             48.3                           0.355               -2.77             -0.721            downtrend_blocked_slope           False                  False
   MAR           95.00               20            0.65              1.90        414.82                26.32         0.566          pass              0.574             16.9                           0.228               -3.42             -0.418            downtrend_blocked_slope           False                  False
  AVGO           58.33               12            3.17              6.95        310.57                86.52         0.550          pass              0.171             34.4                           0.408               -8.54             -1.193            downtrend_blocked_slope           False                  False
   CEG           90.32               31            1.78              3.14        250.37                65.44         0.531          pass              0.616             49.2                           0.434               -7.53             -1.378 downtrend_blocked_slope_and_streak           False                  False
  PANW           77.78               36            1.28              3.16        352.08                70.38         0.526          pass              0.382             52.1                           0.369                6.91              0.950                                 ok           False                  False
  SBUX           88.57               35            0.16              0.12        106.31                36.16         0.521          pass              0.705             85.8                           0.563               -2.85             -0.351            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:00:05.622595-05:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124103504)

</details>
