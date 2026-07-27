# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 10:35:01 EDT`
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
  CSCO           87.50               32            0.88              0.70        113.87                39.56         0.517            pass              0.411              4.3                           0.100               -5.10             -0.243                                 ok            True                  False
   CSX          100.00                8            1.50              0.56         52.99                24.65         0.584            pass              0.523             21.6                           0.334                5.62              0.583                                 ok           False                  False
  KLAC           84.62               13            5.10              7.52        207.30                94.03         0.520            pass              0.198              0.9                           0.065              -10.11             -0.889 downtrend_blocked_slope_and_streak           False                  False
   TXN           88.24               34            1.02              1.99        278.73                50.69         0.509            pass              0.435              1.4                           0.039               -7.31             -0.735            downtrend_blocked_slope           False                  False
  QCOM           86.05               43            0.02              0.02        166.96                45.64         0.497 below_threshold              0.675             88.2                           0.321               -9.26             -0.675            downtrend_blocked_slope           False                  False
  MPWR           82.35               34            1.79             16.73       1326.64                65.61         0.497 below_threshold              0.283              3.4                           0.040                1.43              0.263                                 ok           False                  False
  UPRO           85.29               34            0.47              0.45        136.08                35.93         0.495 below_threshold              0.393             14.0                           0.192               -4.98             -0.552            downtrend_blocked_slope           False                  False
  AVGO           78.57               28            1.30              3.46        380.44                43.69         0.493 below_threshold              0.170              0.2                           0.026               -1.84              0.020                                 ok           False                  False
  DRAM           76.19               21            4.63              1.73         52.46                97.77         0.488 below_threshold              0.122              0.0                           0.150              -11.46             -0.644            downtrend_blocked_slope           False                  False
   ADI           84.62               26            1.70              4.43        369.96                41.03         0.479 below_threshold              0.322             14.7                           0.193               -5.31             -0.450 downtrend_blocked_slope_and_streak           False                  False
  NXPI           82.14               28            1.56              2.95        267.98                43.93         0.470 below_threshold              0.225              0.2                           0.011               -4.80             -0.281            downtrend_blocked_slope           False                  False
  MCHP           90.00               20            3.03              1.67         78.14                53.73         0.449 below_threshold              0.378              0.0                           0.150               -9.21             -0.813 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-27T10:35:01.579138-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "GILD260918C00130000", "fill_price": 7.65, "pnl": 2750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.79, "ticker": "GILD"}
2026-07-27T10:25:04.556459-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:20:01.585305-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:15:03.558106-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:10:05.779963-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:05:02.641100-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:00:03.474876-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T09:35:01.555025-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727103501)

</details>
