# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:55:06 EST`
Last processed slot: `manage_1200`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           58.33               12            3.91              1.66         59.84               129.60         0.727            pass              0.198             37.4                           0.609              -37.41             -4.994            downtrend_blocked_slope           False                  False
  FTNT           91.84               49            0.04              0.03        128.10                91.30         0.649            pass              0.876             98.5                           0.553              -26.42             -4.256 downtrend_blocked_slope_and_streak           False                  False
  REGN           75.00               12            1.85             12.61        967.96                48.26         0.551            pass              0.200             43.8                           0.400               18.58              2.141                                 ok           False                  False
    ZS           91.67               36            0.93              1.47        224.46                64.45         0.534            pass              0.712             58.1                           0.522               -3.61             -0.933 downtrend_blocked_slope_and_streak           False                  False
  NVDA           78.95               19            1.21              1.75        205.94                32.59         0.507            pass              0.280             56.5                           0.651               -8.01             -0.709 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67                9            2.58             28.00       1540.14                44.05         0.505            pass              0.187             45.3                           0.751               -9.70             -0.560            downtrend_blocked_slope           False                  False
  TEAM           95.65               23            1.92              2.57        189.95                53.65         0.500            pass              0.655             39.4                           0.365              -16.90             -2.285            downtrend_blocked_slope           False                  False
  DRAM           62.50               16            3.48              1.16         47.14                69.30         0.500            pass              0.213             41.1                           0.630               -6.47             -0.185                                 ok           False                  False
  AVGO           75.00               32            0.90              2.10        331.23                44.04         0.492 below_threshold              0.409             71.2                           0.799               -2.57             -0.025                                 ok           False                  False
  PANW           82.22               45            0.15              0.37        350.04                58.95         0.485 below_threshold              0.590             93.9                           0.583                0.70             -0.399                                 ok           False                  False
  LRCX           60.87               23            2.39              3.85        229.07                62.98         0.481 below_threshold              0.257             40.7                           0.472              -13.65             -0.626            downtrend_blocked_slope           False                  False
  MCHP           92.59               27            1.35              0.74         77.58                45.40         0.455 below_threshold              0.722             75.9                           0.896               -0.39              0.263                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:45:05.372887-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:40:03.980969-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:35:05.266988-05:00 early_entry_1135 early_entry_shadow  {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "entry_ask": 9.15, "entry_bid": 8.25, "entry_mode": "early", "entry_option_price": 8.7, "hypothetical_budget": 64815.78, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 10.34, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "matched_signals": 31, "recovery_stability_score": 0.72, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:30:01.206100-05:00 early_entry_1130 early_entry_shadow {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "entry_ask": 9.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.025, "hypothetical_budget": 64815.78, "hypothetical_contracts": 71, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 11.63, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "matched_signals": 30, "recovery_stability_score": 0.671, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:25:01.112223-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:10:06.095882-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104115506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104115506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104115506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104115506)

</details>
