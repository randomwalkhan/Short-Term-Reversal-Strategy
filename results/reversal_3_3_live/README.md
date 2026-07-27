# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 11:05:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           88.24               34            0.57              0.46        113.97                39.56         0.523            pass              0.596             54.7                           0.511               -4.81             -0.228                                 ok            True                  False
  MPWR           82.86               35            0.99              9.29       1329.83                65.61         0.523            pass              0.514             72.8                           0.693                2.26              0.300                                 ok            True                  False
   CSX          100.00                4            2.00              0.75         52.91                24.65         0.577            pass              0.467              3.2                           0.190                5.09              0.560                                 ok           False                  False
  DRAM           78.26               23            3.38              1.26         52.66                97.77         0.547            pass              0.260             39.4                           0.586              -10.30             -0.585            downtrend_blocked_slope           False                  False
   XEL          100.00               28            0.23              0.13         81.61                20.22         0.531            pass              0.715             47.2                           0.293                1.24              0.173                                 ok           False                  False
  KLAC           84.62               13            4.88              7.19        207.44                94.03         0.519            pass              0.269             24.8                           0.487               -9.90             -0.878 downtrend_blocked_slope_and_streak           False                  False
  CRWD           91.67               48            0.01              0.02        183.27                61.00         0.516            pass              0.857             98.0                           0.538               -2.48             -1.126 downtrend_blocked_slope_and_streak           False                  False
   TXN           88.89               36            0.62              1.21        279.06                50.69         0.512            pass              0.674             70.8                           0.615               -6.94             -0.717            downtrend_blocked_slope           False                  False
   WBD           92.00               25            0.54              0.10         25.73                22.96         0.511            pass              0.690             73.1                           0.586               -5.39             -0.814            downtrend_blocked_slope           False                  False
   ADI           82.14               28            1.31              3.41        370.40                41.03         0.480 below_threshold              0.382             52.2                           0.574               -4.93             -0.432 downtrend_blocked_slope_and_streak           False                  False
   AEP           80.65               31            0.47              0.45        135.35                20.37         0.467 below_threshold              0.343             46.5                           0.286               -0.54              0.015                                 ok           False                  False
   LIN           91.18               34            0.51              1.84        511.49                22.09         0.459 below_threshold              0.615             37.1                           0.334               -2.75             -0.295            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-27T11:05:01.695331-04:00 early_entry_1105 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:00:02.589986-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:55:02.550949-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:50:04.424988-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:45:02.371125-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:40:03.993472-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:35:01.579138-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "GILD260918C00130000", "fill_price": 7.65, "pnl": 2750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.79, "ticker": "GILD"}
2026-07-27T10:25:04.556459-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727110501)

</details>
