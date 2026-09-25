# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 11:00:05 EDT`
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

- Cash: `$73,553.30`
- Equity: `$73,553.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.68              1.90        160.80               109.71         0.720          pass              0.654             35.3                           0.469               21.33              2.826                                 ok            True                  False
  CRWD           86.11               36            1.51              2.74        258.49                96.70         0.674          pass              0.545             47.2                           0.411               22.45              2.083                                 ok            True                  False
   TRI           87.88               33            0.71              0.50        100.11                57.78         0.573          pass              0.677             85.4                           0.685                4.07             -0.102                                 ok            True                  False
  FTNT           85.00               20            2.36              2.95        177.41                58.17         0.551          pass              0.339             27.9                           0.363                9.83              1.071                                 ok            True                  False
  SHOP           82.61               23            2.03              2.06        144.28                62.63         0.517          pass              0.299             30.3                           0.440               10.42              1.292                                 ok            True                  False
  PANW           61.90               21            2.87              7.84        386.56                80.20         0.582          pass              0.219             29.1                           0.518               11.88              1.202                                 ok           False                  False
   XEL           88.89                9            0.97              0.47         69.36                16.48         0.551          pass              0.315              7.6                           0.227               -7.92             -0.775 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.75               16            0.88              0.15         23.80                23.05         0.541          pass              0.514             17.6                           0.172               -3.03             -0.343            downtrend_blocked_slope           False                  False
  CHTR           82.76               29            1.96              1.61        116.86                64.78         0.529          pass              0.325             24.0                           0.346              -18.01             -2.541 downtrend_blocked_slope_and_streak           False                  False
   EXC           93.33               15            0.71              0.20         40.11                15.59         0.518          pass              0.559             39.4                           0.429               -8.01             -0.788 downtrend_blocked_slope_and_streak           False                  False
  NVDA           91.89               37            0.08              0.12        224.53                44.14         0.517          pass              0.814             88.3                           0.641                2.80              0.675                                 ok           False                  False
  INTC           79.31               29            2.47              2.20        126.45                68.53         0.501          pass              0.228             17.0                           0.219               20.70              2.946                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-25T11:00:05.604422-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:55:06.018237-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:50:05.033774-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:45:06.089500-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:40:06.403638-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:35:06.003979-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:30:06.584523-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:25:05.951093-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:20:05.036960-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:15:03.948523-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925110005)

</details>
