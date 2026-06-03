# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:00:05 EDT`
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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   TXN     option         option TXN260717C00310000      8          2026-06-03         2026-06-03         22.0        19.8 -1760.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.29               35            0.91             10.60       1668.29                61.01         0.591          pass              0.764             52.4                           0.556                3.94              0.368                                 ok            True                  False
  NXPI           96.77               31            0.77              1.75        322.87                50.93         0.566          pass              0.749             50.9                           0.334                9.12              0.680                                 ok            True                  False
  FTNT          100.00               42            0.61              0.64        148.59                71.83         0.556          pass              0.909             84.5                           0.699               15.91              1.538                                 ok            True                   True
  CDNS          100.00               11            2.48              7.21        413.30                43.85         0.536          pass              0.556             31.9                           0.289               20.10              1.836                                 ok            True                  False
  CRWD           82.35               17            1.75              9.43        764.91                51.19         0.533          pass              0.312             49.8                           0.642               22.47              2.220                                 ok            True                  False
  MCHP          100.00               24            1.08              0.73         96.65                44.80         0.529          pass              0.739             64.4                           0.579                4.99              0.382                                 ok            True                  False
  AAPL           93.75               16            1.18              2.60        314.08                17.72         0.524          pass              0.484              8.4                           0.165                4.18              0.382                                 ok            True                  False
  UPRO           92.31               26            1.23              1.30        150.31                28.22         0.508          pass              0.589             34.6                           0.346                9.05              0.897                                 ok            True                  False
  WDAY           82.14               28            2.40              2.50        147.81                75.59         0.506          pass              0.344             38.9                           0.475               12.35              2.096                                 ok            True                  False
  INSM           79.07               43            0.29              0.21        103.64               108.46         0.752          pass              0.532             85.5                           0.382               -3.71             -0.397 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.77              5.82        141.65               159.87         0.734          pass              0.105             10.5                           0.318              -22.49             -2.910            downtrend_blocked_slope           False                  False
  INTU           73.68               19            2.98              6.71        319.26               101.75         0.654          pass              0.181             18.7                           0.441              -21.81             -1.280            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                         detail
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:40:06.216111-04:00 early_entry_1040 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:25:05.972496-04:00 early_entry_1025 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00 early_entry_1020 entry_skipped                                                                                                                                                {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "TXN260717C00310000", "fill_price": 19.8, "pnl": -1760.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TXN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603110005)

</details>
