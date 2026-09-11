# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 15:20:04 EDT`
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
   EXC          100.00               11            0.58              0.18         43.31                15.10         0.581            pass              0.567             34.2                           0.262               -0.93             -0.004                                 ok            True                  False
  CRWD           86.49               37            1.34              1.95        208.02                89.85         0.639            pass              0.527             36.7                           0.504               -9.60             -0.911            downtrend_blocked_slope           False                  False
  AMGN          100.00               19            0.88              2.36        381.46                44.93         0.636            pass              0.588             21.6                           0.323              -13.25             -1.557 downtrend_blocked_slope_and_streak           False                  False
  TEAM           95.12               41            0.01              0.02        179.56                63.98         0.571            pass              0.954             99.1                           0.828               -3.27             -0.697            downtrend_blocked_slope           False                  False
   PEP           89.47               19            0.18              0.18        136.57                17.04         0.566            pass              0.546             59.0                           0.518               -1.33             -0.188                                 ok           False                  False
    MU           87.18               39            0.23              1.55        976.75                56.22         0.552            pass              0.674             78.0                           0.503                4.26              0.730                                 ok           False                  False
 CMCSA           93.94               33            0.08              0.01         25.16                36.51         0.530            pass              0.843             88.2                           0.499               -4.77             -0.711 downtrend_blocked_slope_and_streak           False                  False
  SBUX           95.65               23            0.72              0.50         99.01                21.90         0.519            pass              0.558              6.6                           0.220               -8.16             -0.946 downtrend_blocked_slope_and_streak           False                  False
  PANW           58.82               17            3.05              7.23        335.39                67.54         0.516            pass              0.127              9.6                           0.205              -14.29             -1.516            downtrend_blocked_slope           False                  False
   CEG           94.12               34            0.37              0.74        285.65                34.28         0.504            pass              0.715             42.7                           0.430                0.89              0.488                                 ok           False                  False
  MELI          100.00               38            0.30              4.04       1904.51                37.18         0.498 below_threshold              0.813             58.9                           0.475               -1.57             -0.318 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               22            1.20              6.64        790.41                28.70         0.497 below_threshold              0.597             22.3                           0.339               -2.96             -0.168           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911152004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911152004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911152004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911152004)

</details>
