# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 11:45:05 EDT`
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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           92.31               26            2.86              3.15        155.79                99.69         0.633          pass              0.517              6.3                           0.116               17.78              2.091                      ok            True                  False
    ZS           97.37               38            0.95              1.33        198.82                81.58         0.594          pass              0.813             55.7                           0.508                1.86              0.352                      ok            True                  False
   BKR           81.82               11            1.61              0.64         56.84                32.18         0.522          pass              0.276             56.2                           0.315               -0.92              0.074                      ok            True                  False
  PYPL           93.10               29            0.90              0.34         54.13                35.54         0.505          pass              0.593             22.2                           0.379               -0.04              0.216                      ok            True                  False
   WBD           95.00               40            0.13              0.03         30.89                38.06         0.576          pass              0.855             65.8                           0.656               10.10              1.216                      ok           False                  False
   TRI           87.88               33            0.87              0.59         97.08                56.59         0.576          pass              0.590             56.4                           0.642               -5.97             -0.300 downtrend_blocked_slope           False                  False
  AMGN           86.84               38            0.17              0.48        417.92                46.33         0.575          pass              0.682             85.1                           0.715               11.12              1.225                      ok           False                  False
  CTAS           83.33                6            1.85              2.59        199.47                21.05         0.528          pass              0.171              9.6                           0.308               -1.04             -0.023                      ok           False                  False
  PANW           69.23               26            2.49              6.83        389.16                69.78         0.526          pass              0.252             31.0                           0.462                1.93              0.419                      ok           False                  False
   KDP           80.00                5            1.80              0.40         31.29                25.35         0.522          pass              0.174             40.5                           0.459               -1.18              0.007                      ok           False                  False
  TMUS           70.00               10            2.11              2.46        165.40                33.31         0.520          pass              0.066              4.7                           0.254               -9.72             -0.718 downtrend_blocked_slope           False                  False
  QCOM           92.50               40            0.33              0.43        187.30                57.69         0.514          pass              0.761             58.8                           0.422               -0.50              0.390                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-29T11:45:05.362745-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:40:04.530036-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:35:05.300798-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:30:04.434130-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                       {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "entry_ask": 15.8, "entry_bid": 15.25, "entry_mode": "early", "entry_option_price": 15.525, "hypothetical_budget": 39379.15, "hypothetical_contracts": 25, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 3.54, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "matched_signals": 42, "recovery_stability_score": 0.731, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:25:05.375211-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:20:05.555943-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:15:04.210610-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:10:05.512150-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:05:04.326934-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:00:04.441545-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "entry_ask": 2.4, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.325, "hypothetical_budget": 39379.15, "hypothetical_contracts": 169, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 6.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "matched_signals": 34, "recovery_stability_score": 0.563, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.801, "early_reclaim_pct": 62.3, "matched_signals": 37, "recovery_stability_score": 0.581, "success_rate": 94.59, "ticker": "ORLY", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929114505)

</details>
