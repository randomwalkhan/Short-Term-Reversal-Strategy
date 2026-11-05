# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 10:10:04 EST`
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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           90.48               21            1.73              8.43        694.93                74.33         0.677            pass              0.420              0.0                           0.170               21.13              2.428                                 ok            True                  False
  MSFT          100.00               10            1.98              7.69        552.51                33.48         0.556            pass              0.507             17.0                           0.164                4.56              0.253                                 ok            True                  False
  DXCM           82.14               28            1.30              0.80         88.14                45.01         0.515            pass              0.229              0.0                           0.150               11.50              1.284                                 ok            True                  False
  FTNT           66.67                6            3.95              3.57        127.86                91.87         0.645            pass              0.113             16.2                           0.307              -28.15             -4.600 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           80.00               20            1.27              2.56        287.83                52.55         0.603            pass              0.167             13.5                           0.150              -12.01             -1.680            downtrend_blocked_slope           False                  False
  GOOG           77.78               18            1.26              2.53        286.21                51.02         0.603            pass              0.164             16.8                           0.180              -11.56             -1.620            downtrend_blocked_slope           False                  False
  INTC          100.00                1            8.32              3.40         56.81               128.90         0.553            pass              0.473              6.0                           0.110              -37.51             -5.840            downtrend_blocked_slope           False                  False
  AMZN           50.00                6            2.46              4.57        264.07                42.79         0.531            pass              0.053              0.0                           0.150                3.64              0.328                                 ok           False                  False
   BKR           80.00               15            2.02              0.70         49.57                49.30         0.519            pass              0.107              7.4                           0.091               -8.87             -1.180 downtrend_blocked_slope_and_streak           False                  False
   KHC           90.91               33            0.45              0.08         25.41                36.26         0.515            pass              0.623             42.5                           0.318                0.94              0.194                                 ok           False                  False
  INTU           87.18               39            0.11              0.27        356.52                43.29         0.510            pass              0.702             88.9                           0.584                0.38              0.355                                 ok           False                  False
  ROST           72.73               11            2.00              3.45        244.26                31.27         0.497 below_threshold              0.137             26.9                           0.246                1.75              0.306                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-05T10:10:04.288762-05:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:05:06.545963-05:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:00:05.848004-05:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105101004)

</details>
