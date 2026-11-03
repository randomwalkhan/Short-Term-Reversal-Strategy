# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 10:25:06 EST`
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

- Cash: `$136,446.55`
- Equity: `$136,446.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.91               11            1.11              0.52         66.16                28.20         0.599          pass              0.495             46.0                           0.681                2.58              0.258                                 ok            True                  False
 CMCSA           90.48               21            0.52              0.09         23.83                32.70         0.576          pass              0.620             70.0                           0.650                6.19              0.548                                 ok            True                  False
   ROP           85.71               21            1.22              4.09        477.79                37.35         0.548          pass              0.430             49.9                           0.711               18.96              1.699                                 ok            True                  False
   KHC           80.00               15            1.70              0.30         24.80                33.68         0.547          pass              0.186             32.5                           0.591                2.83              0.159                                 ok            True                  False
   ADP           82.35               17            1.17              2.46        297.73                27.85         0.540          pass              0.301             46.0                           0.641                0.86             -0.197                                 ok            True                  False
   XEL           82.35               17            0.89              0.50         79.12                19.18         0.519          pass              0.262             33.6                           0.458                2.53              0.279                                 ok            True                  False
   EXC           85.71               21            0.83              0.27         46.33                22.18         0.517          pass              0.397             39.8                           0.498                7.05              0.729                                 ok            True                  False
  ALNY           89.13               46            0.32              0.36        157.85               108.76         0.675          pass              0.691             60.2                           0.353              -31.74             -4.337 downtrend_blocked_slope_and_streak           False                  False
  TMUS           55.56                9            2.31              2.59        159.04                68.40         0.646          pass              0.112             15.7                           0.266               -0.82              0.086                                 ok           False                  False
  IDXX           92.68               41            0.34              1.61        670.95                75.67         0.637          pass              0.859             85.7                           0.820               19.97              1.494                                 ok           False                  False
  MRVL           90.24               41            0.37              0.45        171.22                97.23         0.585          pass              0.749             72.4                           0.317              -28.97             -3.218 downtrend_blocked_slope_and_streak           False                  False
   PEP           77.78                9            1.52              1.50        139.78                26.86         0.571          pass              0.123             21.9                           0.377                3.18              0.218                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-03T10:25:06.138898-05:00 early_entry_1025 early_entry_shadow                                                {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "entry_ask": 3.55, "entry_bid": 3.25, "entry_mode": "early", "entry_option_price": 3.4, "hypothetical_budget": 68223.28, "hypothetical_contracts": 200, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 3546.0, "option_spread_pct": 8.82, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "matched_signals": 39, "recovery_stability_score": 0.776, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-03T10:20:04.960698-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "entry_ask": 33.3, "entry_bid": 26.8, "entry_mode": "early", "entry_option_price": 30.05, "hypothetical_budget": 68223.28, "hypothetical_contracts": 22, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.63, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "matched_signals": 39, "recovery_stability_score": 0.743, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:20:04.960698-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CEG261218C00260000", "fill_price": 21.05, "pnl": 9520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.34, "ticker": "CEG"}
2026-11-03T10:15:05.119649-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:10:03.895876-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:05:06.784837-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:00:06.027735-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T00:00:06.091042-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-02T15:10:04.822162-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-11-02T15:05:06.352149-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103102506)

</details>
