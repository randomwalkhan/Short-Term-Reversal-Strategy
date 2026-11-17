# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 15:40:04 EST`
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

- Cash: `$58,029.80`
- Equity: `$108,179.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$-3,060.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP261218C00400000       2026-11-17                   0     17     53210.0                 50150.0         31.3           29.5      402.79        398.86          bid_ask_mid                       29.5                bid_ask_mid                    True         -3060.0                  -5.75         94.12               17              2.99         63.29           64.13                  119.5                1252.0          197.0               0.01                      ok
```

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           95.83               24            1.32              6.48        697.87                77.90         0.726          pass              0.651             28.4                           0.508                2.88              0.326                  ok            True                  False
   ADI           90.62               32            0.93              2.49        382.10                67.56         0.605          pass              0.588             32.5                           0.365               -9.57             -0.156                  ok            True                  False
  MDLZ           93.75               16            0.97              0.46         67.34                29.55         0.594          pass              0.509             14.4                           0.286                2.71              0.178                  ok            True                  False
   TXN           93.75               32            0.63              1.29        293.66                59.80         0.592          pass              0.784             70.6                           0.591               -6.44             -0.012                  ok            True                   True
   CEG           84.62               13            2.73              5.31        275.54                60.48         0.578          pass              0.261             20.2                           0.362                2.75              1.219                  ok            True                  False
  QCOM           83.33               24            1.91              2.25        167.55                68.75         0.570          pass              0.380             46.9                           0.483                0.53              0.336                  ok            True                  False
  SBUX           88.24               17            0.98              0.75        108.40                31.47         0.567          pass              0.433             36.7                           0.354                3.36              0.197                  ok            True                  False
  CTAS           95.00               20            0.88              1.38        223.57                28.21         0.559          pass              0.578             18.5                           0.305               -0.46             -0.028                  ok            True                  False
  ODFL           80.95               21            1.59              1.94        173.46                43.33         0.553          pass              0.241             29.0                           0.483               -3.47             -0.132                  ok            True                  False
   EXC           82.35               17            1.05              0.34         46.31                21.89         0.545          pass              0.187              7.5                           0.227                1.03              0.047                  ok            True                  False
  INSM           81.58               38            1.08              0.93        122.48                61.88         0.544          pass              0.491             69.4                           0.710               16.38              1.480                  ok            True                  False
   WMT           86.36               22            0.78              0.70        128.11                25.56         0.537          pass              0.465             53.9                           0.379                2.04              0.088                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-11-17T14:50:06.628486-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 53210.0, "asset_type": "option", "contract_symbol": "APP261218C00400000", "contracts": 17, "early_entry_score": 0.66, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 1252.0, "option_spread_pct": 1.28, "option_volume": 197.0, "success_rate": 94.12, "ticker": "APP", "timing_score": 0.778}
2026-11-17T14:50:06.628486-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-17", "training_samples": 6239, "window": 5}
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:55:01.833366-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:50:06.047053-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:45:03.924491-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "entry_ask": 23.75, "entry_bid": 21.55, "entry_mode": "early", "entry_option_price": 22.65, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 9.71, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "matched_signals": 32, "recovery_stability_score": 0.589, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117154004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117154004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117154004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117154004)

</details>
