# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 15:00:02 EDT`
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

- Cash: `$16,083.25`
- Equity: `$32,088.25`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$247.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   0     55     15757.5                 16005.0         2.86           2.91       58.15         58.11          bid_ask_mid                       2.91                bid_ask_mid                    True           247.5                   1.57         91.18               34              0.66         31.86           32.37                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.12               34            0.65              0.32         70.12                58.11         0.626          pass              0.644             14.8                           0.254               13.73              1.699                       ok            True                  False
  PYPL           90.91               33            0.73              0.30         58.41                60.15         0.615          pass              0.731             75.1                           0.468                4.68              0.478                       ok            True                  False
 CMCSA           83.33               12            1.48              0.26         24.82                44.00         0.594          pass              0.275             37.8                           0.538                4.42              0.998                       ok            True                  False
  CTAS           90.00               20            1.33              1.90        202.84                37.77         0.582          pass              0.486             31.4                           0.474               -0.21             -0.118                       ok            True                  False
  PAYX          100.00               17            0.84              0.70        118.36                35.13         0.575          pass              0.722             72.7                           0.561                7.36              0.760                       ok            True                  False
   KDP           80.95               21            0.66              0.14         31.04                28.75         0.554          pass              0.311             52.3                           0.331                2.30              0.459                       ok            True                  False
   PEP           84.00               25            0.55              0.53        138.87                25.68         0.549          pass              0.368             35.6                           0.315                1.98              0.238                       ok            True                  False
  MSFT           81.58               38            0.62              2.14        491.89                57.86         0.545          pass              0.454             57.1                           0.536               25.47              3.077                       ok            True                  False
  CPRT           87.50               16            2.21              0.45         29.20                38.86         0.515          pass              0.358             22.2                           0.393                5.82              0.599                       ok            True                  False
  DRAM           77.14               35            0.28              0.11         54.84               109.93         0.737          pass              0.519             92.9                           0.629               -5.25             -0.563 downtrend_blocked_streak           False                  False
  SOXL           78.79               33            3.06              3.00        138.62               182.46         0.729          pass              0.396             56.8                           0.445              -15.76             -1.803 downtrend_blocked_streak           False                  False
  AMAT           90.32               31            1.21              4.65        544.63                87.24         0.657          pass              0.657             58.6                           0.409               -2.52             -0.301 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-05T15:00:02.739208-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:55:01.792293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:50:06.241655-04:00       entry_1500                   entry {"allocated_cash": 15757.5, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 55, "early_entry_score": 0.753, "entry_mode": "regular", "entry_option_price": 2.865, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7033.0, "option_spread_pct": 3.84, "option_volume": 38.0, "success_rate": 91.18, "ticker": "PYPL", "timing_score": 0.614}
2026-08-05T14:50:06.241655-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.655, "option_liquidity_status": "low_volume", "option_open_interest": 2148.0, "option_spread_pct": 6.06, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "GEHC", "timing_score": 0.628}
2026-08-05T14:50:06.241655-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-05", "training_samples": 5567, "window": 5}
2026-08-05T12:00:04.693066-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200                    exit                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805150002)

</details>
