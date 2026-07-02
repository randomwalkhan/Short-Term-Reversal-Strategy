# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 09:50:01 EDT`
Last processed slot: `manage_1000`

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
  LRCX           96.15               26            1.16              3.18        389.90               101.74         0.670            pass              0.821             82.5                           0.508                3.35              0.519                                 ok            True                  False
  KLAC           89.47               19            2.79              5.20        263.96               114.88         0.642            pass              0.468             30.3                           0.292                8.39              1.036                                 ok            True                  False
  AMAT           95.83               24            1.48              6.75        648.02               105.28         0.624            pass              0.813             85.8                           0.424                8.15              1.248                                 ok            True                  False
  DRAM           92.31               26            1.28              0.59         65.61               129.95         0.831            pass              0.756             79.3                           0.629               -7.05             -1.034            downtrend_blocked_slope           False                  False
   STX           97.22               36            0.30              1.93        914.36                90.35         0.635            pass              0.913             92.2                           0.605              -14.35             -1.826            downtrend_blocked_slope           False                  False
 CMCSA           75.00               16            0.13              0.02         23.72                36.53         0.550            pass              0.385             96.8                           0.617                5.87              0.904                                 ok           False                  False
  CSCO           95.00               20            1.50              1.22        116.49                39.12         0.535            pass              0.589             22.9                           0.197               -1.76             -0.351 downtrend_blocked_slope_and_streak           False                  False
   APP           86.36               44            0.50              1.97        563.76                73.83         0.510            pass              0.667             82.1                           0.657               17.16              1.786                                 ok           False                  False
  CPRT           87.88               33            0.78              0.16         28.72                40.74         0.482 below_threshold              0.412              0.0                           0.197               -3.24             -0.539            downtrend_blocked_slope           False                  False
  FTNT           96.77               31            1.33              1.48        158.34                36.03         0.455 below_threshold              0.634             16.2                           0.169                8.82              1.002                                 ok           False                  False
  SNPS           88.24               34            0.79              2.51        453.46                30.90         0.443 below_threshold              0.548             41.3                           0.423               -2.34             -0.302 downtrend_blocked_slope_and_streak           False                  False
  META           25.00                4            3.17             13.59        607.08                52.22         0.439 below_threshold              0.231             62.2                           0.377                4.56              0.407                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702095001)

</details>
