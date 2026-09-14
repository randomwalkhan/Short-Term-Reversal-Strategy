# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 11:15:01 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           84.62               13            0.91              0.79        122.99                16.49         0.522            pass              0.282             29.0                           0.393               -0.09              0.055                                 ok            True                  False
   KHC           93.33               15            0.35              0.06         24.57                26.10         0.586            pass              0.613             55.3                           0.471               -3.09             -0.451            downtrend_blocked_slope           False                  False
  SNPS           55.56                9            2.74              7.61        394.12                60.55         0.574            pass              0.078              7.0                           0.187              -12.68             -1.259            downtrend_blocked_slope           False                  False
   EXC          100.00                8            0.95              0.29         43.04                14.68         0.553            pass              0.485              9.9                           0.235               -1.76             -0.092           downtrend_blocked_streak           False                  False
 CMCSA           96.67               30            0.48              0.08         25.16                34.99         0.527            pass              0.757             57.1                           0.443               -7.32             -0.833 downtrend_blocked_slope_and_streak           False                  False
  NVDA           83.33                6            3.39              5.17        216.07                43.68         0.524            pass              0.204             21.0                           0.493               -2.95             -0.176           downtrend_blocked_streak           False                  False
  UPRO           92.86               14            2.22              2.30        147.04                26.03         0.502            pass              0.454             11.6                           0.302               -4.64             -0.371 downtrend_blocked_slope_and_streak           False                  False
  CDNS           71.43               14            2.41              4.89        287.27                43.36         0.501            pass              0.112             11.6                           0.223              -17.04             -1.879 downtrend_blocked_slope_and_streak           False                  False
   CSX           76.92               13            1.17              0.40         48.78                18.07         0.500            pass              0.120             16.7                           0.116               -5.41             -0.358            downtrend_blocked_slope           False                  False
  ALNY           88.89               36            0.60              1.04        248.24                49.38         0.488 below_threshold              0.712             84.2                           0.754                4.26              0.244                                 ok           False                   True
  ABNB           94.44               36            0.29              0.35        170.04                31.21         0.480 below_threshold              0.809             67.5                           0.468              -10.42             -1.195 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.88               32            0.32              0.22         98.64                21.82         0.475 below_threshold              0.702             35.8                           0.253               -8.74             -1.017 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-14T11:15:01.136676-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.598, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "matched_signals": 33, "recovery_stability_score": 0.598, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.712, "early_reclaim_pct": 84.2, "matched_signals": 36, "recovery_stability_score": 0.754, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:10:05.058091-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                   {"contract_symbol": "ALNY261016C00250000", "current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "entry_ask": 12.3, "entry_bid": 11.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 38058.05, "hypothetical_contracts": 32, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 838.0, "option_spread_pct": 10.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:05:02.179238-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:00:03.361025-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "matched_signals": 34, "recovery_stability_score": 0.663, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:55:03.263135-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.722, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:50:05.324545-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.724, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:45:01.220656-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:40:02.381036-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "matched_signals": 35, "recovery_stability_score": 0.748, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:35:03.129508-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:30:01.152638-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.771, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "matched_signals": 34, "recovery_stability_score": 0.771, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914111501)

</details>
