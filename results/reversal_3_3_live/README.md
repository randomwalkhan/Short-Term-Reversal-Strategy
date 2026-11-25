# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-25 14:43:49 EST`
Last processed slot: `manual`

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
  REGN           80.77               26            1.10              7.60        983.83                56.69         0.606          pass              0.331             47.9                           0.405                1.86              0.094                                 ok            True                  False
  AMGN           91.30               23            0.51              1.70        473.21                33.69         0.565          pass              0.671             75.4                           0.520                1.31             -0.087                                 ok            True                  False
  SOXL           65.38               26            4.31              0.98         32.18               318.24         0.887          pass              0.443             82.4                           0.830              -52.76             -7.668            downtrend_blocked_slope           False                  False
  INTC           64.52               31            2.11              0.81         54.45               154.72         0.781          pass              0.457             79.5                           0.692              -14.17             -1.230 downtrend_blocked_slope_and_streak           False                  False
   APP           90.00               50            0.31              0.84        380.75               128.63         0.751          pass              0.828             95.4                           0.742               -6.14             -1.017 downtrend_blocked_slope_and_streak           False                  False
  MPWR           75.61               41            0.22              1.87       1189.31               121.95         0.713          pass              0.563             97.2                           0.868              -19.70             -2.092            downtrend_blocked_slope           False                  False
  MRVL           75.76               33            1.88              1.73        130.83               142.93         0.707          pass              0.470             82.1                           0.730              -23.52             -2.627            downtrend_blocked_slope           False                  False
  IDXX           97.78               45            0.04              0.19        712.00                78.73         0.678          pass              0.963             98.3                           0.673                1.31             -0.001                                 ok           False                  False
  NVDA           75.00                8            4.66              5.07        153.21               127.00         0.668          pass              0.214             49.0                           0.650              -14.73             -1.386 downtrend_blocked_slope_and_streak           False                  False
  KLAC           72.22               36            0.39              0.36        133.49               108.62         0.667          pass              0.526             95.4                           0.735              -17.19             -1.808            downtrend_blocked_slope           False                  False
   WDC           73.68               38            1.43              2.74        272.78               121.85         0.637          pass              0.510             86.6                           0.837              -13.81             -1.215            downtrend_blocked_slope           False                  False
  DRAM           50.00               20            3.67              0.92         35.52               133.83         0.636          pass              0.331             67.0                           0.725              -22.85             -2.386 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261125144349)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261125144349)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261125144349)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261125144349)

</details>
