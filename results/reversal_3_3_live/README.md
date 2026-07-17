# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:10:04 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           91.30               23            1.76              3.58        289.68                64.46         0.610            pass              0.621             57.3                           0.814               -2.38             -0.192                      ok            True                  False
  AAPL           94.44               18            1.13              2.62        332.14                36.90         0.595            pass              0.511              4.3                           0.099                6.77              0.685                      ok            True                  False
   ADI           86.67               30            1.11              2.96        379.26                54.65         0.574            pass              0.576             69.2                           0.864               -0.23              0.012                      ok            True                  False
  ASML           91.67               24            2.16             26.94       1773.32                64.12         0.556            pass              0.618             52.8                           0.811               -1.30             -0.069                      ok            True                  False
  NXPI           87.10               31            0.96              1.82        269.88                54.99         0.546            pass              0.620             78.6                           0.916               -1.94             -0.199                      ok            True                  False
  UPRO           94.44               18            1.74              1.75        142.86                37.18         0.524            pass              0.663             57.4                           0.852                0.25              0.094                      ok            True                  False
  BKNG           84.21               19            2.19              2.83        183.40                41.98         0.500 below_threshold              0.222              0.0                           0.163               -2.16             -0.008                      ok            True                  False
  SOXL           88.46               26            3.79              3.78        140.86               207.84         0.723            pass              0.642             79.2                           0.884              -24.46             -2.524 downtrend_blocked_slope           False                  False
  KLAC           81.82               22            2.34              3.59        217.83               106.93         0.684            pass              0.393             65.3                           0.856               -9.05             -0.511 downtrend_blocked_slope           False                  False
   WDC           82.76               29            0.76              2.49        465.74               109.88         0.668            pass              0.538             90.2                           0.876              -14.05             -1.551 downtrend_blocked_slope           False                  False
  PYPL           77.78               18            1.42              0.56         56.49                63.95         0.658            pass              0.256             45.7                           0.339               22.99              2.468                      ok           False                  False
  MSTR           78.26               46            0.32              0.21         93.94                90.37         0.636            pass              0.543             93.0                           0.952               -6.99             -0.525 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-17T10:10:04.802091-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:05:01.944429-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-16", "training_samples": 5411, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717101004)

</details>
