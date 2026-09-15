# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 15:50:04 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$36,616.10`
- Equity: `$71,966.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$-350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TMUS     option         option TMUS261016C00185000       2026-09-15                   0     70     35700.0                 35350.0          5.1           5.05      181.68         180.5          bid_ask_mid                       5.05                bid_ask_mid                    True          -350.0                  -0.98          96.0               25              0.67         31.58            33.3                  25.87                 294.0          103.0               0.08                      ok
```

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.00               20            0.97              0.74        108.76                40.03         0.603          pass              0.154              9.1                           0.104                3.01              0.212                                 ok            True                  False
  TEAM          100.00               28            1.85              2.50        191.70                63.46         0.556          pass              0.689             37.9                           0.223               -2.56             -0.314                                 ok            True                  False
  TMUS           93.33               15            1.31              1.68        182.18                25.87         0.534          pass              0.442              0.0                           0.158                0.03             -0.186                                 ok            True                  False
   PEP           87.50               16            0.57              0.55        136.11                16.22         0.532          pass              0.446             50.9                           0.458               -2.37             -0.246                                 ok            True                  False
  CTSH           96.88               32            0.92              0.41         63.92                45.53         0.514          pass              0.817             73.1                           0.387               -1.66             -0.435                                 ok            True                  False
  AAPL           88.00               25            0.73              1.70        332.35                23.75         0.510          pass              0.510             48.6                           0.546                4.36              0.320                                 ok            True                  False
  MSFT          100.00               14            1.84              6.51        502.62                22.76         0.501          pass              0.494              5.8                           0.181               -2.20             -0.155                                 ok            True                  False
  AMGN           87.50                8            1.65              4.40        379.62                45.29         0.627          pass              0.263              0.0                           0.198              -12.72             -1.931 downtrend_blocked_slope_and_streak           False                  False
  PYPL           91.43               35            0.32              0.12         53.98                58.07         0.620          pass              0.753             73.1                           0.562                2.51              0.033                                 ok           False                  False
  MSTR           90.00               10            5.64              5.41        134.62               103.17         0.557          pass              0.421             32.8                           0.290               -2.81              0.090           downtrend_blocked_streak           False                  False
   EXC          100.00                7            1.05              0.31         42.59                14.63         0.553          pass              0.503             15.9                           0.199               -2.40             -0.223           downtrend_blocked_streak           False                  False
  REGN          100.00                1            2.80             15.54        787.08                29.50         0.542          pass              0.454              0.0                           0.167               -3.45             -0.664 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T15:10:04.348747-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-15T15:05:02.260320-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-15T15:00:05.246314-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-15T14:55:04.231884-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-15T14:50:04.834862-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 35700.0, "asset_type": "option", "contract_symbol": "TMUS261016C00185000", "contracts": 70, "early_entry_score": 0.689, "entry_mode": "regular", "entry_option_price": 5.1, "execution_mode": "option", "matched_signals": 25, "option_liquidity_status": "ok", "option_open_interest": 294.0, "option_spread_pct": 7.84, "option_volume": 103.0, "success_rate": 96.0, "ticker": "TMUS", "timing_score": 0.517}
2026-09-15T14:50:04.834862-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"early_entry_score": 0.751, "option_liquidity_status": "wide_spread", "option_open_interest": 7403.0, "option_spread_pct": 15.92, "option_volume": 40.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.562}
2026-09-15T14:50:04.834862-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-15", "training_samples": 5782, "window": 5}
2026-09-15T12:00:02.459407-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "VRSK261016C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.714, "early_reclaim_pct": 92.0, "entry_ask": 7.4, "entry_bid": 6.3, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 52, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.06, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.865, "shadow_only": true, "success_rate": 88.57, "ticker": "VRSK", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.714, "early_reclaim_pct": 92.0, "matched_signals": 35, "recovery_stability_score": 0.865, "success_rate": 88.57, "ticker": "VRSK", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:55:01.104674-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T11:50:04.267935-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915155004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915155004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915155004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915155004)

</details>
