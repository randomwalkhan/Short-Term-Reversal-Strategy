# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:10:05 EDT`
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

- Cash: `$36,331.75`
- Equity: `$36,331.75`
- Realized PnL: `$26,331.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
    MU           83.33               30            1.52             11.31       1059.25               101.17         0.686          pass              0.402             36.9                           0.267               49.98              4.534                  ok            True                  False
  MELI           92.31               26            1.33             15.53       1666.17                61.01         0.622          pass              0.588             30.2                           0.334                3.50              0.348                  ok            True                  False
  CSCO           95.24               21            1.22              1.10        127.53                53.71         0.621          pass              0.703             55.9                           0.568                9.58              0.900                  ok            True                  False
  FTNT          100.00               35            1.01              1.05        148.41                71.83         0.579          pass              0.848             74.4                           0.786               15.45              1.519                  ok            True                   True
   TXN          100.00               28            0.67              1.44        307.50                42.90         0.551          pass              0.778             67.6                           0.455                1.24              0.000                  ok            True                  False
   ROP           88.89               18            1.57              3.69        334.92                35.89         0.529          pass              0.411             22.7                           0.358                0.71              0.335                  ok            True                  False
  CDNS           92.31               13            2.37              6.89        413.44                43.85         0.520          pass              0.505             34.9                           0.555               20.24              1.841                  ok            True                  False
  MCHP          100.00               20            1.63              1.11         96.48                44.80         0.519          pass              0.657             46.3                           0.287                4.40              0.357                  ok            True                  False
  WDAY           84.00               25            2.61              2.72        147.71                75.59         0.515          pass              0.358             33.4                           0.509               12.10              2.086                  ok            True                  False
  CRWD           82.35               17            2.08             11.17        764.16                51.19         0.511          pass              0.282             40.5                           0.547               22.06              2.205                  ok            True                  False
   ADP          100.00               13            2.31              3.73        229.58                34.09         0.510          pass              0.510             13.0                           0.101                2.45              0.421                  ok            True                  False
  UPRO           92.86               28            1.11              1.18        150.37                28.22         0.503          pass              0.636             40.9                           0.393                9.18              0.903                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-03T10:10:05.039776-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-03T10:10:05.039776-04:00 early_entry_1010 entry_candidate_skipped {"early_entry_score": 0.848, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 383.0, "option_spread_pct": 21.64, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.579}
2026-06-03T10:05:03.196018-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-03T10:00:06.995022-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-03T09:20:04.119925-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
2026-06-02T15:10:01.501174-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                        {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603101005)

</details>
