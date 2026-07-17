# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 11:25:05 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.95               21            1.22              0.48         56.52                63.95         0.655          pass              0.325             53.5                           0.525               23.25              2.477                      ok            True                  False
   ADI           86.36               22            1.94              5.17        378.32                54.65         0.570          pass              0.446             46.3                           0.475               -1.06             -0.026                      ok            True                  False
  ASML           91.67               24            2.22             27.74       1772.98                64.12         0.552          pass              0.614             51.4                           0.555               -1.36             -0.072                      ok            True                  False
   ADP           96.30               27            0.79              1.41        255.95                34.79         0.528          pass              0.622             18.5                           0.229                5.06              0.570                      ok            True                  False
  TEAM           85.00               40            0.62              0.40         92.19                71.47         0.526          pass              0.635             83.0                           0.438                9.48              0.923                      ok            True                  False
  PAYX          100.00               28            0.81              0.65        114.42                35.43         0.520          pass              0.604             10.6                           0.182                6.98              0.749                      ok            True                  False
  UPRO           90.91               11            2.48              2.49        142.54                37.18         0.518          pass              0.467             39.2                           0.418               -0.51              0.059                      ok            True                  False
  AVGO           81.48               27            1.47              3.85        372.80                50.81         0.506          pass              0.404             67.0                           0.536                2.36              0.241                      ok            True                  False
  DRAM           84.85               33            0.06              0.02         52.33               117.20         0.776          pass              0.658             99.2                           0.720              -13.72             -1.722 downtrend_blocked_slope           False                  False
    MU           81.82               33            0.13              0.75        852.88               110.15         0.731          pass              0.568             97.8                           0.622              -12.64             -1.223 downtrend_blocked_slope           False                  False
  MSTR           75.61               41            1.20              0.79         93.69                90.37         0.605          pass              0.481             73.5                           0.549               -7.81             -0.565 downtrend_blocked_slope           False                  False
   WDC           78.26               23            2.30              7.53        463.58               109.88         0.591          pass              0.357             70.4                           0.481              -15.39             -1.622 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T11:25:05.915843-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:20:01.891090-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:15:01.934131-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:10:03.757690-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:05:01.918068-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:00:05.852875-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:55:01.965202-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:50:05.950291-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:45:01.895782-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:40:02.017826-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717112505)

</details>
