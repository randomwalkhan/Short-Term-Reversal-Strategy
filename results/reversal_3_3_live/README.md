# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 16:00:04 EDT`
Last processed slot: `manage_1600`

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
   EXC           91.67               12            0.55              0.17         43.32                15.10         0.565            pass              0.492             36.8                           0.283               -0.91             -0.003                                 ok            True                  False
  AMGN          100.00               12            1.34              3.60        380.93                44.93         0.647            pass              0.484              2.1                           0.177              -13.65             -1.579 downtrend_blocked_slope_and_streak           False                  False
  CRWD           87.18               39            1.05              1.53        208.20                89.85         0.645            pass              0.600             50.3                           0.539               -9.34             -0.898            downtrend_blocked_slope           False                  False
   PEP           89.47               19            0.24              0.23        136.55                17.04         0.563            pass              0.507             45.9                           0.366               -1.39             -0.191                                 ok           False                  False
  NVDA           92.50               40            0.07              0.11        218.31                43.75         0.553            pass              0.804             71.9                           0.401               -4.18             -0.049           downtrend_blocked_streak           False                  False
    MU           87.18               39            0.25              1.73        976.67                56.22         0.551            pass              0.666             75.4                           0.516                4.23              0.729                                 ok           False                  False
  REGN          100.00               12            1.50              8.34        789.68                28.70         0.541            pass              0.480              4.3                           0.181               -3.26             -0.182           downtrend_blocked_streak           False                  False
  PANW           68.00               25            2.31              5.47        336.15                67.54         0.524            pass              0.248             31.7                           0.569              -13.63             -1.481            downtrend_blocked_slope           False                  False
   CEG           94.12               34            0.38              0.76        285.64                34.28         0.504            pass              0.713             42.0                           0.368                0.88              0.488                                 ok           False                  False
  SBUX           96.55               29            0.47              0.33         99.08                21.90         0.498 below_threshold              0.691             38.2                           0.507               -7.93             -0.935 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00               37            0.44              5.87       1903.72                37.18         0.496 below_threshold              0.750             40.1                           0.277               -1.70             -0.324 downtrend_blocked_slope_and_streak           False                  False
  FTNT           86.21               29            1.76              1.95        158.01                53.57         0.493 below_threshold              0.423             27.3                           0.349               -9.68             -0.890            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911160004)

</details>
