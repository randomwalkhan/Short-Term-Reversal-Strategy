# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:55:01 EDT`
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
   WBD           94.44               18            0.57              0.11         26.76                21.87         0.594          pass              0.650             50.8                           0.376                1.59              0.127                      ok            True                  False
  INTC           92.00               25            2.67              2.37        126.00               102.61         0.585          pass              0.594             38.4                           0.199                2.09             -0.157                      ok            True                  False
  ASML           91.67               24            2.03             26.22       1831.80                76.04         0.578          pass              0.641             59.4                           0.291               -3.33             -0.117                      ok            True                  False
  PCAR           84.62               26            0.87              0.74        120.92                34.47         0.520          pass              0.358             25.4                           0.306                2.42              0.249                      ok            True                  False
    MU           93.33               15            3.78             27.31       1020.58               134.25         0.729          pass              0.503             13.8                           0.103               -4.79             -0.471 downtrend_blocked_slope           False                  False
  AVGO           85.29               34            0.56              1.43        368.73                71.90         0.682          pass              0.552             60.9                           0.283               -6.37             -0.866 downtrend_blocked_slope           False                  False
  MPWR           86.67               30            1.32             12.27       1326.47                89.16         0.643          pass              0.499             41.1                           0.197               -9.11             -1.527 downtrend_blocked_slope           False                  False
  DRAM           83.33                6            6.44              2.97         64.59               129.95         0.631          pass              0.172              6.6                           0.173              -11.91             -1.278 downtrend_blocked_slope           False                  False
  SOXL           83.33               12            9.69             14.76        211.23               253.51         0.621          pass              0.201             12.3                           0.190              -15.99             -2.046 downtrend_blocked_slope           False                  False
  MCHP           91.30               23            1.86              1.15         88.20                71.75         0.608          pass              0.537             29.3                           0.246               -7.51             -1.237 downtrend_blocked_slope           False                  False
   ADI           89.66               29            0.94              2.55        387.89                61.24         0.607          pass              0.550             34.9                           0.176               -7.02             -1.176 downtrend_blocked_slope           False                  False
  NXPI           89.29               28            1.09              2.13        278.27                63.41         0.593          pass              0.505             26.1                           0.139               -7.09             -1.297 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-02T10:55:01.729347-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:50:04.749926-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:45:02.720384-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:40:05.626608-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:35:03.761213-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:30:06.141099-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:25:06.771097-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:20:04.785381-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702105501)

</details>
