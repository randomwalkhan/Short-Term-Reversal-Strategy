# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 10:39:22 EDT`
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
   XEL          100.00               20            0.56              0.32         82.09                23.26         0.589          pass              0.635             36.6                           0.271                4.00              0.527                      ok            True                  False
   TRI           80.77               26            1.19              0.70         83.57                56.35         0.578          pass              0.258             24.2                           0.231                1.79              0.290                      ok            True                  False
  GILD           90.00               10            1.67              1.49        127.24                29.34         0.574          pass              0.342              5.8                           0.160                0.79              0.070                      ok            True                  False
  SBUX           88.46               26            0.59              0.43        104.41                26.41         0.531          pass              0.423             12.7                           0.269                0.91              0.257                      ok            True                  False
  SOXL           95.45               22            3.34              5.04        213.44               243.65         0.919          pass              0.779             69.1                           0.679              -11.20             -1.295 downtrend_blocked_slope           False                  False
  MRVL          100.00               18            3.70              6.90        263.81               157.15         0.816          pass              0.653             39.3                           0.565               -8.15             -1.074 downtrend_blocked_slope           False                  False
  DRAM           85.71                7            5.77              2.90         70.64               125.47         0.656          pass              0.288             23.3                           0.491                4.18              0.464                      ok           False                  False
  MPWR           89.29               28            1.06              9.70       1309.16                89.21         0.649          pass              0.620             62.6                           0.589              -17.62             -1.930 downtrend_blocked_slope           False                  False
   TXN           92.59               27            0.95              1.90        284.61                70.58         0.631          pass              0.728             71.9                           0.822               -6.11             -0.618 downtrend_blocked_slope           False                  False
  QCOM           87.50               24            1.22              1.62        188.70                89.86         0.627          pass              0.537             60.2                           0.609              -11.64             -1.471 downtrend_blocked_slope           False                  False
  MCHP           95.83               24            1.66              1.02         87.49                74.63         0.602          pass              0.701             49.1                           0.522               -9.21             -1.055 downtrend_blocked_slope           False                  False
  NXPI           90.00               20            1.73              3.35        275.58                66.10         0.598          pass              0.517             41.4                           0.447              -10.40             -1.052 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T10:39:22.639470-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:20:14.360345-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:12.530028-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629103922)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629103922)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629103922)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629103922)

</details>
