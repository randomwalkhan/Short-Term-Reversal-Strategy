# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 15:15:01 EDT`
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

- Cash: `$34,398.10`
- Equity: `$65,560.60`
- Realized PnL: `$58,746.10`
- Unrealized PnL: `$-3,185.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL261016C00055000       2026-09-16                   0    277     34348.0                 31162.5         1.24           1.12       52.95         52.59          bid_ask_mid                       1.12                bid_ask_mid                    True         -3185.5                  -9.27         86.67               15               1.6         34.82           35.65                  57.87                7856.0         1919.0               0.11                      ok
```

## Today's Closed Trades (2026-09-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TMUS     option         option TMUS261016C00185000     70          2026-09-15         2026-09-16          5.1        4.59 -3570.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           86.84               38            1.09              1.85        241.70               100.47         0.675          pass              0.631             64.7                           0.376               11.52              1.322                                 ok            True                  False
  PYPL           80.00               10            2.27              0.85         53.44                57.87         0.635          pass              0.068              1.6                           0.056                0.61             -0.191                                 ok            True                  False
    ZS           97.14               35            1.04              1.41        193.28                82.15         0.621          pass              0.835             68.6                           0.366                7.57              0.909                                 ok            True                  False
  MSTR           83.33               24            3.76              3.41        128.14               105.80         0.574          pass              0.306             22.3                           0.317               -0.12             -0.186                                 ok            True                  False
  TEAM          100.00               36            0.95              1.27        189.27                62.94         0.568          pass              0.817             62.4                           0.339                0.52             -0.019                                 ok            True                  False
   ADP           95.00               20            0.83              1.60        275.84                24.27         0.544          pass              0.671             49.9                           0.375               -2.64             -0.262                                 ok            True                  False
  CTSH          100.00               20            1.99              0.88         62.90                43.25         0.542          pass              0.547              8.7                           0.134               -2.16             -0.222                                 ok            True                  False
  FTNT           90.48               42            0.58              0.70        172.07                59.28         0.533          pass              0.755             74.0                           0.412                5.88              0.893                                 ok            True                  False
  SOXL           81.08               37            0.59              0.42        102.14               117.61         0.664          pass              0.430             51.6                           0.308               -3.96             -0.460            downtrend_blocked_slope           False                  False
   TRI           93.33               30            1.11              0.80        102.27                58.06         0.589          pass              0.639             30.5                           0.263               -4.59             -0.654 downtrend_blocked_slope_and_streak           False                  False
  ADSK           78.57               14            2.83              4.49        224.57                56.46         0.532          pass              0.080              0.0                           0.197              -11.15             -0.923 downtrend_blocked_slope_and_streak           False                  False
 CMCSA          100.00                8            2.58              0.44         24.23                34.84         0.528          pass              0.462              3.1                           0.138               -9.54             -1.115 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T15:05:01.537613-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T15:00:06.128176-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T14:55:02.603343-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T14:50:31.812161-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 34348.0, "asset_type": "option", "contract_symbol": "PYPL261016C00055000", "contracts": 277, "early_entry_score": 0.302, "entry_mode": "regular", "entry_option_price": 1.24, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 7856.0, "option_spread_pct": 11.29, "option_volume": 1919.0, "success_rate": 86.67, "ticker": "PYPL", "timing_score": 0.657}
2026-09-16T14:50:31.812161-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-16", "training_samples": 5761, "window": 5}
2026-09-16T11:50:05.471536-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "entry_ask": 14.9, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.07, "option_volume": 90.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.719, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "matched_signals": 31, "recovery_stability_score": 0.719, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:45:04.644986-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:40:01.643996-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:35:01.673280-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916151501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916151501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916151501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916151501)

</details>
