# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 09:55:01 EDT`
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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ISRG           84.62               39            0.66              1.66        361.09                72.57         0.602          pass              0.596             73.1                           0.555               -7.59             -0.852                                 ok            True                  False
  FAST          100.00               19            0.72              0.24         48.00                27.18         0.574          pass              0.704             62.1                           0.635                4.98              0.481                                 ok            True                  False
   HON           84.21               19            1.03              1.78        246.29                39.75         0.543          pass              0.283             18.7                           0.180                9.80              1.175                                 ok            True                  False
   MAR          100.00               32            0.56              1.51        382.87                28.18         0.510          pass              0.813             71.8                           0.583                5.00              0.415                                 ok            True                   True
  META           90.00               30            0.94              3.90        591.74                53.87         0.601          pass              0.497             12.4                           0.215              -13.72             -1.532 downtrend_blocked_slope_and_streak           False                  False
  MRVL           85.71               35            0.74              0.90        174.08                89.75         0.586          pass              0.638             86.8                           0.559              -16.04             -1.020 downtrend_blocked_slope_and_streak           False                  False
   WDC           83.87               31            0.66              2.14        462.59                95.99         0.577          pass              0.572             90.3                           0.454              -10.39             -0.150           downtrend_blocked_streak           False                  False
   APP           77.14               35            1.86              5.45        415.88                74.36         0.540          pass              0.279             19.6                           0.220               -9.34             -0.892            downtrend_blocked_slope           False                  False
  DRAM           77.78               27            2.44              0.82         47.41               100.66         0.519          pass              0.399             77.8                           0.445              -18.83             -1.253 downtrend_blocked_slope_and_streak           False                  False
  MPWR           84.21               38            0.54              4.82       1279.95                58.32         0.517          pass              0.587             78.9                           0.569               -7.36             -0.237           downtrend_blocked_streak           False                  False
   CEG           69.44               36            0.43              0.78        259.48                41.76         0.509          pass              0.368             48.0                           0.400                0.23              0.502                                 ok           False                  False
    EA          100.00               30            0.11              0.16        208.80                 3.93         0.505          pass              0.691             35.7                           0.292                0.97              0.087                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-07-29T09:50:04.461343-04:00  manage_1000         exit {"asset_type": "option", "contract_symbol": "CSX260918C00052500", "fill_price": 1.2825, "pnl": -1838.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-07-29T09:35:02.435322-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:30:03.798822-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:25:01.530149-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:20:02.789351-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:15:01.480372-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:10:04.312418-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:05:01.483120-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T09:00:02.430762-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-29T08:55:05.405467-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729095501)

</details>
