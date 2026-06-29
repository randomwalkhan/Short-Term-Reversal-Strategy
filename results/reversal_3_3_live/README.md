# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 10:20:14 EDT`
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
   TRI           82.76               29            0.82              0.48         83.66                56.35         0.588          pass              0.364             34.9                           0.231                2.17              0.307                      ok            True                  False
  GILD           87.50               16            1.26              1.12        127.40                29.34         0.557          pass              0.340             14.6                           0.270                1.21              0.089                      ok            True                  False
  PCAR           80.00               20            1.19              1.01        120.25                36.52         0.548          pass              0.184             20.9                           0.237                0.61              0.020                      ok            True                  False
  SOXL           92.86               14            7.65             11.54        210.65               243.65         0.789          pass              0.536             29.2                           0.243              -15.16             -1.502 downtrend_blocked_slope           False                  False
  MRVL          100.00               12            5.12              9.56        262.67               157.15         0.778          pass              0.539             16.0                           0.188               -9.51             -1.142 downtrend_blocked_slope           False                  False
  AVGO           87.88               33            0.48              1.24        364.49                77.46         0.691          pass              0.616             61.2                           0.347               -4.78             -0.592 downtrend_blocked_slope           False                  False
  ASML           96.88               32            0.69              8.70       1790.89                67.49         0.670          pass              0.745             43.8                           0.310               -4.37             -0.520 downtrend_blocked_slope           False                  False
   TXN           92.31               13            2.52              5.03        283.27                70.58         0.620          pass              0.487             25.5                           0.248               -7.60             -0.691 downtrend_blocked_slope           False                  False
   STX           97.14               35            0.09              0.60        899.64                85.77         0.617          pass              0.915             95.7                           0.580               -3.37             -0.773 downtrend_blocked_slope           False                  False
  MPWR           89.29               28            1.60             14.72       1307.01                89.21         0.611          pass              0.559             43.3                           0.285              -18.07             -1.955 downtrend_blocked_slope           False                  False
  DRAM           80.00                5            6.62              3.33         70.45               125.47         0.606          pass              0.097             12.0                           0.180                3.25              0.423                      ok           False                  False
  MCHP          100.00               19            2.26              1.39         87.33                74.63         0.601          pass              0.613             30.8                           0.259               -9.76             -1.083 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-06-29T10:20:14.360345-04:00 early_entry_1020      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:12.530028-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:10:06.044962-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                         {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T14:50:01.669190-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.416, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3233.0, "option_spread_pct": 43.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.62}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629102014)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629102014)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629102014)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629102014)

</details>
