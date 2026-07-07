# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-07 11:06:09 EDT`
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

- Cash: `$25,746.75`
- Equity: `$25,746.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AMAT     option         option AMAT260821C00600000      1          2026-07-06         2026-07-07       75.775     68.1975 -757.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           90.91               11            2.29              2.31        143.42                55.41         0.599            pass              0.357              0.0                             NaN                0.00              0.515                                 ok            True                  False
  PCAR           80.00               15            1.64              1.45        125.29                37.79         0.537            pass              0.160             24.2                           0.414                3.10              0.459                                 ok            True                  False
  VRTX           93.33               15            1.53              5.66        527.16                27.95         0.514            pass              0.596             51.9                           0.675               11.72              1.314                                 ok            True                  False
  FAST           91.67               12            1.55              0.52         48.09                20.37         0.514            pass              0.384              2.6                           0.163                3.12              0.534                                 ok            True                  False
  CSCO           95.24               21            1.26              1.01        113.55                39.71         0.534            pass              0.625             32.9                           0.445               -7.05             -0.707 downtrend_blocked_slope_and_streak           False                  False
  MSTR           75.00               40            1.46              1.03        100.33               102.64         0.525            pass              0.437             61.4                           0.683               -9.28             -0.152           downtrend_blocked_streak           False                  False
   ADI           62.50                8            3.56              9.69        384.68                61.47         0.501            pass              0.116             22.0                           0.447              -15.82             -1.307            downtrend_blocked_slope           False                  False
  ODFL           88.10               42            0.15              0.23        216.34                38.04         0.486 below_threshold              0.713             83.0                           0.510               -1.55             -0.135                                 ok           False                  False
  QCOM           73.68               19            3.16              4.13        184.71                82.48         0.483 below_threshold              0.172             21.2                           0.348              -18.62             -1.813 downtrend_blocked_slope_and_streak           False                  False
  ASML           80.00                5            5.35             68.33       1795.79                78.10         0.473 below_threshold              0.076              9.4                           0.364              -10.46             -0.302            downtrend_blocked_slope           False                  False
    MU           75.00                8            6.98             48.09        964.14               132.57         0.463 below_threshold              0.125             26.2                           0.702              -24.37             -1.982            downtrend_blocked_slope           False                  False
  FTNT           95.00               20            1.84              2.09        161.46                37.70         0.454 below_threshold              0.678             55.3                           0.744                9.62              1.072                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-07T11:06:09.093047-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "CRWD260821C00197500", "current_drop_pct": 0.89, "early_entry_score": 0.701, "early_reclaim_pct": 75.3, "entry_ask": 18.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 12873.38, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 537.0, "option_spread_pct": 4.52, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.679, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.356, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.701, "early_reclaim_pct": 75.3, "matched_signals": 38, "recovery_stability_score": 0.679, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.356, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T10:46:12.062462-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-07T09:56:39.997866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "AMAT260821C00600000", "fill_price": 68.1975, "pnl": -757.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AMAT"}
2026-07-07T00:00:02.324788-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-07-06T15:10:01.561163-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-06T15:05:05.496825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-06T15:00:02.458877-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-06T14:55:01.446622-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-06T14:50:04.793934-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 7577.5, "asset_type": "option", "contract_symbol": "AMAT260821C00600000", "contracts": 1, "early_entry_score": 0.663, "entry_mode": "regular", "entry_option_price": 75.775, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 762.0, "option_spread_pct": 7.32, "option_volume": 41.0, "success_rate": 95.83, "ticker": "AMAT", "timing_score": 0.677}
2026-07-06T14:50:04.793934-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-06", "training_samples": 5342, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260707110609)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260707110609)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260707110609)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260707110609)

</details>
