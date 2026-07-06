# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 10:55:01 EDT`
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

- Cash: `$26,504.50`
- Equity: `$26,504.50`
- Realized PnL: `$16,504.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-06)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KDP     option         option KDP260821C00033000     96          2026-07-02         2026-07-06         1.45       1.305 -1392.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   AEP           81.82               11            1.25              1.21        137.99                19.65         0.553          pass              0.204             31.1                           0.202                7.12              0.593                  ok            True                  False
  PAYX          100.00               19            1.32              0.98        105.93                31.56         0.548          pass              0.567             17.4                           0.304                6.83              0.870                  ok            True                  False
  MNST          100.00               17            1.00              0.69         97.31                16.38         0.535          pass              0.597             32.4                           0.470                5.78              0.579                  ok            True                  False
   ADP           94.12               17            1.45              2.46        241.22                30.79         0.534          pass              0.559             27.5                           0.458                9.32              1.097                  ok            True                  False
  BKNG           82.61               23            1.35              1.74        183.81                41.33         0.531          pass              0.278             22.9                           0.309                5.99              0.821                  ok            True                  False
  VRTX           93.33               15            1.52              5.61        525.63                28.87         0.509          pass              0.587             48.9                           0.663               15.14              1.373                  ok            True                  False
   XEL          100.00                3            1.66              0.95         81.55                20.81         0.604          pass              0.485              8.1                           0.184                4.12              0.281                  ok           False                  False
   PEP           80.00                5            1.55              1.56        143.55                27.18         0.592          pass              0.124             21.5                           0.458               -0.02             -0.024                  ok           False                  False
   EXC           87.50                8            1.40              0.47         47.68                22.14         0.587          pass              0.291             10.9                           0.197                3.06              0.263                  ok           False                  False
   KHC          100.00                2            3.00              0.53         25.14                36.79         0.570          pass              0.498             13.6                           0.251                7.84              1.229                  ok           False                  False
  CTAS           70.00               10            1.69              2.15        180.45                35.27         0.564          pass              0.097             13.5                           0.272                4.36              0.518                  ok           False                  False
  GILD           87.50                8            2.10              1.93        130.44                30.05         0.531          pass              0.308             18.3                           0.430                3.84              0.408                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-07-06T10:55:01.329795-04:00 early_entry_1055 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:50:01.323991-04:00 early_entry_1050 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:45:01.326292-04:00 early_entry_1045 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:40:05.174623-04:00 early_entry_1040 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:35:05.425058-04:00 early_entry_1035 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:30:05.295059-04:00 early_entry_1030 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:25:05.297833-04:00 early_entry_1025 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:20:05.672223-04:00 early_entry_1020 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:20:05.672223-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "KDP260821C00033000", "fill_price": 1.305, "pnl": -1392.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KDP"}
2026-07-06T10:15:06.215817-04:00 early_entry_1015 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706105501)

</details>
