# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 15:40:07 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$34,082.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$860.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   0     86     16555.0                 17415.0         1.92           2.02       50.11         50.12          bid_ask_mid                       2.02                bid_ask_mid                    True           860.0                   5.19         92.31               13              1.24         25.34           27.32                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           82.61               23            1.11              0.45         58.16                61.52         0.661          pass              0.407             61.7                           0.666                3.93              0.232                      ok            True                  False
  AAPL           91.67               12            1.39              3.29        336.78                28.00         0.584          pass              0.519             45.3                           0.508                1.83              0.200                      ok            True                  False
   CSX           92.31               13            1.19              0.42         50.56                28.82         0.581          pass              0.517             37.0                           0.443                1.43              0.263                      ok            True                  False
   MAR          100.00               11            1.82              4.84        379.04                28.18         0.568          pass              0.598             45.0                           0.287                3.03              0.328                      ok            True                  False
  GILD           88.24               17            1.53              1.42        132.12                34.28         0.539          pass              0.483             54.4                           0.547                0.51             -0.117                      ok            True                  False
  ABNB           96.67               30            1.05              1.13        152.53                40.20         0.528          pass              0.766             59.8                           0.487                3.32              0.107                      ok            True                  False
  DXCM           84.62               26            1.43              0.75         74.82                45.20         0.522          pass              0.412             43.4                           0.614               -0.07             -0.312                      ok            True                  False
   AEP           80.00               15            1.28              1.16        128.90                20.00         0.521          pass              0.146             20.2                           0.328               -5.34             -0.172                      ok            True                  False
  VRTX           93.75               32            0.79              2.69        482.18                33.19         0.510          pass              0.776             70.4                           0.624                0.67              0.019                      ok            True                   True
  IDXX           81.25               16            2.09              8.34        566.19                36.22         0.505          pass              0.194             23.4                           0.390                3.18             -0.031                      ok            True                  False
  ISRG           84.62               39            0.41              1.01        352.67                72.57         0.640          pass              0.615             78.3                           0.600               -9.59             -0.952 downtrend_blocked_slope           False                  False
  MDLZ          100.00                2            3.03              1.38         64.40                42.70         0.594          pass              0.524             21.5                           0.328                7.32              0.571                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
2026-07-30T12:00:05.999997-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:55:01.696793-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "entry_ask": 15.45, "entry_bid": 14.6, "entry_mode": "early", "entry_option_price": 15.025, "hypothetical_budget": 16611.13, "hypothetical_contracts": 11, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 5.66, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.714, "shadow_only": true, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "matched_signals": 39, "recovery_stability_score": 0.714, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T11:50:03.981372-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:45:03.023708-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730154007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730154007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730154007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730154007)

</details>
