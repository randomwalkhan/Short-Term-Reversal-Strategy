# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 09:40:01 EDT`
Last processed slot: `manage_0930`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           94.29               35            0.87              0.77        126.69               102.61         0.649          pass              0.853             80.0                           0.400                3.98             -0.073                                 ok            True                  False
  KLAC           92.86               14            3.38              6.29        263.49               114.88         0.638          pass              0.480             15.6                           0.285                7.74              1.008                                 ok            True                  False
  LRCX           96.15               26            1.73              4.74        389.23               101.74         0.630          pass              0.791             73.9                           0.388                2.76              0.493                                 ok            True                  False
  ASML           93.75               32            0.79             10.16       1838.69                76.04         0.615          pass              0.828             84.3                           0.426               -2.10             -0.060                                 ok            True                  False
  AMAT           93.75               16            2.59             11.80        645.85               105.28         0.597          pass              0.692             75.2                           0.421                6.94              1.197                                 ok            True                  False
  SOXL           89.29               28            2.35              3.58        216.13               253.51         0.930          pass              0.663             67.4                           0.391               -9.11             -1.688            downtrend_blocked_slope           False                  False
  DRAM           91.30               23            1.95              0.90         65.49               129.95         0.813          pass              0.675             68.5                           0.566               -7.66             -1.064            downtrend_blocked_slope           False                  False
  MRVL           96.00               25            2.16              4.12        270.29               126.33         0.731          pass              0.713             46.8                           0.310               -8.07             -0.996            downtrend_blocked_slope           False                  False
   WDC           91.18               34            0.55              2.29        597.39               119.34         0.690          pass              0.793             88.5                           0.585              -16.43             -2.130            downtrend_blocked_slope           False                  False
   STX           96.00               25            1.31              8.37        911.60                90.35         0.636          pass              0.762             66.0                           0.481              -15.21             -1.872            downtrend_blocked_slope           False                  False
  CSCO           94.12               17            1.70              1.40        116.41                39.12         0.542          pass              0.499              7.2                           0.193               -1.97             -0.360 downtrend_blocked_slope_and_streak           False                  False
  META           66.67                9            2.27              9.76        608.73                52.22         0.519          pass              0.271             72.9                           0.447                5.53              0.449                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702094001)

</details>
