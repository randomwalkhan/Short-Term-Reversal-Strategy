# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 15:45:06 EDT`
Last processed slot: `manual`

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
  CSCO           96.15               26            0.69              0.62        127.74                53.71         0.617          pass              0.794             75.2                           0.397               10.18              0.924                                 ok            True                  False
  MELI           87.50               16            2.30             26.95       1661.28                61.01         0.613          pass              0.335             11.1                           0.361                2.47              0.303                                 ok            True                  False
  FTNT          100.00               25            1.60              1.66        148.15                71.83         0.609          pass              0.739             59.5                           0.531               14.76              1.492                                 ok            True                  False
   WBD           94.12               17            0.59              0.11         27.13                 9.03         0.546          pass              0.495              5.9                           0.236               -0.26             -0.029                                 ok            True                  False
  AAPL           92.31               13            1.36              3.00        313.92                17.72         0.524          pass              0.498             32.6                           0.560                4.00              0.374                                 ok            True                  False
  CDNS           93.33               15            2.18              6.35        413.67                43.85         0.519          pass              0.564             41.0                           0.688               20.47              1.850                                 ok            True                  False
  UPRO           95.00               20            1.74              1.84        150.08                28.22         0.516          pass              0.596             25.9                           0.365                8.50              0.874                                 ok            True                  False
   ROP           85.71               14            2.05              4.84        334.43                35.89         0.511          pass              0.314             28.0                           0.486                0.21              0.312                                 ok            True                  False
  SNPS           93.33               15            2.20              7.82        505.00                42.98         0.510          pass              0.545             34.9                           0.410                0.67             -0.241                                 ok            True                  False
  WDAY           84.38               32            1.98              2.06        148.00                75.59         0.509          pass              0.463             49.6                           0.592               12.83              2.116                                 ok            True                  False
   CEG           81.82               22            2.20              4.20        270.85                55.62         0.507          pass              0.236             19.1                           0.382                2.29             -0.296                                 ok            True                  False
  INSM           79.07               43            0.39              0.28        103.61               108.46         0.747          pass              0.517             80.7                           0.631               -3.80             -0.401 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603154506)

</details>
