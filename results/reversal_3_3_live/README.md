# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:00:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               29            1.70              1.44        119.99               109.00         0.643          pass              0.720             42.9                           0.211               25.13              3.116                                 ok            True                  False
  TEAM           81.82               11            5.16              3.07         83.68               115.69         0.595          pass              0.140              8.5                           0.162               14.36              1.311                                 ok            True                  False
  QCOM           94.44               36            0.57              0.84        209.95                94.36         0.561          pass              0.783             56.0                           0.275               34.04              3.262                                 ok            True                  False
   XEL           95.00               20            0.88              0.49         79.69                27.12         0.545          pass              0.656             44.9                           0.525                0.48             -0.232                                 ok            True                  False
  SNPS           96.55               29            1.40              5.03        511.06                43.23         0.545          pass              0.602              7.0                           0.105                5.16              0.673                                 ok            True                  False
   ADP          100.00               10            2.46              3.68        212.23                33.54         0.542          pass              0.569             38.3                           0.235               -3.02             -0.111                                 ok            True                  False
    ZS           82.05               39            0.81              0.83        145.82                59.81         0.505          pass              0.486             62.4                           0.399                7.62              1.106                                 ok            True                  False
  CDNS           97.30               37            0.80              2.01        357.18                38.69         0.503          pass              0.823             64.3                           0.420                7.64              0.892                                 ok            True                  False
  CHTR           63.64               11            3.43              3.56        146.40               118.13         0.757          pass              0.107              8.3                           0.178               -9.97             -1.395            downtrend_blocked_slope           False                  False
 CMCSA           92.86               28            0.46              0.08         24.87                62.10         0.687          pass              0.738             68.9                           0.695               -7.38             -0.997 downtrend_blocked_slope_and_streak           False                  False
  INSM           82.61               46            0.09              0.08        115.97               110.65         0.595          pass              0.621             97.2                           0.858              -14.17             -2.806 downtrend_blocked_slope_and_streak           False                  False
  GEHC           66.67               30            1.11              0.48         62.08                57.10         0.571          pass              0.329             46.0                           0.583                3.55              0.351                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T10:00:05.846029-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513100005)

</details>
