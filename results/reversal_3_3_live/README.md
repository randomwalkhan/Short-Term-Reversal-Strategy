# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:05:03 EDT`
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
    MU           82.76               29            1.83             13.64       1058.25               101.17         0.673          pass              0.339             23.9                           0.176               49.50              4.519                  ok            True                  False
  CSCO           92.86               14            1.60              1.44        127.38                53.71         0.641          pass              0.560             42.3                           0.450                9.16              0.882                  ok            True                  False
  FTNT          100.00               25            1.62              1.69        148.14                71.83         0.607          pass              0.737             58.9                           0.660               14.74              1.491                  ok            True                  False
  MELI           94.29               35            0.96             11.23       1668.02                61.01         0.588          pass              0.755             49.5                           0.492                3.88              0.365                  ok            True                  False
   TXN          100.00               20            1.12              2.42        307.08                42.90         0.576          pass              0.661             45.5                           0.304                0.78             -0.020                  ok            True                  False
  NXPI           96.67               30            0.93              2.11        322.72                50.93         0.562          pass              0.712             40.9                           0.268                8.95              0.673                  ok            True                  False
  WDAY           84.21               19            2.95              3.07        147.56                75.59         0.535          pass              0.300             24.8                           0.372               11.71              2.070                  ok            True                  False
  MCHP          100.00               17            1.97              1.34         96.39                44.80         0.518          pass              0.604             35.3                           0.247                4.05              0.341                  ok            True                  False
   ROP           91.30               23            1.32              3.10        335.17                35.89         0.514          pass              0.545             35.1                           0.536                0.96              0.346                  ok            True                  False
  UPRO           92.31               26            1.27              1.34        150.30                28.22         0.506          pass              0.584             32.9                           0.278                9.02              0.896                  ok            True                  False
 CMCSA           86.67               15            1.33              0.23         24.75                17.52         0.506          pass              0.344             27.5                           0.279               -1.13             -0.084                  ok            True                  False
  SNPS           94.12               17            2.12              7.56        505.11                42.98         0.505          pass              0.569             31.6                           0.404                0.75             -0.238                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T10:05:03.196018-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-03T10:00:06.995022-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-03T09:20:04.119925-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-06-02T15:10:01.501174-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603100503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603100503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603100503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603100503)

</details>
