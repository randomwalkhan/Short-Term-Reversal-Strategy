# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 15:00:06 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$14,060.75`
- Equity: `$27,710.75`
- Realized PnL: `$17,898.25`
- Unrealized PnL: `$-187.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GOOG     option         option GOOG260724C00380000       2026-06-17                   0     15     13837.5                 13650.0         9.23            9.1      363.95        362.59          bid_ask_mid                        9.1                bid_ask_mid                    True          -187.5                  -1.36          80.0               10              1.93         34.49           35.37                  27.92                 639.0          103.0               0.09                      ok
```

## Today's Closed Trades (2026-06-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  DRAM     option         option DRAM260717C00069000     17          2026-06-16         2026-06-17        7.425        8.55 1912.5   15.151515 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               10            1.18              0.65         78.70                23.22         0.632          pass              0.487              7.9                           0.259                0.99              0.230                                 ok            True                  False
  PAYX          100.00               11            1.80              1.27         99.74                31.37         0.593          pass              0.506             13.4                           0.181               -2.30              0.035                                 ok            True                  False
  UPRO           95.24               21            1.41              1.42        143.53                48.01         0.583          pass              0.676             48.1                           0.450               -5.81             -0.535                                 ok            True                  False
  FTNT           94.44               18            1.85              1.91        146.20                47.06         0.535          pass              0.639             48.9                           0.519               -3.07             -0.267                                 ok            True                  False
   ROP           88.89               18            1.61              3.81        335.70                28.84         0.518          pass              0.397             18.1                           0.189               -1.37             -0.004                                 ok            True                  False
   LIN           96.55               29            0.64              2.34        517.17                19.32         0.502          pass              0.729             50.6                           0.376                4.14              0.419                                 ok            True                  False
    ZS           72.41               29            1.67              1.48        126.59               152.67         0.869          pass              0.297             27.7                           0.280               -6.89             -0.604 downtrend_blocked_slope_and_streak           False                  False
  INTU           73.91               23            2.53              4.98        278.86                99.11         0.689          pass              0.179              7.8                           0.177              -14.98             -1.555 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                1            2.08              0.35         23.65                25.54         0.632          pass              0.524             20.2                           0.275                4.25              0.760                                 ok           False                  False
   WBD           88.89                9            0.70              0.13         26.54                17.02         0.611          pass              0.425             42.2                           0.461               -2.81             -0.129                                 ok           False                  False
  AMGN           85.71                7            1.53              3.73        346.24                26.73         0.599          pass              0.237              8.3                           0.203                4.34              0.425                                 ok           False                  False
   AEP           71.43                7            1.33              1.21        129.23                20.43         0.589          pass              0.083              8.0                           0.226                0.72              0.182                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-17T15:00:06.393380-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00       entry_1500                   entry {"allocated_cash": 13837.5, "asset_type": "option", "contract_symbol": "GOOG260724C00380000", "contracts": 15, "early_entry_score": 0.146, "entry_mode": "regular", "entry_option_price": 9.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 639.0, "option_spread_pct": 9.21, "option_volume": 103.0, "success_rate": 80.0, "ticker": "GOOG", "timing_score": 0.538}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                  {"early_entry_score": 0.1, "error": "AEP: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "AEP", "timing_score": 0.582}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.711, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 67.0, "option_spread_pct": 30.66, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.589}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                              {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                 {"early_entry_score": 0.468, "error": "XEL: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "XEL", "timing_score": 0.64}
2026-06-17T14:50:06.575124-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
2026-06-17T12:20:05.226581-04:00      manage_1230                    exit                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "DRAM260717C00069000", "fill_price": 8.55, "pnl": 1912.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.15, "ticker": "DRAM"}
2026-06-17T12:00:04.853951-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617150006)

</details>
