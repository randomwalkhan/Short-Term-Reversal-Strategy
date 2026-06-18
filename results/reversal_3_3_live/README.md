# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 14:10:03 EDT`
Last processed slot: `manage_1400`

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
   WMT           81.82               22            1.02              0.84        117.77                34.58         0.570          pass              0.216             10.1                           0.276               -0.69              0.006                                 ok            True                  False
  MDLZ           93.33               15            1.12              0.48         60.66                21.28         0.549          pass              0.515             23.6                           0.336               -1.33             -0.165                                 ok            True                  False
  INTU           76.47               34            1.33              2.51        268.00                98.62         0.682          pass              0.419             63.6                           0.671              -12.08             -1.270 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                2            1.33              0.22         23.11                27.50         0.671          pass              0.491              8.1                           0.193                3.72              0.372                                 ok           False                  False
   PEP          100.00               21            0.16              0.15        141.52                22.29         0.609          pass              0.722             62.7                           0.335                0.50              0.161                                 ok           False                  False
   TRI           77.27               22            1.19              0.66         78.97                52.51         0.583          pass              0.308             56.7                           0.451               -8.67             -0.826 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.85              4.43        339.76                27.62         0.568          pass              0.196             16.9                           0.390               -2.97             -0.127           downtrend_blocked_streak           False                  False
  TEAM           88.10               42            0.69              0.41         84.22                82.55         0.555          pass              0.705             77.9                           0.643              -17.43             -1.870 downtrend_blocked_slope_and_streak           False                  False
   STX           97.37               38            0.18              1.31       1065.51                67.39         0.544          pass              0.862             73.5                           0.503               14.93              2.367                                 ok           False                  False
  CRWD           87.50               40            0.38              1.82        682.18                64.33         0.544          pass              0.719             88.2                           0.731               -5.39              0.075                                 ok           False                  False
  GILD           83.33                6            2.07              1.82        124.67                29.17         0.543          pass              0.185             13.9                           0.322               -4.28             -0.257 downtrend_blocked_slope_and_streak           False                  False
   AEP           78.26               23            0.34              0.30        128.14                19.26         0.528          pass              0.352             70.7                           0.334                0.04              0.067                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618141003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618141003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618141003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618141003)

</details>
