# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 10:55:05 EST`
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
  MDLZ           92.86               14            0.90              0.42         66.20                28.20         0.595          pass              0.598             56.2                           0.705                2.80              0.267                                 ok            True                  False
   PEP           81.82               11            1.45              1.43        139.81                26.86         0.567          pass              0.189             25.5                           0.470                3.25              0.221                                 ok            True                  False
   KHC           80.00               15            1.70              0.30         24.80                33.68         0.547          pass              0.186             32.5                           0.582                2.83              0.159                                 ok            True                  False
   ROP           88.00               25            1.14              3.82        477.90                37.35         0.531          pass              0.526             53.3                           0.660               19.06              1.703                                 ok            True                  False
   ADP           88.46               26            0.65              1.35        298.20                27.85         0.522          pass              0.595             70.2                           0.797                1.40             -0.172                                 ok            True                  False
   EXC           86.96               23            0.72              0.23         46.35                22.18         0.512          pass              0.466             47.7                           0.641                7.17              0.734                                 ok            True                  False
   XEL           86.96               23            0.63              0.35         79.18                19.18         0.503          pass              0.482             53.3                           0.722                2.80              0.291                                 ok            True                  False
  TMUS           60.00               10            2.07              2.32        159.16                68.40         0.658          pass              0.139             24.5                           0.365               -0.58              0.098                                 ok           False                  False
  MRVL           90.00               40            0.47              0.57        171.17                97.23         0.584          pass              0.720             65.1                           0.365              -29.04             -3.223 downtrend_blocked_slope_and_streak           False                  False
  PAYX           63.64               11            1.07              0.87        115.12                35.36         0.583          pass              0.261             65.3                           0.817                2.48             -0.068                                 ok           False                  False
 CMCSA           92.86               28            0.02              0.00         23.87                32.70         0.566          pass              0.816             98.8                           0.882                6.73              0.571                                 ok           False                  False
   CSX           75.00               12            1.13              0.41         51.44                27.65         0.560          pass              0.164             31.6                           0.510                6.15              0.585                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-03T10:55:05.970636-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:50:06.376487-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:45:05.029360-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:40:06.271998-05:00 early_entry_1040 early_entry_shadow     {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 101, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.76, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:35:07.004174-05:00 early_entry_1035 early_entry_shadow   {"contract_symbol": "CTAS261204C00225000", "current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "entry_ask": 6.4, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 118, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.61, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "matched_signals": 32, "recovery_stability_score": 0.762, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:30:03.257135-05:00 early_entry_1030 early_entry_shadow   {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.56, "early_entry_score": 0.789, "early_reclaim_pct": 66.4, "entry_ask": 7.3, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.65, "hypothetical_budget": 68223.28, "hypothetical_contracts": 102, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 19.55, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.752, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.789, "early_reclaim_pct": 66.4, "matched_signals": 31, "recovery_stability_score": 0.752, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:25:06.138898-05:00 early_entry_1025 early_entry_shadow                                                {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "entry_ask": 3.55, "entry_bid": 3.25, "entry_mode": "early", "entry_option_price": 3.4, "hypothetical_budget": 68223.28, "hypothetical_contracts": 200, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 3546.0, "option_spread_pct": 8.82, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.705, "early_reclaim_pct": 69.4, "matched_signals": 39, "recovery_stability_score": 0.776, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-03T10:20:04.960698-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "entry_ask": 33.3, "entry_bid": 26.8, "entry_mode": "early", "entry_option_price": 30.05, "hypothetical_budget": 68223.28, "hypothetical_contracts": 22, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.63, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.819, "early_reclaim_pct": 78.0, "matched_signals": 39, "recovery_stability_score": 0.743, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:20:04.960698-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CEG261218C00260000", "fill_price": 21.05, "pnl": 9520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.34, "ticker": "CEG"}
2026-11-03T10:15:05.119649-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103105505)

</details>
