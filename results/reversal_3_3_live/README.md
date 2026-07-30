# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 15:05:01 EDT`
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

- Cash: `$16,667.25`
- Equity: `$33,652.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$430.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   0     86     16555.0                 16985.0         1.92           1.98       50.11         50.11          bid_ask_mid                       1.98                bid_ask_mid                    True           430.0                    2.6         92.31               13              1.24         25.34           26.05                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   CSX           92.31               13            1.23              0.44         50.55                28.82         0.578          pass              0.511             34.9                           0.489                1.39              0.262                      ok            True                  False
   MAR          100.00               13            1.56              4.16        379.34                28.18         0.571          pass              0.635             52.8                           0.413                3.30              0.340                      ok            True                  False
  AAPL           93.33               15            1.31              3.10        336.86                28.00         0.571          pass              0.591             48.5                           0.665                1.91              0.204                      ok            True                  False
  DXCM           80.95               21            1.69              0.89         74.76                45.20         0.532          pass              0.251             33.2                           0.434               -0.34             -0.324                      ok            True                  False
  GILD           85.00               20            1.30              1.20        132.21                34.28         0.530          pass              0.437             61.3                           0.721                0.75             -0.107                      ok            True                  False
  VRTX           92.86               28            1.00              3.37        481.88                33.19         0.523          pass              0.704             62.9                           0.684                0.46              0.010                      ok            True                  False
  MNST           96.43               28            0.51              0.35         97.08                25.74         0.520          pass              0.824             84.1                           0.636               -1.31             -0.237                      ok            True                  False
   AEP           82.35               17            1.21              1.09        128.93                20.00         0.516          pass              0.236             25.0                           0.321               -5.26             -0.168                      ok            True                  False
  ABNB           94.12               34            0.79              0.85        152.65                40.20         0.515          pass              0.797             69.8                           0.516                3.59              0.119                      ok            True                  False
  IDXX           81.25               16            2.04              8.15        566.28                36.22         0.508          pass              0.200             25.2                           0.454                3.23             -0.029                      ok            True                  False
  PYPL           78.95               19            1.31              0.54         58.12                61.52         0.669          pass              0.291             54.9                           0.685                3.72              0.223                      ok           False                  False
  ISRG           84.62               39            0.40              1.00        352.67                72.57         0.640          pass              0.616             78.5                           0.728               -9.59             -0.952 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
2026-07-30T12:00:05.999997-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:55:01.696793-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "entry_ask": 15.45, "entry_bid": 14.6, "entry_mode": "early", "entry_option_price": 15.025, "hypothetical_budget": 16611.13, "hypothetical_contracts": 11, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 5.66, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.714, "shadow_only": true, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "matched_signals": 39, "recovery_stability_score": 0.714, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T11:50:03.981372-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:45:03.023708-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:40:02.091678-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730150501)

</details>
