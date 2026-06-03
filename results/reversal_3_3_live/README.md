# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:45:06 EDT`
Last processed slot: `early_entry_1145`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MELI           92.00               25            1.66             19.48       1664.48                61.01         0.607          pass              0.518             12.5                           0.167                3.14              0.333                  ok            True                  False
  FTNT          100.00               31            1.21              1.26        148.32                71.83         0.593          pass              0.807             69.3                           0.584               15.21              1.510                  ok            True                   True
  NXPI           96.88               32            0.59              1.33        323.05                50.93         0.571          pass              0.792             62.7                           0.376                9.32              0.688                  ok            True                  False
  WDAY           84.21               19            2.98              3.10        147.55                75.59         0.533          pass              0.298             24.1                           0.263               11.68              2.069                  ok            True                  False
  MCHP          100.00               23            1.19              0.81         96.61                44.80         0.529          pass              0.723             61.0                           0.388                4.88              0.377                  ok            True                  False
  AAPL           93.75               16            1.17              2.58        314.09                17.72         0.522          pass              0.532             24.5                           0.389                4.19              0.382                  ok            True                  False
   ADP          100.00               11            2.36              3.81        229.55                34.09         0.521          pass              0.494             11.9                           0.171                2.40              0.419                  ok            True                  False
  UPRO           95.00               20            1.77              1.87        150.07                28.22         0.519          pass              0.537              6.2                           0.141                8.46              0.873                  ok            True                  False
  DXCM           80.00               20            1.80              0.92         73.05                46.47         0.509          pass              0.154             12.0                           0.110                7.74              0.595                  ok            True                  False
  CRWD           80.00               15            2.32             12.46        763.61                51.19         0.507          pass              0.185             33.6                           0.335               21.77              2.193                  ok            True                  False
  SNPS          100.00               10            2.95             10.49        503.85                42.98         0.503          pass              0.488             12.6                           0.179               -0.10             -0.276                  ok            True                  False
   HON           83.33               24            0.77              1.27        234.69                23.49         0.503          pass              0.304             23.9                           0.234                7.49              0.849                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:45:06.164113-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603114506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603114506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603114506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603114506)

</details>
