# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 10:30:04 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.51              0.17         46.63               551.83         1.000          pass              0.619             14.3                           0.220               -0.77              0.159                                 ok            True                  False
  AMGN          100.00               18            0.90              2.76        435.81                27.65         0.583          pass              0.571             19.8                           0.270                4.91              0.536                                 ok            True                  False
  CSCO           83.33               30            1.17              0.92        111.76                41.41         0.537          pass              0.341             21.6                           0.362               -0.75             -0.026                                 ok            True                  False
  FAST          100.00               12            1.61              0.58         50.89                21.07         0.534          pass              0.474              2.4                           0.077               -1.39             -0.106                                 ok            True                  False
  REGN          100.00               12            1.49              8.43        804.10                24.94         0.533          pass              0.631             54.8                           0.320               -0.86             -0.025                                 ok            True                  False
  NVDA           86.67               30            1.32              2.11        227.07                42.92         0.504          pass              0.470             36.2                           0.376               -0.09             -0.158                                 ok            True                  False
  INSM           75.00               16            2.30              1.95        120.55               110.68         0.786          pass              0.221             34.2                           0.480               -4.15             -0.587            downtrend_blocked_slope           False                  False
  DRAM           75.68               37            0.07              0.03         56.82                68.22         0.620          pass              0.536             98.1                           0.796               -0.92             -0.218                                 ok           False                  False
  MCHP           89.29               28            1.53              0.81         75.14                63.59         0.610          pass              0.502             24.5                           0.239               -5.54             -0.682            downtrend_blocked_slope           False                  False
  SOXL           78.79               33            3.18              2.74        121.88               111.92         0.604          pass              0.334             40.1                           0.535              -17.81             -2.090            downtrend_blocked_slope           False                  False
  INTC           82.50               40            0.04              0.03         92.08                58.21         0.554          pass              0.617             98.4                           0.618              -10.20             -1.319 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.74               38            0.14              0.34        353.73                33.75         0.540          pass              0.693             19.9                           0.182               -0.73             -0.036                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-28T10:30:04.053969-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:25:02.074094-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:20:02.098332-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:15:03.828658-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:10:03.076583-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:05:04.075473-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:00:04.882804-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T09:20:06.065187-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-27T12:00:04.808984-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:55:06.264052-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828103004)

</details>
