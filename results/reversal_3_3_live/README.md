# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:20:05 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  META     option         option META261120C00735000      8          2026-09-30         2026-10-01       48.425     43.5825 -3874.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           84.85               33            1.22              1.27        147.32               113.77         0.694            pass              0.473             40.3                           0.255               27.28              1.758                                 ok            True                  False
  AMGN           82.35               17            1.24              3.65        419.95                46.02         0.609            pass              0.304             44.5                           0.285                9.62              0.998                                 ok            True                  False
  INTC           87.10               31            1.78              1.50        119.59                73.63         0.563            pass              0.461             25.3                           0.252                8.53              0.492                                 ok            True                  False
  ASML           81.25               32            0.68              8.59       1807.99                42.37         0.539            pass              0.303             23.2                           0.154               10.42              0.938                                 ok            True                  False
  META           87.18               39            0.21              1.06        724.72                55.93         0.562            pass              0.630             62.9                           0.266                6.14              0.532                                 ok           False                  False
  DRAM           79.31               29            1.23              0.52         60.14                53.77         0.548            pass              0.183              0.7                           0.035                3.18              0.060                                 ok           False                  False
  MPWR           91.18               34            0.47              4.41       1345.33                50.40         0.544            pass              0.696             61.2                           0.476               14.82              1.132                                 ok           False                  False
  QCOM           91.67               36            0.46              0.59        183.79                56.29         0.534            pass              0.620             27.4                           0.270               -2.92             -0.234           downtrend_blocked_streak           False                  False
   XEL           80.00               15            0.78              0.38         70.32                18.32         0.526            pass              0.218             43.9                           0.579               -5.03             -0.451            downtrend_blocked_slope           False                  False
   EXC           81.25               16            0.74              0.21         40.31                14.97         0.503            pass              0.271             49.2                           0.628               -5.96             -0.588 downtrend_blocked_slope_and_streak           False                  False
  NFLX           70.59               17            1.78              0.87         69.21                37.25         0.498 below_threshold              0.147             16.8                           0.227               -9.26             -0.749            downtrend_blocked_slope           False                  False
  NXPI           85.71               35            0.48              0.80        237.19                38.88         0.494 below_threshold              0.508             46.4                           0.290                3.70              0.362                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-01T10:20:05.454377-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "META261120C00735000", "fill_price": 43.5825, "pnl": -3874.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "META"}
2026-10-01T10:15:02.462190-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:10:05.306830-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:05:05.587824-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "entry_ask": 17.55, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 16.425, "hypothetical_budget": 23249.15, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 78.0, "option_spread_pct": 13.7, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "matched_signals": 41, "recovery_stability_score": 0.567, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T10:00:05.588413-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T00:00:05.224460-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-09-30T15:10:04.050158-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:05:04.200259-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:00:05.217258-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001102005)

</details>
