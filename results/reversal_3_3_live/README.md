# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 12:38:07 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GOOG           83.33               18            1.57              4.37        395.18                37.66         0.572          pass              0.275             25.2                           0.320               12.13              1.423                                 ok            True                  False
  TMUS           84.62               26            1.08              1.46        193.00                36.59         0.540          pass              0.353             23.2                           0.198                4.81              0.260                                 ok            True                  False
   ADP           92.31               26            0.83              1.23        212.47                34.95         0.528          pass              0.663             58.3                           0.364                7.10              0.487                                 ok            True                  False
    ZS           83.33               36            1.07              1.14        151.64                58.64         0.521          pass              0.505             63.5                           0.753               12.22              1.393                                 ok            True                  False
  MDLZ           85.71               21            0.87              0.38         61.39                24.76         0.516          pass              0.475             65.9                           0.454                6.25              0.483                                 ok            True                  False
  ASML           89.47               19            2.59             28.82       1579.67                48.89         0.506          pass              0.487             41.3                           0.675                8.27              1.237                                 ok            True                  False
  CHTR           66.67                9            3.62              3.92        153.18               119.48         0.744          pass              0.146             23.9                           0.447              -14.52             -1.263            downtrend_blocked_slope           False                  False
 CMCSA           88.89                9            1.63              0.29         25.27                62.19         0.705          pass              0.321              4.6                           0.161               -9.20             -0.865 downtrend_blocked_slope_and_streak           False                  False
  TEAM           71.43                7            5.97              3.83         89.96               114.36         0.569          pass              0.065              2.8                           0.080               24.44              3.228                                 ok           False                  False
  GEHC           64.29               28            1.23              0.55         63.24                57.03         0.566          pass              0.289             37.6                           0.497              -11.05             -0.699                                 ok           False                  False
  ORLY           80.00                5            2.37              1.54         92.30                35.12         0.559          pass              0.087             10.4                           0.371               -1.32             -0.023                                 ok           False                  False
  META           74.07               27            1.03              4.41        607.74                41.33         0.547          pass              0.276             35.9                           0.562              -11.09             -1.110 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511123807)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511123807)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511123807)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511123807)

</details>
