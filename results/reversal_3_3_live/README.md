# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:00:05 EST`
Last processed slot: `manage_1000`

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

- Cash: `$52,781.30`
- Equity: `$96,461.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$-4,485.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 43680.0        37.05           33.6      380.27        374.96          bid_ask_mid                       33.6                bid_ask_mid                    True         -4485.0                  -9.31         94.74               19              2.72          61.7           61.34                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT           80.56               36            1.14              1.05        131.01                96.17         0.667          pass              0.441             62.0                           0.416                9.35              0.743                                 ok            True                  False
   TXN           88.24               17            1.62              3.24        284.36                59.73         0.609          pass              0.468             46.8                           0.610                1.36             -0.277                                 ok            True                  False
   ADI           83.33               18            1.78              4.71        375.42                64.58         0.603          pass              0.369             55.5                           0.664                1.97             -0.330                                 ok            True                  False
   CEG           91.18               34            1.11              1.96        251.19                57.98         0.511          pass              0.722             71.0                           0.696               -0.14             -0.435                                 ok            True                   True
   APP           90.70               43            0.98              2.59        377.91               122.37         0.749          pass              0.793             77.6                           0.706               -4.06             -0.484 downtrend_blocked_slope_and_streak           False                  False
  SOXL           55.00               20            7.60              2.41         44.27               254.86         0.720          pass              0.275             45.4                           0.693               -8.95             -2.371            downtrend_blocked_slope           False                  False
  MRVL           66.67               21            3.43              3.32        137.05               121.47         0.624          pass              0.288             50.6                           0.719               -5.29             -1.151            downtrend_blocked_slope           False                  False
  MCHP           88.10               42            0.26              0.11         58.42                78.21         0.606          pass              0.750             91.0                           0.699               -0.05             -0.349                                 ok           False                  False
  DRAM           52.17               23            3.03              0.82         38.08               105.80         0.601          pass              0.304             52.4                           0.688               -5.15             -1.000 downtrend_blocked_slope_and_streak           False                  False
  MPWR           57.14               21            2.48             22.52       1286.21                90.01         0.598          pass              0.301             55.8                           0.746                6.15             -0.372                                 ok           False                  False
  ASML           72.73               22            1.50             14.20       1350.11                61.72         0.576          pass              0.320             60.7                           0.763               -6.24             -1.148 downtrend_blocked_slope_and_streak           False                  False
   WDC           70.83               24            3.51              7.30        293.65               104.69         0.568          pass              0.309             52.9                           0.731                8.56              0.175                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-20T10:00:05.975978-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "entry_ask": 18.0, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 26390.65, "hypothetical_contracts": 15, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "matched_signals": 34, "recovery_stability_score": 0.696, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T01:25:03.363046-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:15:06.809821-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:10:05.934124-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:05:05.898904-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:00:05.809710-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T00:55:04.836951-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T00:50:02.820195-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T00:45:05.761865-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120100005)

</details>
