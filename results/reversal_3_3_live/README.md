# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 11:05:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.37               38            0.87              1.20        196.95                82.85         0.626          pass              0.842             64.3                           0.747               10.10              1.871                                 ok            True                   True
   KHC           90.91               11            1.13              0.20         24.65                21.70         0.536          pass              0.506             51.7                           0.729               -2.28             -0.137                                 ok            True                  False
  CTSH          100.00               15            2.51              1.09         61.41                39.55         0.523          pass              0.515              9.9                           0.228               -6.68             -0.015                                 ok            True                  False
  FTNT           83.33               12            2.89              3.49        171.08                57.60         0.522          pass              0.224             23.2                           0.482                7.19              1.143                                 ok            True                  False
   WBD           83.33               12            1.01              0.20         28.15                10.21         0.504          pass              0.201             16.2                           0.162               -1.46             -0.069                                 ok            True                  False
  CRWD           71.43               14            3.32              5.71        243.25                97.92         0.632          pass              0.163             24.4                           0.502               10.50              1.740                                 ok           False                  False
  PYPL           91.43               35            0.43              0.16         52.87                57.74         0.611          pass              0.735             67.4                           0.663               -7.00             -0.422            downtrend_blocked_slope           False                  False
  MRVL           80.00               40            0.47              0.80        240.42                74.50         0.599          pass              0.441             60.4                           0.474               14.75              0.807                                 ok           False                  False
   TRI           90.91               11            3.11              2.16         98.55                55.72         0.564          pass              0.373              6.4                           0.225              -13.75             -0.630 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00                6            1.29              0.38         42.48                15.46         0.559          pass              0.466              3.5                           0.185               -4.58             -0.470 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.85              1.31        218.08                55.63         0.555          pass              0.401             27.4                           0.368               -8.73             -0.062           downtrend_blocked_streak           False                  False
   AEP           77.78                9            1.08              0.92        121.23                17.28         0.533          pass              0.126             24.3                           0.352               -3.53             -0.423 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-18T11:05:05.479852-04:00 early_entry_1105 early_entry_shadow                        {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "entry_ask": 13.95, "entry_bid": 12.45, "entry_mode": "early", "entry_option_price": 13.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 11.36, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:00:06.440780-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:55:06.922976-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:50:04.964114-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:45:06.500204-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:40:04.793356-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:35:06.106609-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:30:04.878508-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:25:05.756600-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:20:05.884783-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "TEAM261023C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "entry_ask": 16.3, "entry_bid": 13.7, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 17.33, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.592, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918110505)

</details>
