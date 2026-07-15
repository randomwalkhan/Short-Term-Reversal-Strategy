# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:20:02 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               22            1.99              4.25        303.73                65.52         0.574          pass              0.522             31.3                           0.418                0.47              0.257                                 ok            True                  False
   ADI           84.00               25            1.40              3.84        391.11                55.85         0.570          pass              0.368             34.9                           0.434               -2.49              0.070                                 ok            True                  False
   CSX           85.71               14            1.07              0.37         49.76                19.08         0.560          pass              0.312             25.7                           0.336                3.90              0.346                                 ok            True                  False
   LIN          100.00               13            1.20              4.39        520.66                20.66         0.556          pass              0.555             26.6                           0.315               -0.52             -0.299                                 ok            True                  False
  NXPI           85.71               21            2.09              4.14        282.09                58.07         0.542          pass              0.324             14.8                           0.174               -1.10              0.222                                 ok            True                  False
   WBD           86.67               15            0.86              0.16         27.41                20.00         0.536          pass              0.377             37.3                           0.510                2.19              0.279                                 ok            True                  False
  KLAC           75.00               12            4.36              7.02        227.36               109.33         0.587          pass              0.102              9.9                           0.228              -26.97             -2.111 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           96.15               26            0.07              0.03         58.79                30.54         0.583          pass              0.852             95.7                           0.569                1.59             -0.063                                 ok           False                  False
  ASML           94.12               34            0.40              5.01       1773.49                66.00         0.580          pass              0.784             63.3                           0.391              -11.11             -0.727            downtrend_blocked_slope           False                  False
  AMAT           80.00               15            3.59             14.96        589.29                98.89         0.571          pass              0.135             15.0                           0.228              -20.56             -1.417 downtrend_blocked_slope_and_streak           False                  False
  MCHP           96.00               25            2.18              1.33         86.54                68.63         0.559          pass              0.604             15.9                           0.251               -6.57             -0.295            downtrend_blocked_slope           False                  False
  QCOM           82.14               28            1.66              2.07        177.21                61.79         0.553          pass              0.258              8.6                           0.161               -5.22             -0.120           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-15T11:20:02.933836-04:00 early_entry_1120 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:15:06.015471-04:00 early_entry_1115 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:10:02.751788-04:00 early_entry_1110 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00 early_entry_1105 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00      manage_1100               exit {"asset_type": "option", "contract_symbol": "META260821C00660000", "fill_price": 54.6, "pnl": 1545.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.48, "ticker": "META"}
2026-07-15T11:00:03.028836-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:55:06.408548-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:50:02.878047-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:45:02.900716-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715112002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715112002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715112002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715112002)

</details>
