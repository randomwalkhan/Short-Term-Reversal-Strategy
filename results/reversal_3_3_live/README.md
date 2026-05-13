# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:10:06 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               22            2.39              2.02        119.75               109.00         0.640          pass              0.638             31.4                           0.246               24.25              3.084                                 ok            True                  False
  TEAM           81.82               22            3.87              2.30         84.01               115.69         0.602          pass              0.283             31.5                           0.411               15.92              1.372                                 ok            True                  False
  QCOM           94.29               35            0.63              0.93        209.91                94.36         0.561          pass              0.777             57.9                           0.342               33.96              3.259                                 ok            True                  False
  SNPS           97.14               35            0.82              2.96        511.94                43.23         0.539          pass              0.757             45.3                           0.420                5.77              0.699                                 ok            True                  False
   ADP           92.31               13            2.06              3.08        212.49                33.54         0.532          pass              0.546             48.3                           0.294               -2.63             -0.092                                 ok            True                  False
  MCHP           80.00               25            1.31              0.90         97.32                50.72         0.515          pass              0.274             40.7                           0.203                6.93              0.730                                 ok            True                  False
  KLAC           86.11               36            0.68              8.63       1807.65                48.58         0.514          pass              0.451             21.0                           0.234               -0.95              0.437                                 ok            True                  False
   XEL           88.89               27            0.61              0.34         79.75                27.12         0.508          pass              0.585             61.4                           0.644                0.75             -0.220                                 ok            True                  False
  MSTR           90.00               30            2.42              3.12        183.08                75.69         0.501          pass              0.599             49.7                           0.632               13.77              1.258                                 ok            True                  False
  CHTR           76.47               17            2.38              2.46        146.86               118.13         0.788          pass              0.235             36.5                           0.472               -8.98             -1.346            downtrend_blocked_slope           False                  False
  INSM           75.76               33            1.24              1.01        115.57               110.65         0.593          pass              0.405             64.0                           0.478              -15.16             -2.859 downtrend_blocked_slope_and_streak           False                  False
  SHOP           81.82               22            2.42              1.69         99.11                84.62         0.573          pass              0.312             42.2                           0.589              -19.66             -2.524 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T10:10:06.807841-04:00 early_entry_1010  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-13T10:05:05.859086-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513101006)

</details>
