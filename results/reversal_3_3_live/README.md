# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:10:02 EDT`
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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               22            1.90              4.06        303.81                65.52         0.580          pass              0.532             34.3                           0.491                0.56              0.261                                 ok            True                  False
   ADI           87.10               31            0.78              2.16        391.83                55.85         0.575          pass              0.577             63.4                           0.631               -1.89              0.098                                 ok            True                  False
   CSX           84.62               13            1.11              0.39         49.75                19.08         0.562          pass              0.268             22.9                           0.315                3.86              0.344                                 ok            True                  False
   LIN          100.00               12            1.22              4.48        520.62                20.66         0.561          pass              0.545             25.1                           0.349               -0.54             -0.300                                 ok            True                  False
  NXPI           84.62               26            1.47              2.92        282.62                58.07         0.549          pass              0.405             40.0                           0.382               -0.47              0.250                                 ok            True                  False
   WBD           83.33               12            0.96              0.19         27.40                20.00         0.544          pass              0.245             29.3                           0.401                2.08              0.274                                 ok            True                  False
  KLAC           78.57               14            3.83              6.18        227.72               109.33         0.613          pass              0.148             20.1                           0.374              -26.57             -2.086 downtrend_blocked_slope_and_streak           False                  False
  AMAT           81.25               16            3.07             12.81        590.21                98.89         0.601          pass              0.210             25.5                           0.358              -20.14             -1.393 downtrend_blocked_slope_and_streak           False                  False
  QCOM           84.85               33            0.75              0.94        177.70                61.79         0.586          pass              0.466             41.5                           0.385               -4.35             -0.078           downtrend_blocked_streak           False                  False
  ASML           94.44               36            0.15              1.88       1774.83                66.00         0.585          pass              0.876             86.2                           0.579              -10.88             -0.715            downtrend_blocked_slope           False                  False
  MDLZ           96.00               25            0.15              0.06         58.77                30.54         0.584          pass              0.829             90.2                           0.587                1.50             -0.067                                 ok           False                  False
  MPWR           78.57               28            2.06             19.82       1367.91                84.79         0.581          pass              0.297             39.5                           0.517               -2.48              0.138                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-15T11:10:02.751788-04:00 early_entry_1110 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00 early_entry_1105 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00      manage_1100               exit {"asset_type": "option", "contract_symbol": "META260821C00660000", "fill_price": 54.6, "pnl": 1545.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.48, "ticker": "META"}
2026-07-15T11:00:03.028836-04:00 early_entry_1100 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:55:06.408548-04:00 early_entry_1055 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:50:02.878047-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:45:02.900716-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:30:03.936476-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715111002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715111002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715111002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715111002)

</details>
