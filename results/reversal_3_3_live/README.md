# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 11:10:01 EDT`
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
  MPWR           84.21               38            0.83              7.78       1330.48                65.61         0.515            pass              0.582             77.2                           0.749                2.43              0.307                                 ok            True                  False
   CSX          100.00                4            2.02              0.75         52.91                24.65         0.575            pass              0.466              2.7                           0.178                5.07              0.560                                 ok           False                  False
  DRAM           78.26               23            3.38              1.26         52.66                97.77         0.547            pass              0.260             39.4                           0.611              -10.30             -0.585            downtrend_blocked_slope           False                  False
   XEL          100.00               25            0.39              0.22         81.57                20.22         0.540            pass              0.595             13.5                           0.224                1.08              0.166                                 ok           False                  False
   EXC           96.67               30            0.11              0.04         47.51                24.01         0.532            pass              0.870             94.6                           0.488                0.83              0.145                                 ok           False                  False
  KLAC           84.62               13            4.74              6.99        207.52                94.03         0.528            pass              0.276             26.8                           0.464               -9.77             -0.872 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.57               35            0.48              0.38        114.01                39.56         0.523            pass              0.633             61.7                           0.601               -4.72             -0.224                                 ok           False                  False
   WBD           91.30               23            0.60              0.11         25.72                22.96         0.520            pass              0.651             70.2                           0.534               -5.44             -0.816            downtrend_blocked_slope           False                  False
  CRWD           91.67               48            0.01              0.01        183.28                61.00         0.517            pass              0.860             99.2                           0.595               -2.47             -1.126 downtrend_blocked_slope_and_streak           False                  False
   TXN           88.89               36            0.65              1.27        279.03                50.69         0.510            pass              0.669             69.2                           0.586               -6.97             -0.718            downtrend_blocked_slope           False                  False
   ADI           82.76               29            1.23              3.19        370.49                41.03         0.479 below_threshold              0.414             55.3                           0.573               -4.85             -0.428 downtrend_blocked_slope_and_streak           False                  False
   AEP           80.00               30            0.50              0.48        135.34                20.37         0.471 below_threshold              0.310             43.2                           0.241               -0.57              0.013                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-27T11:10:01.834108-04:00 early_entry_1110 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:05:01.695331-04:00 early_entry_1105 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:00:02.589986-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:55:02.550949-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:50:04.424988-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:45:02.371125-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:40:03.993472-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:35:01.579138-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "GILD260918C00130000", "fill_price": 7.65, "pnl": 2750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.79, "ticker": "GILD"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727111001)

</details>
