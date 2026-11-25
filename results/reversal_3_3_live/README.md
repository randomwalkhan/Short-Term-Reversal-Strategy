# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-25 13:30:06 EST`
Last processed slot: `manage_1330`

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
  REGN           85.71               35            0.69              4.74        985.06                56.69         0.581          pass              0.580             67.5                           0.682                2.28              0.113                                 ok            True                  False
   APP           88.89               36            1.36              3.64        379.55               128.63         0.770          pass              0.728             80.1                           0.796               -7.13             -1.066 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.89               19            3.92              1.50         54.16               154.72         0.745          pass              0.320             61.9                           0.829              -15.76             -1.315 downtrend_blocked_slope_and_streak           False                  False
  SOXL           64.71               17            9.48              2.16         31.67               318.24         0.696          pass              0.300             61.4                           0.861              -55.31             -7.921            downtrend_blocked_slope           False                  False
  MCHP           87.88               33            0.37              0.15         56.30                89.73         0.685          pass              0.710             92.9                           0.886               -8.88             -0.859            downtrend_blocked_slope           False                  False
  MPWR           59.09               22            2.44             20.29       1181.41               121.95         0.684          pass              0.356             69.1                           0.889              -21.48             -2.194            downtrend_blocked_slope           False                  False
  IDXX           97.78               45            0.01              0.05        712.06                78.73         0.683          pass              0.967             99.6                           0.846                1.34              0.000                                 ok           False                  False
  MRVL           68.18               22            3.55              3.27        130.17               142.93         0.666          pass              0.345             66.1                           0.871              -24.82             -2.705            downtrend_blocked_slope           False                  False
  NVDA           80.00                5            5.19              5.64        152.96               127.00         0.660          pass              0.196             43.3                           0.757              -15.20             -1.411 downtrend_blocked_slope_and_streak           False                  False
  UPRO           80.95               21            1.92              1.59        117.24                94.19         0.630          pass              0.403             80.4                           0.914              -18.38             -2.405 downtrend_blocked_slope_and_streak           False                  False
  KLAC           67.86               28            2.10              1.96        132.81               108.62         0.611          pass              0.407             75.1                           0.851              -18.61             -1.887            downtrend_blocked_slope           False                  False
   KDP           89.19               37            0.17              0.04         35.78                47.26         0.578          pass              0.730             82.4                           0.394               -6.56             -0.387                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261125133006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261125133006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261125133006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261125133006)

</details>
