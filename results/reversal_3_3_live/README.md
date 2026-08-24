# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 10:30:01 EDT`
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
  LRCX           80.95               21            3.86              8.48        310.37                88.60         0.562          pass              0.231             25.3                           0.509               -1.47             -0.352                                 ok            True                  False
  ASML           84.00               25            1.78             21.95       1754.35                48.84         0.541          pass              0.312             16.9                           0.209               -0.06             -0.285                                 ok            True                  False
  REGN          100.00               29            0.82              4.82        831.98                30.64         0.516          pass              0.659             26.9                           0.306                2.48              0.468                                 ok            True                  False
  SBUX           84.21               19            0.68              0.51        106.86                20.57         0.510          pass              0.367             47.9                           0.422                2.21             -0.030                                 ok            True                  False
  ALNY           77.78               18            2.40              3.96        234.52               131.78         0.801          pass              0.211             25.8                           0.294                6.26              0.699                                 ok           False                  False
  INSM           86.67               45            0.47              0.41        125.59               110.84         0.757          pass              0.692             79.7                           0.881               -7.10             -0.584 downtrend_blocked_slope_and_streak           False                  False
  AMAT           87.50               24            2.75              9.49        488.25                82.60         0.618          pass              0.437             27.3                           0.408               -8.21             -1.015            downtrend_blocked_slope           False                  False
   APP           66.67               36            1.94              4.16        303.99                90.15         0.611          pass              0.316             27.3                           0.227              -11.55             -0.699            downtrend_blocked_slope           False                  False
  GEHC           97.50               40            0.27              0.14         74.76                48.71         0.583          pass              0.815             52.4                           0.304                2.30              0.279                                 ok           False                  False
  UPRO           77.78               27            0.91              0.96        149.47                39.04         0.571          pass              0.272             33.7                           0.345               -4.17             -0.487            downtrend_blocked_slope           False                  False
  MCHP           82.61               23            3.29              1.74         74.88                69.56         0.554          pass              0.238              8.6                           0.252              -10.14             -0.868            downtrend_blocked_slope           False                  False
   AEP           95.00               20            0.50              0.42        120.76                19.55         0.547          pass              0.568             15.5                           0.148               -2.04             -0.131           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T10:30:01.238985-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:25:06.425653-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:20:01.387196-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:15:01.389030-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:10:01.316901-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:05:05.120136-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:00:02.345614-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-21T12:00:13.505037-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824103001)

</details>
