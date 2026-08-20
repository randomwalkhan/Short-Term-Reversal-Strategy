# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-20 10:38:39 EDT`
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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           84.21               38            0.57              0.69        173.93               121.79         0.760          pass              0.577             67.3                           0.585               57.25              2.907                  ok            True                  False
  WDAY           82.86               35            1.31              1.81        197.64                85.33         0.606          pass              0.390             28.8                           0.269               15.03              1.303                  ok            True                  False
  MCHP           85.37               41            0.51              0.27         76.96                71.63         0.581          pass              0.619             72.5                           0.644                3.13             -0.332                  ok            True                  False
   KHC           86.36               22            1.03              0.19         25.60                39.84         0.567          pass              0.391             28.4                           0.185                1.82              0.164                  ok            True                  False
 CMCSA           90.00               20            1.00              0.19         26.51                43.42         0.559          pass              0.389              0.0                           0.192                4.59              0.502                  ok            True                  False
  UPRO           80.77               26            0.91              0.97        151.74                40.33         0.551          pass              0.339             52.2                           0.573               -1.09             -0.162                  ok            True                  False
  BKNG           96.97               33            0.91              1.36        212.42                45.88         0.538          pass              0.671             21.5                           0.245                1.77             -0.076                  ok            True                  False
  REGN          100.00               21            1.27              7.47        837.64                29.05         0.538          pass              0.530              1.0                           0.111                7.65              0.629                  ok            True                  False
   BKR           81.25               16            1.35              0.61         64.22                32.39         0.537          pass              0.235             36.0                           0.303                1.74              0.274                  ok            True                  False
  ISRG           80.00               15            1.89              5.27        395.46                37.69         0.533          pass              0.124             12.3                           0.173                4.41              0.292                  ok            True                  False
  FAST          100.00               24            0.57              0.21         51.35                21.74         0.532          pass              0.699             50.8                           0.619                0.68             -0.105                  ok            True                  False
  MELI           97.22               36            0.69              9.24       1904.69                47.33         0.516          pass              0.784             52.9                           0.315                3.58              0.122                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-20T10:38:39.121946-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-20T10:19:19.114673-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "entry_ask": 26.9, "entry_bid": 24.1, "entry_mode": "early", "entry_option_price": 25.5, "hypothetical_budget": 26569.0, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 92.0, "option_spread_pct": 10.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "matched_signals": 30, "recovery_stability_score": 0.605, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T09:18:16.446091-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-08-19T11:30:46.509801-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-19T10:58:16.376316-04:00 early_entry_1055 early_entry_shadow                       {"contract_symbol": "ZS260918C00185000", "current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "entry_ask": 15.8, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 26569.0, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1626.0, "option_spread_pct": 4.53, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "matched_signals": 41, "recovery_stability_score": 0.774, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-19T10:25:26.675121-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T12:30:08.738941-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260820103839)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260820103839)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260820103839)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260820103839)

</details>
