# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:20:05 EST`
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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           57.14                7            7.17              3.00         58.38               154.63         0.666          pass              0.077              3.6                           0.196               -4.73             -1.009 downtrend_blocked_slope_and_streak           False                  False
  UPRO           75.00               16            2.19              1.83        118.95                94.72         0.652          pass              0.262             52.4                           0.531              -14.12             -2.413 downtrend_blocked_slope_and_streak           False                  False
  QCOM           78.57               28            1.37              1.58        164.70                82.33         0.642          pass              0.366             60.5                           0.568               -6.00             -1.136 downtrend_blocked_slope_and_streak           False                  False
   BKR           76.19               21            1.13              0.36         45.88                56.59         0.596          pass              0.240             35.8                           0.334               -4.71             -0.829 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           79.31               29            0.72              1.41        281.49                61.35         0.589          pass              0.366             60.2                           0.637               -2.54             -0.736            downtrend_blocked_slope           False                  False
  ASML           66.67                9            3.50             33.94       1369.23                73.86         0.581          pass              0.072              4.5                           0.095              -11.44             -1.570 downtrend_blocked_slope_and_streak           False                  False
  NVDA           75.00                4            6.86              7.93        161.65               126.24         0.569          pass              0.069              4.2                           0.218               -8.98             -1.609 downtrend_blocked_slope_and_streak           False                  False
  GOOG           81.82               33            0.57              1.12        279.05                58.63         0.566          pass              0.459             66.8                           0.673               -2.46             -0.706            downtrend_blocked_slope           False                  False
   CEG           91.67               24            2.07              3.65        250.16                65.44         0.560          pass              0.583             40.9                           0.353               -7.80             -1.391 downtrend_blocked_slope_and_streak           False                  False
  CSCO           50.00               10            2.37              1.61         96.11                56.18         0.560          pass              0.071              5.2                           0.126               -3.71             -0.633            downtrend_blocked_slope           False                  False
  PANW           81.40               43            0.35              0.87        353.06                70.38         0.546          pass              0.552             86.9                           0.675                7.92              0.992                                 ok           False                  False
  AVGO           63.64               11            3.48              7.64        310.27                86.52         0.543          pass              0.145             27.9                           0.454               -8.84             -1.208            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:00:05.622595-05:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-21T02:55:05.433853-05:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124102005)

</details>
