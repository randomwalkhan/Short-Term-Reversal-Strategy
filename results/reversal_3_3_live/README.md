# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-25 13:48:41 EST`
Last processed slot: `manage_1400`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  REGN           85.71               35            0.70              4.81        985.03                56.69         0.581          pass              0.578             67.0                           0.696                2.27              0.112                                 ok            True                  False
  SOXL           65.38               26            5.98              1.37         32.01               318.24         0.830          pass              0.416             75.6                           0.913              -53.58             -7.749            downtrend_blocked_slope           False                  False
  INTC           59.26               27            2.68              1.03         54.36               154.72         0.768          pass              0.412             74.0                           0.850              -14.67             -1.257 downtrend_blocked_slope_and_streak           False                  False
   APP           90.20               51            0.25              0.66        380.83               128.63         0.753          pass              0.836             96.4                           0.890               -6.08             -1.014 downtrend_blocked_slope_and_streak           False                  False
  MPWR           66.67               27            1.61             13.41       1184.36               121.95         0.709          pass              0.423             79.6                           0.807              -20.81             -2.156            downtrend_blocked_slope           False                  False
  MRVL           75.00               28            2.50              2.31        130.58               142.93         0.699          pass              0.418             76.1                           0.846              -24.01             -2.656            downtrend_blocked_slope           False                  False
  NVDA           75.00                8            4.64              5.05        153.22               127.00         0.669          pass              0.215             49.3                           0.699              -14.71             -1.385 downtrend_blocked_slope_and_streak           False                  False
  KLAC           71.43               35            0.64              0.60        133.39               108.62         0.661          pass              0.510             92.4                           0.977              -17.40             -1.820            downtrend_blocked_slope           False                  False
  UPRO           78.79               33            0.59              0.48        117.71                94.19         0.637          pass              0.499             94.0                           0.902              -17.27             -2.344 downtrend_blocked_slope_and_streak           False                  False
  AVGO           72.22               18            2.06              4.35        299.22                86.06         0.601          pass              0.333             73.1                           0.813              -14.58             -1.839            downtrend_blocked_slope           False                  False
   WDC           70.97               31            2.83              5.42        271.63               121.85         0.590          pass              0.419             73.4                           0.859              -15.04             -1.281            downtrend_blocked_slope           False                  False
  DRAM           47.37               19            4.55              1.14         35.43               133.83         0.585          pass              0.296             59.1                           0.778              -23.56             -2.427 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                    detail
2026-11-25T11:56:08.535993-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:40:03.209992-05:00 early_entry_1040      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:06:20.719395-05:00 early_entry_1005      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T09:20:10.412914-05:00     data_refresh            data_refresh                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-24T15:10:06.406477-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:05:05.745009-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:00:04.642854-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:55:06.326922-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:50:04.541007-05:00       entry_1500           entry_skipped                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-11-24T14:50:04.541007-05:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.494, "option_liquidity_status": "low_volume", "option_open_interest": 122.0, "option_spread_pct": 8.89, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "ODFL", "timing_score": 0.512}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261125134841)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261125134841)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261125134841)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261125134841)

</details>
