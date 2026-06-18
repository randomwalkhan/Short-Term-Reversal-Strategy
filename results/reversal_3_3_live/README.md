# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 14:20:05 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           84.00               25            0.88              0.73        117.82                34.58         0.561          pass              0.329             22.1                           0.414               -0.55              0.012                                 ok            True                  False
  CRWD           87.18               39            0.54              2.58        681.86                64.33         0.540          pass              0.689             83.3                           0.615               -5.54              0.068                                 ok            True                  False
  MDLZ           94.44               18            1.05              0.45         60.67                21.28         0.533          pass              0.576             28.1                           0.334               -1.26             -0.162                                 ok            True                  False
  INTU           75.00               32            1.44              2.72        267.92                98.62         0.686          pass              0.397             60.6                           0.653              -12.18             -1.275 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.32              0.22         23.11                27.50         0.665          pass              0.492              8.6                           0.145                3.73              0.373                                 ok           False                  False
   TRI           77.27               22            1.21              0.67         78.96                52.51         0.581          pass              0.305             55.8                           0.408               -8.69             -0.827 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.74              4.16        339.88                27.62         0.575          pass              0.212             21.9                           0.495               -2.86             -0.122           downtrend_blocked_streak           False                  False
  TEAM           88.10               42            0.53              0.31         84.26                82.55         0.566          pass              0.722             83.0                           0.714              -17.30             -1.862 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.50                8            1.90              1.67        124.74                29.17         0.545          pass              0.318             21.2                           0.457               -4.10             -0.249           downtrend_blocked_streak           False                  False
   STX           97.37               38            0.33              2.48       1065.01                67.39         0.533          pass              0.789             49.9                           0.327               14.74              2.360                                 ok           False                  False
  WDAY           76.92               26            2.31              1.97        120.99                69.08         0.524          pass              0.264             35.1                           0.457              -19.53             -2.134 downtrend_blocked_slope_and_streak           False                  False
  COST           50.00               10            1.62             10.95        960.90                23.27         0.516          pass              0.080              9.4                           0.270               -2.30             -0.077                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-18T12:00:02.352957-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:55:04.331586-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:50:03.235877-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:45:01.152442-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:40:06.149608-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:35:05.166451-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:30:05.153206-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:25:04.328726-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:20:05.337026-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:15:05.288880-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618142005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618142005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618142005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618142005)

</details>
