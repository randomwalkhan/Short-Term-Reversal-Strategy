# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 09:50:01 EDT`
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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           88.57               35            0.50              1.17        332.17                92.16         0.658            pass              0.610             49.7                           0.251               12.50              1.234                                 ok            True                  False
  SOXL           84.62               26            2.08              3.28        224.38               148.29         0.658            pass              0.500             68.3                           0.360               28.16              2.202                                 ok            True                  False
  INTC           94.12               17            3.71              3.21        122.15                91.80         0.578            pass              0.568             29.1                           0.256               -1.38              0.366                                 ok            True                  False
  ASML           89.66               29            1.46             16.62       1624.91                54.27         0.538            pass              0.534             32.2                           0.258                5.74              0.603                                 ok            True                  False
  LRCX           84.85               33            0.72              1.64        321.98                57.65         0.516            pass              0.500             55.1                           0.329               10.75              0.995                                 ok            True                  False
  MSFT           86.36               22            1.16              3.37        414.59                23.55         0.500 below_threshold              0.376             25.3                           0.311                1.06              0.204                                 ok            True                  False
   TRI           84.62               26            0.12              0.07         83.69                55.63         0.651            pass              0.570             91.8                           0.590               -3.46              0.221                                 ok           False                  False
  FTNT          100.00                6            4.06              3.81        132.33                66.88         0.586            pass              0.554             31.7                           0.297               12.87              1.400                                 ok           False                  False
   AEP           86.67               30            0.06              0.05        130.88                25.21         0.552            pass              0.651             95.0                           0.732               -0.85              0.179                                 ok           False                  False
  SBUX           96.97               33            0.17              0.12        101.37                33.52         0.543            pass              0.868             86.8                           0.551               -4.44             -0.461 downtrend_blocked_slope_and_streak           False                  False
  NVDA           85.71               21            1.72              2.58        213.75                40.94         0.516            pass              0.311             11.3                           0.121               -4.35             -0.673 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.44               36            0.21              0.21        145.77                30.88         0.515            pass              0.786             58.8                           0.328                4.32              0.289                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T09:20:01.591516-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
2026-05-26T12:00:02.390044-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527095001)

</details>
