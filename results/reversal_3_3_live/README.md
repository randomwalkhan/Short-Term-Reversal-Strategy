# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 12:40:06 EDT`
Last processed slot: `manage_1230`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.24               34            0.83              1.53        263.92                64.38         0.602          pass              0.657             72.5                           0.486               -3.31             -0.232                                 ok            True                  False
  FAST           94.12               17            0.82              0.30         52.42                21.92         0.538          pass              0.579             33.8                           0.559                2.67              0.212                                 ok            True                  False
  MSFT          100.00               14            1.50              5.57        527.75                19.58         0.510          pass              0.627             49.6                           0.584               -1.30             -0.073                                 ok            True                  False
  FTNT           70.00               10            3.16              3.08        137.78                91.61         0.660          pass              0.085              6.4                           0.249              -20.36             -1.582            downtrend_blocked_slope           False                  False
  ALNY           83.87               31            1.30              1.58        173.32               108.34         0.658          pass              0.510             67.0                           0.880              -25.92             -2.395            downtrend_blocked_slope           False                  False
  GOOG           75.00               20            1.23              2.44        281.28                50.42         0.632          pass              0.208             26.0                           0.179              -17.24             -1.756 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.91               23            1.18              2.34        282.82                51.94         0.624          pass              0.241             30.7                           0.206              -17.65             -1.810 downtrend_blocked_slope_and_streak           False                  False
  ISRG           87.50                8            2.26              7.10        445.72                27.40         0.523          pass              0.264              3.9                           0.234                2.79              0.382                                 ok           False                  False
  MELI           76.67               30            1.51             17.51       1652.63                48.11         0.519          pass              0.336             50.1                           0.498              -10.84             -1.473 downtrend_blocked_slope_and_streak           False                  False
   CSX           76.19               21            0.79              0.29         52.12                27.59         0.514          pass              0.290             54.9                           0.703                6.46              0.948                                 ok           False                  False
  META           79.41               34            0.52              2.28        623.54                38.13         0.509          pass              0.447             78.8                           0.594              -12.42             -1.627 downtrend_blocked_slope_and_streak           False                  False
  SBUX           71.43                7            2.27              1.67        104.79                26.25         0.505          pass              0.132             27.0                           0.381                5.74              0.708                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030124006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030124006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030124006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030124006)

</details>
