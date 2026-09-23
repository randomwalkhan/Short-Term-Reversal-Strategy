# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 09:30:01 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.86               35            1.09              1.16        151.46               119.97         0.759          pass              0.547             76.0                           0.861               19.49              2.659                                 ok            True                  False
  DRAM           81.82               33            0.82              0.36         63.51                51.53         0.579          pass              0.427             55.9                           0.582                2.55              0.701                                 ok            True                  False
  INTC           84.21               38            0.93              0.81        123.51                69.88         0.564          pass              0.490             45.0                           0.488               17.45              1.580                                 ok            True                  False
  SHOP           88.24               34            1.24              1.28        147.19                60.99         0.551          pass              0.535             33.4                           0.537               15.08              1.273                                 ok            True                  False
  MPWR           84.38               32            1.13             10.92       1375.94                46.25         0.545          pass              0.423             35.1                           0.311               12.03              0.710                                 ok            True                  False
  ASML           80.00               35            0.62              7.56       1744.66                40.77         0.517          pass              0.434             71.9                           0.723               -1.57             -0.182                                 ok            True                  False
  MSTR           94.87               39            0.14              0.17        167.26               109.37         0.763          pass              0.940             91.2                           0.725               22.39              2.221                                 ok           False                  False
  CRWD           88.64               44            0.25              0.44        249.87                96.94         0.693          pass              0.638             46.1                           0.359               18.77              2.134                                 ok           False                  False
  PYPL           89.19               37            0.31              0.11         52.84                57.22         0.610          pass              0.554             22.6                           0.318                1.07             -0.113                                 ok           False                  False
  NVDA           91.43               35            0.24              0.39        228.70                44.57         0.591          pass              0.725             64.8                           0.680                2.19              0.494                                 ok           False                  False
  AMGN           85.71               35            0.22              0.62        409.97                42.33         0.581          pass              0.603             75.3                           0.415                4.12              0.223                                 ok           False                  False
  CHTR           87.80               41            0.65              0.53        117.03                64.47         0.549          pass              0.463              0.0                           0.211              -20.06             -1.784 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                 detail
2026-09-23T09:30:01.473090-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.689, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 24.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.507}
2026-09-22T14:50:01.294026-04:00   entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923093001)

</details>
