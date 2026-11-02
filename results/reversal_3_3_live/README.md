# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 15:20:06 EST`
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

- Cash: `$64,876.55`
- Equity: `$125,566.55`
- Realized PnL: `$116,926.55`
- Unrealized PnL: `$-1,360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-11-02                   0     34     62050.0                 60690.0        18.25          17.85      257.89        259.49          bid_ask_mid                      17.85                bid_ask_mid                    True         -1360.0                  -2.19         85.19               27              1.71         52.01            50.4                  64.43                 487.0           31.0               0.03                      ok
```

## Today's Closed Trades (2026-11-02)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     30          2026-10-30         2026-11-02         19.4       22.65 9750.0   16.752577 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.67               30            1.11              2.03        261.51                64.43         0.600          pass              0.490             39.6                           0.522               -1.41             -0.038                                 ok            True                  False
   CSX           80.95               21            0.84              0.30         51.86                27.38         0.536          pass              0.191             13.0                           0.337                7.68              0.866                                 ok            True                  False
   XEL           81.25               16            0.94              0.53         79.59                18.77         0.507          pass              0.337             71.0                           0.368                5.23              0.418                                 ok            True                  False
  ALNY           76.19               21            2.42              2.79        163.80               108.44         0.644          pass              0.305             55.7                           0.670              -30.98             -3.555            downtrend_blocked_slope           False                  False
  INTC          100.00                1            8.30              3.82         64.12               126.81         0.562          pass              0.476              6.6                           0.267              -34.47             -2.886            downtrend_blocked_slope           False                  False
   BKR           77.78                9            2.55              0.99         54.81                45.39         0.556          pass              0.080              8.1                           0.244               -3.57             -0.181                                 ok           False                  False
  FTNT          100.00                2            6.13              5.84        133.58                91.18         0.532          pass              0.470              5.7                           0.261              -25.52             -2.743 downtrend_blocked_slope_and_streak           False                  False
  DRAM           68.18               22            2.38              0.80         47.67                67.83         0.532          pass              0.206             24.1                           0.408               -3.03              0.395                                 ok           False                  False
  TEAM          100.00               28            1.56              2.10        190.82                55.13         0.520          pass              0.697             41.5                           0.278              -12.12             -1.436            downtrend_blocked_slope           False                  False
  CSCO           66.67               12            1.85              1.35        103.93                35.63         0.517          pass              0.137             23.8                           0.503               -3.69             -0.081           downtrend_blocked_streak           False                  False
  VRTX           76.92               13            1.70              6.65        556.03                30.58         0.516          pass              0.165             31.0                           0.321                9.45              0.766                                 ok           False                  False
  META           80.65               31            0.69              2.97        613.72                38.01         0.515          pass              0.302             30.9                           0.362              -13.42             -1.535 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-02T15:10:04.822162-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:05:06.352149-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:00:04.459159-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:55:05.914374-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:50:01.614756-05:00       entry_1500              entry {"allocated_cash": 62050.0, "asset_type": "option", "contract_symbol": "CEG261218C00260000", "contracts": 34, "early_entry_score": 0.324, "entry_mode": "regular", "entry_option_price": 18.25, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 487.0, "option_spread_pct": 2.74, "option_volume": 31.0, "success_rate": 85.19, "ticker": "CEG", "timing_score": 0.582}
2026-11-02T14:50:01.614756-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-02", "training_samples": 6238, "window": 5}
2026-11-02T12:00:05.602652-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:55:05.694334-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:50:03.622445-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:45:06.353234-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102152006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102152006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102152006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102152006)

</details>
