# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:15:06 EDT`
Last processed slot: `early_entry_1115`

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
  MELI           92.31               26            1.54             18.06       1665.09                61.01         0.608          pass              0.552             18.8                           0.189                3.27              0.338                                 ok            True                  False
  FTNT          100.00               40            0.73              0.76        148.54                71.83         0.562          pass              0.901             81.6                           0.657               15.78              1.532                                 ok            True                   True
  MCHP           96.15               26            0.71              0.48         96.75                44.80         0.536          pass              0.790             76.6                           0.685                5.38              0.399                                 ok            True                  False
  AAPL           90.91               11            1.48              3.26        313.80                17.72         0.535          pass              0.360              3.1                           0.123                3.87              0.368                                 ok            True                  False
  CDNS          100.00               11            2.52              7.36        413.24                43.85         0.533          pass              0.552             30.6                           0.260               20.04              1.834                                 ok            True                  False
  WDAY           81.82               22            2.71              2.82        147.67                75.59         0.527          pass              0.274             30.9                           0.471               11.99              2.082                                 ok            True                  False
  CRWD           85.71               21            1.58              8.49        765.31                51.19         0.520          pass              0.442             54.8                           0.715               22.69              2.228                                 ok            True                  False
   ADP          100.00               15            2.12              3.42        229.71                34.09         0.508          pass              0.547             20.9                           0.332                2.65              0.430                                 ok            True                  False
  UPRO           92.00               25            1.41              1.49        150.23                28.22         0.503          pass              0.545             25.0                           0.283                8.85              0.889                                 ok            True                  False
  INSM           79.07               43            0.29              0.21        103.64               108.46         0.752          pass              0.532             85.7                           0.415               -3.71             -0.397 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.62              5.67        141.72               159.87         0.742          pass              0.113             13.0                           0.375              -22.37             -2.903            downtrend_blocked_slope           False                  False
  INTU           73.68               19            2.96              6.66        319.28               101.75         0.656          pass              0.183             19.3                           0.470              -21.79             -1.279            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:40:06.216111-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603111506)

</details>
