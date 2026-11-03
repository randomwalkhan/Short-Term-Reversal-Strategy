# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 14:55:04 EST`
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

- Cash: `$68,296.55`
- Equity: `$135,271.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$-1,175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MDLZ     option         option MDLZ261218C00067500       2026-11-03                   0    470     68150.0                 66975.0         1.45           1.42       65.69         65.62          bid_ask_mid                       1.42                bid_ask_mid                    True         -1175.0                  -1.72         90.91               11              1.03         24.34           24.02                   28.2                1121.0           33.0               0.07                      ok
```

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           91.67               12            1.13              0.19         23.79                32.70         0.596          pass              0.489             35.1                           0.315                5.55              0.520                                 ok            True                  False
  MDLZ           90.91               11            1.18              0.55         66.14                28.20         0.595          pass              0.485             42.7                           0.560                2.51              0.255                                 ok            True                  False
   ROP           82.35               17            1.37              4.61        477.57                37.35         0.561          pass              0.296             43.6                           0.384               18.77              1.692                                 ok            True                  False
   KHC           80.00               10            2.07              0.36         24.78                33.68         0.557          pass              0.110             18.3                           0.275                2.45              0.143                                 ok            True                  False
  TMUS           42.86                7            3.36              3.76        158.54                68.40         0.580          pass              0.059              0.5                           0.072               -1.89              0.037                                 ok           False                  False
   PEP           66.67                3            1.82              1.79        139.65                26.86         0.579          pass              0.078              6.6                           0.158                2.87              0.204                                 ok           False                  False
  MRVL           89.47               38            0.92              1.11        170.94                97.23         0.558          pass              0.677             60.6                           0.470              -29.36             -3.243 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           88.10               42            0.14              0.28        278.87                50.76         0.556          pass              0.744             90.7                           0.483              -18.13             -2.170 downtrend_blocked_slope_and_streak           False                  False
   EXC           71.43                7            1.38              0.45         46.26                22.18         0.555          pass              0.067              3.8                           0.232                6.46              0.704                                 ok           False                  False
  GOOG           87.80               41            0.27              0.52        277.82                49.16         0.550          pass              0.708             81.5                           0.449              -17.57             -2.090 downtrend_blocked_slope_and_streak           False                  False
   CSX           66.67                9            1.52              0.55         51.38                27.65         0.546          pass              0.096             13.7                           0.311                5.73              0.567                                 ok           False                  False
  CTSH           76.92               13            2.49              1.13         64.60                51.60         0.543          pass              0.194             40.0                           0.261               -6.91             -1.164            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-03T14:55:04.978613-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:50:06.793337-05:00       entry_1500              entry {"allocated_cash": 68150.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "contracts": 470, "early_entry_score": 0.508, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 1121.0, "option_spread_pct": 6.9, "option_volume": 33.0, "success_rate": 90.91, "ticker": "MDLZ", "timing_score": 0.603}
2026-11-03T14:50:06.793337-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-03", "training_samples": 6256, "window": 5}
2026-11-03T12:00:06.009720-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:55:04.283382-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:50:06.620716-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:45:05.991467-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:40:01.980819-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:35:05.840286-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:05.077695-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103145504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103145504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103145504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103145504)

</details>
