# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 12:45:06 EDT`
Last processed slot: `manual`

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

- Cash: `$117,176.55`
- Equity: `$117,176.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  MSTR     option         option MSTR261218C00140000     41          2026-10-29         2026-10-30       15.025     13.5225 -6160.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           87.10               31            0.96              1.77        263.82                64.38         0.611            pass              0.595             68.1                           0.467               -3.43             -0.238                                 ok            True                  False
  FAST           94.12               17            0.86              0.32         52.41                21.92         0.536            pass              0.569             30.8                           0.512                2.63              0.210                                 ok            True                  False
  MSFT          100.00               14            1.52              5.66        527.72                19.58         0.509            pass              0.624             48.8                           0.579               -1.32             -0.074                                 ok            True                  False
  FTNT           72.73               11            3.04              2.96        137.83                91.61         0.663            pass              0.103             10.0                           0.303              -20.26             -1.577            downtrend_blocked_slope           False                  False
  ALNY           79.17               24            2.07              2.52        172.92               108.34         0.650            pass              0.300             47.4                           0.658              -26.50             -2.431            downtrend_blocked_slope           False                  False
  GOOG           75.00               20            1.24              2.45        281.27                50.42         0.632            pass              0.206             25.5                           0.193              -17.24             -1.756 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.91               23            1.19              2.36        282.81                51.94         0.623            pass              0.239             30.0                           0.234              -17.66             -1.810 downtrend_blocked_slope_and_streak           False                  False
   CSX           78.95               19            0.87              0.32         52.10                27.59         0.526            pass              0.264             50.6                           0.674                6.38              0.944                                 ok           False                  False
  ISRG           80.00                5            2.46              7.72        445.45                27.40         0.523            pass              0.052              0.0                           0.251                2.59              0.372                                 ok           False                  False
  MELI           75.86               29            1.58             18.33       1652.28                48.11         0.521            pass              0.322             47.8                           0.542              -10.91             -1.477 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               35            0.48              2.11        623.61                38.13         0.505            pass              0.458             80.4                           0.642              -12.38             -1.625 downtrend_blocked_slope_and_streak           False                  False
  IDXX           80.00               10            2.23              8.99        572.13                25.33         0.499 below_threshold              0.095             15.1                           0.366                0.50              0.207                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-30T12:00:06.415858-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:55:05.950697-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:50:06.698728-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:45:05.073767-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:40:04.093863-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:35:04.895794-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:30:05.799923-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:25:03.898317-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:20:07.033470-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:15:06.943574-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030124506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030124506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030124506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030124506)

</details>
