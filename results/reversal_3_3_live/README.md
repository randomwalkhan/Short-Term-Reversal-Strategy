# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 14:20:06 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               22            1.77              3.78        303.93                65.52         0.584          pass              0.568             46.2                           0.449                0.70              0.267                                 ok            True                  False
   ADI           86.67               30            0.88              2.43        391.71                55.85         0.572          pass              0.558             63.3                           0.638               -1.99              0.093                                 ok            True                  False
   LIN          100.00               10            1.37              5.03        520.39                20.66         0.564          pass              0.521             21.4                           0.329               -0.69             -0.307                                 ok            True                  False
   AEP           83.33               12            1.27              1.20        134.43                21.64         0.564          pass              0.199             13.4                           0.153               -2.62             -0.213                                 ok            True                  False
  NXPI           86.21               29            1.16              2.31        282.88                58.07         0.542          pass              0.541             65.0                           0.669               -0.16              0.265                                 ok            True                  False
   WBD           83.33               12            1.04              0.20         27.39                20.00         0.536          pass              0.270             38.0                           0.469                2.01              0.271                                 ok            True                  False
   XEL          100.00               18            0.81              0.46         79.97                21.57         0.521          pass              0.581             25.3                           0.360               -0.97             -0.097                                 ok            True                  False
  MDLZ           93.33               15            0.45              0.19         58.72                30.54         0.627          pass              0.665             71.2                           0.396                1.20             -0.081                                 ok           False                  False
  KLAC           80.00               20            3.12              5.03        228.21               109.33         0.608          pass              0.272             48.3                           0.592              -26.03             -2.053 downtrend_blocked_slope_and_streak           False                  False
  SOXL           85.00               20            7.35              9.09        172.77               219.49         0.585          pass              0.412             51.3                           0.500              -38.63             -3.100            downtrend_blocked_slope           False                  False
  CTSH           83.72               43            0.05              0.01         43.02                65.21         0.584          pass              0.611             84.6                           0.448               11.05              0.885                                 ok           False                  False
  QCOM           87.50               40            0.07              0.09        178.06                61.79         0.579          pass              0.746             96.1                           0.755               -3.69             -0.047           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-07-15T12:00:03.706415-04:00 early_entry_1200 early_entry_shadow                                   {"contract_symbol": "CRWD260821C00210000", "current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "entry_ask": 14.6, "entry_bid": 14.25, "entry_mode": "early", "entry_option_price": 14.425, "hypothetical_budget": 15315.13, "hypothetical_contracts": 10, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1292.0, "option_spread_pct": 2.43, "option_volume": 518.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.726, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "matched_signals": 39, "recovery_stability_score": 0.726, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-15T11:55:06.679355-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:50:02.876804-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:45:04.888686-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:40:05.824741-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "entry_ask": 109.0, "entry_bid": 89.0, "entry_mode": "early", "entry_option_price": 99.0, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.2, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "matched_signals": 30, "recovery_stability_score": 0.731, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:35:03.044078-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:30:02.764880-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "entry_ask": 109.0, "entry_bid": 88.7, "entry_mode": "early", "entry_option_price": 98.85, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.54, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "matched_signals": 30, "recovery_stability_score": 0.806, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:25:06.537726-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:20:02.933836-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:15:06.015471-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715142006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715142006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715142006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715142006)

</details>
