# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 14:50:04 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$32,973.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-630.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12780.0         44.7           42.6      510.62        507.07          -630.0                   -4.7         97.14               35               0.5         52.16           52.77                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           86.67               15            4.66              2.77         83.81               115.69         0.606          pass              0.324             17.5                           0.292               14.97              1.335                                 ok            True                  False
   ADP          100.00               12            2.11              3.16        212.46                33.54         0.542          pass              0.621             51.2                           0.754               -2.68             -0.095                                 ok            True                  False
  SNPS           96.88               32            1.20              4.30        511.37                43.23         0.531          pass              0.731             43.7                           0.623                5.37              0.682                                 ok            True                  False
  CDNS           96.67               30            1.39              3.49        356.54                38.69         0.513          pass              0.699             38.0                           0.317                7.00              0.864                                 ok            True                  False
  MSTR           90.32               31            2.14              2.76        183.24                75.69         0.510          pass              0.633             55.4                           0.613               14.09              1.271                                 ok            True                  False
  MDLZ           83.33               24            0.80              0.35         61.55                23.07         0.506          pass              0.371             46.2                           0.491                0.27              0.034                                 ok            True                  False
  MCHP           82.76               29            1.13              0.77         97.37                50.72         0.505          pass              0.398             49.1                           0.235                7.13              0.739                                 ok            True                  False
  CHTR           70.00               10            3.79              3.92        146.24               118.13         0.750          pass              0.098              7.7                           0.174              -10.29             -1.412            downtrend_blocked_slope           False                  False
  GEHC           73.68               38            0.53              0.23         62.19                57.10         0.566          pass              0.466             74.2                           0.503                4.16              0.377                                 ok           False                  False
  ORLY           87.50                8            2.16              1.39         91.25                35.45         0.566          pass              0.360             34.4                           0.311               -2.00             -0.558 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.89                9            1.69              1.80        151.08                21.96         0.530          pass              0.323             11.1                           0.317               -3.87             -0.470            downtrend_blocked_slope           False                  False
  TMUS           84.00               25            1.26              1.70        192.57                36.44         0.519          pass              0.330             23.8                           0.386               -3.68             -0.293            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:00:06.549783-04:00 early_entry_1100  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T10:55:05.050603-04:00 early_entry_1055  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513145004)

</details>
