# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 15:35:03 EDT`
Last processed slot: `manage_1530`

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
   EXC          100.00               11            0.66              0.20         43.30                15.10         0.577            pass              0.539             25.0                           0.192               -1.01             -0.008                                 ok            True                  False
   CEG           93.94               33            0.51              1.02        285.53                34.28         0.502            pass              0.638             21.1                           0.298                0.74              0.482                                 ok            True                  False
  CRWD           87.18               39            1.12              1.64        208.16                89.85         0.641            pass              0.589             46.8                           0.595               -9.41             -0.901            downtrend_blocked_slope           False                  False
  AMGN          100.00               17            1.03              2.76        381.29                44.93         0.639            pass              0.536              8.4                           0.220              -13.38             -1.564 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               18            0.18              0.03         24.38                28.75         0.603            pass              0.757             81.2                           0.380               -1.57             -0.353            downtrend_blocked_slope           False                  False
  TEAM           95.12               41            0.17              0.22        179.48                63.98         0.561            pass              0.923             89.0                           0.746               -3.43             -0.704            downtrend_blocked_slope           False                  False
   PEP           90.00               20            0.18              0.17        136.58                17.04         0.561            pass              0.571             60.7                           0.503               -1.33             -0.188                                 ok           False                  False
    MU           87.18               39            0.25              1.71        976.68                56.22         0.551            pass              0.667             75.7                           0.502                4.23              0.729                                 ok           False                  False
  SBUX           96.00               25            0.60              0.42         99.04                21.90         0.514            pass              0.615             21.1                           0.300               -8.06             -0.941 downtrend_blocked_slope_and_streak           False                  False
  PANW           63.64               22            2.73              6.47        335.72                67.54         0.511            pass              0.189             19.2                           0.395              -14.00             -1.501            downtrend_blocked_slope           False                  False
  REGN          100.00               22            1.14              6.33        790.55                28.70         0.501            pass              0.608             26.0                           0.323               -2.91             -0.166           downtrend_blocked_streak           False                  False
   ROP          100.00               36            0.10              0.26        388.47                26.95         0.496 below_threshold              0.900             92.4                           0.729               -8.16             -1.073 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:55:01.842224-04:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:50:02.882708-04:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:45:05.865744-04:00 early_entry_1145 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911153503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911153503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911153503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911153503)

</details>
