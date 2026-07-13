# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 10:00:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  QCOM           83.33               30            1.09              1.44        188.54                63.33         0.583          pass              0.494             71.2                           0.667               -0.86              0.262                                 ok            True                  False
   ADI           86.96               23            1.73              4.80        393.59                55.18         0.580          pass              0.439             36.3                           0.505               -0.76             -0.006                                 ok            True                  False
   TXN           86.67               15            2.90              6.33        308.75                64.14         0.576          pass              0.338             23.1                           0.239                5.93              0.518                                 ok            True                  False
  META           82.76               29            0.86              4.02        667.49                55.99         0.568          pass              0.420             54.3                           0.365               17.93              1.736                                 ok            True                  False
  UPRO           86.21               29            0.52              0.53        145.93                40.56         0.564          pass              0.574             75.2                           0.662                4.79              0.419                                 ok            True                  False
  NXPI           85.00               20            2.10              4.30        290.42                55.03         0.557          pass              0.376             40.2                           0.528                2.78              0.436                                 ok            True                  False
  ABNB           93.33               15            2.09              2.17        147.69                37.12         0.539          pass              0.461              5.9                           0.120               -1.12             -0.020                                 ok            True                  False
   LIN          100.00               20            0.94              3.48        528.30                20.88         0.525          pass              0.522              1.0                           0.166                2.69              0.055                                 ok            True                  False
  AVGO           80.95               21            2.34              6.54        397.17                49.47         0.513          pass              0.237             29.1                           0.272                4.88              0.780                                 ok            True                  False
  KLAC           81.25               16            3.40              5.52        229.16               110.61         0.672          pass              0.240             33.3                           0.468              -19.67             -2.562 downtrend_blocked_slope_and_streak           False                  False
  AMAT           78.57               14            3.32             13.99        596.50                98.14         0.622          pass              0.214             41.8                           0.501              -16.14             -1.892 downtrend_blocked_slope_and_streak           False                  False
  ASML           92.00               25            1.95             24.48       1786.83                63.97         0.598          pass              0.601             40.4                           0.442               -6.41             -0.808            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-07-13T10:00:02.015857-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:00:02.015857-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-07-13T09:55:05.995868-04:00     data_refresh       data_refresh                                                                                    {'saved': 92, 'empty': 1}
2026-07-13T09:20:04.012010-04:00     data_refresh       data_refresh                                                                                   {'empty': 63, 'saved': 30}
2026-07-10T15:10:08.910811-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:05:06.429039-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:00:09.226035-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:55:05.716481-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:50:05.489745-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-07-10T14:50:05.489745-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-10", "training_samples": 5470, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713100002)

</details>
