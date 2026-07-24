# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 10:55:02 EDT`
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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.95               21            1.07              0.42         55.82                61.86         0.671          pass              0.346             60.0                           0.470               19.60              1.846                                 ok            True                  False
  GILD           91.67               24            0.70              0.64        130.59                35.55         0.572          pass              0.532             23.4                           0.295                0.09             -0.045                                 ok            True                  False
   STX           89.47               19            4.29             27.44        901.60               102.76         0.568          pass              0.438             22.9                           0.282               -3.97              0.324                                 ok            True                  False
  ASML           92.31               26            1.86             23.46       1792.95                56.08         0.552          pass              0.585             31.8                           0.374               -1.55              0.090                                 ok            True                  False
   HON           83.33               18            1.25              2.16        245.35                40.09         0.552          pass              0.325             42.6                           0.248                7.41              0.877                                 ok            True                  False
  KLAC           84.00               25            2.35              3.60        217.19                98.03         0.668          pass              0.389             38.4                           0.372               -7.74             -0.724 downtrend_blocked_slope_and_streak           False                  False
  LRCX           83.33               24            2.67              5.97        317.22                88.87         0.588          pass              0.354             37.8                           0.338              -11.16             -0.987 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.24               17            3.75             14.77        556.47                96.41         0.549          pass              0.391             23.4                           0.282              -10.09             -0.869 downtrend_blocked_slope_and_streak           False                  False
  PANW           95.65               46            0.14              0.31        325.50                61.92         0.547          pass              0.883             76.2                           0.470               -0.22             -0.277                                 ok           False                  False
  META           86.96               46            0.12              0.53        605.87                54.86         0.544          pass              0.710             90.1                           0.706               -9.54             -1.020 downtrend_blocked_slope_and_streak           False                  False
  CSCO           90.00               40            0.03              0.02        112.75                38.92         0.542          pass              0.807             95.4                           0.491               -7.08             -0.638 downtrend_blocked_slope_and_streak           False                  False
   WDC           94.12               17            5.65             22.08        548.83               114.14         0.525          pass              0.517             13.9                           0.241               -9.58             -0.315            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-24T10:55:02.424626-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:50:02.430847-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:45:05.925719-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:40:02.342835-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:35:04.435807-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:30:02.438509-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:25:03.433473-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:20:04.356287-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:15:02.377890-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:10:05.990333-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724105502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724105502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724105502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724105502)

</details>
