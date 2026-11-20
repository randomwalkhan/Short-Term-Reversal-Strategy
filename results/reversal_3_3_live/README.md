# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:35:04 EST`
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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           86.67               15            2.27              4.00        250.05                49.35         0.526          pass              0.291              8.9                           0.180               -0.90             -0.369                                 ok            True                  False
  INTC           60.00               25            2.78              1.08         55.26               141.91         0.761          pass              0.335             53.0                           0.313               -3.75             -0.888 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.55             14.71        372.71               122.37         0.725          pass              0.492              6.7                           0.175               -8.49             -0.699 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.83               46            0.00              0.02        689.64                78.44         0.687          pass              0.964             98.5                           0.524                2.01             -0.020                                 ok           False                  False
  FTNT           68.42               19            2.57              2.37        130.45                96.17         0.669          pass              0.171             14.6                           0.148                7.78              0.677                                 ok           False                  False
  UPRO           87.50                8            2.83              2.34        116.89                72.20         0.599          pass              0.325             21.8                           0.163              -11.16             -1.607 downtrend_blocked_slope_and_streak           False                  False
  QCOM           84.00               25            1.58              1.79        161.24                69.46         0.587          pass              0.399             44.6                           0.285               -3.60             -0.748 downtrend_blocked_slope_and_streak           False                  False
   BKR           69.23               13            2.21              0.72         46.36                56.86         0.578          pass              0.131             17.8                           0.144               -4.20             -0.431 downtrend_blocked_slope_and_streak           False                  False
  MCHP           75.00               16            3.06              1.25         57.93                78.21         0.571          pass              0.114              5.5                           0.131               -2.86             -0.478            downtrend_blocked_slope           False                  False
  CSCO           72.73               22            1.23              0.82         94.35                50.60         0.553          pass              0.244             36.3                           0.233               -0.34             -0.365                                 ok           False                  False
   TXN          100.00                2            4.22              8.45        282.13                59.73         0.546          pass              0.478              7.9                           0.172               -1.33             -0.399                                 ok           False                  False
   ADI          100.00                5            4.42             11.69        372.43                64.58         0.536          pass              0.478              8.1                           0.198               -0.78             -0.454                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-20T10:35:04.912768-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:30:06.085636-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:25:04.965468-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:10:04.986532-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:05:06.571641-05:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "entry_ask": 17.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 26390.65, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 13.66, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "matched_signals": 34, "recovery_stability_score": 0.745, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T10:00:05.975978-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "entry_ask": 18.0, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 26390.65, "hypothetical_contracts": 15, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "matched_signals": 34, "recovery_stability_score": 0.696, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T01:25:03.363046-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120103504)

</details>
