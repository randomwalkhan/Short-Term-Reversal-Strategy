# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 09:45:06 EDT`
Last processed slot: `manual`

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
    MU           83.87               31            1.23              9.17       1060.17               101.17         0.705          pass              0.393             26.6                           0.219               50.41              4.547                  ok            True                  False
  QCOM           97.14               35            0.75              1.27        240.30               100.94         0.660          pass              0.869             78.9                           0.780               22.20              1.809                  ok            True                   True
  CSCO           90.91               11            1.83              1.64        127.30                53.71         0.644          pass              0.464             33.9                           0.321                8.91              0.872                  ok            True                  False
  MELI           92.31               26            1.47             17.18       1665.47                61.01         0.617          pass              0.511              5.0                           0.128                3.35              0.342                  ok            True                  False
  PAYX           90.00               10            1.75              1.23        100.26                33.97         0.583          pass              0.349              7.9                           0.103                4.82              0.666                  ok            True                  False
   TXN          100.00               28            0.65              1.40        307.52                42.90         0.557          pass              0.758             60.9                           0.397                1.26              0.001                  ok            True                  False
   CEG           80.65               31            0.97              1.85        271.85                55.62         0.547          pass              0.246             11.5                           0.112                3.58             -0.239                  ok            True                  False
  WDAY           84.21               19            3.00              3.12        147.54                75.59         0.537          pass              0.269             14.3                           0.210               11.66              2.068                  ok            True                  False
   ROP           88.24               17            1.76              4.14        334.73                35.89         0.523          pass              0.359             13.3                           0.186                0.51              0.326                  ok            True                  False
  MCHP           96.67               30            0.57              0.38         96.80                44.80         0.519          pass              0.829             81.4                           0.526                5.54              0.406                  ok            True                  False
  SNPS          100.00               14            2.41              8.57        504.68                42.98         0.518          pass              0.517             12.8                           0.245                0.45             -0.251                  ok            True                  False
  CTSH           81.25               16            2.36              0.91         54.75                50.18         0.515          pass              0.151              8.8                           0.174                5.81              0.896                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T09:20:04.119925-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-06-02T15:10:01.501174-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603094506)

</details>
