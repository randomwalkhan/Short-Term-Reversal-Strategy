# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:15:02 EDT`
Last processed slot: `early_entry_1015`

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
  NXPI           87.10               31            1.09              2.54        331.58                92.16         0.644          pass              0.394              0.0                           0.163               11.83              1.207                                 ok            True                  False
  INTC           94.44               18            3.54              3.06        122.21                91.80         0.582          pass              0.594             32.3                           0.386               -1.21              0.374                                 ok            True                  False
  ROST           93.75               32            0.65              1.07        234.22                38.50         0.535          pass              0.746             59.7                           0.289                7.11              1.014                                 ok            True                  False
  ASML           89.29               28            1.83             20.90       1623.07                54.27         0.519          pass              0.464             14.7                           0.180                5.34              0.586                                 ok            True                  False
  ISRG           87.50               24            1.46              4.46        434.73                35.34         0.505          pass              0.457             37.7                           0.333               -0.37              0.180                                 ok            True                  False
  LRCX           82.14               28            1.34              3.02        321.39                57.65         0.505          pass              0.292             21.5                           0.233               10.07              0.966                                 ok            True                  False
  INSM           76.19               42            0.34              0.26        108.76               110.60         0.749          pass              0.511             78.9                           0.418               -6.47             -0.814            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.61              0.56        130.66                25.21         0.609          pass              0.221             46.6                           0.332               -1.40              0.154                                 ok           False                  False
  FTNT          100.00                6            3.95              3.70        132.37                66.88         0.593          pass              0.560             33.5                           0.260               13.00              1.405                                 ok           False                  False
  REGN           90.91               44            0.06              0.27        634.50                48.91         0.546          pass              0.833             95.9                           0.534              -12.20             -1.457 downtrend_blocked_slope_and_streak           False                  False
  SBUX           97.22               36            0.02              0.01        101.41                33.52         0.533          pass              0.922             98.4                           0.675               -4.30             -0.454 downtrend_blocked_slope_and_streak           False                  False
  NVDA           82.35               17            1.95              2.93        213.60                40.94         0.522          pass              0.188              8.8                           0.118               -4.58             -0.684 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527101502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527101502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527101502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527101502)

</details>
