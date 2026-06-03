# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:50:05 EDT`
Last processed slot: `manage_1200`

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
  FTNT          100.00               18            1.80              1.88        148.06                71.83         0.643          pass              0.680             54.3                           0.372               14.53              1.483                                 ok            True                  False
  MELI           92.31               26            1.53             17.91       1665.16                61.01         0.609          pass              0.554             19.5                           0.252                3.28              0.339                                 ok            True                  False
  MCHP           96.00               25            0.90              0.61         96.70                44.80         0.530          pass              0.765             70.5                           0.542                5.19              0.391                                 ok            True                  False
  AAPL           93.33               15            1.24              2.74        314.03                17.72         0.524          pass              0.501             20.0                           0.329                4.12              0.379                                 ok            True                  False
  WDAY           84.21               19            3.15              3.29        147.47                75.59         0.521          pass              0.283             19.6                           0.223               11.48              2.061                                 ok            True                  False
   ADP          100.00               11            2.47              4.00        229.47                34.09         0.513          pass              0.481              7.5                           0.159                2.28              0.414                                 ok            True                  False
  UPRO           95.65               23            1.60              1.69        150.15                28.22         0.510          pass              0.583             15.2                           0.199                8.65              0.881                                 ok            True                  False
  SNPS          100.00               10            2.87             10.22        503.97                42.98         0.508          pass              0.496             14.9                           0.223               -0.02             -0.272                                 ok            True                  False
  INSM           80.00               45            0.13              0.10        103.69               108.46         0.751          pass              0.555             93.3                           0.620               -3.56             -0.390 downtrend_blocked_slope_and_streak           False                  False
    MU           82.86               35            0.33              2.44       1063.06               101.17         0.724          pass              0.575             86.4                           0.464               51.79              4.588                                 ok           False                  False
    ZS           60.00                5            6.17              6.23        141.48               159.87         0.711          pass              0.084              4.3                           0.133              -22.82             -2.930            downtrend_blocked_slope           False                  False
  INTU           73.68               19            3.15              7.11        319.09               101.75         0.643          pass              0.166             13.9                           0.244              -21.95             -1.288            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:50:05.337681-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603115005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603115005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603115005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603115005)

</details>
