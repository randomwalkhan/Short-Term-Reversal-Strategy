# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 15:10:04 EST`
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

- Cash: `$64,876.55`
- Equity: `$125,906.55`
- Realized PnL: `$116,926.55`
- Unrealized PnL: `$-1,020.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-11-02                   0     34     62050.0                 61030.0        18.25          17.95      257.89        258.61          bid_ask_mid                      17.95                bid_ask_mid                    True         -1020.0                  -1.64         85.19               27              1.71         52.01           50.49                  64.43                 487.0           31.0               0.03                      ok
```

## Today's Closed Trades (2026-11-02)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     30          2026-10-30         2026-11-02         19.4       22.65 9750.0   16.752577 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               28            1.58              2.89        261.14                64.43         0.584          pass              0.373             14.0                           0.300               -1.88             -0.060                                 ok            True                  False
  QCOM           94.44               36            0.52              0.59        164.54                51.87         0.517          pass              0.803             64.1                           0.555               -5.53             -0.235                                 ok            True                   True
   CSX           80.00               25            0.77              0.28         51.87                27.38         0.514          pass              0.211             20.0                           0.355                7.75              0.869                                 ok            True                  False
  ALNY           72.22               18            2.53              2.93        163.75               108.44         0.651          pass              0.279             53.6                           0.561              -31.06             -3.560            downtrend_blocked_slope           False                  False
   BKR           77.78                9            2.48              0.96         54.82                45.39         0.560          pass              0.088             10.7                           0.305               -3.49             -0.178                                 ok           False                  False
  INTC          100.00                1            8.61              3.96         64.06               126.81         0.545          pass              0.460              1.7                           0.167              -34.70             -2.902            downtrend_blocked_slope           False                  False
  TEAM          100.00               22            1.89              2.54        190.63                55.13         0.538          pass              0.622             29.2                           0.223              -12.41             -1.451            downtrend_blocked_slope           False                  False
  FTNT          100.00                1            6.26              5.96        133.52                91.18         0.533          pass              0.456              0.8                           0.271              -25.62             -2.749 downtrend_blocked_slope_and_streak           False                  False
  DRAM           68.18               22            2.40              0.80         47.67                67.83         0.531          pass              0.205             23.8                           0.389               -3.04              0.394                                 ok           False                  False
  META           80.65               31            0.69              2.95        613.72                38.01         0.516          pass              0.303             31.3                           0.389              -13.42             -1.534 downtrend_blocked_slope_and_streak           False                  False
  CSCO           60.00               10            1.98              1.45        103.89                35.63         0.516          pass              0.107             18.5                           0.441               -3.81             -0.087           downtrend_blocked_streak           False                  False
  AVGO           77.50               40            0.17              0.40        325.91                45.61         0.513          pass              0.498             82.2                           0.637               -2.71              0.052                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102151004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102151004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102151004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102151004)

</details>
