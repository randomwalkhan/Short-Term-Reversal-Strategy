# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 15:25:06 EDT`
Last processed slot: `manage_1530`

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
  MELI           92.86               14            2.46             28.80       1660.49                61.01         0.622          pass              0.447              5.0                           0.226                2.31              0.296                                 ok            True                  False
  FTNT          100.00               27            1.43              1.49        148.22                71.83         0.606          pass              0.765             63.7                           0.583               14.96              1.500                                 ok            True                  False
  NXPI           96.67               30            1.03              2.33        322.62                50.93         0.555          pass              0.692             34.5                           0.203                8.84              0.668                                 ok            True                  False
  CDNS          100.00               11            2.52              7.35        413.24                43.85         0.532          pass              0.555             31.7                           0.509               20.04              1.834                                 ok            True                  False
  MCHP           96.30               27            0.69              0.47         96.76                44.80         0.531          pass              0.799             77.5                           0.481                5.41              0.400                                 ok            True                  False
  AAPL           90.91               11            1.61              3.56        313.67                17.72         0.521          pass              0.409             19.8                           0.468                3.73              0.362                                 ok            True                  False
   ROP           85.71               14            1.98              4.65        334.51                35.89         0.517          pass              0.323             30.7                           0.476                0.29              0.316                                 ok            True                  False
  CRWD           86.36               22            1.54              8.32        765.39                51.19         0.515          pass              0.468             55.7                           0.747               22.73              2.229                                 ok            True                  False
  WDAY           84.38               32            1.93              2.02        148.02                75.59         0.512          pass              0.467             50.7                           0.623               12.88              2.118                                 ok            True                  False
  UPRO           95.00               20            1.91              2.02        150.01                28.22         0.505          pass              0.573             18.6                           0.201                8.31              0.866                                 ok            True                  False
   CEG           80.95               21            2.36              4.51        270.72                55.62         0.502          pass              0.189             13.2                           0.315                2.13             -0.303                                 ok            True                  False
  INSM           76.32               38            0.90              0.65        103.45               108.46         0.744          pass              0.428             55.7                           0.366               -4.29             -0.424 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T15:10:03.976623-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:05:05.758809-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:00:06.248089-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:55:06.012322-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:50:06.341439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
2026-06-03T12:00:06.118457-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603152506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603152506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603152506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603152506)

</details>
