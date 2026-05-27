# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:25:01 EDT`
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
  NXPI           85.71               28            1.22              2.83        331.46                92.16         0.651            pass              0.370             10.8                           0.102               11.69              1.201                                 ok            True                  False
  ROST           94.29               35            0.51              0.84        234.32                38.50         0.524            pass              0.805             68.4                           0.403                7.26              1.021                                 ok            True                  False
  ASML           91.30               23            2.38             27.19       1620.38                54.27         0.517            pass              0.445              1.9                           0.069                4.75              0.560                                 ok            True                  False
  INSM           75.61               41            0.46              0.35        108.72               110.60         0.747            pass              0.489             71.4                           0.419               -6.58             -0.820            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.68              0.63        130.63                25.21         0.605            pass              0.201             40.3                           0.244               -1.47              0.151                                 ok           False                  False
  INTC           92.86               14            4.12              3.56        121.99                91.80         0.570            pass              0.490             21.2                           0.248               -1.81              0.346           downtrend_blocked_streak           False                  False
  FTNT          100.00                4            4.73              4.43        132.06                66.88         0.558            pass              0.517             20.5                           0.171               12.08              1.368                                 ok           False                  False
  UPRO           94.44               36            0.21              0.22        145.77                30.88         0.514            pass              0.784             58.1                           0.434                4.31              0.289                                 ok           False                  False
  NVDA           81.25               16            2.21              3.32        213.44                40.94         0.508            pass              0.140              5.2                           0.089               -4.83             -0.696 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.32              1.16        524.15                63.86         0.503            pass              0.703             17.4                           0.276                7.01              0.517                                 ok           False                  False
  VRSK           83.72               43            0.05              0.06        171.56                45.01         0.487 below_threshold              0.642             98.1                           0.842                3.11              0.692                                 ok           False                  False
  AMAT           77.78               18            2.39              7.61        451.63                55.57         0.486 below_threshold              0.114              4.1                           0.063                3.10              0.235                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527102501)

</details>
