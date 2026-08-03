# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:05:02 EDT`
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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           88.89               18            0.98              0.66         96.10                24.15         0.566            pass              0.425             26.0                           0.197               -0.01              0.239                                 ok            True                  False
  CDNS           83.33               18            2.14              5.09        337.84                48.77         0.501            pass              0.231             12.9                           0.119                0.85              0.018                                 ok            True                  False
  AAPL           91.67               12            1.40              3.03        307.61                37.33         0.621            pass              0.403              5.4                           0.140               -6.74             -0.360 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.89               27            1.73              6.15        505.03                87.25         0.601            pass              0.561             50.3                           0.614               -5.10             -1.464 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.55               29            0.37              0.13         50.34                27.78         0.551            pass              0.771             63.0                           0.544                0.21             -0.054                                 ok           False                  False
  DRAM           75.00               24            3.51              1.24         49.84               111.30         0.505            pass              0.246             34.2                           0.568               -8.41             -1.809 downtrend_blocked_slope_and_streak           False                  False
  CSCO           84.62               26            1.04              0.84        115.63                33.42         0.492 below_threshold              0.426             48.9                           0.529                3.69              0.325                                 ok           False                  False
  ASML           91.43               35            0.77              8.83       1625.21                49.80         0.491 below_threshold              0.740             73.1                           0.756               -6.93             -1.288 downtrend_blocked_slope_and_streak           False                  False
   BKR           70.00               20            1.62              0.69         60.20                35.32         0.491 below_threshold              0.207             30.5                           0.352                7.91              0.859                                 ok           False                  False
  MRVL           80.00               30            2.87              3.77        185.95                91.71         0.468 below_threshold              0.319             46.1                           0.589               -6.55             -1.615 downtrend_blocked_slope_and_streak           False                  False
  LRCX           80.95               21            3.54              7.26        289.91                90.68         0.465 below_threshold              0.253             35.9                           0.555               -7.86             -1.449 downtrend_blocked_slope_and_streak           False                  False
  MCHP           88.24               34            1.33              0.69         73.99                53.53         0.451 below_threshold              0.575             50.3                           0.389               -8.96             -1.463 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-03T10:05:02.768000-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00      manage_1000               exit       {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.7325, "pnl": -1655.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-03T10:00:05.013413-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:00:05.013413-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.055, "pnl": 3663.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 22.2, "ticker": "PYPL"}
2026-08-03T03:00:01.318857-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-01T02:55:05.543757-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:50:03.559727-04:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:45:01.711119-04:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:40:01.558683-04:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:35:03.491522-04:00   share_ext_0235      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803100502)

</details>
