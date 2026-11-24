# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 09:40:06 EST`
Last processed slot: `manage_0930`

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
  INTC           61.54               13            5.88              2.46         58.61               154.63         0.711          pass              0.151             20.0                           0.305               -3.41             -0.946 downtrend_blocked_slope_and_streak           False                  False
  UPRO           70.00               10            2.80              2.35        118.69                94.72         0.645          pass              0.180             38.6                           0.649              -14.68             -2.443 downtrend_blocked_slope_and_streak           False                  False
  NVDA           80.00                5            5.83              6.74        162.16               126.24         0.635          pass              0.109             15.2                           0.291               -7.97             -1.559 downtrend_blocked_slope_and_streak           False                  False
  QCOM           84.62               39            0.77              0.90        165.00                82.33         0.619          pass              0.611             77.6                           0.840               -5.43             -1.109 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.59               17            1.56              3.07        280.78                61.35         0.600          pass              0.141             11.5                           0.293               -3.36             -0.775            downtrend_blocked_slope           False                  False
  ASML           66.67               12            2.97             28.72       1371.47                73.86         0.600          pass              0.097              8.0                           0.287              -10.95             -1.545 downtrend_blocked_slope_and_streak           False                  False
   BKR           73.68               19            1.37              0.44         45.85                56.59         0.589          pass              0.186             22.2                           0.233               -4.94             -0.840 downtrend_blocked_slope_and_streak           False                  False
  GOOG           73.68               19            1.48              2.90        278.29                58.63         0.587          pass              0.153             11.5                           0.293               -3.34             -0.748            downtrend_blocked_slope           False                  False
  MRVL           57.14               14            6.20              6.28        142.05               142.96         0.585          pass              0.138             17.6                           0.311              -12.06             -2.176            downtrend_blocked_slope           False                  False
   WDC           76.47               17            5.21             10.84        292.61               122.75         0.579          pass              0.152             15.7                           0.322               -2.57             -0.758            downtrend_blocked_slope           False                  False
   CEG           89.47               19            2.36              4.16        249.94                65.44         0.571          pass              0.468             32.6                           0.369               -8.07             -1.405 downtrend_blocked_slope_and_streak           False                  False
  DRAM           83.33                6            7.47              2.07         38.69               132.05         0.571          pass              0.166              6.8                           0.279               -9.88             -1.844 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-21T02:55:05.433853-05:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:50:06.291709-05:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:45:05.697713-05:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:40:04.140323-05:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:35:05.478218-05:00   share_ext_0235      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:30:05.376683-05:00   share_ext_0230      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124094006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124094006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124094006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124094006)

</details>
