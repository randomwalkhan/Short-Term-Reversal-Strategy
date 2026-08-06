# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 11:50:03 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$34,370.75`
- Equity: `$34,370.75`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     55          2026-08-05         2026-08-06        2.865       3.325 2530.0   16.055846 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           96.55               29            0.66              1.83        393.74                46.42         0.603          pass              0.723             45.4                           0.455               10.36              0.805                                 ok            True                  False
  MNST           88.24               17            0.94              0.62         94.19                25.70         0.567          pass              0.382             19.8                           0.188                0.01             -0.083                                 ok            True                  False
  WDAY           83.33               30            1.75              2.09        169.74                67.74         0.527          pass              0.475             66.8                           0.777               31.11              2.498                                 ok            True                  False
   PEP           83.33               24            0.67              0.65        138.50                25.05         0.519          pass              0.363             42.9                           0.393                2.15              0.073                                 ok            True                  False
  ADSK           81.82               33            0.75              1.27        239.49                45.93         0.517          pass              0.492             79.6                           0.752               16.06              1.238                                 ok            True                  False
  ROST           90.00               30            0.66              1.18        252.72                22.84         0.503          pass              0.537             29.0                           0.384                8.24              0.667                                 ok            True                  False
  ALNY           87.10               31            1.15              1.84        227.93               127.65         0.820          pass              0.545             44.7                           0.483              -15.87             -2.859            downtrend_blocked_slope           False                  False
  ISRG           87.80               41            0.18              0.48        375.00                72.98         0.671          pass              0.716             80.4                           0.776               12.80              1.086                                 ok           False                  False
  DRAM           78.12               32            1.79              0.67         53.45               109.54         0.635          pass              0.452             80.6                           0.629               -9.47             -0.061           downtrend_blocked_streak           False                  False
  GEHC           94.59               37            0.45              0.22         70.15                58.07         0.628          pass              0.735             34.4                           0.422               12.86              1.571                                 ok           False                  False
   MAR           94.74               19            1.22              3.08        359.99                38.12         0.579          pass              0.562             17.0                           0.321               -2.07             -0.712 downtrend_blocked_slope_and_streak           False                  False
   EXC           93.33               15            1.14              0.36         45.60                21.34         0.543          pass              0.489             15.4                           0.250               -4.31             -0.505            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-06T11:50:03.918933-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00      manage_1200               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.325, "pnl": 2530.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.06, "ticker": "PYPL"}
2026-08-06T11:45:03.120724-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:40:04.059152-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:35:02.131091-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:30:05.087052-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:25:02.082331-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:20:02.141414-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:15:03.902464-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:10:04.141911-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "entry_ask": 32.9, "entry_bid": 31.7, "entry_mode": "early", "entry_option_price": 32.3, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 3.72, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "matched_signals": 46, "recovery_stability_score": 0.657, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806115003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806115003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806115003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806115003)

</details>
