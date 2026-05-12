# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:00:02 EDT`
Last processed slot: `manage_1100`

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
  TEAM           86.84               38            1.23              0.75         86.99               115.89         0.704          pass              0.592             50.9                           0.372               23.71              2.550                                 ok            True                  False
   TXN           91.67               12            1.99              4.15        295.98                67.69         0.702          pass              0.485             30.1                           0.436               10.68              0.970                                 ok            True                  False
  GOOG           89.47               38            0.52              1.41        386.16                39.86         0.540          pass              0.664             56.9                           0.619               10.72              1.056                                 ok            True                  False
    ZS           82.86               35            0.93              0.97        148.46                59.15         0.538          pass              0.443             48.9                           0.479                8.39              1.278                                 ok            True                  False
   XEL           94.44               18            0.99              0.56         80.36                27.14         0.526          pass              0.697             68.5                           0.564                0.40             -0.072                                 ok            True                  False
  CDNS           96.15               26            1.70              4.33        362.34                37.36         0.521          pass              0.597             12.6                           0.239               10.05              1.151                                 ok            True                  False
   CSX           86.21               29            0.83              0.26         44.63                30.07         0.511          pass              0.428             28.2                           0.425               -1.90             -0.127                                 ok            True                  False
  CHTR           89.74               39            0.59              0.61        147.53               118.46         0.793          pass              0.687             51.4                           0.285              -15.13             -1.370            downtrend_blocked_slope           False                  False
 CMCSA           92.31               26            0.60              0.11         24.98                62.25         0.682          pass              0.607             34.8                           0.256               -9.99             -0.987 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.24               41            0.75              0.54        102.31                84.99         0.648          pass              0.655             39.0                           0.227              -16.62             -2.103            downtrend_blocked_slope           False                  False
  NXPI           75.00                4            3.91              8.37        302.40                87.21         0.644          pass              0.215             50.3                           0.331               27.62              1.314                                 ok           False                  False
  FTNT           95.35               43            0.47              0.38        115.28                70.54         0.573          pass              0.866             69.7                           0.635               34.04              3.628                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:20:02.261414-04:00 early_entry_1020 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512110002)

</details>
