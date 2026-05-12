# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 12:30:04 EDT`
Last processed slot: `manage_1230`

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
  TEAM           86.49               37            1.54              0.94         86.91               115.89         0.694          pass              0.537             38.3                           0.343               23.32              2.536                                 ok            True                  False
  FTNT           93.94               33            1.08              0.87        115.07                70.54         0.595          pass              0.674             29.8                           0.359               33.21              3.600                                 ok            True                  False
  GOOG           86.21               29            0.96              2.61        385.65                39.86         0.565          pass              0.410             20.5                           0.171               10.23              1.036                                 ok            True                  False
   XEL           92.31               13            1.17              0.66         80.32                27.14         0.542          pass              0.591             62.8                           0.501                0.22             -0.080                                 ok            True                  False
    ZS           83.33               30            1.43              1.49        148.23                59.15         0.540          pass              0.340             21.1                           0.253                7.84              1.255                                 ok            True                  False
  CDNS           96.00               25            1.81              4.61        362.22                37.36         0.518          pass              0.612             20.2                           0.391                9.93              1.146                                 ok            True                  False
  INTU           88.57               35            0.93              2.55        392.20                46.70         0.513          pass              0.588             47.2                           0.417               -2.68             -0.108                                 ok            True                  False
   CSX           86.21               29            0.85              0.27         44.63                30.07         0.510          pass              0.422             26.2                           0.289               -1.92             -0.128                                 ok            True                  False
  WDAY           88.10               42            0.80              0.68        121.13                61.87         0.509          pass              0.526             19.6                           0.229               -0.61              0.077                                 ok            True                  False
 CMCSA           94.12               34            0.18              0.03         25.02                62.25         0.664          pass              0.844             80.4                           0.735               -9.61             -0.968 downtrend_blocked_slope_and_streak           False                  False
   TXN           75.00                4            3.22              6.70        294.89                67.69         0.660          pass              0.078              3.9                           0.185                9.30              0.913                                 ok           False                  False
  SHOP           86.67               30            1.82              1.31        101.98                84.99         0.639          pass              0.381              1.8                           0.091              -17.51             -2.152            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-12T12:00:02.098694-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:45:01.039711-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:40:05.033124-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:35:01.042494-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:30:01.054285-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:25:05.158793-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512123004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512123004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512123004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512123004)

</details>
