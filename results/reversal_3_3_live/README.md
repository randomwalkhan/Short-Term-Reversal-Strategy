# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 11:00:08 EDT`
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
  DRAM           90.91               11            4.99              2.51         70.80               125.47         0.685          pass              0.467             33.7                           0.514                5.05              0.502                      ok            True                  False
   XEL          100.00               20            0.66              0.38         82.07                23.26         0.583          pass              0.602             25.5                           0.275                3.90              0.523                      ok            True                  False
   EXC           84.62               13            0.90              0.30         47.27                19.58         0.582          pass              0.241             13.3                           0.184                1.66              0.247                      ok            True                  False
  GILD           92.31               13            1.49              1.34        127.31                29.34         0.565          pass              0.465             20.1                           0.320                0.96              0.078                      ok            True                  False
   TRI           80.00               25            1.54              0.90         83.48                56.35         0.560          pass              0.167              3.7                           0.229                1.44              0.274                      ok            True                  False
  PCAR           81.25               16            1.52              1.28        120.13                36.52         0.557          pass              0.129              0.0                           0.197                0.28              0.005                      ok            True                  False
  SBUX           82.35               17            1.02              0.75        104.28                26.41         0.556          pass              0.173              2.7                           0.225                0.48              0.237                      ok            True                  False
  INTC           90.00               20            3.52              3.16        126.97                98.20         0.544          pass              0.550             54.0                           0.797               -0.61              0.471                      ok            True                  False
   HON           87.50               24            0.36              0.62        243.14               250.29         0.998          pass              0.673             93.4                           0.442               10.08              6.168                      ok           False                  False
  MRVL          100.00               24            1.92              3.58        265.24               157.15         0.862          pass              0.785             68.5                           0.744               -6.45             -0.991 downtrend_blocked_slope           False                  False
  MPWR           91.18               34            0.32              2.93       1312.06                89.21         0.661          pass              0.790             88.7                           0.573              -17.00             -1.896 downtrend_blocked_slope           False                  False
   TXN           93.94               33            0.53              1.05        284.97                70.58         0.621          pass              0.841             84.4                           0.833               -5.71             -0.599 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T11:00:08.009230-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:39:22.639470-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:20:14.360345-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:12.530028-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629110008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629110008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629110008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629110008)

</details>
