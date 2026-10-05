# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 10:05:01 EDT`
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

- Cash: `$88,586.80`
- Equity: `$88,586.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.76               29            2.93              3.36        162.27               114.85         0.677          pass              0.312             14.7                           0.230               12.04              0.915                                 ok            True                  False
  AMGN           83.87               31            0.53              1.49        402.40                47.11         0.561          pass              0.493             64.5                           0.591                1.97              0.120                                 ok            True                  False
   TRI           87.50               32            0.98              0.67         97.33                53.36         0.541          pass              0.542             47.2                           0.398                1.29              0.077                                 ok            True                  False
  AMAT           84.62               39            0.89              3.35        538.61                49.71         0.519          pass              0.443             24.7                           0.189               15.30              1.618                                 ok            True                  False
  LRCX           80.56               36            1.24              3.02        346.19                57.64         0.518          pass              0.274             11.4                           0.122               13.65              1.413                                 ok            True                  False
   ADI           84.21               19            1.66              4.85        415.07                32.86         0.515          pass              0.237              4.3                           0.107                7.11              0.764                                 ok            True                  False
  MRVL           82.86               35            0.90              1.72        271.55                54.74         0.510          pass              0.430             45.4                           0.344                4.84              0.465                                 ok            True                  False
    MU           90.32               31            1.23              9.23       1070.93                50.82         0.504          pass              0.561             31.8                           0.296                1.70              0.029                                 ok            True                  False
  DRAM           80.00               35            0.32              0.14         61.72                54.09         0.578          pass              0.375             50.0                           0.359                0.00             -0.121                                 ok           False                  False
  QCOM           88.00               25            1.36              1.76        184.12                56.36         0.550          pass              0.497             42.8                           0.310               -6.11             -0.942 downtrend_blocked_slope_and_streak           False                  False
  ASML           76.92               26            1.11             14.56       1861.07                42.39         0.550          pass              0.262             33.4                           0.309                7.90              0.822                                 ok           False                  False
  INTC           82.14               28            2.44              2.04        118.46                74.20         0.540          pass              0.378             49.1                           0.503               -4.40             -0.558            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-10-05T10:05:01.984758-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T10:00:05.004899-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T09:55:04.847980-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "ZS261120C00200000", "fill_price": 17.525, "pnl": 7222.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.01, "ticker": "ZS"}
2026-10-05T03:00:05.114767-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00   share_ext_0255      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00   share_ext_0250      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00   share_ext_0245      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00   share_ext_0240      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00   share_ext_0235      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00   share_ext_0230      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005100501)

</details>
