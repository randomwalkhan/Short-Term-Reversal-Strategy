# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 11:20:05 EDT`
Last processed slot: `manage_1130`

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
  FAST          100.00               10            1.54              0.52         47.88                27.18         0.577          pass              0.514             18.7                           0.188                4.11              0.444                                 ok            True                  False
   XEL          100.00               13            1.10              0.62         80.07                19.80         0.571          pass              0.559             27.3                           0.289               -0.90              0.097                                 ok            True                  False
   CSX           95.45               22            0.68              0.24         50.74                28.82         0.552          pass              0.570             11.5                           0.116                2.15              0.296                                 ok            True                  False
   EXC           95.65               23            0.54              0.18         47.23                23.57         0.549          pass              0.629             29.2                           0.252                0.29              0.214                                 ok            True                  False
   MAR          100.00               24            0.98              2.64        382.39                28.18         0.536          pass              0.699             50.7                           0.342                4.56              0.395                                 ok            True                  False
  PCAR           90.91               11            1.92              1.86        137.41                29.38         0.502          pass              0.359              3.6                           0.188                9.38              1.027                                 ok            True                  False
   AEP           81.82               11            1.59              1.48        132.38                20.00         0.501          pass              0.138             10.9                           0.139               -2.99             -0.061                                 ok            True                  False
  ISRG           75.00               20            1.49              3.77        360.19                72.57         0.655          pass              0.249             38.9                           0.300               -8.37             -0.891                                 ok           False                  False
  TMUS           90.91               33            0.56              0.71        182.08                56.22         0.573          pass              0.671             56.4                           0.368               -3.33             -0.871            downtrend_blocked_slope           False                  False
  META           93.02               43            0.30              1.24        592.88                53.87         0.561          pass              0.828             74.7                           0.726              -13.16             -1.503 downtrend_blocked_slope_and_streak           False                  False
   KDP           90.91               33            0.17              0.04         31.06                34.46         0.552          pass              0.728             76.1                           0.332                2.54              0.022                                 ok           False                  False
  MSTR           76.74               43            0.61              0.41         95.98                69.55         0.537          pass              0.391             45.8                           0.455               -1.94             -0.067                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-29T11:20:05.598758-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:15:04.531641-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:10:04.418819-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:05:04.380925-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:00:05.486916-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:55:01.499037-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:50:04.275621-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "IDXX260918C00570000", "current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "entry_ask": 38.2, "entry_bid": 34.2, "entry_mode": "early", "entry_option_price": 36.2, "hypothetical_budget": 17477.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 2.0, "option_spread_pct": 11.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.552, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "matched_signals": 40, "recovery_stability_score": 0.552, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:45:02.234081-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:40:06.811413-04:00 early_entry_1040 early_entry_shadow                 {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "entry_ask": 20.1, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 19.25, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 8.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.659, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:35:06.000891-04:00 early_entry_1035 early_entry_shadow                      {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "entry_ask": 20.1, "entry_bid": 18.7, "entry_mode": "early", "entry_option_price": 19.4, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 7.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.647, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.78, "early_reclaim_pct": 65.0, "matched_signals": 30, "recovery_stability_score": 0.647, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729112005)

</details>
