# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 10:00:05 EDT`
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

- Cash: `$14,720.50`
- Equity: `$28,160.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-1,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 13440.0         4.58            4.2      126.19        125.86          bid_ask_mid                        4.2                bid_ask_mid                    True         -1200.0                   -8.2         93.33               15              1.32         33.41            31.4                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           84.62               13            8.62             16.09        259.81               249.48         0.741          pass              0.329             37.3                           0.685                7.75             -0.162                      ok            True                  False
  MRVL           95.45               22            2.79              5.82        295.39               157.45         0.706          pass              0.721             56.7                           0.795                3.91             -0.280                      ok            True                  False
  ASML           95.00               20            2.64             36.72       1973.70                71.16         0.576          pass              0.677             51.0                           0.766                7.38              0.386                      ok            True                  False
  INTC           90.00               20            3.92              3.83        137.99                95.61         0.530          pass              0.459             24.1                           0.488               14.62              0.925                      ok            True                  False
  MPWR           88.57               35            0.09              0.85       1382.00                91.02         0.718          pass              0.760             97.7                           0.985               -7.85             -1.296 downtrend_blocked_slope           False                  False
  AVGO           78.26               23            1.36              3.58        376.21                74.76         0.687          pass              0.287             43.9                           0.604               -0.93             -0.579                      ok           False                  False
  MCHP           89.66               29            0.73              0.47         91.00                74.43         0.667          pass              0.663             70.6                           0.734               -5.33             -0.947 downtrend_blocked_slope           False                  False
   ADI           91.18               34            0.29              0.81        396.82                64.06         0.627          pass              0.784             87.8                           0.861               -4.81             -0.893 downtrend_blocked_slope           False                  False
  UPRO           87.10               31            0.39              0.39        141.62                55.16         0.626          pass              0.618             75.5                           0.752               -1.80             -0.191                      ok           False                  False
   WDC           91.67               12            4.69             20.95        629.74               116.88         0.607          pass              0.502             39.0                           0.697              -10.61             -1.673 downtrend_blocked_slope           False                  False
   XEL          100.00               20            0.47              0.27         80.19                19.51         0.592          pass              0.526              0.0                           0.157                1.19              0.434                      ok           False                  False
    MU           87.50                8            6.56             52.97       1131.59               128.04         0.579          pass              0.306             16.0                           0.394                5.67              0.653                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-01T10:00:05.880743-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-30T17:05:09.028498-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500                   entry {"allocated_cash": 14640.0, "asset_type": "option", "contract_symbol": "GILD260821C00130000", "contracts": 32, "early_entry_score": 0.533, "entry_mode": "regular", "entry_option_price": 4.575, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 807.0, "option_spread_pct": 7.65, "option_volume": 40.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.563}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
2026-06-29T14:50:09.505108-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-29", "training_samples": 5314, "window": 5}
2026-06-29T12:00:02.850105-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701100005)

</details>
