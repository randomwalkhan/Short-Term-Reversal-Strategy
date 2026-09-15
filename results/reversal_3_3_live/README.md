# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:00:04 EDT`
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

- Cash: `$72,316.10`
- Equity: `$72,316.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.37               38            0.82              1.11        191.26                82.09         0.616          pass              0.846             65.9                           0.474                0.94             -0.000                                 ok            True                  False
  PANW           80.95               42            0.62              1.62        373.24                81.04         0.598          pass              0.488             67.7                           0.459               -2.75              0.049                                 ok            True                  False
  MSTR           81.82               22            4.11              3.94        135.25               103.17         0.591          pass              0.257             23.3                           0.356               -1.23              0.163                                 ok            True                  False
   WMT           84.38               32            0.51              0.39        108.91                40.03         0.570          pass              0.429             36.3                           0.339                3.48              0.233                                 ok            True                  False
  TEAM          100.00               31            1.48              2.00        191.91                63.46         0.567          pass              0.748             50.5                           0.416               -2.19             -0.297                                 ok            True                  False
  FTNT           90.48               42            0.52              0.62        169.92                60.22         0.532          pass              0.790             85.8                           0.701               -0.95              0.200                                 ok            True                   True
   AEP           87.50               16            0.73              0.62        121.96                16.70         0.519          pass              0.351             19.8                           0.207               -0.89             -0.085                                 ok            True                  False
  AAPL           88.00               25            0.79              1.84        332.29                23.75         0.507          pass              0.498             44.5                           0.394                4.29              0.317                                 ok            True                  False
  ALNY           85.00               20            2.13              3.73        248.39                49.37         0.507          pass              0.334             27.8                           0.250                1.65             -0.216                                 ok            True                  False
  AMGN           90.91               11            1.47              3.92        379.82                45.29         0.625          pass              0.370              3.2                           0.169              -12.56             -1.922 downtrend_blocked_slope_and_streak           False                  False
  PYPL           92.50               40            0.13              0.05         54.01                58.07         0.607          pass              0.854             86.5                           0.462                2.71              0.042                                 ok           False                  False
  CHTR           92.86               42            0.13              0.13        143.29                68.19         0.568          pass              0.878             93.0                           0.737               -6.08             -0.843            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-15T10:00:04.052597-04:00 early_entry_1000 early_entry_shadow                         {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "entry_ask": 10.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.525, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 602.0, "option_spread_pct": 21.52, "option_volume": 98.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "matched_signals": 42, "recovery_stability_score": 0.701, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:00:04.052597-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "EXC261016C00043000", "fill_price": 0.855, "pnl": -3800.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "EXC"}
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-14T15:00:05.039225-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-14T14:55:02.132179-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-14T14:50:04.030674-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-14", "training_samples": 5764, "window": 5}
2026-09-14T14:50:04.030674-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 38000.0, "asset_type": "option", "contract_symbol": "EXC261016C00043000", "contracts": 400, "early_entry_score": 0.606, "entry_mode": "regular", "entry_option_price": 0.95, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 123.0, "option_spread_pct": 10.53, "option_volume": 93.0, "success_rate": 100.0, "ticker": "EXC", "timing_score": 0.551}
2026-09-14T12:00:04.262790-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "matched_signals": 33, "recovery_stability_score": 0.663, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915100004)

</details>
