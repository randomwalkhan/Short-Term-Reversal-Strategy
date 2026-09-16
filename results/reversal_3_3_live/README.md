# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 10:00:05 EDT`
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

- Cash: `$68,746.10`
- Equity: `$68,746.10`
- Realized PnL: `$58,746.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TMUS     option         option TMUS261016C00185000     70          2026-09-15         2026-09-16          5.1        4.59 -3570.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           86.11               36            1.21              1.10        129.13               105.80         0.674          pass              0.502             32.9                           0.193                2.52             -0.067                                 ok            True                  False
  CTSH          100.00               35            0.64              0.28         63.16                43.25         0.531          pass              0.832             70.7                           0.729               -0.81             -0.160                                 ok            True                   True
  CRWD           88.64               44            0.49              0.83        242.14               100.47         0.687          pass              0.752             84.2                           0.734               12.20              1.349                                 ok           False                  False
    ZS           97.67               43            0.19              0.26        193.78                82.15         0.629          pass              0.946             94.3                           0.837                8.50              0.948                                 ok           False                  False
  PYPL           91.67               36            0.30              0.11         53.76                57.87         0.622          pass              0.785             79.5                           0.710                2.64             -0.100                                 ok           False                  False
   TRI           94.29               35            0.38              0.27        102.49                58.06         0.605          pass              0.837             76.2                           0.808               -3.88             -0.621           downtrend_blocked_streak           False                  False
  TEAM          100.00               38            0.36              0.48        189.60                62.94         0.594          pass              0.903             85.7                           0.782                1.12              0.008                                 ok           False                  False
   WMT           84.38               32            0.48              0.36        107.93                40.04         0.563          pass              0.320              0.0                           0.170                1.56              0.152                                 ok           False                  False
  ADSK           85.71               28            1.26              2.00        225.64                56.46         0.557          pass              0.443             38.3                           0.358               -9.71             -0.850           downtrend_blocked_streak           False                  False
  WDAY           93.75               32            0.79              1.06        190.22                46.67         0.540          pass              0.763             65.2                           0.696               -4.65             -0.681 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.48               21            0.19              0.18        135.42                15.04         0.529          pass              0.506             33.4                           0.254               -2.22             -0.269            downtrend_blocked_slope           False                  False
  ADBE           96.15               26            1.73              3.12        256.42                48.65         0.523          pass              0.643             28.1                           0.439              -11.45             -1.181 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-16T10:00:05.613145-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "entry_ask": 3.5, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 3.125, "hypothetical_budget": 34373.05, "hypothetical_contracts": 109, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 24.0, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "matched_signals": 35, "recovery_stability_score": 0.729, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-16T09:50:01.541163-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "TMUS261016C00185000", "fill_price": 4.59, "pnl": -3570.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TMUS"}
2026-09-16T00:00:06.550315-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-15T15:10:04.348747-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:05:02.260320-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:00:05.246314-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T14:55:04.231884-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T14:50:04.834862-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.751, "option_liquidity_status": "wide_spread", "option_open_interest": 7403.0, "option_spread_pct": 15.92, "option_volume": 40.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.562}
2026-09-15T14:50:04.834862-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-15", "training_samples": 5782, "window": 5}
2026-09-15T14:50:04.834862-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 35700.0, "asset_type": "option", "contract_symbol": "TMUS261016C00185000", "contracts": 70, "early_entry_score": 0.689, "entry_mode": "regular", "entry_option_price": 5.1, "execution_mode": "option", "matched_signals": 25, "option_liquidity_status": "ok", "option_open_interest": 294.0, "option_spread_pct": 7.84, "option_volume": 103.0, "success_rate": 96.0, "ticker": "TMUS", "timing_score": 0.517}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916100005)

</details>
