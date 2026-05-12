# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:35:01 EDT`
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
  TEAM           87.50               40            1.11              0.68         87.02               115.89         0.701          pass              0.637             55.5                           0.357               23.86              2.555                                 ok            True                  False
  FTNT           93.33               30            1.23              0.99        115.01                70.54         0.603          pass              0.610             20.2                           0.141               33.01              3.593                                 ok            True                  False
  MNST           80.00               25            0.87              0.52         86.19                49.64         0.552          pass              0.376             73.7                           0.371               10.97              1.197                                 ok            True                  False
  GOOG           88.89               36            0.58              1.58        386.09                39.86         0.547          pass              0.621             51.9                           0.605               10.65              1.053                                 ok            True                  False
    ZS           82.86               35            1.06              1.11        148.40                59.15         0.531          pass              0.420             41.5                           0.324                8.25              1.272                                 ok            True                  False
   XEL           94.12               17            1.04              0.59         80.35                27.14         0.528          pass              0.677             66.9                           0.585                0.35             -0.074                                 ok            True                  False
  CDNS           95.24               21            2.07              5.28        361.94                37.36         0.527          pass              0.552              8.7                           0.148                9.64              1.134                                 ok            True                  False
  INTU           89.19               37            0.54              1.49        392.65                46.70         0.523          pass              0.685             69.2                           0.425               -2.30             -0.090                                 ok            True                  False
   CSX           86.21               29            0.85              0.27         44.63                30.07         0.510          pass              0.422             26.2                           0.373               -1.92             -0.128                                 ok            True                  False
  CHTR           89.36               47            0.25              0.26        147.68               118.46         0.774          pass              0.766             79.6                           0.529              -14.84             -1.355            downtrend_blocked_slope           False                  False
   TXN           80.00                5            2.98              6.20        295.10                67.69         0.674          pass              0.095              9.3                           0.185                9.57              0.924                                 ok           False                  False
 CMCSA           93.33               30            0.41              0.07         25.00                62.25         0.672          pass              0.721             55.0                           0.514               -9.82             -0.979 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-12T11:35:01.042494-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:30:01.054285-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:25:05.158793-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512113501)

</details>
