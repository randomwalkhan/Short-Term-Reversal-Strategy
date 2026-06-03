# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 14:50:06 EDT`
Last processed slot: `entry_1500`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           86.67               15            2.33             27.28       1661.14                61.01         0.620            pass              0.273              0.0                           0.175                2.45              0.302                                 ok            True                  False
  FTNT          100.00               25            1.58              1.65        148.15                71.83         0.610            pass              0.741             59.9                           0.507               14.78              1.493                                 ok            True                  False
   WBD           95.45               22            0.53              0.10         27.14                 9.03         0.516            pass              0.576             14.7                           0.335               -0.20             -0.026                                 ok            True                  False
  AAPL           90.91               11            1.75              3.86        313.55                17.72         0.512            pass              0.388             13.2                           0.372                3.59              0.356                                 ok            True                  False
   ROP           85.71               14            2.09              4.93        334.39                35.89         0.509            pass              0.310             26.6                           0.425                0.17              0.310                                 ok            True                  False
  UPRO           95.65               23            1.54              1.63        150.17                28.22         0.508            pass              0.640             34.2                           0.472                8.71              0.883                                 ok            True                  False
  CRWD           80.00               15            2.31             12.43        763.62                51.19         0.507            pass              0.185             33.8                           0.359               21.77              2.194                                 ok            True                  False
   CEG           81.82               22            2.24              4.28        270.82                55.62         0.505            pass              0.232             17.7                           0.458                2.25             -0.298                                 ok            True                  False
  WDAY           84.38               32            2.11              2.20        147.94                75.59         0.500 below_threshold              0.452             46.1                           0.494               12.68              2.109                                 ok            True                  False
  INSM           80.85               47            0.01              0.01        103.73               108.46         0.748            pass              0.596             99.5                           0.680               -3.44             -0.384 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            6.19              6.24        141.47               159.87         0.701            pass              0.118             16.0                           0.439              -22.84             -2.930            downtrend_blocked_slope           False                  False
  INTU           73.68               19            3.13              7.06        319.12               101.75         0.644            pass              0.168             14.5                           0.335              -21.93             -1.287            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T14:50:06.341439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
2026-06-03T12:00:06.118457-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603145006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603145006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603145006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603145006)

</details>
