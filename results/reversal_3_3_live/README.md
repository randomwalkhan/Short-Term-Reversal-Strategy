# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 10:05:06 EDT`
Last processed slot: `manage_1000`

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

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC          100.00               11            0.60              0.18         43.08                14.68         0.558            pass              0.474              3.7                           0.131               -1.41             -0.076                                 ok            True                  False
   AEP           87.50               16            0.83              0.71        123.02                16.49         0.514            pass              0.332             13.4                           0.141               -0.00              0.059                                 ok            True                  False
  SNPS           72.73               22            1.85              5.13        395.18                60.55         0.575            pass              0.194             18.8                           0.328              -11.88             -1.217            downtrend_blocked_slope           False                  False
  UPRO           94.12               17            1.51              1.56        147.35                26.03         0.526            pass              0.595             39.7                           0.692               -3.95             -0.338 downtrend_blocked_slope_and_streak           False                  False
  CHTR           89.74               39            1.07              1.09        145.30                68.13         0.521            pass              0.695             63.1                           0.383               -6.13             -0.904            downtrend_blocked_slope           False                  False
  NVDA           80.00                5            3.47              5.31        216.01                43.68         0.521            pass              0.109             19.0                           0.547               -3.04             -0.180           downtrend_blocked_streak           False                  False
  CDNS           66.67               12            2.53              5.12        287.18                43.36         0.502            pass              0.076              4.1                           0.159              -17.14             -1.884 downtrend_blocked_slope_and_streak           False                  False
   CSX           80.00               20            0.66              0.23         48.85                18.07         0.494 below_threshold              0.276             53.3                           0.370               -4.91             -0.334            downtrend_blocked_slope           False                  False
  MELI           97.44               39            0.34              4.48       1895.45                37.25         0.488 below_threshold              0.832             63.2                           0.451               -3.83             -0.484 downtrend_blocked_slope_and_streak           False                  False
  ABNB           94.12               34            0.45              0.53        169.96                31.21         0.483 below_threshold              0.726             47.2                           0.275              -10.56             -1.202 downtrend_blocked_slope_and_streak           False                  False
  AMZN           68.42               19            1.51              2.72        255.62                26.09         0.481 below_threshold              0.215             35.7                           0.304               -5.08             -0.337 downtrend_blocked_slope_and_streak           False                  False
   LIN           75.00               20            0.71              2.31        465.23                15.11         0.479 below_threshold              0.195             26.9                           0.259               -5.12             -0.640 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-14T10:05:06.288532-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:00:06.059973-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
2026-09-11T14:50:04.839039-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914100506)

</details>
