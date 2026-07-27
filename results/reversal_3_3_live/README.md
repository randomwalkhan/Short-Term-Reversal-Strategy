# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 11:00:02 EDT`
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
   CSX          100.00                4            1.97              0.73         52.92                24.65         0.580            pass              0.458              0.0                           0.259                5.12              0.562                                 ok           False                  False
  KLAC           86.67               15            4.13              6.08        207.91                94.03         0.559            pass              0.376             36.4                           0.542               -9.19             -0.843 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.92               26            2.96              1.10         52.73                97.77         0.552            pass              0.303             47.0                           0.583               -9.90             -0.565            downtrend_blocked_slope           False                  False
  MPWR           84.21               38            0.37              3.41       1332.35                65.61         0.546            pass              0.624             90.0                           0.852                2.91              0.329                                 ok           False                  False
   TXN           89.47               38            0.04              0.07        279.55                50.69         0.539            pass              0.788             98.3                           0.718               -6.39             -0.690            downtrend_blocked_slope           False                  False
   XEL          100.00               27            0.26              0.15         81.61                20.22         0.536            pass              0.692             41.7                           0.272                1.22              0.172                                 ok           False                  False
   EXC           96.77               31            0.05              0.02         47.52                24.01         0.529            pass              0.885             97.3                           0.559                0.88              0.147                                 ok           False                  False
  CSCO           88.57               35            0.44              0.35        114.02                39.56         0.526            pass              0.643             65.2                           0.496               -4.68             -0.222                                 ok           False                  False
  PANW           95.65               46            0.38              0.85        323.42                61.51         0.521            pass              0.691             12.9                           0.149               -2.34             -0.778 downtrend_blocked_slope_and_streak           False                  False
  CRWD           91.30               46            0.29              0.37        183.12                61.00         0.510            pass              0.726             57.9                           0.302               -2.75             -1.139 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.32               31            1.20              0.66         78.58                53.73         0.483 below_threshold              0.677             71.2                           0.795               -7.50             -0.728 downtrend_blocked_slope_and_streak           False                  False
   ADI           84.38               32            0.93              2.41        370.83                41.03         0.481 below_threshold              0.510             66.2                           0.634               -4.56             -0.415 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-27T11:00:02.589986-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:55:02.550949-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:50:04.424988-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:45:02.371125-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:40:03.993472-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:35:01.579138-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "GILD260918C00130000", "fill_price": 7.65, "pnl": 2750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.79, "ticker": "GILD"}
2026-07-27T10:25:04.556459-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:20:01.585305-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727110002)

</details>
