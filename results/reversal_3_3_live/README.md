# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 11:05:06 EST`
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
  MDLZ           90.91               11            1.30              0.60         66.12                28.20         0.589          pass              0.468             37.2                           0.367                2.39              0.249                                 ok            True                  False
   KHC           80.00               10            2.03              0.35         24.78                33.68         0.559          pass              0.115             19.8                           0.278                2.50              0.144                                 ok            True                  False
   ADP           86.96               23            0.73              1.53        298.12                27.85         0.534          pass              0.524             66.3                           0.684                1.31             -0.176                                 ok            True                  False
  CTAS           96.00               25            0.73              1.15        224.28                26.23         0.525          pass              0.721             56.3                           0.478                2.81              0.046                                 ok            True                  False
   EXC           85.71               21            0.83              0.27         46.33                22.18         0.517          pass              0.397             39.8                           0.532                7.05              0.729                                 ok            True                  False
  FAST           96.30               27            0.52              0.19         52.47                22.62         0.514          pass              0.712             49.1                           0.413                1.72              0.089                                 ok            True                  False
   ROP           86.67               30            0.95              3.20        478.17                37.35         0.509          pass              0.545             60.8                           0.684               19.28              1.712                                 ok            True                  False
   XEL           86.36               22            0.70              0.39         79.16                19.18         0.504          pass              0.445             48.1                           0.646                2.73              0.288                                 ok            True                  False
  TMUS           63.64               11            1.79              2.01        159.29                68.40         0.671          pass              0.178             34.6                           0.454               -0.30              0.110                                 ok           False                  False
  IDXX           93.33               45            0.24              1.15        671.15                75.67         0.616          pass              0.887             89.8                           0.731               20.09              1.498                                 ok           False                  False
  MRVL           90.24               41            0.11              0.13        171.35                97.23         0.601          pass              0.809             92.0                           0.501              -28.78             -3.206 downtrend_blocked_slope_and_streak           False                  False
   PEP           83.33                6            1.58              1.55        139.76                26.86         0.592          pass              0.206             19.2                           0.324                3.12              0.216                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-03T11:05:06.948885-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:00:05.972600-05:00 early_entry_1100 early_entry_shadow    {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "entry_ask": 7.5, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 6.8, "hypothetical_budget": 68223.28, "hypothetical_contracts": 100, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 20.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.675, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:55:05.970636-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:50:06.376487-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:45:05.029360-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:40:06.271998-05:00 early_entry_1040 early_entry_shadow     {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 101, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.76, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:35:07.004174-05:00 early_entry_1035 early_entry_shadow   {"contract_symbol": "CTAS261204C00225000", "current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "entry_ask": 6.4, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 118, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.61, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "matched_signals": 32, "recovery_stability_score": 0.762, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:30:03.257135-05:00 early_entry_1030 early_entry_shadow   {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.56, "early_entry_score": 0.789, "early_reclaim_pct": 66.4, "entry_ask": 7.3, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.65, "hypothetical_budget": 68223.28, "hypothetical_contracts": 102, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 19.55, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.752, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.789, "early_reclaim_pct": 66.4, "matched_signals": 31, "recovery_stability_score": 0.752, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:25:06.138898-05:00 early_entry_1025 early_entry_shadow                                                {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "entry_ask": 3.55, "entry_bid": 3.25, "entry_mode": "early", "entry_option_price": 3.4, "hypothetical_budget": 68223.28, "hypothetical_contracts": 200, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 3546.0, "option_spread_pct": 8.82, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "matched_signals": 39, "recovery_stability_score": 0.776, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-03T10:20:04.960698-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "entry_ask": 33.3, "entry_bid": 26.8, "entry_mode": "early", "entry_option_price": 30.05, "hypothetical_budget": 68223.28, "hypothetical_contracts": 22, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.63, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "matched_signals": 39, "recovery_stability_score": 0.743, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103110506)

</details>
