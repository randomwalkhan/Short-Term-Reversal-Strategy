# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC           92.00               25            2.50              2.22        126.07               102.61         0.598          pass              0.607             42.4                           0.214                2.27             -0.149                      ok            True                  False
   WBD           94.44               18            0.58              0.11         26.76                21.87         0.593          pass              0.647             49.8                           0.329                1.58              0.127                      ok            True                  False
  ASML           91.67               24            1.91             24.65       1832.48                76.04         0.587          pass              0.649             61.9                           0.301               -3.21             -0.111                      ok            True                  False
  PCAR           81.82               22            1.09              0.92        120.84                34.47         0.531          pass              0.182              0.0                           0.048                2.20              0.240                      ok            True                  False
    MU           89.47               19            3.11             22.50       1022.64               134.25         0.743          pass              0.474             29.0                           0.160               -4.13             -0.440 downtrend_blocked_slope           False                  False
  DRAM           87.50                8            5.48              2.53         64.78               129.95         0.694          pass              0.303             11.1                           0.098              -11.01             -1.232 downtrend_blocked_slope           False                  False
  AVGO           85.29               34            0.53              1.36        368.76                71.90         0.684          pass              0.558             62.8                           0.297               -6.34             -0.865 downtrend_blocked_slope           False                  False
  MPWR           86.67               30            1.03              9.61       1327.61                89.16         0.663          pass              0.539             53.9                           0.243               -8.85             -1.514 downtrend_blocked_slope           False                  False
   TXN           91.43               35            0.30              0.64        298.14                67.74         0.634          pass              0.755             73.3                           0.324               -1.45             -0.820                      ok           False                  False
  SOXL           83.33               12            9.71             14.78        211.21               253.51         0.629          pass              0.182              5.7                           0.170              -16.01             -2.046 downtrend_blocked_slope           False                  False
  MCHP           95.00               20            2.21              1.37         88.10                71.75         0.607          pass              0.576             16.1                           0.202               -7.84             -1.253 downtrend_blocked_slope           False                  False
   ADI           89.29               28            1.04              2.84        387.76                61.24         0.606          pass              0.510             27.4                           0.149               -7.13             -1.181 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-02T10:45:02.720384-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:40:05.626608-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:35:03.761213-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:30:06.141099-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:25:06.771097-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:20:04.785381-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702104502)

</details>
