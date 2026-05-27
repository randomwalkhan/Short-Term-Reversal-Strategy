# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:20:05 EDT`
Last processed slot: `manage_1030`

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
  NXPI           87.50               32            0.99              2.31        331.68                92.16         0.643            pass              0.464             17.7                           0.135               11.94              1.212                                 ok            True                  False
  INTC           95.00               20            3.42              2.95        122.25                91.80         0.577            pass              0.628             34.6                           0.358               -1.09              0.379                                 ok            True                  False
  ROST           94.12               34            0.55              0.90        234.29                38.50         0.528            pass              0.788             66.2                           0.341                7.22              1.019                                 ok            True                  False
  ASML           89.29               28            1.77             20.18       1623.38                54.27         0.523            pass              0.473             17.7                           0.189                5.41              0.588                                 ok            True                  False
  ISRG           90.48               21            1.69              5.18        434.42                35.34         0.514            pass              0.487             27.6                           0.367               -0.61              0.170                                 ok            True                  False
  LRCX           82.76               29            1.19              2.68        321.53                57.65         0.509            pass              0.342             30.4                           0.236               10.24              0.973                                 ok            True                  False
   AEP           66.67               12            0.73              0.67        130.61                25.21         0.605            pass              0.184             36.7                           0.254               -1.51              0.149                                 ok           False                  False
  FTNT          100.00                5            4.37              4.10        132.20                66.88         0.573            pass              0.536             26.4                           0.223               12.50              1.385                                 ok           False                  False
  NVDA           81.25               16            2.22              3.34        213.43                40.94         0.508            pass              0.124              0.0                           0.157               -4.84             -0.697 downtrend_blocked_slope_and_streak           False                  False
   WMT           92.50               40            0.16              0.14        118.51                34.19         0.491 below_threshold              0.780             65.8                           0.336               -9.19             -1.240 downtrend_blocked_slope_and_streak           False                  False
  MSFT           85.71               28            0.70              2.04        415.15                23.55         0.487 below_threshold              0.485             54.7                           0.656                1.53              0.225                                 ok           False                  False
  AMAT           79.17               24            1.82              5.80        452.40                55.57         0.485 below_threshold              0.202             20.0                           0.163                3.70              0.262                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527102005)

</details>
