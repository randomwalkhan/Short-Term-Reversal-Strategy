# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 16:00:05 EST`
Last processed slot: `manage_1600`

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
  INTC           53.85               13            3.75              1.59         59.87               129.60         0.727            pass              0.212             39.9                           0.370              -37.31             -4.986            downtrend_blocked_slope           False                  False
    ZS           93.02               43            0.28              0.44        224.90                64.45         0.533            pass              0.863             87.4                           0.387               -2.97             -0.903 downtrend_blocked_slope_and_streak           False                  False
  AVGO           66.67               18            1.94              4.50        330.20                44.04         0.505            pass              0.218             38.1                           0.346               -3.58             -0.073                                 ok           False                  False
  REGN          100.00                1            4.38             29.81        960.58                48.26         0.488 below_threshold              0.471              7.3                           0.141               15.53              2.023                                 ok           False                  False
  TEAM           97.44               39            0.62              0.83        190.69                53.65         0.483 below_threshold              0.884             80.8                           0.412              -15.81             -2.226            downtrend_blocked_slope           False                  False
  PANW           80.49               41            0.61              1.49        349.56                58.95         0.479 below_threshold              0.488             75.7                           0.360                0.24             -0.420                                 ok           False                  False
   TXN           91.43               35            0.30              0.66        312.21                35.19         0.475 below_threshold              0.786             88.9                           0.672                9.98              1.067                                 ok           False                  False
  ASML           66.67                6            3.60             39.09       1535.39                44.05         0.463 below_threshold              0.117             23.7                           0.343              -10.64             -0.607            downtrend_blocked_slope           False                  False
  NVDA           71.43                7            2.98              4.31        204.84                32.59         0.461 below_threshold              0.082             12.1                           0.215               -9.66             -0.791 downtrend_blocked_slope_and_streak           False                  False
  CRWD           85.71               35            1.50              2.58        243.58                59.77         0.455 below_threshold              0.517             50.7                           0.266                0.69             -0.144                                 ok           False                  False
  AMAT           60.00               15            3.28              8.76        378.16                58.39         0.453 below_threshold              0.181             34.1                           0.518               -9.67             -0.352            downtrend_blocked_slope           False                  False
  DRAM           70.00               10            5.27              1.76         46.89                69.30         0.439 below_threshold              0.077             11.0                           0.214               -8.20             -0.269            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104160005)

</details>
