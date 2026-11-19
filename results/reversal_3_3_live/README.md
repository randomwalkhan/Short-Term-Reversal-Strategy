# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:25:05 EST`
Last processed slot: `manage_1030`

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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               22            2.36              6.45        388.14               121.61         0.778          pass              0.495             15.3                           0.185                7.19              0.336                  ok            True                  False
  IDXX           96.55               29            1.16              5.68        696.04                78.12         0.710          pass              0.679             27.0                           0.269                2.93              0.198                  ok            True                  False
  ABNB           83.33               24            1.50              1.90        179.40                55.20         0.574          pass              0.257              5.9                           0.093                4.33             -0.116                  ok            True                  False
  AAPL          100.00               19            1.02              2.51        351.38                27.20         0.556          pass              0.546             10.3                           0.203                1.44              0.211                  ok            True                  False
  ODFL           85.71               28            1.11              1.35        174.53                43.99         0.545          pass              0.332              1.8                           0.046                1.53              0.390                  ok            True                  False
   CSX           83.33               12            1.56              0.56         51.09                35.07         0.539          pass              0.162              1.8                           0.182               -0.59              0.205                  ok            True                  False
  COST           86.96               23            0.57              4.37       1094.75                23.52         0.536          pass              0.477             50.5                           0.528                2.33              0.455                  ok            True                  False
   ADP           81.82               11            1.68              3.59        304.03                28.97         0.535          pass              0.126              5.7                           0.169               -2.18              0.039                  ok            True                  False
   CEG           90.91               33            1.09              2.00        261.88                59.92         0.527          pass              0.551             18.1                           0.164                8.61              0.574                  ok            True                  False
  FAST           94.12               17            1.00              0.38         53.80                20.11         0.527          pass              0.548             23.9                           0.323                0.98              0.103                  ok            True                  False
   XEL           83.33               12            1.25              0.71         80.35                18.19         0.524          pass              0.198             14.4                           0.231               -0.91              0.052                  ok            True                  False
   HON           82.14               28            0.67              1.05        222.25                33.05         0.521          pass              0.289             20.1                           0.177                2.84             -0.028                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                           detail
2026-11-19T10:25:05.944079-05:00 early_entry_1025 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00 early_entry_1020 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "APP270115C00400000", "fill_price": 29.835, "pnl": -4972.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119102505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119102505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119102505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119102505)

</details>
