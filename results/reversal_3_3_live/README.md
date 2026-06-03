# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 12:30:05 EDT`
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
  MELI           92.31               26            1.65             19.26       1664.57                61.01         0.601          pass              0.535             13.4                           0.252                3.16              0.333                                 ok            True                  False
  FTNT          100.00               31            1.22              1.27        148.31                71.83         0.592          pass              0.806             68.9                           0.591               15.20              1.510                                 ok            True                   True
  NXPI           96.88               32            0.71              1.62        322.93                50.93         0.563          pass              0.767             54.6                           0.369                9.19              0.682                                 ok            True                  False
  MCHP           96.00               25            0.75              0.51         96.74                44.80         0.540          pass              0.780             75.3                           0.661                5.34              0.397                                 ok            True                  False
  AAPL           90.91               11            1.74              3.85        313.55                17.72         0.515          pass              0.359              3.3                           0.159                3.59              0.356                                 ok            True                  False
   ROP           85.71               14            2.03              4.78        334.45                35.89         0.513          pass              0.317             28.9                           0.599                0.23              0.313                                 ok            True                  False
   CEG           80.95               21            2.29              4.37        270.78                55.62         0.510          pass              0.178              9.5                           0.194                2.20             -0.300                                 ok            True                  False
  UPRO           94.74               19            2.02              2.13        149.96                28.22         0.507          pass              0.529              8.4                           0.232                8.19              0.861                                 ok            True                  False
  CRWD           82.35               17            2.17             11.68        763.94                51.19         0.505          pass              0.273             37.8                           0.375               21.95              2.200                                 ok            True                  False
   ADP           93.75               16            1.96              3.17        229.82                34.09         0.504          pass              0.537             26.6                           0.608                2.81              0.437                                 ok            True                  False
  WDAY           83.87               31            2.17              2.26        147.91                75.59         0.503          pass              0.428             44.7                           0.647               12.61              2.107                                 ok            True                  False
  INSM           79.07               43            0.29              0.21        103.64               108.46         0.752          pass              0.532             85.7                           0.529               -3.71             -0.397 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T12:00:06.118457-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603123005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603123005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603123005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603123005)

</details>
