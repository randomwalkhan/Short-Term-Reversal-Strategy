# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:50:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            0.96              0.72        107.19                39.87         0.584          pass              0.168              3.7                           0.086                0.36              0.072                                 ok            True                  False
  CTSH          100.00               34            0.74              0.32         61.71                43.69         0.503          pass              0.742             43.9                           0.289               -3.17             -0.114                                 ok            True                  False
   TRI           92.00               25            1.61              1.14        100.82                57.96         0.582          pass              0.481              0.9                           0.219               -5.85             -0.583 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.33               15            0.34              0.06         24.70                25.04         0.569          pass              0.446              0.0                           0.018               -4.65             -0.319            downtrend_blocked_slope           False                  False
   PEP          100.00               13            0.76              0.71        134.03                14.34         0.541          pass              0.474              0.0                           0.165               -4.11             -0.376            downtrend_blocked_slope           False                  False
  ADSK           85.71               28            1.47              2.26        219.34                56.33         0.532          pass              0.378             17.4                           0.224              -10.20             -0.494 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.48               42            0.55              0.52        134.78                64.77         0.527          pass              0.687             51.8                           0.471              -15.55             -1.338 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.30               37            0.45              0.79        250.16                47.92         0.524          pass              0.866             77.9                           0.700              -10.87             -1.044 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.30               27            0.46              0.87        272.82                24.48         0.515          pass              0.780             71.6                           0.574               -2.66             -0.142                                 ok           False                  False
   EXC           95.83               24            0.14              0.04         42.42                15.25         0.515          pass              0.755             70.0                           0.548               -2.70             -0.419 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               33            0.77              1.72        317.39                44.10         0.512          pass              0.733             42.8                           0.310               -7.95             -0.559 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           87.50               16            1.71              0.28         23.61                34.54         0.501          pass              0.359             22.9                           0.402              -13.00             -1.358 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-17T10:50:04.360759-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:45:01.293299-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:30:05.183690-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:25:03.246728-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:20:02.157972-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917105004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917105004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917105004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917105004)

</details>
