# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 15:35:06 EST`
Last processed slot: `manage_1530`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           58.33               12            4.13              1.75         59.80               129.60         0.716            pass              0.187             33.9                           0.343              -37.55             -5.004            downtrend_blocked_slope           False                  False
  AVGO           66.67               18            1.91              4.45        330.22                44.04         0.507            pass              0.221             38.9                           0.335               -3.56             -0.071                                 ok           False                  False
  REGN          100.00                2            4.06             27.69        961.49                48.26         0.505            pass              0.458              2.4                           0.230               15.90              2.037                                 ok           False                  False
   TXN           90.00               30            0.68              1.48        311.86                35.19         0.482 below_threshold              0.675             75.4                           0.532                9.57              1.050                                 ok           False                  False
  TEAM           97.78               45            0.08              0.11        191.00                53.65         0.480 below_threshold              0.940             97.4                           0.649              -15.35             -2.201            downtrend_blocked_slope           False                  False
  NVDA           63.64               11            2.21              3.20        205.32                32.59         0.479 below_threshold              0.116             20.4                           0.201               -8.94             -0.756 downtrend_blocked_slope_and_streak           False                  False
  CRWD           87.50               48            0.06              0.10        244.64                59.77         0.467 below_threshold              0.741             98.1                           0.762                2.17             -0.077                                 ok           False                  False
  DRAM           63.64               11            4.92              1.64         46.94                69.30         0.446 below_threshold              0.102             16.8                           0.293               -7.86             -0.253            downtrend_blocked_slope           False                  False
  ASML           50.00                4            3.83             41.61       1534.31                44.05         0.445 below_threshold              0.101             18.8                           0.310              -10.86             -0.618            downtrend_blocked_slope           False                  False
   ADI           60.00                5            3.46             10.18        415.43                38.61         0.416 below_threshold              0.152             36.9                           0.462               -0.17              0.505                                 ok           False                  False
  AMAT           50.00               10            4.27             11.41        377.03                58.39         0.414 below_threshold              0.084             14.2                           0.406              -10.59             -0.399            downtrend_blocked_slope           False                  False
  MCHP           71.43                7            3.95              2.16         76.98                45.40         0.402 below_threshold              0.128             29.3                           0.314               -3.02              0.142                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:45:05.372887-05:00 early_entry_1145 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104153506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104153506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104153506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104153506)

</details>
