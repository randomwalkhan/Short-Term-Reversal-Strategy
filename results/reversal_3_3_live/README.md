# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 10:20:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           91.18               34            0.60              6.22       1477.22                53.63         0.573          pass              0.726             70.3                           0.399                6.70              0.821                                 ok            True                  False
  DRAM           84.00               25            1.60              0.69         61.37                49.40         0.563          pass              0.347             28.1                           0.319               -4.61             -0.168                                 ok            True                  False
  ASML           80.65               31            0.67              8.70       1856.13                40.48         0.546          pass              0.240              9.3                           0.159                5.69              0.791                                 ok            True                  False
  ABNB           85.71               28            1.24              1.43        163.46                40.56         0.518          pass              0.324              0.0                           0.210                0.14              0.595                                 ok            True                  False
  INTC           87.80               41            0.47              0.39        116.02                74.54         0.588          pass              0.553             28.6                           0.195               -6.64             -0.698 downtrend_blocked_slope_and_streak           False                  False
  META           85.37               41            0.15              0.78        741.57                55.50         0.584          pass              0.637             78.6                           0.572                0.57             -0.216                                 ok           False                  False
  QCOM           90.24               41            0.27              0.35        180.64                57.17         0.559          pass              0.727             66.1                           0.442               -9.07             -1.089 downtrend_blocked_slope_and_streak           False                  False
    MU           92.68               41            0.02              0.11       1063.91                46.96         0.530          pass              0.888             99.1                           0.631               -2.95             -0.143                                 ok           False                  False
  AMGN           66.67                9            1.58              4.46        401.07                46.96         0.519          pass              0.052              0.2                           0.015               -3.32             -0.227           downtrend_blocked_streak           False                  False
  GILD           90.91               11            1.30              1.32        144.07                20.39         0.515          pass              0.349              0.0                           0.197               -6.50             -0.624 downtrend_blocked_slope_and_streak           False                  False
  LRCX           74.07               27            2.27              5.50        343.44                55.68         0.510          pass              0.173              3.0                           0.113                8.79              1.327                                 ok           False                  False
  TEAM          100.00               41            0.27              0.38        196.49                55.00         0.509          pass              0.874             74.4                           0.474                3.95              0.162                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-06T10:20:05.384079-04:00 early_entry_1020 early_entry_shadow                                                 {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "entry_ask": 13.1, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 52573.4, "hypothetical_contracts": 42, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 9.6, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.723, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.723, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:15:05.337195-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:10:04.391057-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:05:04.347348-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 52573.4, "hypothetical_contracts": 138, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 21.05, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "matched_signals": 34, "recovery_stability_score": 0.637, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:00:02.462849-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T09:50:05.348208-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MRVL261120C00270000", "fill_price": 33.65, "pnl": 16560.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 37.63, "ticker": "MRVL"}
2026-10-06T00:00:06.226199-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-10-05T15:10:05.053706-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T15:05:06.249640-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-05T15:00:06.038960-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006102005)

</details>
