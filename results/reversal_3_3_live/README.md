# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 11:15:04 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               12            1.23              0.41         47.92                27.18         0.585          pass              0.577             35.2                           0.267                4.44              0.458                                 ok            True                  False
   XEL          100.00               12            1.19              0.67         80.04                19.80         0.572          pass              0.534             21.1                           0.218               -0.99              0.092                                 ok            True                  False
   CSX           95.83               24            0.56              0.20         50.75                28.82         0.546          pass              0.629             26.9                           0.181                2.28              0.301                                 ok            True                  False
   MAR          100.00               23            1.01              2.71        382.36                28.18         0.541          pass              0.689             49.4                           0.340                4.53              0.394                                 ok            True                  False
  ISRG           72.73               22            1.35              3.42        360.34                72.57         0.648          pass              0.279             44.6                           0.346               -8.24             -0.884                                 ok           False                  False
  TMUS           90.62               32            0.63              0.80        182.05                56.22         0.574          pass              0.640             50.9                           0.330               -3.40             -0.875            downtrend_blocked_slope           False                  False
  META           93.02               43            0.35              1.44        592.79                53.87         0.558          pass              0.815             70.8                           0.679              -13.20             -1.505 downtrend_blocked_slope_and_streak           False                  False
   KDP           91.18               34            0.08              0.02         31.07                34.46         0.552          pass              0.779             88.6                           0.378                2.63              0.026                                 ok           False                  False
   EXC           96.00               25            0.36              0.12         47.26                23.57         0.548          pass              0.713             52.8                           0.352                0.47              0.222                                 ok           False                  False
  MSTR           77.78               45            0.28              0.19         96.08                69.55         0.547          pass              0.480             75.0                           0.600               -1.62             -0.052                                 ok           False                  False
  GILD           90.00               30            0.47              0.44        134.13                34.28         0.513          pass              0.641             63.4                           0.638                2.81             -0.014                                 ok           False                  False
  SHOP           88.89               45            0.01              0.01        130.28                56.09         0.510          pass              0.786             99.5                           0.795                5.44              0.199                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-29T11:15:04.531641-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:10:04.418819-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:05:04.380925-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:00:05.486916-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:55:01.499037-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:50:04.275621-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "IDXX260918C00570000", "current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "entry_ask": 38.2, "entry_bid": 34.2, "entry_mode": "early", "entry_option_price": 36.2, "hypothetical_budget": 17477.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 2.0, "option_spread_pct": 11.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.552, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "matched_signals": 40, "recovery_stability_score": 0.552, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:45:02.234081-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:40:06.811413-04:00 early_entry_1040 early_entry_shadow                 {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "entry_ask": 20.1, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 19.25, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 8.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.659, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:35:06.000891-04:00 early_entry_1035 early_entry_shadow                      {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "entry_ask": 20.1, "entry_bid": 18.7, "entry_mode": "early", "entry_option_price": 19.4, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 7.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.647, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "matched_signals": 30, "recovery_stability_score": 0.647, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:30:04.319629-04:00 early_entry_1030 early_entry_shadow                 {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "entry_ask": 20.1, "entry_bid": 17.9, "entry_mode": "early", "entry_option_price": 19.0, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 11.58, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.788, "early_reclaim_pct": 65.8, "matched_signals": 31, "recovery_stability_score": 0.642, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729111504)

</details>
