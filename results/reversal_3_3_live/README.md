# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:25:04 EST`
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
  INTC           57.14                7            7.61              3.18         58.30               154.63         0.638          pass              0.069              1.7                           0.087               -5.18             -1.031 downtrend_blocked_slope_and_streak           False                  False
  UPRO           62.50                8            2.98              2.50        118.67                94.72         0.637          pass              0.169             35.0                           0.314              -14.81             -2.450 downtrend_blocked_slope_and_streak           False                  False
  QCOM           80.00               25            1.98              2.30        164.40                82.33         0.625          pass              0.290             42.7                           0.362               -6.59             -1.164 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            0.96              1.90        281.29                61.35         0.584          pass              0.311             46.4                           0.423               -2.78             -0.747            downtrend_blocked_slope           False                  False
   BKR           73.68               19            1.46              0.47         45.84                56.59         0.584          pass              0.170             17.3                           0.204               -5.02             -0.844 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67                9            3.56             34.48       1369.00                73.86         0.577          pass              0.069              3.9                           0.123              -11.50             -1.572 downtrend_blocked_slope_and_streak           False                  False
  GOOG           80.00               30            0.82              1.61        278.84                58.63         0.567          pass              0.348             52.6                           0.463               -2.70             -0.717            downtrend_blocked_slope           False                  False
   MAR           95.45               22            0.52              1.53        414.98                26.32         0.564          pass              0.588             17.1                           0.266               -3.29             -0.412            downtrend_blocked_slope           False                  False
   CEG           91.30               23            2.12              3.74        250.12                65.44         0.563          pass              0.563             39.5                           0.313               -7.84             -1.394 downtrend_blocked_slope_and_streak           False                  False
  DASH           82.00               50            0.04              0.05        161.33                67.28         0.535          pass              0.599             97.4                           0.505               -9.52             -1.328 downtrend_blocked_slope_and_streak           False                  False
  AVGO           70.00               10            3.95              8.68        309.83                86.52         0.528          pass              0.107             18.1                           0.254               -9.29             -1.230            downtrend_blocked_slope           False                  False
  PANW           78.95               38            1.09              2.71        352.27                70.38         0.527          pass              0.416             58.9                           0.477                7.11              0.958                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:00:05.622595-05:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124102504)

</details>
