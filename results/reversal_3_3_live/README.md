# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 09:40:04 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$16,069.75`
- Equity: `$31,029.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$-765.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-08                   1     17     15725.0                 14960.0         9.25            8.8       97.75         96.81     last_price_stale                        NaN                unavailable                   False          -765.0                  -4.86         93.94               33              1.73         79.38            3.13                  86.36                1396.0           69.0               0.05                      ok
```

## Today's Closed Trades (2026-06-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               26            1.35              2.73        287.68               136.27         0.776          pass              0.608              7.8                           0.163               36.82              4.551                       ok            True                  False
  CSCO           96.15               26            1.14              0.99        123.72                58.94         0.632          pass              0.675             35.2                           0.264                3.72              0.545                       ok            True                  False
  TEAM           94.44               36            1.10              0.76         97.57                87.01         0.631          pass              0.818             65.6                           0.469               14.00              0.887                       ok            True                  False
  PAYX          100.00               20            0.57              0.39         98.75                34.09         0.631          pass              0.729             66.3                           0.459                3.76              0.486                       ok            True                  False
  PANW           84.21               19            2.03              3.79        264.71                58.75         0.596          pass              0.308             25.5                           0.276                1.62              0.394                       ok            True                  False
   APP           86.84               38            1.15              4.56        561.74                67.73         0.545          pass              0.555             43.7                           0.271                8.35             -0.098                       ok            True                  False
  WDAY           82.35               17            3.31              3.33        142.33                70.13         0.527          pass              0.214             17.3                           0.156               12.08              1.285                       ok            True                  False
  ADBE           82.35               34            1.09              1.88        244.19                49.77         0.520          pass              0.392             39.0                           0.439                0.76              0.180                       ok            True                  False
    ZS           81.82               33            1.02              0.92        128.85               157.94         0.897          pass              0.430             46.1                           0.420              -30.70             -1.764  downtrend_blocked_slope           False                  False
  INTU           80.49               41            0.23              0.50        305.30               100.92         0.729          pass              0.561             91.6                           0.730                0.15             -0.450                       ok           False                  False
  QCOM           88.89                9            2.82              4.31        215.92               102.17         0.689          pass              0.347             13.7                           0.248              -14.64             -1.249  downtrend_blocked_slope           False                  False
  CRWD           78.57               14            2.45             11.28        653.96                61.55         0.576          pass              0.096              4.0                           0.166               -4.30             -0.196 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-09T00:00:03.806421-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-08T15:10:01.789141-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:05:04.798011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:00:02.588621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:55:02.835387-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:50:04.804691-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-08", "training_samples": 5231, "window": 5}
2026-06-08T14:50:04.804691-04:00       entry_1500              entry {"allocated_cash": 15725.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 17, "early_entry_score": 0.733, "entry_mode": "regular", "entry_option_price": 9.25, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1396.0, "option_spread_pct": 5.41, "option_volume": 69.0, "success_rate": 93.94, "ticker": "TEAM", "timing_score": 0.623}
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609094004)

</details>
