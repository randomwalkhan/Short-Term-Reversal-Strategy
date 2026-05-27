# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:30:06 EDT`
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
  NXPI           85.19               27            1.29              3.01        331.38                92.16         0.647            pass              0.399             27.7                           0.243               11.60              1.198                                 ok            True                  False
  ASML           95.24               21            2.60             29.68       1619.31                54.27         0.515            pass              0.565             13.5                           0.214                4.52              0.550                                 ok            True                  False
  ISRG           90.48               21            1.68              5.13        434.44                35.34         0.515            pass              0.489             28.3                           0.422               -0.59              0.170                                 ok            True                  False
  INSM           73.68               38            0.84              0.64        108.60               110.60         0.741            pass              0.404             47.7                           0.328               -6.94             -0.837            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.64              0.58        130.65                25.21         0.608            pass              0.214             44.3                           0.300               -1.42              0.153                                 ok           False                  False
  INTC           92.31               13            4.23              3.65        121.95                91.80         0.569            pass              0.463             19.1                           0.222               -1.92              0.341           downtrend_blocked_streak           False                  False
  FTNT          100.00                3            4.97              4.66        131.96                66.88         0.550            pass              0.504             16.4                           0.143               11.80              1.357                                 ok           False                  False
  REGN           90.91               44            0.03              0.13        634.57                48.91         0.549            pass              0.840             98.1                           0.612              -12.17             -1.456 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.74               38            0.06              0.07        145.83                30.88         0.511            pass              0.893             87.3                           0.506                4.47              0.296                                 ok           False                  False
  NVDA           80.00               15            2.26              3.40        213.40                40.94         0.508            pass              0.113              9.5                           0.195               -4.88             -0.698 downtrend_blocked_slope_and_streak           False                  False
  ROST           95.56               45            0.06              0.11        234.63                38.50         0.485 below_threshold              0.937             96.1                           0.609                7.75              1.041                                 ok           False                  False
  DXCM           83.33               42            0.27              0.14         71.95                50.51         0.484 below_threshold              0.594             85.7                           0.803               17.46              2.450                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T10:30:06.423656-04:00 early_entry_1030 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527103006)

</details>
