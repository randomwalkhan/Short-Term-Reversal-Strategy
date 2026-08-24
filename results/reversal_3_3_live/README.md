# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 10:40:01 EDT`
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
  ALNY           80.00               20            2.24              3.71        234.63               131.78         0.801          pass              0.238             30.5                           0.365                6.42              0.706                                 ok            True                  False
  LRCX           82.61               23            3.29              7.23        310.90                88.60         0.585          pass              0.324             36.3                           0.702               -0.89             -0.325                                 ok            True                  False
  ASML           85.71               28            1.23             15.18       1757.25                48.84         0.556          pass              0.456             42.6                           0.545                0.50             -0.259                                 ok            True                  False
  REGN          100.00               25            0.96              5.58        831.65                30.64         0.533          pass              0.599             15.3                           0.261                2.35              0.462                                 ok            True                  False
  SBUX           83.33               18            0.79              0.59        106.83                20.57         0.508          pass              0.311             39.3                           0.326                2.09             -0.035                                 ok            True                  False
  INSM           87.50               48            0.21              0.18        125.69               110.84         0.756          pass              0.749             91.0                           0.908               -6.86             -0.572 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.89               27            2.36              8.13        488.84                82.60         0.625          pass              0.526             37.7                           0.650               -7.83             -0.996            downtrend_blocked_slope           False                  False
   APP           65.62               32            2.45              5.24        303.53                90.15         0.604          pass              0.236              9.6                           0.141              -12.01             -0.722            downtrend_blocked_slope           False                  False
  GEHC           97.44               39            0.29              0.15         74.75                48.71         0.587          pass              0.795             47.6                           0.303                2.28              0.278                                 ok           False                  False
  UPRO           76.67               30            0.78              0.82        149.53                39.04         0.559          pass              0.320             43.4                           0.592               -4.04             -0.481            downtrend_blocked_slope           False                  False
  MCHP           81.82               22            3.34              1.77         74.87                69.56         0.557          pass              0.206              7.3                           0.244              -10.19             -0.870            downtrend_blocked_slope           False                  False
   AEP           95.00               20            0.46              0.39        120.77                19.55         0.549          pass              0.585             21.1                           0.163               -2.00             -0.129           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T10:40:01.398782-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:35:01.378502-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:30:01.238985-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:25:06.425653-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:20:01.387196-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:15:01.389030-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:10:01.316901-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:05:05.120136-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:00:02.345614-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T09:20:01.323688-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824104001)

</details>
