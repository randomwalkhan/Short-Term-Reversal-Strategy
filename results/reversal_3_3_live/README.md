# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 14:10:04 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  UPRO           89.47               19            1.44              1.42        140.78                55.10         0.617            pass              0.494             39.8                           0.415                0.67              0.046                      ok            True                  False
   KDP          100.00               11            1.09              0.26         33.26                28.32         0.614            pass              0.533             21.5                           0.333                7.61              1.058                      ok            True                  False
  AVGO           76.47               17            2.21              5.71        366.89                71.90         0.652            pass              0.199             29.1                           0.435               -7.93             -0.942 downtrend_blocked_slope           False                  False
   WBD           66.67                3            1.40              0.26         26.70                21.87         0.598            pass              0.164             34.8                           0.391                0.74              0.089                      ok           False                  False
   TXN           86.67               15            2.47              5.17        296.20                67.74         0.588            pass              0.334             21.4                           0.353               -3.59             -0.920 downtrend_blocked_slope           False                  False
    MU           88.89                9            6.16             44.51       1013.21               134.25         0.568            pass              0.349             18.4                           0.356               -7.14             -0.585 downtrend_blocked_slope           False                  False
   ADI           71.43                7            3.30              8.99        385.13                61.24         0.541            pass              0.110             18.6                           0.375               -9.24             -1.286 downtrend_blocked_slope           False                  False
  PCAR           78.57               14            1.64              1.39        120.64                34.47         0.532            pass              0.148             22.9                           0.376                1.63              0.214                      ok           False                  False
  NXPI           81.82               11            3.26              6.37        276.45                63.41         0.513            pass              0.170             21.3                           0.400               -9.12             -1.398 downtrend_blocked_slope           False                  False
  MPWR           86.67               15            4.05             37.73       1315.56                89.16         0.512            pass              0.329             22.3                           0.334              -11.63             -1.655 downtrend_blocked_slope           False                  False
  ASML           88.89                9            4.52             58.28       1818.06                76.04         0.499 below_threshold              0.324             12.4                           0.312               -5.78             -0.234                      ok           False                  False
  CDNS           94.74               38            0.41              1.08        377.27                42.41         0.497 below_threshold              0.866             78.7                           0.816               -3.44             -0.368 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-02T12:00:01.950437-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:55:04.784699-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:50:04.781471-04:00 early_entry_1150 early_entry_shadow    {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "entry_ask": 14.2, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 2.86, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:45:01.785204-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "entry_ask": 14.9, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.87, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "matched_signals": 44, "recovery_stability_score": 0.678, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:40:01.586831-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "entry_ask": 14.5, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.125, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.31, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "matched_signals": 43, "recovery_stability_score": 0.641, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:35:01.638961-04:00 early_entry_1135 early_entry_shadow     {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "entry_ask": 14.55, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 3.5, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "matched_signals": 44, "recovery_stability_score": 0.691, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:30:01.731929-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "entry_ask": 15.0, "entry_bid": 13.95, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 7.25, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "matched_signals": 43, "recovery_stability_score": 0.648, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:25:01.740560-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.62, "early_entry_score": 0.829, "early_reclaim_pct": 62.4, "entry_ask": 14.35, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.125, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 3.19, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.65, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.829, "early_reclaim_pct": 62.4, "matched_signals": 43, "recovery_stability_score": 0.65, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:20:05.689456-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:15:06.544213-04:00 early_entry_1115 early_entry_shadow  {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "entry_ask": 14.1, "entry_bid": 13.35, "entry_mode": "early", "entry_option_price": 13.725, "hypothetical_budget": 13948.25, "hypothetical_contracts": 10, "matched_signals": 45, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.46, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "matched_signals": 45, "recovery_stability_score": 0.685, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702141004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702141004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702141004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702141004)

</details>
