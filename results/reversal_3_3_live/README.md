# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:10:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           95.00               20            1.34              0.83         88.74                49.60         0.630          pass              0.576             15.6                           0.189               -0.71              0.179                                 ok            True                  False
  MELI           87.50               16            2.31             27.99       1718.99                60.28         0.616          pass              0.366             21.6                           0.236                6.63              0.698                                 ok            True                  False
  AMGN           90.00               10            1.32              3.03        327.83                20.27         0.555          pass              0.432             36.5                           0.334                0.12              0.017                                 ok            True                  False
   CSX           85.71               21            0.76              0.25         45.75                23.46         0.515          pass              0.463             61.8                           0.336               -1.19             -0.065                                 ok            True                  False
  CDNS           89.47               19            1.97              5.70        411.72                44.19         0.509          pass              0.477             37.9                           0.619               17.35              1.723                                 ok            True                  False
  AMZN           85.71               14            1.75              3.21        259.89                24.44         0.502          pass              0.330             33.5                           0.556               -3.09             -0.003                                 ok            True                  False
  INSM           50.00               12            3.90              2.89        104.79               110.78         0.678          pass              0.155             24.5                           0.497               -4.90             -0.319            downtrend_blocked_slope           False                  False
  FTNT          100.00                8            2.90              2.98        145.86                71.69         0.661          pass              0.564             32.6                           0.314               12.95              1.194                                 ok           False                  False
   WMT           84.21               19            1.10              0.88        114.22                32.65         0.562          pass              0.268             13.1                           0.224              -15.00             -1.697 downtrend_blocked_slope_and_streak           False                  False
  SHOP           72.73               11            4.17              3.63        122.57                84.68         0.553          pass              0.125             20.9                           0.264               16.16              1.964                                 ok           False                  False
    ZS           66.67                3            8.58              9.35        151.70               157.27         0.548          pass              0.085              9.9                           0.201              -18.51             -2.797            downtrend_blocked_slope           False                  False
   HON           76.92               13            1.13              1.88        235.74                24.20         0.542          pass              0.124             16.5                           0.216                7.66              0.979                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-02T10:10:06.260122-04:00 early_entry_1010  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602101006)

</details>
