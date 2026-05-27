# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:10:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.88               33            0.80              1.87        331.87                92.16         0.651          pass              0.488             19.8                           0.139               12.16              1.220                                 ok            True                  False
  INTC           95.24               21            3.17              2.74        122.34                91.80         0.587          pass              0.650             39.3                           0.489               -0.84              0.391                                 ok            True                  False
  ROST           91.67               24            1.04              1.72        233.94                38.50         0.562          pass              0.567             35.5                           0.192                6.69              0.996                                 ok            True                  False
  ASML           89.66               29            1.61             18.42       1624.13                54.27         0.527          pass              0.511             24.8                           0.281                5.57              0.596                                 ok            True                  False
  ISRG           90.48               21            1.69              5.17        434.42                35.34         0.514          pass              0.487             27.7                           0.282               -0.61              0.170                                 ok            True                  False
  SOXL           85.71               21            4.78              7.55        222.55               148.29         0.512          pass              0.358             27.0                           0.246               24.62              2.074                                 ok            True                  False
  LRCX           81.48               27            1.48              3.34        321.25                57.65         0.503          pass              0.228              8.4                           0.098                9.91              0.960                                 ok            True                  False
  INSM           75.61               41            0.54              0.41        108.69               110.60         0.743          pass              0.473             66.3                           0.397               -6.66             -0.823            downtrend_blocked_slope           False                  False
   AEP           75.00               16            0.53              0.49        130.69                25.21         0.601          pass              0.260             53.3                           0.395               -1.32              0.157                                 ok           False                  False
  FTNT          100.00                6            4.03              3.78        132.34                66.88         0.588          pass              0.556             32.2                           0.247               12.91              1.401                                 ok           False                  False
  REGN           90.91               44            0.06              0.27        634.50                48.91         0.546          pass              0.834             96.0                           0.535              -12.20             -1.457 downtrend_blocked_slope_and_streak           False                  False
  NVDA           82.35               17            1.94              2.92        213.61                40.94         0.523          pass              0.190              9.3                           0.120               -4.57             -0.683 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T10:10:01.607453-04:00 early_entry_1010  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527101001)

</details>
