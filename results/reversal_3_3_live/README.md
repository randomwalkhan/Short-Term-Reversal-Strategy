# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:55:05 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           86.49               37            0.66              4.51        975.48                56.22         0.537            pass              0.514             35.8                           0.239                3.80              0.710                                 ok            True                  False
  CRWD           86.11               36            1.61              2.36        207.85                89.85         0.630            pass              0.448             16.2                           0.192               -9.86             -0.924            downtrend_blocked_slope           False                  False
  AMGN          100.00               24            0.69              1.84        381.68                44.93         0.618            pass              0.672             39.0                           0.398              -13.08             -1.548 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.48               21            0.13              0.12        136.60                17.04         0.561            pass              0.550             47.0                           0.284               -1.28             -0.186                                 ok           False                  False
   EXC           93.33               15            0.44              0.13         43.33                15.10         0.556            pass              0.594             50.0                           0.258               -0.79              0.002                                 ok           False                  False
  TEAM           94.74               38            0.80              1.01        179.14                63.98         0.541            pass              0.779             48.4                           0.511               -4.04             -0.733            downtrend_blocked_slope           False                  False
  LRCX           83.33               42            0.05              0.11        297.96                53.83         0.527            pass              0.628             95.4                           0.563               -6.50              0.013           downtrend_blocked_streak           False                  False
  PANW           66.67               24            2.52              5.98        335.93                67.54         0.522            pass              0.165              6.5                           0.116              -13.82             -1.491            downtrend_blocked_slope           False                  False
  REGN          100.00               22            1.18              6.53        790.46                28.70         0.499 below_threshold              0.601             23.6                           0.332               -2.94             -0.167           downtrend_blocked_streak           False                  False
   ROP          100.00               30            0.77              2.09        387.69                26.95         0.493 below_threshold              0.699             38.8                           0.497               -8.77             -1.103 downtrend_blocked_slope_and_streak           False                  False
   CSX           79.17               24            0.45              0.15         48.97                18.09         0.493 below_threshold              0.226             27.9                           0.221               -5.02             -0.479 downtrend_blocked_slope_and_streak           False                  False
  FTNT           87.10               31            1.63              1.81        158.07                53.57         0.490 below_threshold              0.476             32.5                           0.181               -9.56             -0.885            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-11T10:55:05.863407-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:50:05.808094-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:45:04.814010-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:40:06.630614-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:35:04.843069-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:30:01.845613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:25:04.822765-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911105505)

</details>
