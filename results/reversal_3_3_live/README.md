# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:50:05 EDT`
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
  PYPL           81.25               16            1.54              0.61         56.47                63.95         0.666          pass              0.263             41.0                           0.334               22.84              2.462                      ok            True                  False
   TXN           90.00               20            2.20              4.48        289.30                64.46         0.599          pass              0.533             46.6                           0.586               -2.82             -0.212                      ok            True                  False
   ADI           84.00               25            1.55              4.12        378.76                54.65         0.574          pass              0.436             57.2                           0.561               -0.67             -0.008                      ok            True                  False
  ASML           92.00               25            1.99             24.85       1774.22                64.12         0.561          pass              0.645             56.4                           0.687               -1.13             -0.062                      ok            True                  False
  CTSH           80.00               35            1.02              0.32         44.42                66.72         0.556          pass              0.407             61.6                           0.336                5.04              0.487                      ok            True                  False
  MPWR           81.25               32            1.51             13.84       1299.72                74.72         0.554          pass              0.456             73.5                           0.578               -0.18              0.073                      ok            True                  False
   ADP           96.30               27            0.72              1.30        256.00                34.79         0.535          pass              0.581              4.6                           0.124                5.13              0.572                      ok            True                  False
  NXPI           86.96               23            1.99              3.76        269.05                54.99         0.528          pass              0.492             55.8                           0.490               -2.95             -0.247                      ok            True                  False
  AVGO           84.85               33            0.88              2.31        373.46                50.81         0.510          pass              0.574             80.2                           0.675                2.97              0.268                      ok            True                  False
  UPRO           94.12               17            2.13              2.14        142.69                37.18         0.505          pass              0.617             47.9                           0.534               -0.15              0.076                      ok            True                  False
  CTAS           90.00               30            0.79              1.13        205.76                39.81         0.501          pass              0.507             19.0                           0.188               12.82              1.305                      ok            True                  False
   WDC           85.71               35            0.18              0.60        466.55               109.88         0.670          pass              0.679             97.7                           0.944              -13.55             -1.524 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T10:50:05.950291-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:45:01.895782-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:40:02.017826-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:35:03.822723-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:30:06.695303-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:25:01.970111-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:20:01.107680-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:15:01.837180-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:04.802091-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717105005)

</details>
