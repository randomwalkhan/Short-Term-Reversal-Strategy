# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:10:06 EDT`
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
  MELI           92.31               26            1.38             16.14       1665.91                61.01         0.619          pass              0.579             27.5                           0.239                3.44              0.346                                 ok            True                  False
  FTNT          100.00               39            0.77              0.80        148.52                71.83         0.566          pass              0.891             80.4                           0.661               15.72              1.530                                 ok            True                   True
  MCHP           96.00               25            0.77              0.52         96.74                44.80         0.539          pass              0.778             74.7                           0.659                5.32              0.397                                 ok            True                  False
  AAPL           93.33               15            1.24              2.73        314.03                17.72         0.527          pass              0.456              4.8                           0.090                4.12              0.379                                 ok            True                  False
  CRWD           85.71               21            1.58              8.49        765.31                51.19         0.520          pass              0.442             54.8                           0.707               22.69              2.228                                 ok            True                  False
  UPRO           92.31               26            1.24              1.31        150.31                28.22         0.508          pass              0.588             34.3                           0.347                9.05              0.897                                 ok            True                  False
  WDAY           82.14               28            2.39              2.49        147.81                75.59         0.507          pass              0.345             39.1                           0.521               12.36              2.097                                 ok            True                  False
  INSM           76.32               38            0.73              0.53        103.50               108.46         0.753          pass              0.453             63.8                           0.298               -4.13             -0.417 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.53              5.58        141.76               159.87         0.747          pass              0.118             14.3                           0.374              -22.29             -2.899            downtrend_blocked_slope           False                  False
  INTU           73.91               23            2.74              6.17        319.49               101.75         0.644          pass              0.227             25.2                           0.640              -21.61             -1.269            downtrend_blocked_slope           False                  False
  NXPI           97.30               37            0.25              0.57        323.37                50.93         0.560          pass              0.888             83.9                           0.554                9.69              0.704                                 ok           False                  False
  PAYX          100.00                5            2.61              1.84        100.00                33.97         0.559          pass              0.506             16.6                           0.307                3.89              0.625                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:40:06.216111-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:25:05.972496-04:00 early_entry_1025 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603111006)

</details>
