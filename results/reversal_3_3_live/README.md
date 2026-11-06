# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 11:45:04 EST`
Last processed slot: `early_entry_1145`

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
  MDLZ           93.75               16            0.57              0.27         66.71                30.66         0.585          pass              0.716             83.6                           0.551                4.14              0.759                                 ok            True                  False
   PEP           88.24               17            1.07              1.06        142.25                27.68         0.531          pass              0.520             66.9                           0.501                3.99              0.650                                 ok            True                  False
  COST           80.95               21            0.65              4.83       1063.52                23.23         0.530          pass              0.365             71.1                           0.594                5.67              0.728                                 ok            True                  False
   ADP           85.71               21            1.04              2.23        306.18                28.50         0.513          pass              0.492             71.7                           0.650               -0.07              0.270                                 ok            True                  False
  CTAS           95.45               22            0.94              1.48        225.77                27.57         0.504          pass              0.733             67.4                           0.670                0.08              0.305                                 ok            True                  False
  FTNT           83.33               36            1.21              1.04        122.06                92.45         0.634          pass              0.458             44.2                           0.565              -32.76             -4.891 downtrend_blocked_slope_and_streak           False                  False
  ISRG           87.50                8            2.17              7.13        465.46                42.48         0.565          pass              0.312             18.6                           0.271                1.34              0.368                                 ok           False                  False
  MSTR           90.62               32            1.16              1.05        128.85                81.05         0.560          pass              0.665             59.7                           0.578              -12.47             -1.064            downtrend_blocked_slope           False                  False
 CMCSA           87.50                8            1.80              0.31         24.81                35.54         0.559          pass              0.417             53.6                           0.431                7.98              1.382                                 ok           False                  False
  PAYX           75.00                4            2.08              1.74        118.75                35.22         0.557          pass              0.212             52.0                           0.509                0.14              0.521                                 ok           False                  False
   CSX           71.43                7            1.62              0.58         50.58                30.62         0.552          pass              0.130             25.0                           0.551               -1.55             -0.172                                 ok           False                  False
   EXC           77.78                9            1.30              0.42         46.35                23.57         0.549          pass              0.208             51.0                           0.492                3.36              0.442                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T11:45:04.961396-05:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "entry_ask": 4.2, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.05, "hypothetical_budget": 61581.4, "hypothetical_contracts": 152, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 7.41, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:40:05.161435-05:00 early_entry_1140 early_entry_shadow  {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "entry_ask": 4.2, "entry_bid": 4.15, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 1.2, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.587, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:35:06.887510-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:30:05.913627-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:25:05.831838-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:20:05.913571-05:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "entry_ask": 2.25, "entry_bid": 2.09, "entry_mode": "early", "entry_option_price": 2.17, "hypothetical_budget": 61581.4, "hypothetical_contracts": 283, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 7.37, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "matched_signals": 39, "recovery_stability_score": 0.55, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:15:06.867015-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:10:06.064757-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:05:04.861391-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:00:05.853352-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "entry_ask": 2.4, "entry_bid": 2.28, "entry_mode": "early", "entry_option_price": 2.34, "hypothetical_budget": 61581.4, "hypothetical_contracts": 263, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 5.13, "option_volume": 85.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.583, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "matched_signals": 37, "recovery_stability_score": 0.583, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106114504)

</details>
