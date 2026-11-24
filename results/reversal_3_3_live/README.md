# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 11:20:05 EST`
Last processed slot: `manage_1130`

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
  QCOM           78.26               23            2.18              2.52        164.30                82.33         0.623          pass              0.260             37.1                           0.291               -6.77             -1.173 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           78.57               14            1.91              3.77        280.48                61.35         0.603          pass              0.121             11.2                           0.179               -3.71             -0.791            downtrend_blocked_slope           False                  False
  GOOG           81.25               16            1.71              3.35        278.09                58.63         0.597          pass              0.177             14.8                           0.206               -3.57             -0.759            downtrend_blocked_slope           False                  False
   BKR           73.68               19            1.22              0.39         45.87                56.59         0.596          pass              0.243             41.1                           0.659               -4.79             -0.833 downtrend_blocked_slope_and_streak           False                  False
  UPRO           57.14                7            3.72              3.11        118.41                94.72         0.592          pass              0.116             19.1                           0.216              -15.46             -2.485 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               16            2.52              4.45        249.81                65.44         0.577          pass              0.382             28.1                           0.276               -8.22             -1.412 downtrend_blocked_slope_and_streak           False                  False
  ABNB           90.24               41            0.19              0.23        173.86                57.35         0.569          pass              0.772             80.5                           0.427               -7.10             -0.820 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.12               17            0.89              2.58        414.53                26.32         0.564          pass              0.577             32.4                           0.337               -3.64             -0.429            downtrend_blocked_slope           False                  False
  SBUX           87.50               24            0.71              0.52        106.14                36.16         0.555          pass              0.466             39.0                           0.217               -3.38             -0.375            downtrend_blocked_slope           False                  False
  SHOP           81.58               38            0.68              0.64        134.03                71.17         0.547          pass              0.497             71.2                           0.351               -9.02             -1.530 downtrend_blocked_slope_and_streak           False                  False
   HON           83.33               30            0.55              0.86        221.60                37.67         0.530          pass              0.482             69.0                           0.390               -2.97             -0.363           downtrend_blocked_streak           False                  False
  FAST          100.00               22            0.85              0.31         51.93                27.50         0.527          pass              0.636             34.3                           0.457               -5.87             -0.865 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T11:20:05.808543-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:15:03.611406-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:10:04.431868-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:05:06.530028-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:00:06.064942-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:55:05.583055-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:50:05.812111-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:45:04.516238-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:40:03.078484-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124112005)

</details>
