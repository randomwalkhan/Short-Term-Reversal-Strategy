# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:45:04 EDT`
Last processed slot: `early_entry_1045`

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
  TEAM           87.50               40            1.01              0.62         87.05               115.89         0.706          pass              0.649             59.6                           0.469               23.99              2.560                                 ok            True                  False
   TXN           91.67               12            2.01              4.19        295.97                67.69         0.702          pass              0.483             29.5                           0.368               10.67              0.969                                 ok            True                  False
  GOOG           86.21               29            0.88              2.39        385.75                39.86         0.569          pass              0.431             27.3                           0.372               10.32              1.040                                 ok            True                  False
    ZS           81.58               38            0.71              0.73        148.56                59.15         0.531          pass              0.465             61.1                           0.647                8.64              1.289                                 ok            True                  False
   XEL           94.12               17            1.03              0.58         80.35                27.14         0.529          pass              0.678             67.3                           0.585                0.36             -0.074                                 ok            True                  False
  CDNS           96.43               28            1.48              3.78        362.58                37.36         0.521          pass              0.643             23.7                           0.299               10.29              1.161                                 ok            True                  False
   CSX           86.21               29            0.79              0.25         44.63                30.07         0.512          pass              0.437             31.1                           0.422               -1.87             -0.125                                 ok            True                  False
 CMCSA           93.33               30            0.38              0.07         25.00                62.25         0.674          pass              0.732             58.7                           0.458               -9.79             -0.977 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.70               43            0.32              0.23        102.44                84.99         0.660          pass              0.773             73.9                           0.467              -16.26             -2.084            downtrend_blocked_slope           False                  False
  NXPI           63.64               11            3.36              7.19        302.91                87.21         0.617          pass              0.240             57.4                           0.389               28.36              1.340                                 ok           False                  False
  FTNT           95.92               49            0.01              0.01        115.44                70.54         0.565          pass              0.955             99.4                           0.794               34.66              3.649                                 ok           False                  False
   AEP           95.83               24            0.10              0.09        130.66                20.54         0.560          pass              0.818             89.7                           0.709               -3.00             -0.425            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:20:02.261414-04:00 early_entry_1020 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:15:01.147250-04:00 early_entry_1015 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:10:05.279382-04:00 early_entry_1010 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:05:06.121865-04:00 early_entry_1005 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512104504)

</details>
