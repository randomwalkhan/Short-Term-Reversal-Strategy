# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:55:05 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.75               32            1.46              1.71        166.60               109.59         0.722          pass              0.752             55.4                           0.595               24.25              2.869                                 ok            True                  False
  PYPL           88.89               18            1.38              0.51         52.67                57.12         0.639          pass              0.451             32.4                           0.391               -0.02             -0.179                                 ok            True                  False
  NVDA           92.31               26            0.99              1.59        228.19                44.57         0.591          pass              0.617             41.0                           0.502                1.42              0.471                                 ok            True                  False
  ADSK           84.21               38            0.53              0.81        219.27                55.47         0.554          pass              0.555             67.0                           0.714                5.73              0.333                                 ok            True                  False
  DRAM           82.14               28            1.98              0.88         63.24                51.34         0.525          pass              0.339             36.4                           0.481                1.27              0.628                                 ok            True                  False
  AMAT           82.50               40            0.56              1.85        471.67                51.05         0.515          pass              0.549             76.9                           0.839                0.21              0.269                                 ok            True                  False
  UPRO           83.33               24            1.29              1.39        153.15                31.44         0.505          pass              0.339             35.4                           0.460                3.10              0.491                                 ok            True                  False
   STX           84.62               39            0.54              3.49        918.35                53.68         0.501          pass              0.624             85.7                           0.716                3.27              0.614                                 ok            True                  False
  MRVL           78.95               38            0.59              1.09        261.89                69.87         0.594          pass              0.465             73.1                           0.610               10.97              1.524                                 ok           False                  False
  SOXL           77.78               27            4.52              4.81        149.89               119.42         0.579          pass              0.305             44.5                           0.660               15.34              2.453                                 ok           False                  False
  AMGN           84.85               33            0.49              1.41        409.63                46.69         0.566          pass              0.471             44.0                           0.222                4.33              0.622                                 ok           False                  False
   XEL          100.00                4            1.53              0.77         71.73                15.29         0.551          pass              0.458              0.9                           0.275               -6.11             -0.575 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-23T10:55:05.536781-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "entry_ask": 4.7, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.6, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.851, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "matched_signals": 36, "recovery_stability_score": 0.851, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "trend_health_status": "ok"}, {"current_drop_pct": 0.85, "early_entry_score": 0.678, "early_reclaim_pct": 66.5, "matched_signals": 32, "recovery_stability_score": 0.814, "success_rate": 90.62, "ticker": "QCOM", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:50:05.940190-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:45:05.446928-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:40:01.660057-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:35:05.492268-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:30:06.224797-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:25:06.407969-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:20:05.981567-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:15:04.258896-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:10:06.450659-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "entry_ask": 5.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 41.86, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.742, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "matched_signals": 33, "recovery_stability_score": 0.742, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923105505)

</details>
