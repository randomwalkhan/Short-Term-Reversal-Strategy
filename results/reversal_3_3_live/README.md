# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 10:05:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           89.66               29            0.92              9.49       1475.82                53.63         0.584            pass              0.607             54.7                           0.270                6.37              0.807                                 ok            True                  False
  DRAM           82.76               29            1.09              0.47         61.47                49.40         0.567            pass              0.410             51.1                           0.562               -4.12             -0.144                                 ok            True                  False
  TMUS           87.88               33            0.55              0.63        164.37                30.04         0.506            pass              0.530             38.6                           0.271                0.82             -0.073                                 ok            True                  False
  INTC           87.80               41            0.30              0.25        116.08                74.54         0.598            pass              0.632             54.5                           0.324               -6.48             -0.690 downtrend_blocked_slope_and_streak           False                  False
  META           83.33               36            0.39              2.05        741.02                55.50         0.597            pass              0.453             43.9                           0.287                0.32             -0.227                                 ok           False                  False
  QCOM           90.24               41            0.35              0.44        180.60                57.17         0.554            pass              0.699             56.8                           0.347               -9.13             -1.092 downtrend_blocked_slope_and_streak           False                  False
  ASML           82.86               35            0.44              5.79       1857.38                40.48         0.538            pass              0.416             39.6                           0.257                5.93              0.801                                 ok           False                  False
  LRCX           78.79               33            1.61              3.90        344.13                55.68         0.516            pass              0.299             31.2                           0.315                9.53              1.358                                 ok           False                  False
  ABNB           86.84               38            0.43              0.50        163.86                40.56         0.513            pass              0.521             33.6                           0.261                0.96              0.632                                 ok           False                  False
  TEAM          100.00               41            0.31              0.42        196.47                55.00         0.507            pass              0.865             71.6                           0.385                3.92              0.161                                 ok           False                  False
  AMAT           83.78               37            1.29              4.91        540.17                48.32         0.492 below_threshold              0.434             34.7                           0.331               13.29              1.612                                 ok           False                  False
  DASH           88.37               43            0.26              0.35        191.62                46.50         0.486 below_threshold              0.616             47.9                           0.418               -0.49             -0.033                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-06T10:05:04.347348-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 52573.4, "hypothetical_contracts": 138, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 21.05, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "matched_signals": 34, "recovery_stability_score": 0.637, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:00:02.462849-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T09:50:05.348208-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MRVL261120C00270000", "fill_price": 33.65, "pnl": 16560.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 37.63, "ticker": "MRVL"}
2026-10-06T00:00:06.226199-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-10-05T15:10:05.053706-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T15:05:06.249640-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T15:00:06.038960-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T14:55:02.074607-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T14:50:07.104378-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"early_entry_score": 0.457, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 29.3, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.53}
2026-10-05T14:50:07.104378-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-05", "training_samples": 5905, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006100504)

</details>
