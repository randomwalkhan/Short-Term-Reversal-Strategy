# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:30:06 EDT`
Last processed slot: `manage_1130`

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
  MELI           92.31               26            1.48             17.35       1665.39                61.01         0.612          pass              0.562             22.0                           0.186                3.33              0.341                                 ok            True                  False
  MCHP           96.00               25            0.96              0.65         96.68                44.80         0.526          pass              0.758             68.5                           0.569                5.12              0.388                                 ok            True                  False
  AAPL           94.12               17            1.11              2.46        314.15                17.72         0.519          pass              0.560             28.2                           0.365                4.25              0.385                                 ok            True                  False
  CRWD           87.50               24            1.29              6.97        765.96                51.19         0.519          pass              0.534             62.9                           0.715               23.04              2.241                                 ok            True                  False
  WDAY           84.00               25            2.57              2.67        147.73                75.59         0.518          pass              0.362             34.6                           0.543               12.15              2.088                                 ok            True                  False
  SNPS          100.00               10            2.88             10.24        503.96                42.98         0.511          pass              0.473              7.4                           0.091               -0.03             -0.273                                 ok            True                  False
   ADP          100.00               13            2.31              3.73        229.58                34.09         0.510          pass              0.512             13.8                           0.194                2.45              0.421                                 ok            True                  False
  UPRO           92.31               26            1.29              1.36        150.29                28.22         0.505          pass              0.580             31.6                           0.333                8.99              0.895                                 ok            True                  False
  INSM           79.07               43            0.30              0.22        103.64               108.46         0.752          pass              0.531             85.2                           0.561               -3.71             -0.397 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.64              5.69        141.71               159.87         0.741          pass              0.112             12.5                           0.395              -22.39             -2.904            downtrend_blocked_slope           False                  False
  INTU           73.68               19            2.98              6.71        319.26               101.75         0.654          pass              0.181             18.7                           0.397              -21.81             -1.280            downtrend_blocked_slope           False                  False
   TXN          100.00               31            0.10              0.22        308.02                42.90         0.568          pass              0.882             95.0                           0.719                1.82              0.026                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603113006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603113006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603113006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603113006)

</details>
