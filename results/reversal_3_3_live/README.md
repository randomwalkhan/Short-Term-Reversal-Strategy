# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 15:05:04 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           93.75               32            1.04             13.17       1809.63                66.00         0.608          pass              0.752             59.3                           0.375               -9.70             -0.655                                 ok            True                  False
  MPWR           81.82               22            3.58             33.85       1338.15                84.79         0.584          pass              0.275             29.4                           0.496               -5.65             -0.012                                 ok            True                  False
   TXN           80.00               10            3.37              7.11        298.14                65.52         0.581          pass              0.118             19.9                           0.321               -2.36              0.127                                 ok            True                  False
  UPRO           88.89               18            1.62              1.65        145.16                41.96         0.574          pass              0.395             15.7                           0.309                1.21              0.244                                 ok            True                  False
   WBD           87.50               16            0.79              0.15         27.21                20.00         0.532          pass              0.523             76.7                           0.701                1.48              0.247                                 ok            True                  False
  FTNT           93.75               16            2.10              2.42        163.47                41.65         0.526          pass              0.569             36.5                           0.276                4.84              0.500                                 ok            True                  False
  CRWD           84.62               26            1.64              2.37        205.76                56.35         0.520          pass              0.430             49.5                           0.314                5.28              0.689                                 ok            True                  False
  KLAC           82.61               23            1.99              3.13        223.16               109.33         0.726          pass              0.384             51.9                           0.335              -27.07             -2.118 downtrend_blocked_slope_and_streak           False                  False
  AMAT           81.25               16            3.08             12.49        574.08                98.89         0.659          pass              0.232             31.0                           0.260              -22.33             -1.519 downtrend_blocked_slope_and_streak           False                  False
  MSTR           70.59               34            2.18              1.48         96.83               100.18         0.624          pass              0.364             47.3                           0.597                9.69              0.335                                 ok           False                  False
  META           76.92               13            2.09              9.95        677.04                54.55         0.609          pass              0.119             12.8                           0.192                8.84              1.313                                 ok           False                  False
   ADI           78.57               14            2.76              7.56        387.72                55.85         0.578          pass              0.141             18.8                           0.303               -4.28             -0.015                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et       slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-16T15:05:04.145038-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:50:02.142710-04:00 entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                              {"early_entry_score": 0.671, "option_liquidity_status": "low_volume", "option_open_interest": 761.0, "option_spread_pct": 4.13, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.508}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                          {"early_entry_score": 0.521, "option_liquidity_status": "wide_spread", "option_open_interest": 3043.0, "option_spread_pct": 25.76, "option_volume": 343.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.531}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped              {"early_entry_score": 0.267, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 84.0, "option_spread_pct": 8.5, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.577}
2026-07-16T14:50:02.142710-04:00 entry_1500 entry_candidate_skipped                            {"early_entry_score": 0.287, "option_liquidity_status": "low_volume", "option_open_interest": 859.0, "option_spread_pct": 12.05, "option_volume": 16.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.591}
2026-07-16T14:50:02.142710-04:00 entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-16", "training_samples": 5411, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716150504)

</details>
