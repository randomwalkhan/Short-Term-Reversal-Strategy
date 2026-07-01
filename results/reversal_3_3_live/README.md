# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 15:00:09 EDT`
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

- Cash: `$14,720.50`
- Equity: `$28,000.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-1,360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 13280.0         4.58           4.15      126.19         125.7          bid_ask_mid                       4.15                bid_ask_mid                    True         -1360.0                  -9.29         93.33               15              1.32         33.41           31.96                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           84.62               13            0.86              0.28         46.50                18.60         0.588          pass              0.284             27.3                           0.448               -0.79              0.185                                 ok            True                  False
   XEL          100.00               17            0.80              0.45         80.11                19.51         0.580          pass              0.609             34.7                           0.491                0.86              0.420                                 ok            True                  False
  GILD           89.29               28            0.51              0.45        126.15                28.09         0.517          pass              0.487             22.6                           0.205               -1.21              0.061                                 ok            True                  False
  AVGO           78.95               19            1.96              5.18        375.53                74.76         0.674          pass              0.199             23.9                           0.347               -1.53             -0.607            downtrend_blocked_slope           False                  False
  MCHP           95.00               20            2.08              1.33         90.63                74.43         0.641          pass              0.592             20.5                           0.238               -6.62             -1.009            downtrend_blocked_slope           False                  False
  QCOM           84.62               26            0.94              1.21        184.27                83.64         0.637          pass              0.472             59.6                           0.282              -14.49             -2.005 downtrend_blocked_slope_and_streak           False                  False
  NXPI           90.91               33            0.20              0.40        280.86                65.46         0.636          pass              0.793             94.9                           0.551               -7.09             -1.126            downtrend_blocked_slope           False                  False
  MPWR           80.00               20            2.84             27.48       1370.58                91.02         0.626          pass              0.204             25.0                           0.222              -10.39             -1.422            downtrend_blocked_slope           False                  False
   ADI           88.00               25            1.32              3.67        395.60                64.06         0.615          pass              0.509             44.9                           0.296               -5.79             -0.941            downtrend_blocked_slope           False                  False
   AEP           78.57               14            1.05              1.00        136.38                19.16         0.546          pass              0.184             34.4                           0.494                4.34              0.774                                 ok           False                  False
   HON           72.22               18            1.06              1.67        223.19                42.01         0.528          pass              0.190             27.9                           0.379               -3.47             -0.183                                 ok           False                  False
  CSCO           96.97               33            0.79              0.65        117.18                44.21         0.523          pass              0.793             62.3                           0.610               -2.54             -0.292 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-01T15:00:09.367331-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped                    {"early_entry_score": 0.2, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 720.0, "option_spread_pct": 17.39, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.543}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped                           {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
2026-07-01T11:59:52.238657-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T11:35:05.893258-04:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T10:59:26.258383-04:00 early_entry_1055      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701150009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701150009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701150009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701150009)

</details>
