# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 09:37:23 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INSM           84.21               38            0.95              0.88        131.90               107.72         0.747          pass              0.506             44.2                           0.317               29.10              3.855                       ok            True                  False
  FAST          100.00               19            0.86              0.31         52.09                25.01         0.582          pass              0.518              0.0                           0.250               10.95              1.179                       ok            True                  False
  BKNG           96.55               29            1.18              1.76        211.51                44.60         0.568          pass              0.584              0.0                           0.250                8.54              1.173                       ok            True                  False
   BKR           84.62               13            1.73              0.78         63.95                33.24         0.561          pass              0.278             26.2                           0.209                5.84              0.758                       ok            True                  False
  ISRG           86.49               37            0.47              1.32        400.70                69.94         0.667          pass              0.516             31.9                           0.303               13.15              1.332                       ok           False                  False
   TRI           87.80               41            0.25              0.18        102.53                74.92         0.618          pass              0.751             93.8                           0.844                3.56              0.393                       ok           False                  False
  ABNB           95.65               46            0.00              0.00        180.09                64.05         0.611          pass              0.958             98.9                           0.497               17.70              2.251                       ok           False                  False
  DXCM           90.70               43            0.01              0.01         90.80                59.17         0.604          pass              0.839             97.8                           0.642               21.80              1.241                       ok           False                  False
   ROP           97.50               40            0.01              0.03        395.22                44.32         0.590          pass              0.950             97.0                           0.681                1.52              0.205                       ok           False                  False
  ROST           83.33               12            1.58              2.74        247.08                22.10         0.529          pass              0.251             32.0                           0.308               -3.26             -0.133 downtrend_blocked_streak           False                  False
  DASH          100.00               43            0.42              0.62        212.22                48.36         0.527          pass              0.839             62.0                           0.369                9.34              1.046                       ok           False                  False
   HON           92.31               39            0.26              0.43        235.16                35.57         0.519          pass              0.691             39.3                           0.339               -2.97             -0.584  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-12T16:10:05.737758-04:00      manage_1600                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T14:50:05.779182-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"early_entry_score": 0.604, "option_liquidity_status": "low_volume", "option_open_interest": 178.0, "option_spread_pct": 8.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.806}
2026-08-12T14:50:05.779182-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-12", "training_samples": 5645, "window": 5}
2026-08-12T14:50:05.779182-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 17360.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 62, "early_entry_score": 0.819, "entry_mode": "regular", "entry_option_price": 2.8, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7246.0, "option_spread_pct": 5.71, "option_volume": 86.0, "success_rate": 93.94, "ticker": "PYPL", "timing_score": 0.657}
2026-08-12T12:00:04.666373-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T11:55:01.784821-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "BKNG260911C00210000", "current_drop_pct": 1.06, "early_entry_score": 0.858, "early_reclaim_pct": 95.4, "entry_ask": 8.3, "entry_bid": 7.3, "entry_mode": "early", "entry_option_price": 7.8, "hypothetical_budget": 17549.0, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 53.0, "option_spread_pct": 12.82, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 96.77, "ticker": "BKNG", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.858, "early_reclaim_pct": 95.4, "matched_signals": 31, "recovery_stability_score": 0.759, "success_rate": 96.77, "ticker": "BKNG", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813093723)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813093723)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813093723)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813093723)

</details>
