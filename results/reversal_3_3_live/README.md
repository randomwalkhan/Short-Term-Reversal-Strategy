# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 14:25:05 EDT`
Last processed slot: `manage_1430`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           91.67               12            1.90              3.97        296.06                67.69         0.701            pass              0.527             44.0                           0.698               10.78              0.974                                 ok            True                  False
  TEAM           87.50               40            1.21              0.74         86.99               115.89         0.696            pass              0.624             51.6                           0.458               23.73              2.551                                 ok            True                  False
  FTNT           93.94               33            0.85              0.69        115.15                70.54         0.607            pass              0.721             44.9                           0.360               33.53              3.611                                 ok            True                  False
  GOOG           84.00               25            1.15              3.11        385.44                39.86         0.567            pass              0.374             37.0                           0.532               10.02              1.028                                 ok            True                  False
  MNST           80.00               25            0.88              0.53         86.18                49.64         0.551            pass              0.375             73.4                           0.536               10.96              1.196                                 ok            True                  False
  INTU           88.00               25            1.53              4.21        391.49                46.70         0.537            pass              0.412             14.8                           0.217               -3.27             -0.135                                 ok            True                  False
    ZS           82.86               35            0.99              1.03        148.43                59.15         0.531            pass              0.455             53.0                           0.527                8.33              1.276                                 ok            True                  False
  CDNS           95.65               23            1.87              4.76        362.16                37.36         0.525            pass              0.603             21.3                           0.404                9.86              1.144                                 ok            True                  False
   XEL           95.65               23            0.81              0.46         80.40                27.14         0.508            pass              0.761             74.4                           0.673                0.59             -0.064                                 ok            True                  False
  WDAY           84.85               33            1.62              1.38        120.83                61.87         0.500 below_threshold              0.372             13.2                           0.199               -1.43              0.039                                 ok            True                  False
 CMCSA           93.33               30            0.38              0.07         25.00                62.25         0.674            pass              0.732             58.7                           0.420               -9.79             -0.977 downtrend_blocked_slope_and_streak           False                  False
  NXPI           80.00                5            3.73              7.99        302.57                87.21         0.655            pass              0.223             52.6                           0.636               27.86              1.322                                 ok           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512142505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512142505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512142505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512142505)

</details>
