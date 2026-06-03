# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:00:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           82.76               29            1.64             12.19       1058.88               101.17         0.685          pass              0.365             32.0                           0.269               49.80              4.528                      ok            True                  False
  FTNT          100.00               10            2.32              2.42        147.82                71.83         0.663          pass              0.589             41.0                           0.502               13.91              1.459                      ok            True                  False
  MELI           92.31               26            1.64             19.20       1664.60                61.01         0.602          pass              0.536             13.7                           0.179                3.17              0.334                      ok            True                  False
   TXN          100.00               22            1.07              2.32        307.13                42.90         0.565          pass              0.680             47.9                           0.350                0.83             -0.018                      ok            True                  False
  NXPI           96.88               32            0.74              1.68        322.90                50.93         0.561          pass              0.761             52.8                           0.334                9.15              0.681                      ok            True                  False
  MCHP          100.00               17            1.70              1.16         96.46                44.80         0.536          pass              0.632             44.1                           0.291                4.33              0.354                      ok            True                  False
   ROP           89.47               19            1.53              3.61        334.95                35.89         0.525          pass              0.438             24.4                           0.284                0.74              0.336                      ok            True                  False
  WDAY           82.35               17            3.48              3.63        147.33                75.59         0.511          pass              0.194             11.3                           0.192               11.10              2.045                      ok            True                  False
  SNPS          100.00               14            2.49              8.87        504.55                42.98         0.508          pass              0.537             19.8                           0.200                0.37             -0.255                      ok            True                  False
  UPRO           92.59               27            1.17              1.24        150.34                28.22         0.506          pass              0.613             37.8                           0.313                9.12              0.900                      ok            True                  False
   ADP          100.00               15            2.14              3.47        229.69                34.09         0.506          pass              0.541             19.2                           0.125                2.62              0.429                      ok            True                  False
    ZS           60.00                5            5.84              5.89        141.62               159.87         0.734          pass              0.081              2.4                           0.157              -22.55             -2.914 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T10:00:06.995022-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-06-03T09:20:04.119925-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-06-02T15:10:01.501174-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603100006)

</details>
