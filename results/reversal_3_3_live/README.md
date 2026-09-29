# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 10:30:04 EDT`
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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.29               35            0.84              0.92        156.74                99.69         0.709          pass              0.724             35.3                           0.237               20.23              2.185                                 ok            True                  False
    ZS           97.56               41            0.67              0.93        198.99                81.58         0.594          pass              0.866             68.9                           0.693                2.15              0.365                                 ok            True                   True
  CTAS           91.67               12            1.61              2.26        199.61                21.05         0.518          pass              0.385              3.0                           0.118               -0.80             -0.012                                 ok            True                  False
   KDP           93.75               16            1.10              0.24         31.36                25.35         0.514          pass              0.649             63.6                           0.414               -0.47              0.039                                 ok            True                  False
  AMGN           85.29               34            0.41              1.20        417.61                46.33         0.579          pass              0.548             62.9                           0.342               10.85              1.213                                 ok           False                  False
   TRI           88.24               34            0.81              0.55         97.09                56.59         0.575          pass              0.616             59.5                           0.536               -5.92             -0.297            downtrend_blocked_slope           False                  False
   WBD           95.00               40            0.15              0.03         30.89                38.06         0.574          pass              0.842             61.5                           0.466               10.08              1.215                                 ok           False                  False
  TMUS           78.95               19            1.27              1.48        165.81                33.31         0.537          pass              0.187             24.6                           0.312               -8.94             -0.680            downtrend_blocked_slope           False                  False
  PANW           68.00               25            2.67              7.33        388.95                69.78         0.519          pass              0.230             25.9                           0.398                1.74              0.410                                 ok           False                  False
  CDNS           65.00               20            1.98              4.54        324.76                46.51         0.510          pass              0.265             49.0                           0.570               16.89              1.958                                 ok           False                  False
   KHC           96.15               26            0.11              0.02         23.55                18.37         0.505          pass              0.834             92.2                           0.677               -4.83             -0.590 downtrend_blocked_slope_and_streak           False                  False
  ADSK           80.00               30            1.28              1.86        206.39                47.99         0.505          pass              0.241             19.1                           0.287               -9.70             -0.859 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-29T10:30:04.372650-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "ZS261120C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.866, "early_reclaim_pct": 68.9, "entry_ask": 21.9, "entry_bid": 19.6, "entry_mode": "early", "entry_option_price": 20.75, "hypothetical_budget": 39379.15, "hypothetical_contracts": 18, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 844.0, "option_spread_pct": 11.08, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.866, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.693, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-29T10:25:05.800774-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ZS261120C00190000", "current_drop_pct": 0.53, "early_entry_score": 0.886, "early_reclaim_pct": 75.2, "entry_ask": 21.9, "entry_bid": 19.6, "entry_mode": "early", "entry_option_price": 20.75, "hypothetical_budget": 39379.15, "hypothetical_contracts": 18, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 844.0, "option_spread_pct": 11.08, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.603, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.886, "early_reclaim_pct": 75.2, "matched_signals": 41, "recovery_stability_score": 0.749, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.603, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-29T10:20:06.606039-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:15:06.005082-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:10:04.385907-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:05:05.319599-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 18.05, "pnl": 8760.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.35, "ticker": "CEG"}
2026-09-29T00:00:05.209830-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 92, 'empty': 1}
2026-09-28T15:10:04.000540-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929103004)

</details>
