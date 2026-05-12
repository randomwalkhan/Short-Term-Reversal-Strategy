# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:25:05 EDT`
Last processed slot: `manage_1130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260618C00520000      5          2026-05-12         2026-05-12         35.0        31.5 -1750.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           86.49               37            1.53              0.93         86.91               115.89         0.694          pass              0.539             38.8                           0.297               23.33              2.536                                 ok            True                  False
  FTNT           93.10               29            1.30              1.05        114.99                70.54         0.605          pass              0.584             15.7                           0.121               32.92              3.590                                 ok            True                  False
  GOOG           89.47               38            0.57              1.54        386.11                39.86         0.537          pass              0.653             53.2                           0.636               10.67              1.054                                 ok            True                  False
  MNST           83.33               30            0.75              0.45         86.22                49.64         0.534          pass              0.508             77.4                           0.558               11.11              1.202                                 ok            True                  False
  CDNS           95.24               21            2.12              5.40        361.88                37.36         0.525          pass              0.545              6.5                           0.117                9.58              1.132                                 ok            True                  False
   XEL           94.44               18            1.02              0.57         80.35                27.14         0.524          pass              0.694             67.7                           0.524                0.38             -0.073                                 ok            True                  False
    ZS           82.35               34            1.28              1.33        148.30                59.15         0.524          pass              0.364             29.6                           0.265                8.01              1.262                                 ok            True                  False
   CSX           84.00               25            1.01              0.31         44.61                30.07         0.522          pass              0.297             12.6                           0.262               -2.08             -0.135                                 ok            True                  False
  CHTR           89.36               47            0.24              0.25        147.68               118.46         0.775          pass              0.767             79.9                           0.491              -14.83             -1.354            downtrend_blocked_slope           False                  False
 CMCSA           94.12               34            0.17              0.03         25.02                62.25         0.665          pass              0.848             81.7                           0.661               -9.60             -0.968 downtrend_blocked_slope_and_streak           False                  False
   TXN           75.00                4            3.14              6.54        294.96                67.69         0.665          pass              0.080              4.4                           0.191                9.39              0.916                                 ok           False                  False
  SHOP           88.57               35            1.24              0.89        102.16                84.99         0.652          pass              0.465              1.6                           0.045              -17.03             -2.126            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-12T11:25:05.158793-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512112505)

</details>
