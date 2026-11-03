# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 10:20:04 EST`
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
  IDXX           92.31               39            0.53              2.48        670.58                75.67         0.637          pass              0.819             78.0                           0.743               19.75              1.485                                 ok            True                   True
 CMCSA           92.86               14            0.92              0.15         23.80                32.70         0.597          pass              0.571             47.1                           0.519                5.77              0.529                                 ok            True                  False
  MDLZ           90.91               11            1.28              0.60         66.12                28.20         0.589          pass              0.470             38.0                           0.627                2.41              0.250                                 ok            True                  False
   ROP           82.35               17            1.34              4.50        477.61                37.35         0.562          pass              0.300             44.9                           0.658               18.81              1.694                                 ok            True                  False
   KHC           80.00               10            2.01              0.35         24.78                33.68         0.561          pass              0.118             20.6                           0.377                2.52              0.145                                 ok            True                  False
  CTAS           95.83               24            0.80              1.26        224.23                26.23         0.527          pass              0.702             51.9                           0.552                2.73              0.042                                 ok            True                  False
   XEL           80.00               15            1.01              0.56         79.09                19.18         0.523          pass              0.161             25.2                           0.394                2.41              0.274                                 ok            True                  False
  FAST           96.30               27            0.51              0.19         52.47                22.62         0.514          pass              0.715             50.0                           0.455                1.73              0.090                                 ok            True                  False
  ALNY           89.80               49            0.13              0.15        157.94               108.76         0.670          pass              0.779             83.6                           0.451              -31.61             -4.328 downtrend_blocked_slope_and_streak           False                  False
  TMUS           55.56                9            2.31              2.59        159.04                68.40         0.646          pass              0.111             15.6                           0.322               -0.83              0.086                                 ok           False                  False
   PEP           83.33                6            1.56              1.53        139.76                26.86         0.593          pass              0.208             20.1                           0.344                3.14              0.216                                 ok           False                  False
  PAYX           50.00                2            2.03              1.64        114.79                35.36         0.569          pass              0.160             34.5                           0.547                1.49             -0.112                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-03T10:20:04.960698-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "entry_ask": 33.3, "entry_bid": 26.8, "entry_mode": "early", "entry_option_price": 30.05, "hypothetical_budget": 68223.28, "hypothetical_contracts": 22, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.63, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "matched_signals": 39, "recovery_stability_score": 0.743, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:20:04.960698-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CEG261218C00260000", "fill_price": 21.05, "pnl": 9520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.34, "ticker": "CEG"}
2026-11-03T10:15:05.119649-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:10:03.895876-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:05:06.784837-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:00:06.027735-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T00:00:06.091042-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-02T15:10:04.822162-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-11-02T15:05:06.352149-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-11-02T15:00:04.459159-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103102004)

</details>
