# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 09:45:02 EDT`
Last processed slot: `manual`

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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           96.15               26            1.15              3.14        389.91               101.74         0.671            pass              0.822             82.7                           0.522                3.36              0.520                                 ok            True                  False
  KLAC           90.00               20            2.48              4.62        264.21               114.88         0.657            pass              0.513             38.0                           0.341                8.74              1.050                                 ok            True                  False
  AMAT           95.65               23            1.54              7.01        647.90               105.28         0.627            pass              0.805             85.2                           0.449                8.09              1.246                                 ok            True                  False
  SOXL           90.32               31            0.29              0.45        217.47               253.51         0.960            pass              0.799             95.9                           0.585               -7.20             -1.593            downtrend_blocked_slope           False                  False
  DRAM           91.30               23            1.92              0.88         65.49               129.95         0.814            pass              0.677             69.0                           0.554               -7.63             -1.063            downtrend_blocked_slope           False                  False
  MRVL           96.55               29            1.13              2.15        271.13               126.33         0.770            pass              0.820             72.3                           0.518               -7.10             -0.948            downtrend_blocked_slope           False                  False
   WDC           92.11               38            0.07              0.30        598.24               119.34         0.698            pass              0.875             98.5                           0.625              -16.03             -2.108            downtrend_blocked_slope           False                  False
  INTC           94.74               38            0.09              0.08        126.98               102.61         0.683            pass              0.941             97.8                           0.582                4.79             -0.038                                 ok           False                  False
   STX           97.14               35            0.52              3.35        913.75                90.35         0.626            pass              0.888             86.4                           0.569              -14.54             -1.836            downtrend_blocked_slope           False                  False
  CSCO           95.24               21            1.40              1.14        116.52                39.12         0.536            pass              0.611             28.0                           0.229               -1.67             -0.346 downtrend_blocked_slope_and_streak           False                  False
  PANW           93.18               44            0.35              0.87        351.67                52.10         0.460 below_threshold              0.836             79.4                           0.656               24.34              2.498                                 ok           False                  False
  META           40.00                5            3.07             13.17        607.26                52.22         0.457 below_threshold              0.236             63.4                           0.390                4.67              0.412                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                              detail
2026-07-02T09:20:05.802169-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                       {'saved': 93}
2026-07-01T15:20:08.894033-04:00  manage_1530                    exit                                                                  {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00   entry_1500          timing_overlay                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
2026-07-01T14:50:09.429141-04:00   entry_1500           entry_skipped                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-01T14:50:09.429141-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.2, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 720.0, "option_spread_pct": 17.39, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.543}
2026-07-01T14:50:09.429141-04:00   entry_1500 entry_candidate_skipped        {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702094502)

</details>
