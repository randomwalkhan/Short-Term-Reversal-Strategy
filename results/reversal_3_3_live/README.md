# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 14:10:05 EDT`
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
  WDAY           82.86               35            0.69              0.83        170.28                67.74         0.576          pass              0.554             84.4                           0.793               32.52              2.547                                 ok            True                  False
  INTC           85.00               40            0.66              0.47        100.86                86.71         0.566          pass              0.653             87.7                           0.623                0.16              0.781                                 ok            True                  False
  MNST           88.24               17            1.03              0.68         94.17                25.70         0.555          pass              0.445             41.2                           0.483               -0.07             -0.087                                 ok            True                  False
  AMGN          100.00               18            1.24              3.54        406.31                30.87         0.510          pass              0.576             23.8                           0.377                8.42              0.688                                 ok            True                  False
  ALNY           66.67                6            3.66              5.87        226.21               127.65         0.778          pass              0.094              5.4                           0.184              -18.01             -2.976            downtrend_blocked_slope           False                  False
    MU           80.56               36            0.44              2.72        892.02               111.75         0.679          pass              0.538             94.1                           0.623              -10.19             -0.505           downtrend_blocked_streak           False                  False
  ISRG           88.37               43            0.01              0.03        375.19                72.98         0.670          pass              0.786             98.7                           0.840               12.99              1.094                                 ok           False                  False
  AMAT           91.67               36            0.80              3.01        532.95                86.87         0.654          pass              0.794             81.5                           0.617               -5.84              0.156           downtrend_blocked_streak           False                  False
   ROP           94.74               38            0.06              0.18        394.45                46.42         0.580          pass              0.922             94.8                           0.784               11.03              0.832                                 ok           False                  False
  AMZN           82.61               46            0.29              0.55        272.42                61.64         0.570          pass              0.385             19.6                           0.337               16.35              2.310                                 ok           False                  False
   MAR           96.30               27            0.84              2.11        360.40                38.12         0.554          pass              0.698             43.0                           0.534               -1.70             -0.694 downtrend_blocked_slope_and_streak           False                  False
   EXC           90.00               10            1.38              0.44         45.57                21.34         0.550          pass              0.395             24.6                           0.435               -4.55             -0.516            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-08-06T12:00:02.173564-04:00 early_entry_1200 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:55:01.207054-04:00 early_entry_1155 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00 early_entry_1150 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.325, "pnl": 2530.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.06, "ticker": "PYPL"}
2026-08-06T11:45:03.120724-04:00 early_entry_1145 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:40:04.059152-04:00 early_entry_1140 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:35:02.131091-04:00 early_entry_1135 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:30:05.087052-04:00 early_entry_1130 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:25:02.082331-04:00 early_entry_1125 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:20:02.141414-04:00 early_entry_1120 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806141005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806141005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806141005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806141005)

</details>
