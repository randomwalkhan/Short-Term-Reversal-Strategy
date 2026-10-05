# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 15:45:06 EDT`
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

- Cash: `$44,576.80`
- Equity: `$88,136.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$-450.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MRVL     option         option MRVL261120C00270000       2026-10-05                   0     18     44010.0                 43560.0        24.45           24.2      269.79        270.53          bid_ask_mid                       24.2                bid_ask_mid                    True          -450.0                  -1.02         82.86               35              0.92         63.78           61.91                  54.74                2381.0          509.0               0.02                      ok
```

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           87.88               33            0.85              0.58         97.37                53.36         0.537            pass              0.617             66.5                           0.769                1.43              0.083                                 ok            True                  False
  MRVL           83.33               36            0.65              1.25        271.76                54.74         0.519            pass              0.495             60.4                           0.447                5.10              0.476                                 ok            True                  False
    MU           90.32               31            1.17              8.78       1071.13                50.82         0.508            pass              0.571             35.1                           0.455                1.76              0.032                                 ok            True                  False
  NXPI           85.71               35            0.53              0.91        243.27                37.68         0.502            pass              0.589             73.3                           0.636                4.28              0.377                                 ok            True                  False
  DRAM           80.56               36            0.29              0.13         61.73                54.09         0.574            pass              0.411             55.0                           0.451                0.03             -0.119                                 ok           False                  False
  AMGN           86.49               37            0.19              0.55        402.80                47.11         0.549            pass              0.669             86.9                           0.626                2.31              0.135                                 ok           False                  False
  ASML           84.21               38            0.17              2.24       1866.35                42.39         0.545            pass              0.623             89.7                           0.677                8.93              0.865                                 ok           False                  False
  INTC           80.00               25            2.67              2.23        118.37                74.20         0.542            pass              0.287             44.3                           0.321               -4.63             -0.568            downtrend_blocked_slope           False                  False
  LRCX           78.95               38            0.79              1.91        346.67                57.64         0.529            pass              0.398             52.8                           0.492               14.17              1.434                                 ok           False                  False
  QCOM           85.71               21            2.44              3.15        183.52                56.36         0.506            pass              0.276              0.0                           0.167               -7.14             -0.992 downtrend_blocked_slope_and_streak           False                  False
  TMUS           89.19               37            0.16              0.19        163.56                31.57         0.497 below_threshold              0.725             83.4                           0.512               -1.15             -0.129                                 ok           False                  False
   PEP           80.95               21            0.42              0.37        125.73                14.60         0.495 below_threshold              0.353             68.4                           0.591               -3.26             -0.418            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-05T15:10:05.053706-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T15:05:06.249640-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T15:00:06.038960-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T14:55:02.074607-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-05T14:50:07.104378-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 44010.0, "asset_type": "option", "contract_symbol": "MRVL261120C00270000", "contracts": 18, "early_entry_score": 0.427, "entry_mode": "regular", "entry_option_price": 24.45, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2381.0, "option_spread_pct": 2.04, "option_volume": 509.0, "success_rate": 82.86, "ticker": "MRVL", "timing_score": 0.509}
2026-10-05T14:50:07.104378-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.457, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 29.3, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.53}
2026-10-05T14:50:07.104378-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-05", "training_samples": 5905, "window": 5}
2026-10-05T12:00:06.148315-04:00 early_entry_1200      early_entry_shadow   {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "matched_signals": 33, "recovery_stability_score": 0.669, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:55:05.965880-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.716, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "matched_signals": 34, "recovery_stability_score": 0.716, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:50:06.228563-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005154506)

</details>
