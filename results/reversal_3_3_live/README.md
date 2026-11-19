# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:45:05 EST`
Last processed slot: `early_entry_1045`

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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           92.31               26            2.10              5.76        388.44               121.61         0.768          pass              0.627             38.4                           0.332                7.47              0.348                                 ok            True                  False
  IDXX           96.97               33            0.96              4.71        696.45                78.12         0.700          pass              0.742             39.5                           0.586                3.14              0.208                                 ok            True                  False
  ABNB           81.82               22            1.57              1.98        179.36                55.20         0.577          pass              0.257             23.5                           0.247                4.26             -0.119                                 ok            True                  False
  COST           84.62               13            0.97              7.46       1093.42                23.52         0.572          pass              0.247             15.5                           0.243                1.91              0.437                                 ok            True                  False
  AAPL          100.00               21            0.88              2.18        351.52                27.20         0.551          pass              0.640             37.2                           0.343                1.58              0.217                                 ok            True                  False
  ODFL           82.61               23            1.32              1.62        174.42                43.99         0.551          pass              0.316             34.7                           0.275                1.31              0.381                                 ok            True                  False
  VRSK           81.82               22            1.58              2.24        201.35                47.31         0.538          pass              0.281             32.9                           0.538               -5.84             -0.167                                 ok            True                  False
  GILD           80.00               10            2.06              2.43        167.94                31.08         0.528          pass              0.066              4.3                           0.137               -1.23             -0.040                                 ok            True                  False
   HON           80.95               21            1.15              1.80        221.93                33.05         0.527          pass              0.203             17.1                           0.211                2.34             -0.050                                 ok            True                  False
   XEL           80.00               10            1.49              0.84         80.29                18.19         0.518          pass              0.081              9.8                           0.209               -1.14              0.041                                 ok            True                  False
   CEG           90.00               30            1.61              2.97        261.47                59.92         0.504          pass              0.537             29.0                           0.235                8.03              0.550                                 ok            True                  False
  ALNY           75.76               33            1.46              1.53        148.74               110.96         0.718          pass              0.293             22.8                           0.170               -6.03             -0.317 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-19T10:45:05.606696-05:00 early_entry_1045 early_entry_shadow {"contract_symbol": "TTWO270115C00220000", "current_drop_pct": 0.78, "early_entry_score": 0.677, "early_reclaim_pct": 83.7, "entry_ask": 14.3, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 50473.15, "hypothetical_contracts": 37, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 4100.0, "option_spread_pct": 13.43, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 88.24, "ticker": "TTWO", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.677, "early_reclaim_pct": 83.7, "matched_signals": 34, "recovery_stability_score": 0.711, "success_rate": 88.24, "ticker": "TTWO", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-19T10:40:04.606267-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:35:05.556374-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:30:04.546056-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:25:05.944079-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "APP270115C00400000", "fill_price": 29.835, "pnl": -4972.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119104505)

</details>
