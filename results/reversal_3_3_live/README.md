# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 11:25:02 EDT`
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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   HON           87.50               16            0.89              1.51        242.76               250.29         0.999          pass              0.591             83.8                           0.378                9.50              6.144                      ok            True                  False
  DRAM           90.91               11            4.88              2.46         70.83               125.47         0.692          pass              0.472             35.1                           0.495                5.17              0.507                      ok            True                  False
   XEL          100.00               13            0.85              0.49         82.02                23.26         0.619          pass              0.492              3.4                           0.152                3.69              0.514                      ok            True                  False
    MU           90.91               11            5.48             43.41       1113.72               130.58         0.586          pass              0.485             42.9                           0.692                9.04              0.951                      ok            True                  False
  GILD           93.33               15            1.40              1.25        127.34                29.34         0.558          pass              0.520             25.1                           0.429                1.06              0.083                      ok            True                  False
  INTC           91.30               23            3.12              2.80        127.12                98.20         0.552          pass              0.621             59.2                           0.774               -0.20              0.490                      ok            True                  False
   AEP           80.00               10            1.26              1.22        138.17                21.35         0.509          pass              0.292             80.5                           0.557                5.97              0.801                      ok            True                  False
  MRVL          100.00               25            1.48              2.76        265.59               157.15         0.874          pass              0.815             75.7                           0.837               -6.03             -0.970 downtrend_blocked_slope           False                  False
  MPWR           90.91               33            0.56              5.18       1311.10                89.21         0.651          pass              0.749             80.0                           0.606              -17.21             -1.907 downtrend_blocked_slope           False                  False
   TXN           91.67               24            1.16              2.32        284.43                70.58         0.636          pass              0.665             65.6                           0.440               -6.31             -0.628 downtrend_blocked_slope           False                  False
  MCHP           93.10               29            0.94              0.58         87.68                74.63         0.614          pass              0.751             71.1                           0.732               -8.55             -1.022 downtrend_blocked_slope           False                  False
   PEP           83.33                6            1.16              1.14        140.90                19.98         0.612          pass              0.211             20.2                           0.307               -3.13             -0.385 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T11:25:02.270662-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:22:12.890748-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:15:24.828732-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:10:30.368323-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:05:08.784584-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:00:08.009230-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:39:22.639470-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:20:14.360345-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:12.530028-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629112502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629112502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629112502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629112502)

</details>
