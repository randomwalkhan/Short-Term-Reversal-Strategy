# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 09:35:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  LRCX           96.43               28            0.77              2.10        390.36               101.74         0.684            pass              0.854             88.4                           0.545                3.76              0.537                      ok            True                  False
  KLAC           90.00               20            2.36              4.39        264.31               114.88         0.672            pass              0.496             31.8                           0.335                8.88              1.056                      ok            True                  False
  INTC           94.44               36            0.55              0.49        126.81               102.61         0.665            pass              0.887             87.4                           0.429                4.31             -0.059                      ok            True                  False
  AMAT           96.30               27            1.04              4.73        648.88               105.28         0.636            pass              0.847             90.1                           0.481                8.64              1.269                      ok            True                  False
  DRAM           92.59               27            0.87              0.40         65.70               129.95         0.844            pass              0.791             85.9                           0.673               -6.65             -1.015 downtrend_blocked_slope           False                  False
  MRVL           96.55               29            0.80              1.53        271.40               126.33         0.787            pass              0.846             80.3                           0.543               -6.79             -0.933 downtrend_blocked_slope           False                  False
   STX           97.30               37            0.01              0.05        915.17                90.35         0.650            pass              0.944             99.8                           0.616              -14.10             -1.813 downtrend_blocked_slope           False                  False
  ASML           94.44               36            0.15              1.88       1842.23                76.04         0.634            pass              0.913             97.1                           0.578               -1.47             -0.030                      ok           False                  False
  META           62.50                8            2.33              9.99        608.63                52.22         0.517            pass              0.268             72.2                           0.477                5.47              0.447                      ok           False                  False
  PCAR           88.57               35            0.19              0.16        121.17                34.47         0.513            pass              0.691             81.5                           0.433                3.13              0.281                      ok           False                  False
  CSCO           96.88               32            0.93              0.76        116.68                39.12         0.499 below_threshold              0.700             34.5                           0.294               -1.20             -0.325                      ok           False                  False
   TRI           83.33               36            0.15              0.09         84.87                38.61         0.499 below_threshold              0.541             76.1                           0.431                6.98              0.840                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702093501)

</details>
