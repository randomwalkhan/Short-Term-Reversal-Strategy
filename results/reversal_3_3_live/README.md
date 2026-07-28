# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-28 15:10:01 EDT`
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

- Cash: `$18,410.50`
- Equity: `$36,470.50`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$-322.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   0    129     18382.5                 18060.0         1.42            1.4       51.22         51.31          bid_ask_mid                        1.4                bid_ask_mid                    True          -322.5                  -1.75         92.86               14              1.11         25.66           25.29                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           94.12               17            0.91              0.33         51.66                24.65         0.577            pass              0.555             24.8                           0.391                3.40              0.487                                 ok            True                  False
  KLAC           84.62               13            5.00              7.11        200.31                94.03         0.554            pass              0.315             38.8                           0.729              -13.07             -1.041 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.32               31            1.49              0.81         77.55                53.73         0.512            pass              0.651             61.5                           0.702               -8.89             -0.797 downtrend_blocked_slope_and_streak           False                  False
  ASML           92.31               13            4.03             46.66       1635.26                55.90         0.503            pass              0.502             34.4                           0.623               -7.96             -0.455            downtrend_blocked_slope           False                  False
   MAR          100.00               38            0.31              0.82        382.71                28.21         0.493 below_threshold              0.895             86.3                           0.689                5.24              0.391                                 ok           False                  False
   TXN           89.47               38            0.31              0.62        279.15                50.69         0.491 below_threshold              0.760             90.6                           0.716               -6.71             -0.706            downtrend_blocked_slope           False                  False
  SBUX           84.00               25            0.88              0.64        103.38                24.10         0.490 below_threshold              0.256              0.3                           0.149               -4.28             -0.382 downtrend_blocked_slope_and_streak           False                  False
   ADI           84.38               32            0.83              2.15        370.97                41.03         0.472 below_threshold              0.530             73.3                           0.724               -4.45             -0.410 downtrend_blocked_slope_and_streak           False                  False
   BKR           75.00                4            3.73              1.58         59.91                42.85         0.472 below_threshold              0.098             16.9                           0.303                1.16              0.215                                 ok           False                  False
  MSTR           67.74               31            2.90              2.01         97.79                77.85         0.471 below_threshold              0.332             48.2                           0.380                4.00              0.183                                 ok           False                  False
  NXPI           82.14               28            1.72              3.23        266.29                43.93         0.449 below_threshold              0.372             49.8                           0.673               -5.51             -0.315            downtrend_blocked_slope           False                  False
  SNPS           78.12               32            1.36              3.71        387.40                41.22         0.449 below_threshold              0.239             15.9                           0.322              -11.56             -1.436 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-28T15:10:01.368201-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T15:05:06.240924-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T15:00:04.083002-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T14:55:03.998605-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T14:50:06.162637-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 18382.5, "asset_type": "option", "contract_symbol": "CSX260918C00052500", "contracts": 129, "early_entry_score": 0.452, "entry_mode": "regular", "entry_option_price": 1.425, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 4433.0, "option_spread_pct": 3.51, "option_volume": 101.0, "success_rate": 92.86, "ticker": "CSX", "timing_score": 0.582}
2026-07-28T14:50:06.162637-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-28", "training_samples": 5521, "window": 5}
2026-07-28T11:54:53.220532-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T11:14:56.207799-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T10:51:29.274795-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T10:15:51.062656-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.78, "early_entry_score": 0.779, "early_reclaim_pct": 64.8, "entry_ask": 20.2, "entry_bid": 16.5, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 18396.5, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "wide_spread", "option_open_interest": 1131.0, "option_spread_pct": 20.16, "option_volume": 41.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.515, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.779, "early_reclaim_pct": 64.8, "matched_signals": 30, "recovery_stability_score": 0.755, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.515, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260728151001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260728151001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260728151001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260728151001)

</details>
