# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 10:25:06 EDT`
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

- Cash: `$57,703.00`
- Equity: `$57,703.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           81.25               16            2.48              4.10        234.46               131.78         0.808          pass              0.224             23.2                           0.222                6.17              0.695                                 ok            True                  False
  ASML           83.33               24            1.79             22.14       1754.27                48.84         0.545          pass              0.285             16.2                           0.179               -0.08             -0.285                                 ok            True                  False
  REGN          100.00               23            1.01              5.89        831.52                30.64         0.542          pass              0.573             10.6                           0.149                2.29              0.460                                 ok            True                  False
  INSM           85.00               40            0.67              0.59        125.52               110.84         0.769          pass              0.623             71.0                           0.823               -7.29             -0.593 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.47               19            3.19             10.99        487.61                82.60         0.624          pass              0.423             15.8                           0.277               -8.62             -1.035            downtrend_blocked_slope           False                  False
   APP           66.67               36            1.84              3.95        304.08                90.15         0.617          pass              0.328             31.0                           0.277              -11.47             -0.694            downtrend_blocked_slope           False                  False
  GEHC           97.37               38            0.39              0.20         74.73                48.71         0.588          pass              0.738             31.0                           0.246                2.18              0.274                                 ok           False                  False
  UPRO           84.00               25            1.13              1.19        149.37                39.04         0.578          pass              0.318             17.7                           0.257               -4.38             -0.497            downtrend_blocked_slope           False                  False
  MCHP           83.33               24            3.24              1.72         74.89                69.56         0.552          pass              0.267             10.0                           0.254              -10.10             -0.866            downtrend_blocked_slope           False                  False
  LRCX           80.00               20            4.18              9.20        310.06                88.60         0.548          pass              0.178             19.0                           0.295               -1.81             -0.367            downtrend_blocked_slope           False                  False
  CSCO           84.38               32            1.01              0.78        110.70                42.43         0.543          pass              0.425             35.6                           0.423              -10.32             -1.173            downtrend_blocked_slope           False                  False
   HON           83.33               24            0.91              1.37        215.31                30.43         0.535          pass              0.326             30.0                           0.270              -11.67             -1.099 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T10:25:06.425653-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:20:01.387196-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:15:01.389030-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:10:01.316901-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:05:05.120136-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:00:02.345614-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-21T12:00:13.505037-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824102506)

</details>
