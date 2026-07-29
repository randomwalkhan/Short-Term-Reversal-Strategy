# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 11:25:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               10            1.43              0.48         47.89                27.18         0.584            pass              0.531             24.2                           0.214                4.22              0.448                                 ok            True                  False
   XEL          100.00               12            1.17              0.66         80.05                19.80         0.573            pass              0.538             22.3                           0.295               -0.97              0.093                                 ok            True                  False
   CSX           96.00               25            0.52              0.19         50.76                28.82         0.542            pass              0.650             32.1                           0.240                2.32              0.303                                 ok            True                  False
   MAR          100.00               23            1.01              2.72        382.35                28.18         0.541            pass              0.688             49.2                           0.329                4.53              0.394                                 ok            True                  False
  ISRG           73.68               19            1.74              4.42        359.91                72.57         0.643            pass              0.209             28.4                           0.224               -8.61             -0.902                                 ok           False                  False
  TMUS           90.91               33            0.53              0.68        182.10                56.22         0.574            pass              0.677             58.3                           0.421               -3.31             -0.870            downtrend_blocked_slope           False                  False
  META           92.50               40            0.48              1.98        592.56                53.87         0.568            pass              0.769             59.8                           0.664              -13.32             -1.511 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.83               24            0.48              0.16         47.24                23.57         0.547            pass              0.661             37.5                           0.345                0.35              0.217                                 ok           False                  False
  MSTR           76.74               43            0.68              0.45         95.97                69.55         0.532            pass              0.373             39.8                           0.380               -2.01             -0.070                                 ok           False                  False
  GILD           90.00               30            0.48              0.45        134.13                34.28         0.512            pass              0.640             62.8                           0.714                2.80             -0.015                                 ok           False                  False
   LIN           90.91               22            1.00              3.57        509.65                21.60         0.506            pass              0.445              7.9                           0.184               -3.15             -0.284            downtrend_blocked_slope           False                  False
  PCAR           90.91               11            1.98              1.92        137.39                29.38         0.497 below_threshold              0.348              0.4                           0.029                9.30              1.024                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-29T11:25:01.480196-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:20:05.598758-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:15:04.531641-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:10:04.418819-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:05:04.380925-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:00:05.486916-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:55:01.499037-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:50:04.275621-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "IDXX260918C00570000", "current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "entry_ask": 38.2, "entry_bid": 34.2, "entry_mode": "early", "entry_option_price": 36.2, "hypothetical_budget": 17477.38, "hypothetical_contracts": 4, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 2.0, "option_spread_pct": 11.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.552, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.855, "early_reclaim_pct": 96.9, "matched_signals": 40, "recovery_stability_score": 0.552, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.309, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-29T10:45:02.234081-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:40:06.811413-04:00 early_entry_1040 early_entry_shadow                 {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "entry_ask": 20.1, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 19.25, "hypothetical_budget": 17477.38, "hypothetical_contracts": 9, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 1134.0, "option_spread_pct": 8.83, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.806, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.659, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.507, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729112501)

</details>
