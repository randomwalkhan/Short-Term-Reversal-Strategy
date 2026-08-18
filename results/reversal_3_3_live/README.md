# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 15:50:05 EDT`
Last processed slot: `manage_1600`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           96.97               33            1.20              1.25        148.12                85.84         0.688          pass              0.747             41.6                           0.298               19.12              1.077                                 ok            True                  False
  UPRO           86.67               15            1.92              2.07        153.51                41.29         0.589          pass              0.295              8.4                           0.283               -1.75             -0.004                                 ok            True                  False
  NVDA           89.47               19            2.38              3.75        223.40                39.09         0.519          pass              0.410             15.2                           0.287                3.64              0.310                                 ok            True                  False
   APP           74.42               43            0.88              1.93        311.15                90.76         0.640          pass              0.368             34.6                           0.338              -26.32             -2.909            downtrend_blocked_slope           False                  False
  AMZN           81.08               37            0.55              1.01        260.88                61.74         0.621          pass              0.450             59.8                           0.362               -6.33             -0.679 downtrend_blocked_slope_and_streak           False                  False
  WDAY           84.62               39            0.17              0.23        191.08                90.90         0.603          pass              0.394              5.7                           0.038               11.43              1.603                                 ok           False                  False
  PCAR          100.00                9            1.90              1.74        130.09                28.21         0.570          pass              0.479              7.3                           0.298               -5.35             -0.395            downtrend_blocked_slope           False                  False
   HON           86.96               23            0.84              1.35        228.87                37.29         0.567          pass              0.339              3.5                           0.112               -8.27             -0.880            downtrend_blocked_slope           False                  False
   AEP           96.15               26            0.12              0.11        126.48                19.03         0.542          pass              0.744             61.0                           0.466               -0.79              0.074                                 ok           False                  False
  CSCO           85.71               28            1.12              0.89        112.52                42.21         0.529          pass              0.475             50.0                           0.455               -8.30             -0.999            downtrend_blocked_slope           False                  False
  AMAT           78.57               14            4.48             16.77        528.12                84.57         0.520          pass              0.187             36.2                           0.689               -6.45             -0.558            downtrend_blocked_slope           False                  False
   CSX           90.91               33            0.49              0.17         50.51                26.74         0.512          pass              0.601             35.1                           0.400               -1.37             -0.137                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818155005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818155005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818155005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818155005)

</details>
