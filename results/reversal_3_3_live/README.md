# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 15:05:04 EDT`
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
- Equity: `$27,485.75`
- Realized PnL: `$17,898.25`
- Unrealized PnL: `$-412.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GOOG     option         option GOOG260724C00380000       2026-06-17                   0     15     13837.5                 13425.0         9.23           8.95      363.95         362.7          bid_ask_mid                       8.95                bid_ask_mid                    True          -412.5                  -2.98          80.0               10              1.93         34.49           34.45                  27.92                 639.0          103.0               0.09                      ok
```

## Today's Closed Trades (2026-06-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  DRAM     option         option DRAM260717C00069000     17          2026-06-16         2026-06-17        7.425        8.55 1912.5   15.151515 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               10            1.23              0.68         78.69                23.22         0.629            pass              0.473              3.5                           0.132                0.93              0.228                                 ok            True                  False
  UPRO           94.12               17            1.75              1.76        143.38                48.01         0.588            pass              0.589             35.6                           0.340               -6.13             -0.550                                 ok            True                  False
  PAYX          100.00               10            2.00              1.40         99.68                31.37         0.588            pass              0.471              4.1                           0.109               -2.50              0.026                                 ok            True                  False
  FTNT           95.83               24            1.58              1.63        146.32                47.06         0.511            pass              0.713             56.3                           0.530               -2.80             -0.255                                 ok            True                  False
   ROP           85.71               14            2.07              4.90        335.23                28.84         0.511            pass              0.230              0.0                           0.157               -1.83             -0.025                                 ok            True                  False
  PYPL           86.67               15            1.66              0.51         43.43                27.37         0.505            pass              0.325             21.2                           0.295                1.07              0.180                                 ok            True                  False
   LIN           96.67               30            0.57              2.06        517.29                19.32         0.500 below_threshold              0.753             56.5                           0.375                4.22              0.423                                 ok            True                  False
    ZS           72.41               29            1.84              1.64        126.53               152.67         0.863            pass              0.273             20.1                           0.228               -7.06             -0.612 downtrend_blocked_slope_and_streak           False                  False
  INTU           73.91               23            2.47              4.86        278.91                99.11         0.693            pass              0.186             10.0                           0.166              -14.93             -1.552 downtrend_blocked_slope_and_streak           False                  False
  MPWR           94.12               34            0.38              3.96       1497.07                71.82         0.673            pass              0.823             73.0                           0.446               -8.12             -0.533            downtrend_blocked_slope           False                  False
   KHC          100.00                1            2.12              0.35         23.65                25.54         0.629            pass              0.519             18.5                           0.231                4.21              0.758                                 ok           False                  False
   WBD           83.33                6            0.85              0.16         26.53                17.02         0.616            pass              0.240             29.7                           0.357               -2.96             -0.136                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-17T15:05:04.450318-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:00:06.393380-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00  entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
2026-06-17T14:50:06.575124-04:00  entry_1500                   entry {"allocated_cash": 13837.5, "asset_type": "option", "contract_symbol": "GOOG260724C00380000", "contracts": 15, "early_entry_score": 0.146, "entry_mode": "regular", "entry_option_price": 9.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 639.0, "option_spread_pct": 9.21, "option_volume": 103.0, "success_rate": 80.0, "ticker": "GOOG", "timing_score": 0.538}
2026-06-17T14:50:06.575124-04:00  entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                  {"early_entry_score": 0.1, "error": "AEP: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "AEP", "timing_score": 0.582}
2026-06-17T14:50:06.575124-04:00  entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.711, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 67.0, "option_spread_pct": 30.66, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.589}
2026-06-17T14:50:06.575124-04:00  entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                              {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
2026-06-17T14:50:06.575124-04:00  entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                 {"early_entry_score": 0.468, "error": "XEL: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "XEL", "timing_score": 0.64}
2026-06-17T12:20:05.226581-04:00 manage_1230                    exit                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "DRAM260717C00069000", "fill_price": 8.55, "pnl": 1912.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.15, "ticker": "DRAM"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617150504)

</details>
