# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 13:40:03 EDT`
Last processed slot: `manage_1330`

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
  TEAM           87.50               40            1.21              0.74         86.99               115.89         0.696          pass              0.624             51.4                           0.509               23.73              2.551                                 ok            True                  False
   TXN           90.00               10            2.31              4.82        295.70                67.69         0.690          pass              0.432             32.1                           0.595               10.32              0.955                                 ok            True                  False
  FTNT           94.74               38            0.68              0.55        115.20                70.54         0.589          pass              0.805             55.6                           0.644               33.75              3.618                                 ok            True                  False
  GOOG           86.96               23            1.34              3.63        385.22                39.86         0.573          pass              0.409             26.5                           0.486                9.81              1.019                                 ok            True                  False
   XEL           92.86               14            1.15              0.65         80.32                27.14         0.538          pass              0.614             63.4                           0.353                0.24             -0.080                                 ok            True                  False
  MNST           83.33               30            0.71              0.43         86.23                49.64         0.537          pass              0.512             78.6                           0.568               11.15              1.204                                 ok            True                  False
    ZS           82.86               35            0.92              0.96        148.46                59.15         0.535          pass              0.465             56.2                           0.734                8.40              1.279                                 ok            True                  False
  INTU           88.46               26            1.47              4.04        391.56                46.70         0.535          pass              0.441             18.3                           0.282               -3.21             -0.133                                 ok            True                  False
  CDNS           95.83               24            1.85              4.72        362.18                37.36         0.520          pass              0.611             22.0                           0.478                9.88              1.144                                 ok            True                  False
   CSX           87.88               33            0.55              0.17         44.67                30.07         0.504          pass              0.571             52.4                           0.506               -1.63             -0.114                                 ok            True                  False
  WDAY           85.71               35            1.36              1.16        120.92                61.87         0.504          pass              0.451             27.1                           0.334               -1.17              0.051                                 ok            True                  False
 CMCSA           91.30               23            0.66              0.12         24.98                62.25         0.693          pass              0.542             28.3                           0.238              -10.04             -0.990 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512134003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512134003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512134003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512134003)

</details>
