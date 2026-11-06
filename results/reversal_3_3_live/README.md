# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 11:05:04 EST`
Last processed slot: `manage_1100`

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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.75               16            0.88              0.23         36.79                35.93         0.580          pass              0.682             72.5                           0.670                5.44              0.608                                 ok            True                  False
 CMCSA           92.31               13            1.34              0.23         24.85                35.54         0.560          pass              0.601             65.5                           0.567                8.48              1.404                                 ok            True                  False
   KHC           84.62               13            1.88              0.33         25.18                36.03         0.534          pass              0.355             52.9                           0.592                0.18              0.334                                 ok            True                  False
  COST           85.00               20            0.78              5.85       1063.08                23.23         0.531          pass              0.448             65.0                           0.543                5.53              0.722                                 ok            True                  False
  ORLY           93.75               16            1.39              0.89         91.11                25.42         0.511          pass              0.622             54.8                           0.492                0.33              0.126                                 ok            True                  False
  CTAS           95.00               20            1.06              1.69        225.69                27.57         0.508          pass              0.706             63.0                           0.602               -0.04              0.299                                 ok            True                  False
   PEP           81.82               22            0.92              0.92        142.31                27.68         0.504          pass              0.393             71.2                           0.568                4.14              0.657                                 ok            True                  False
  FTNT           81.48               27            1.70              1.46        121.89                92.45         0.654          pass              0.284             21.8                           0.282              -33.09             -4.913 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.83               46            0.02              0.12        670.66                77.01         0.626          pass              0.960             99.2                           0.788               19.66              2.465                                 ok           False                  False
  ISRG           87.50                8            2.11              6.92        465.56                42.48         0.569          pass              0.320             21.1                           0.300                1.40              0.371                                 ok           False                  False
   EXC           66.67                3            1.48              0.48         46.32                23.57         0.565          pass              0.189             44.1                           0.427                3.17              0.433                                 ok           False                  False
  MDLZ           95.24               21            0.46              0.21         66.73                30.66         0.563          pass              0.790             86.9                           0.643                4.26              0.764                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-06T11:05:04.861391-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:00:05.853352-05:00 early_entry_1100 early_entry_shadow   {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "entry_ask": 2.4, "entry_bid": 2.28, "entry_mode": "early", "entry_option_price": 2.34, "hypothetical_budget": 61581.4, "hypothetical_contracts": 263, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 5.13, "option_volume": 85.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.583, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "matched_signals": 37, "recovery_stability_score": 0.583, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:55:05.752017-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:50:06.578402-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:45:05.896863-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:40:04.864524-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:35:02.947980-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:30:05.862007-05:00 early_entry_1030 early_entry_shadow {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "entry_ask": 21.65, "entry_bid": 21.1, "entry_mode": "early", "entry_option_price": 21.375, "hypothetical_budget": 61581.4, "hypothetical_contracts": 28, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 2.57, "option_volume": 42.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "matched_signals": 30, "recovery_stability_score": 0.763, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:25:04.812264-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:20:05.873622-05:00 early_entry_1020 early_entry_shadow   {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "entry_ask": 19.7, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.15, "hypothetical_budget": 61581.4, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 5.74, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "matched_signals": 30, "recovery_stability_score": 0.749, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106110504)

</details>
