# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 09:55:05 EST`
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
  PANW           80.00               40            0.86              2.13        352.52                70.38         0.530          pass              0.456             67.7                           0.517                7.36              0.969                                 ok            True                  False
  INTC           61.54               13            5.60              2.34         58.66               154.63         0.726          pass              0.164             23.9                           0.289               -3.11             -0.933 downtrend_blocked_slope_and_streak           False                  False
  NVDA           80.00                5            5.80              6.70        162.18               126.24         0.637          pass              0.111             15.8                           0.235               -7.94             -1.557 downtrend_blocked_slope_and_streak           False                  False
  UPRO           78.57               28            1.33              1.12        119.26                94.72         0.636          pass              0.397             71.0                           0.883              -13.36             -2.374 downtrend_blocked_slope_and_streak           False                  False
  QCOM           77.78               27            1.55              1.80        164.61                82.33         0.636          pass              0.342             55.1                           0.601               -6.18             -1.145 downtrend_blocked_slope_and_streak           False                  False
  MRVL           60.00               15            5.71              5.78        142.26               142.96         0.613          pass              0.167             24.1                           0.288              -11.60             -2.152            downtrend_blocked_slope           False                  False
  ASML           66.67               12            2.76             26.71       1372.33                73.86         0.613          pass              0.118             14.4                           0.227              -10.76             -1.535 downtrend_blocked_slope_and_streak           False                  False
  DRAM           83.33                6            6.90              1.91         38.76               132.05         0.606          pass              0.191             13.9                           0.223               -9.33             -1.816 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            1.11              2.19        281.16                61.35         0.575          pass              0.286             38.3                           0.302               -2.93             -0.754            downtrend_blocked_slope           False                  False
   BKR           84.85               33            0.50              0.16         45.97                56.59         0.572          pass              0.555             71.6                           0.616               -4.10             -0.800 downtrend_blocked_slope_and_streak           False                  False
  CSCO           61.54               13            2.12              1.43         96.19                56.18         0.572          pass              0.123             15.3                           0.232               -3.46             -0.621            downtrend_blocked_slope           False                  False
  GOOG           78.57               28            1.00              1.96        278.69                58.63         0.566          pass              0.303             42.0                           0.327               -2.88             -0.726            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124095505)

</details>
