# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:35:06 EDT`
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
  PYPL           92.00               25            0.90              0.34         53.88                58.07         0.645          pass              0.509              8.0                           0.137                1.92              0.007                                 ok            True                  False
    ZS           97.14               35            1.05              1.41        191.13                82.09         0.621          pass              0.798             56.6                           0.409                0.71             -0.010                                 ok            True                  False
  TEAM          100.00               26            2.33              3.14        191.42                63.46         0.547          pass              0.628             22.0                           0.170               -3.03             -0.336                                 ok            True                  False
   ADP           95.24               21            0.74              1.44        276.01                26.20         0.541          pass              0.694             55.5                           0.404               -3.44             -0.484                                 ok            True                  False
  FTNT           90.48               42            0.63              0.76        169.86                60.22         0.524          pass              0.779             82.5                           0.516               -1.07              0.195                                 ok            True                  False
  CTSH           96.67               30            1.17              0.53         63.87                45.53         0.513          pass              0.782             65.8                           0.332               -1.90             -0.446                                 ok            True                  False
  MSFT          100.00               18            1.33              4.70        503.40                22.76         0.511          pass              0.529              8.2                           0.123               -1.69             -0.131                                 ok            True                  False
  AAPL           85.71               21            1.18              2.75        331.90                23.75         0.506          pass              0.327             16.9                           0.185                3.88              0.299                                 ok            True                  False
  AMGN           93.33               15            1.10              2.93        380.24                45.29         0.626          pass              0.542             30.3                           0.523              -12.23             -1.905 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.61               46            0.12              0.32        373.80                81.04         0.605          pass              0.611             93.6                           0.751               -2.26              0.072                                 ok           False                  False
   KHC           93.33               15            0.35              0.06         24.24                26.10         0.585          pass              0.698             83.7                           0.855               -4.39             -0.512            downtrend_blocked_slope           False                  False
  MSTR           81.25               16            4.87              4.67        134.94               103.17         0.583          pass              0.159              9.1                           0.252               -2.01              0.127           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-15T10:35:06.132265-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:30:04.241835-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "entry_ask": 9.9, "entry_bid": 9.25, "entry_mode": "early", "entry_option_price": 9.575, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 602.0, "option_spread_pct": 6.79, "option_volume": 100.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "matched_signals": 42, "recovery_stability_score": 0.581, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.778, "early_reclaim_pct": 74.8, "matched_signals": 38, "recovery_stability_score": 0.752, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:25:01.133088-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                            {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "entry_ask": 4.8, "entry_bid": 4.3, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 36158.05, "hypothetical_contracts": 79, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 10.99, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.739, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "matched_signals": 38, "recovery_stability_score": 0.739, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:20:02.316834-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "entry_ask": 4.8, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.5, "hypothetical_budget": 36158.05, "hypothetical_contracts": 80, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "matched_signals": 38, "recovery_stability_score": 0.753, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:15:01.098518-04:00 early_entry_1015 early_entry_shadow       {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "entry_ask": 13.8, "entry_bid": 12.0, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 13.95, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "matched_signals": 38, "recovery_stability_score": 0.618, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 67.1, "matched_signals": 34, "recovery_stability_score": 0.698, "success_rate": 91.18, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:10:06.048953-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "entry_ask": 4.4, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 93, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 28.57, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:05:04.072258-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "entry_ask": 14.15, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 11.19, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "matched_signals": 38, "recovery_stability_score": 0.593, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:00:04.052597-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "EXC261016C00043000", "fill_price": 0.855, "pnl": -3800.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "EXC"}
2026-09-15T10:00:04.052597-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                        {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "entry_ask": 10.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.525, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 602.0, "option_spread_pct": 21.52, "option_volume": 98.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "matched_signals": 42, "recovery_stability_score": 0.701, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915103506)

</details>
