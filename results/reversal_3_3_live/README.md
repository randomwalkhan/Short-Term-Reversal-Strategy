# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:05:06 EDT`
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
  MELI           92.31               26            1.55             18.19       1665.03                61.01         0.607          pass              0.550             18.2                           0.222                3.26              0.338                                 ok            True                  False
  NXPI           96.77               31            0.77              1.75        322.87                50.93         0.566          pass              0.750             51.0                           0.314                9.12              0.680                                 ok            True                  False
  FTNT          100.00               40            0.74              0.77        148.53                71.83         0.562          pass              0.900             81.3                           0.689               15.77              1.532                                 ok            True                   True
   TXN          100.00               27            0.71              1.53        307.46                42.90         0.555          pass              0.765             65.5                           0.388                1.20             -0.002                                 ok            True                  False
  MCHP           96.00               25            0.86              0.58         96.71                44.80         0.533          pass              0.768             71.7                           0.622                5.23              0.392                                 ok            True                  False
  WDAY           81.82               22            2.67              2.79        147.69                75.59         0.530          pass              0.277             31.8                           0.449               12.03              2.083                                 ok            True                  False
  AAPL           93.33               15            1.26              2.79        314.01                17.72         0.526          pass              0.450              2.8                           0.160                4.10              0.378                                 ok            True                  False
  CRWD           86.36               22            1.49              8.04        765.50                51.19         0.519          pass              0.473             57.2                           0.716               22.79              2.231                                 ok            True                  False
  CDNS           93.33               15            2.29              6.69        413.52                43.85         0.512          pass              0.551             36.9                           0.403               20.32              1.845                                 ok            True                  False
  UPRO           92.00               25            1.39              1.47        150.24                28.22         0.505          pass              0.550             26.4                           0.309                8.88              0.890                                 ok            True                  False
  INSM           78.57               42            0.50              0.36        103.58               108.46         0.746          pass              0.501             75.5                           0.343               -3.91             -0.406 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.63              5.68        141.71               159.87         0.741          pass              0.112             12.7                           0.361              -22.38             -2.904            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:40:06.216111-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:25:05.972496-04:00 early_entry_1025 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00 early_entry_1020 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603110506)

</details>
