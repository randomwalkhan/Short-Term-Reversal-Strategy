# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 14:50:10 EDT`
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

- Cash: `$14,359.25`
- Equity: `$28,399.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00135000       2026-07-09                   0     24     14040.0                 14040.0         5.85           5.85      133.88        133.93          bid_ask_mid                       5.85                bid_ask_mid                    True             0.0                    0.0         93.33               15              1.42          35.3            35.3                  35.14                8090.0           34.0               0.07                      ok
```

## Today's Closed Trades (2026-07-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   CSX     option         option  CSX260821C00047500     54          2026-07-07         2026-07-09        2.350      3.0750  3915.0   30.851064 take_profit_day2_hit_at_scan
  PAYX     option         option PAYX260821C00110000     50          2026-07-08         2026-07-09        2.525      2.2725 -1262.5  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GILD           93.33               15            1.42              1.35        135.24                35.14         0.541          pass              0.621             59.3                           0.430                6.97              0.899                                 ok            True                  False
   ADP           94.44               18            1.15              1.94        240.54                32.32         0.538          pass              0.658             55.1                           0.372                8.52              1.212                                 ok            True                  False
  PAYX          100.00               25            0.81              0.61        106.32                32.56         0.531          pass              0.762             69.5                           0.400                9.78              1.163                                 ok            True                  False
  AMGN           91.67               12            1.48              3.81        366.36                27.70         0.529          pass              0.421             14.6                           0.210                3.16              0.427                                 ok            True                  False
  WDAY           82.05               39            0.61              0.59        137.63                60.72         0.504          pass              0.566             89.1                           0.751               16.05              2.064                                 ok            True                  False
  MDLZ          100.00                3            1.79              0.75         59.16                30.45         0.586          pass              0.483              8.2                           0.107               -4.59             -0.258 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           69.23               13            0.28              0.05         23.17                30.42         0.577          pass              0.328             83.5                           0.685                3.53              0.295                                 ok           False                  False
   KDP          100.00               14            0.95              0.21         30.88                33.74         0.568          pass              0.637             51.2                           0.381               -1.61             -0.468 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               13            0.89              0.50         79.41                21.16         0.561          pass              0.527             17.0                           0.272               -3.14             -0.311            downtrend_blocked_slope           False                  False
  CTAS           75.00               12            1.67              2.10        179.27                32.70         0.527          pass              0.134             22.6                           0.196                3.65              0.701                                 ok           False                  False
  CPRT           86.67               15            1.85              0.37         28.43                44.46         0.526          pass              0.361             32.5                           0.600               -7.70             -0.533            downtrend_blocked_slope           False                  False
   AEP           75.00                8            1.43              1.37        135.31                20.33         0.513          pass              0.084             10.8                           0.205               -0.75             -0.102                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-09T14:50:10.393351-04:00       entry_1500              entry {"allocated_cash": 14040.0, "asset_type": "option", "contract_symbol": "GILD260821C00135000", "contracts": 24, "early_entry_score": 0.621, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 8090.0, "option_spread_pct": 6.84, "option_volume": 34.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.541}
2026-07-09T14:50:10.393351-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-09", "training_samples": 5465, "window": 5}
2026-07-09T12:00:04.046756-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:55:06.157143-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:50:05.085430-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:45:03.060463-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:40:06.148178-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:35:06.621543-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:30:06.104076-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:25:02.920653-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709145010)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709145010)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709145010)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709145010)

</details>
