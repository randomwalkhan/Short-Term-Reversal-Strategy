# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:05:04 EDT`
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
  TEAM           87.50               40            1.16              0.71         87.01               115.89         0.698          pass              0.630             53.4                           0.372               23.79              2.553                                 ok            True                  False
  FTNT           94.12               34            0.83              0.67        115.15                70.54         0.603          pass              0.736             46.3                           0.375               33.56              3.612                                 ok            True                  False
  GOOG           88.57               35            0.64              1.74        386.03                39.86         0.550          pass              0.592             47.1                           0.470               10.59              1.051                                 ok            True                  False
   XEL           93.33               15            1.10              0.62         80.33                27.14         0.536          pass              0.637             65.0                           0.441                0.29             -0.077                                 ok            True                  False
    ZS           82.86               35            1.03              1.07        148.41                59.15         0.532          pass              0.426             43.3                           0.405                8.28              1.274                                 ok            True                  False
  CDNS           95.83               24            1.85              4.72        362.18                37.36         0.525          pass              0.560              4.7                           0.161                9.88              1.144                                 ok            True                  False
   CSX           86.21               29            0.79              0.25         44.63                30.07         0.512          pass              0.437             31.1                           0.460               -1.87             -0.125                                 ok            True                  False
  CHTR           90.24               41            0.49              0.51        147.57               118.46         0.790          pass              0.730             59.2                           0.295              -15.05             -1.366            downtrend_blocked_slope           False                  False
   TXN           88.89                9            2.39              4.98        295.63                67.69         0.696          pass              0.355             16.2                           0.317               10.24              0.951                                 ok           False                  False
 CMCSA           92.31               26            0.51              0.09         24.99                62.25         0.687          pass              0.637             44.5                           0.327               -9.90             -0.983 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.24               41            0.70              0.50        102.32                84.99         0.651          pass              0.667             43.0                           0.223              -16.58             -2.101            downtrend_blocked_slope           False                  False
  NXPI           66.67                3            4.03              8.62        302.29                87.21         0.632          pass              0.210             48.8                           0.317               27.47              1.308                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512110504)

</details>
