# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 12:20:01 EDT`
Last processed slot: `manage_1230`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.12               34            0.68              0.33         70.10                58.07         0.631          pass              0.636             12.0                           0.248               12.61              1.560                       ok            True                  False
   ROP           93.75               32            0.54              1.50        393.89                46.42         0.586          pass              0.738             55.3                           0.657               10.49              0.810                       ok            True                  False
  MNST           88.24               17            1.31              0.87         94.09                25.70         0.540          pass              0.336              5.3                           0.142               -0.36             -0.100                       ok            True                  False
  WDAY           81.25               32            1.44              1.72        169.90                67.74         0.532          pass              0.451             72.7                           0.774               31.53              2.513                       ok            True                  False
  INTC           84.62               39            1.30              0.92        100.67                86.71         0.526          pass              0.597             75.9                           0.374               -0.48              0.752                       ok            True                  False
  UPRO           81.25               32            0.74              0.79        152.90                43.16         0.519          pass              0.285             17.8                           0.202               11.74              1.443                       ok            True                  False
  AMGN          100.00               18            1.21              3.46        406.35                30.87         0.513          pass              0.567             20.8                           0.327                8.45              0.689                       ok            True                  False
   PEP           83.33               24            0.78              0.76        138.46                25.05         0.512          pass              0.335             33.7                           0.329                2.04              0.068                       ok            True                  False
  ADSK           83.78               37            0.52              0.87        239.66                45.93         0.509          pass              0.590             86.0                           0.806               16.33              1.249                       ok            True                  False
  ALNY           86.21               29            1.25              2.00        227.86               127.65         0.823          pass              0.495             40.1                           0.430              -15.95             -2.863  downtrend_blocked_slope           False                  False
    MU           80.56               36            0.43              2.68        892.04               111.75         0.680          pass              0.539             94.2                           0.548              -10.18             -0.505 downtrend_blocked_streak           False                  False
  ISRG           87.80               41            0.18              0.47        375.00                72.98         0.671          pass              0.717             80.7                           0.753               12.80              1.086                       ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806122001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806122001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806122001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806122001)

</details>
