# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 15:25:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  ALNY     option         option ALNY260918C00220000     16          2026-08-17         2026-08-18         13.9        17.8 6240.0   28.057554 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           97.06               34            0.92              0.96        148.24                85.84         0.696            pass              0.795             55.1                           0.428               19.45              1.090                                 ok            True                  False
  UPRO           86.67               15            1.79              1.94        153.57                41.29         0.595            pass              0.313             14.2                           0.259               -1.63              0.002                                 ok            True                  False
  NVDA           88.24               17            2.57              4.05        223.28                39.09         0.518            pass              0.344              8.5                           0.152                3.44              0.301                                 ok            True                  False
   APP           73.33               45            0.41              0.90        311.60                90.76         0.654            pass              0.474             69.7                           0.581              -25.97             -2.888            downtrend_blocked_slope           False                  False
  AMZN           81.08               37            0.51              0.93        260.91                61.74         0.624            pass              0.460             62.8                           0.420               -6.29             -0.677 downtrend_blocked_slope_and_streak           False                  False
   HON           88.00               25            0.55              0.88        229.07                37.29         0.574            pass              0.478             35.6                           0.340               -8.00             -0.867            downtrend_blocked_slope           False                  False
  PCAR          100.00               11            1.69              1.55        130.18                28.21         0.570            pass              0.517             17.7                           0.262               -5.14             -0.385            downtrend_blocked_slope           False                  False
  CSCO           85.71               28            1.12              0.88        112.52                42.21         0.530            pass              0.477             50.4                           0.441               -8.30             -0.999            downtrend_blocked_slope           False                  False
   CSX           90.91               33            0.43              0.15         50.52                26.74         0.516            pass              0.628             44.2                           0.453               -1.30             -0.134                                 ok           False                  False
  MCHP           83.33               24            3.32              1.87         79.46                73.04         0.509            pass              0.360             42.2                           0.706               -3.81             -0.211           downtrend_blocked_streak           False                  False
  QCOM           82.05               39            0.93              1.06        161.73                49.62         0.497 below_threshold              0.514             72.1                           0.769               -1.23              0.087                                 ok           False                  False
  AMAT           78.57               14            4.88             18.28        527.48                84.57         0.495 below_threshold              0.168             30.5                           0.546               -6.85             -0.577            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-18T12:30:08.738941-04:00      manage_1230               exit {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818152502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818152502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818152502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818152502)

</details>
