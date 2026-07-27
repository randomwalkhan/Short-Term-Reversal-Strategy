# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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
  CSCO           83.33               24            1.07              0.86        113.80                39.56         0.547            pass              0.273             11.9                           0.207               -5.29             -0.252                                 ok            True                  False
   CSX          100.00                8            1.51              0.56         52.99                24.65         0.584            pass              0.522             21.1                           0.384                5.61              0.583                                 ok           False                  False
  PANW           95.65               46            0.25              0.56        323.55                61.51         0.530            pass              0.783             43.2                           0.231               -2.21             -0.772 downtrend_blocked_slope_and_streak           False                  False
   TXN           87.10               31            1.18              2.30        278.59                50.69         0.505            pass              0.513             44.3                           0.290               -7.46             -0.743            downtrend_blocked_slope           False                  False
  CRWD           91.30               46            0.39              0.50        183.07                61.00         0.503            pass              0.683             43.7                           0.283               -2.84             -1.143 downtrend_blocked_slope_and_streak           False                  False
  UPRO           84.38               32            0.60              0.57        136.03                35.93         0.494 below_threshold              0.423             36.8                           0.264               -5.10             -0.558            downtrend_blocked_slope           False                  False
  DRAM           76.19               21            4.49              1.67         52.48                97.77         0.486 below_threshold              0.181             19.5                           0.212              -11.33             -0.637            downtrend_blocked_slope           False                  False
  KLAC           80.00               10            5.60              8.26        206.98                94.03         0.485 below_threshold              0.089             13.6                           0.197              -10.58             -0.913 downtrend_blocked_slope_and_streak           False                  False
  QCOM           85.71               42            0.16              0.19        166.89                45.64         0.484 below_threshold              0.652             83.8                           0.415               -9.39             -0.682            downtrend_blocked_slope           False                  False
  AVGO           80.77               26            1.61              4.29        380.08                43.69         0.479 below_threshold              0.257             27.2                           0.238               -2.15              0.005                                 ok           False                  False
  NXPI           83.33               30            1.34              2.53        268.16                43.93         0.463 below_threshold              0.402             44.4                           0.296               -4.58             -0.271            downtrend_blocked_slope           False                  False
   ADI           84.62               26            1.91              4.96        369.73                41.03         0.458 below_threshold              0.367             30.4                           0.248               -5.50             -0.460 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-27T10:45:02.371125-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:40:03.993472-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:35:01.579138-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:30:04.376237-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "GILD260918C00130000", "fill_price": 7.65, "pnl": 2750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.79, "ticker": "GILD"}
2026-07-27T10:25:04.556459-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:20:01.585305-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:15:03.558106-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:10:05.779963-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:05:02.641100-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727104502)

</details>
