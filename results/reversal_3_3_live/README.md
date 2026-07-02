# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 09:55:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  LRCX           95.83               24            1.91              5.23        389.02               101.74         0.631            pass              0.770             71.2                           0.344                2.57              0.484                      ok            True                  False
  KLAC           88.24               17            3.14              5.86        263.68               114.88         0.629            pass              0.393             21.4                           0.204                8.00              1.019                      ok            True                  False
  AMAT           95.45               22            1.73              7.89        647.53               105.28         0.620            pass              0.792             83.4                           0.401                7.88              1.237                      ok            True                  False
   APP           85.71               42            0.74              2.92        563.36                73.83         0.505            pass              0.624             73.5                           0.493               16.88              1.775                      ok            True                  False
  DRAM           93.10               29            0.62              0.29         65.74               129.95         0.847            pass              0.830             89.9                           0.785               -6.43             -1.004 downtrend_blocked_slope           False                  False
   WBD           96.00               25            0.47              0.09         26.77                21.87         0.552            pass              0.733             59.2                           0.391                1.69              0.132                      ok           False                  False
 CMCSA           63.64               11            0.48              0.08         23.70                36.53         0.545            pass              0.324             87.6                           0.517                5.49              0.888                      ok           False                  False
  PCAR           88.24               34            0.32              0.27        121.12                34.47         0.509            pass              0.636             68.5                           0.454                2.99              0.275                      ok           False                  False
  CSCO           96.77               31            1.15              0.94        116.61                39.12         0.483 below_threshold              0.711             41.0                           0.326               -1.41             -0.334                      ok           False                  False
  CPRT           88.89               36            0.61              0.12         28.74                40.74         0.474 below_threshold              0.539             27.1                           0.205               -3.07             -0.531 downtrend_blocked_slope           False                  False
  TTWO           90.48               42            0.13              0.22        250.22                35.84         0.461 below_threshold              0.784             86.2                           0.568                9.63              0.742                      ok           False                  False
  FTNT           97.30               37            0.92              1.03        158.54                36.03         0.442 below_threshold              0.750             41.9                           0.297                9.28              1.021                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702095501)

</details>
