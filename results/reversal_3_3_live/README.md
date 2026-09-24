# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 11:15:04 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$67,953.30`
- Equity: `$67,953.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.12               34            1.12              1.27        161.66               109.59         0.759          pass              0.825             70.9                           0.372               20.86              2.743                  ok            True                  False
  PYPL           91.18               34            0.60              0.22         52.42                57.12         0.614          pass              0.589             23.2                           0.207                0.05             -0.176                  ok            True                  False
  NVDA           90.91               22            1.74              2.75        224.33                44.57         0.570          pass              0.461             11.1                           0.142               -0.82              0.369                  ok            True                  False
  ADSK           81.25               32            1.04              1.58        216.47                55.47         0.555          pass              0.411             58.3                           0.651                4.01              0.258                  ok            True                  False
  MPWR           85.19               27            1.96             18.60       1347.50                51.84         0.535          pass              0.417             37.3                           0.456               10.40              1.204                  ok            True                  False
  MSFT          100.00               15            1.46              5.12        498.39                22.42         0.528          pass              0.552             21.9                           0.309                0.33              0.076                  ok            True                  False
   ADP           95.00               20            0.76              1.41        263.08                21.61         0.525          pass              0.565             15.2                           0.248               -0.71             -0.020                  ok            True                  False
    MU           84.85               33            1.62             12.13       1066.68                49.67         0.520          pass              0.471             45.5                           0.504                2.61              0.949                  ok            True                  False
  UPRO           84.21               19            1.65              1.73        149.56                31.44         0.519          pass              0.321             32.4                           0.210                0.43              0.372                  ok            True                  False
   WMT           83.33               18            1.18              0.91        110.14                21.22         0.515          pass              0.274             26.8                           0.437                3.21              0.283                  ok            True                  False
  DRAM           82.14               28            2.53              1.10         61.43                51.34         0.503          pass              0.256              9.5                           0.195               -2.02              0.478                  ok            True                  False
  CTSH          100.00               13            2.71              1.12         58.66                40.91         0.501          pass              0.489              6.4                           0.224               -1.14             -0.191                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-24T11:15:04.671941-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:10:04.620195-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:05:05.575607-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:00:01.778455-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:55:04.808112-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:50:06.565866-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:45:04.775481-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:40:03.659687-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:35:04.814352-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:30:06.608889-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924111504)

</details>
