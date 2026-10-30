# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 11:10:05 EDT`
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
  FAST           95.24               21            0.74              0.27         52.43                21.92         0.523            pass              0.547              7.1                           0.275                2.75              0.215                                 ok            True                  False
  MSFT          100.00               14            1.47              5.46        527.80                19.58         0.511            pass              0.630             50.6                           0.480               -1.27             -0.071                                 ok            True                  False
  FTNT           82.35               17            2.53              2.46        138.04                91.61         0.667            pass              0.244             22.6                           0.315              -19.84             -1.553            downtrend_blocked_slope           False                  False
  ALNY           73.33               15            2.75              3.35        172.57               108.34         0.666            pass              0.124              8.1                           0.092              -27.01             -2.462            downtrend_blocked_slope           False                  False
 GOOGL           83.78               37            0.45              0.89        283.44                51.94         0.591            pass              0.561             73.7                           0.794              -17.04             -1.776 downtrend_blocked_slope_and_streak           False                  False
  GOOG           82.86               35            0.58              1.15        281.83                50.42         0.588            pass              0.497             65.1                           0.739              -16.69             -1.726 downtrend_blocked_slope_and_streak           False                  False
   CSX           66.67                9            1.46              0.54         52.01                27.59         0.543            pass              0.105             16.9                           0.278                5.74              0.917                                 ok           False                  False
  ISRG           87.50                8            2.01              6.30        446.06                27.40         0.538            pass              0.269              5.0                           0.140                3.06              0.393                                 ok           False                  False
  TEAM          100.00               10            3.61              5.16        201.89                50.04         0.513            pass              0.549             32.5                           0.464               -5.34             -0.495            downtrend_blocked_slope           False                  False
  MELI           74.29               35            1.09             12.70       1654.69                48.11         0.509            pass              0.409             63.8                           0.689              -10.47             -1.454 downtrend_blocked_slope_and_streak           False                  False
  SBUX           66.67                3            2.73              2.02        104.65                26.25         0.502            pass              0.077              8.9                           0.250                5.24              0.687                                 ok           False                  False
  NXPI           91.67               12            2.42              4.51        264.07                41.25         0.497 below_threshold              0.453             26.4                           0.300               13.18              1.358                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-30T11:10:05.957084-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:05:06.234381-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:00:06.842901-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:55:02.033173-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:50:05.964469-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:45:04.211437-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:40:05.937875-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:35:06.022002-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:30:06.573840-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:25:05.620452-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030111005)

</details>
