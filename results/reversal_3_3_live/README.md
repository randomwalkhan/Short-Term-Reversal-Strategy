# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 15:15:01 EDT`
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

- Cash: `$36,616.10`
- Equity: `$73,016.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TMUS     option         option TMUS261016C00185000       2026-09-15                   0     70     35700.0                 36400.0          5.1            5.2      181.68        181.41          bid_ask_mid                        5.2                bid_ask_mid                    True           700.0                   1.96          96.0               25              0.67         31.58           32.41                  25.87                 294.0          103.0               0.08                      ok
```

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM          100.00               32            1.36              1.84        191.98                63.46         0.561          pass              0.766             54.4                           0.342               -2.07             -0.291                                 ok            True                  False
  CTSH           97.14               35            0.51              0.23         64.00                45.53         0.520          pass              0.873             84.9                           0.418               -1.25             -0.416                                 ok            True                  False
  TMUS           95.65               23            0.81              1.04        182.45                25.87         0.520          pass              0.639             33.6                           0.343                0.54             -0.164                                 ok            True                  False
  MSFT          100.00               15            1.63              5.78        502.93                22.76         0.509          pass              0.486              0.5                           0.055               -2.00             -0.146                                 ok            True                  False
  AAPL           87.50               24            0.87              2.03        332.21                23.75         0.508          pass              0.460             38.7                           0.456                4.21              0.313                                 ok            True                  False
  AMGN           92.86               14            1.25              3.33        380.07                45.29         0.623          pass              0.494             20.8                           0.189              -12.36             -1.912 downtrend_blocked_slope_and_streak           False                  False
  PYPL           92.86               42            0.04              0.01         54.02                58.07         0.599          pass              0.894             96.9                           0.809                2.81              0.046                                 ok           False                  False
   WMT           84.85               33            0.45              0.35        108.93                40.03         0.567          pass              0.470             43.7                           0.279                3.54              0.235                                 ok           False                  False
  MSTR           80.00               15            4.89              4.69        134.93               103.17         0.559          pass              0.214             41.7                           0.649               -2.03              0.126           downtrend_blocked_streak           False                  False
  REGN          100.00                4            2.30             12.79        788.26                29.50         0.555          pass              0.475              6.5                           0.165               -2.95             -0.641 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00               10            0.75              0.22         42.62                14.63         0.554          pass              0.576             40.2                           0.352               -2.10             -0.209           downtrend_blocked_streak           False                  False
    MU           87.18               39            0.19              1.20        923.51                57.16         0.550          pass              0.607             55.9                           0.481               -3.80             -0.113           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915151501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915151501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915151501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915151501)

</details>
