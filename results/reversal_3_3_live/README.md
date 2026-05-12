# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 13:45:05 EDT`
Last processed slot: `manual`

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
  TEAM           86.49               37            1.40              0.85         86.94               115.89         0.701          pass              0.555             44.0                           0.480               23.50              2.542                                 ok            True                  False
   TXN           90.00               10            2.32              4.84        295.69                67.69         0.690          pass              0.431             31.8                           0.585               10.31              0.954                                 ok            True                  False
  FTNT           94.74               38            0.68              0.55        115.20                70.54         0.589          pass              0.805             55.6                           0.672               33.75              3.618                                 ok            True                  False
  GOOG           86.96               23            1.34              3.63        385.22                39.86         0.573          pass              0.409             26.5                           0.514                9.81              1.019                                 ok            True                  False
  MNST           80.77               26            0.86              0.52         86.19                49.64         0.548          pass              0.404             74.1                           0.481               10.99              1.197                                 ok            True                  False
   XEL           93.33               15            1.12              0.63         80.33                27.14         0.535          pass              0.636             64.6                           0.388                0.28             -0.078                                 ok            True                  False
  INTU           88.89               27            1.38              3.79        391.66                46.70         0.535          pass              0.474             23.2                           0.381               -3.12             -0.129                                 ok            True                  False
    ZS           82.86               35            0.94              0.98        148.45                59.15         0.534          pass              0.462             55.2                           0.749                8.38              1.278                                 ok            True                  False
  CDNS           95.65               23            1.87              4.77        362.16                37.36         0.525          pass              0.602             21.1                           0.494                9.86              1.143                                 ok            True                  False
  WDAY           86.84               38            1.12              0.95        121.01                61.87         0.501          pass              0.540             40.1                           0.453               -0.92              0.062                                 ok            True                  False
 CMCSA           92.86               28            0.46              0.08         25.00                62.25         0.680          pass              0.681             50.0                           0.336               -9.86             -0.981 downtrend_blocked_slope_and_streak           False                  False
  NXPI           66.67                3            4.00              8.58        302.31                87.21         0.633          pass              0.211             49.1                           0.509               27.50              1.309                                 ok           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512134505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512134505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512134505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512134505)

</details>
