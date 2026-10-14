# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 15:20:05 EDT`
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

- Cash: `$68,187.30`
- Equity: `$133,162.30`
- Realized PnL: `$125,462.30`
- Unrealized PnL: `$-2,300.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261120C00115000       2026-10-14                   0    115     67275.0                 64975.0         5.85           5.65       113.6        113.64          bid_ask_mid                       5.65                bid_ask_mid                    True         -2300.0                  -3.42         86.67               15              1.28         44.93           43.08                  34.22                4547.0          159.0               0.02                      ok
```

## Today's Closed Trades (2026-10-14)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS261120C00500000     28          2026-10-13         2026-10-14         25.4       22.86 -7112.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           86.67               15            1.22              0.98        114.65                34.22         0.549            pass              0.335             23.1                           0.359                6.02              0.624                                 ok            True                  False
    ZS           89.47               19            2.47              3.95        226.97                58.33         0.530            pass              0.444             26.2                           0.486               11.83              1.681                                 ok            True                  False
  MSFT          100.00               11            1.71              6.50        540.67                20.68         0.526            pass              0.504             14.9                           0.266                4.15              0.540                                 ok            True                  False
  SNPS           71.43                7            3.14             10.89        489.84                50.26         0.554            pass              0.093             12.5                           0.338               10.12              0.602                                 ok           False                  False
  META           57.14                7            3.16             16.85        755.28                53.30         0.548            pass              0.099             14.7                           0.403                1.83              0.236                                 ok           False                  False
  QCOM           83.33               18            2.48              3.07        175.55                53.60         0.541            pass              0.271             25.0                           0.562               -6.28             -0.639 downtrend_blocked_slope_and_streak           False                  False
  MELI           70.00               10            2.47             32.38       1862.16                40.00         0.535            pass              0.116             20.9                           0.438                5.86              0.975                                 ok           False                  False
  SHOP           75.00               16            2.53              3.13        175.18                46.81         0.508            pass              0.178             29.0                           0.467               16.01              1.868                                 ok           False                  False
  TEAM          100.00               25            1.96              2.85        206.82                43.11         0.498 below_threshold              0.602             17.4                           0.278               13.76              1.327                                 ok           False                  False
  UPRO          100.00                2            3.55              3.86        153.74                28.27         0.496 below_threshold              0.507             19.1                           0.431                1.98              0.356                                 ok           False                  False
  INTC           84.62               13            4.24              3.05        101.50                67.54         0.495 below_threshold              0.238             15.2                           0.329              -18.12             -2.150 downtrend_blocked_slope_and_streak           False                  False
  CDNS           77.78               18            1.96              4.59        332.23                36.71         0.495 below_threshold              0.168             21.6                           0.353               -0.77             -0.264                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-14T15:10:06.171047-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T15:05:05.885010-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T15:00:05.913118-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T14:55:05.778063-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T14:50:04.996677-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 67275.0, "asset_type": "option", "contract_symbol": "CSCO261120C00115000", "contracts": 115, "early_entry_score": 0.292, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 4547.0, "option_spread_pct": 1.71, "option_volume": 159.0, "success_rate": 86.67, "ticker": "CSCO", "timing_score": 0.547}
2026-10-14T14:50:04.996677-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-14", "training_samples": 6059, "window": 5}
2026-10-14T12:00:05.972511-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:55:04.759815-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261120C00055000", "current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "entry_ask": 3.65, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 67731.15, "hypothetical_contracts": 189, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 9142.0, "option_spread_pct": 4.2, "option_volume": 152.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "matched_signals": 40, "recovery_stability_score": 0.597, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-14T11:50:06.783855-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:45:05.905160-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014152005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014152005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014152005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014152005)

</details>
