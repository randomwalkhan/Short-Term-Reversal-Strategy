# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:30:01 EDT`
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
  TEAM           86.49               37            1.40              0.86         86.94               115.89         0.700          pass              0.554             43.8                           0.298               23.49              2.542                                 ok            True                  False
  FTNT           93.33               30            1.23              0.99        115.01                70.54         0.603          pass              0.610             20.2                           0.141               33.01              3.593                                 ok            True                  False
  MNST           80.00               25            0.93              0.56         86.17                49.64         0.549          pass              0.371             72.0                           0.391               10.91              1.194                                 ok            True                  False
    ZS           82.86               35            1.06              1.11        148.40                59.15         0.531          pass              0.420             41.5                           0.323                8.25              1.272                                 ok            True                  False
   XEL           94.12               17            1.07              0.60         80.34                27.14         0.527          pass              0.674             66.1                           0.538                0.33             -0.076                                 ok            True                  False
  CDNS           95.65               23            1.86              4.74        362.17                37.36         0.526          pass              0.593             18.0                           0.236                9.87              1.144                                 ok            True                  False
   CSX           85.71               28            0.87              0.27         44.62                30.07         0.514          pass              0.397             24.3                           0.348               -1.95             -0.129                                 ok            True                  False
   TXN           80.00                5            3.12              6.50        294.97                67.69         0.667          pass              0.081              4.9                           0.127                9.41              0.917                                 ok           False                  False
 CMCSA           94.74               38            0.06              0.01         25.03                62.25         0.650          pass              0.925             93.5                           0.843               -9.50             -0.963 downtrend_blocked_slope_and_streak           False                  False
  SHOP           89.19               37            1.21              0.87        102.17                84.99         0.642          pass              0.532             14.2                           0.186              -17.00             -2.124            downtrend_blocked_slope           False                  False
  NXPI           50.00                2            4.50              9.64        301.86                87.21         0.590          pass              0.187             42.8                           0.255               26.84              1.286                                 ok           False                  False
   BKR           72.22               18            1.24              0.56         64.36                39.66         0.558          pass              0.167             19.2                           0.326               -5.40             -0.882 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-12T11:30:01.054285-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:25:05.158793-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512113001)

</details>
