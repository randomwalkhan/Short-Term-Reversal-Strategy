# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 15:45:06 EDT`
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

- Cash: `$16,083.25`
- Equity: `$31,263.25`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$-577.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   0     55     15757.5                 15180.0         2.86           2.76       58.15          58.1          bid_ask_mid                       2.76                bid_ask_mid                    True          -577.5                  -3.66         91.18               34              0.66         31.86           31.01                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PYPL           90.91               33            0.76              0.31         58.41                60.15         0.613          pass              0.728             74.3                           0.435                4.66              0.477                       ok            True                  False
 CMCSA           81.25               16            0.86              0.15         24.87                44.00         0.605          pass              0.325             63.9                           0.702                5.08              1.027                       ok            True                  False
  CTAS           91.30               23            1.01              1.43        203.04                37.77         0.585          pass              0.591             48.1                           0.568                0.12             -0.103                       ok            True                  False
  SOXL           81.25               32            3.32              3.25        138.51               182.46         0.722          pass              0.411             53.1                           0.416              -15.99             -1.815 downtrend_blocked_streak           False                  False
  DRAM           76.47               34            1.18              0.45         54.70               109.93         0.689          pass              0.440             70.4                           0.355               -6.10             -0.603 downtrend_blocked_streak           False                  False
  AMAT           90.32               31            1.24              4.75        544.59                87.24         0.655          pass              0.654             57.8                           0.454               -2.54             -0.302 downtrend_blocked_streak           False                  False
   STX           88.89               36            0.30              1.79        844.58                92.19         0.644          pass              0.722             82.4                           0.331               -7.19             -0.484                       ok           False                  False
  TMUS           80.00               10            2.31              2.86        175.98                55.59         0.630          pass              0.159             32.2                           0.551               -9.33             -0.442  downtrend_blocked_slope           False                  False
  GEHC           95.12               41            0.11              0.05         70.24                58.11         0.618          pass              0.920             86.1                           0.771               14.35              1.724                       ok           False                  False
  AMZN           73.68               19            1.96              3.81        275.79                61.32         0.591          pass              0.175             18.6                           0.416               11.08              1.962                       ok           False                  False
  LRCX           85.71               28            2.28              5.07        315.57                92.33         0.584          pass              0.455             41.5                           0.356               -2.75             -0.148 downtrend_blocked_streak           False                  False
  WDAY           85.37               41            0.05              0.06        171.25                70.04         0.566          pass              0.688             96.3                           0.676               29.28              2.914                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-05T15:10:01.218994-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T15:05:03.750105-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T15:00:02.739208-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:55:01.792293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:50:06.241655-04:00       entry_1500                   entry {"allocated_cash": 15757.5, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 55, "early_entry_score": 0.753, "entry_mode": "regular", "entry_option_price": 2.865, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7033.0, "option_spread_pct": 3.84, "option_volume": 38.0, "success_rate": 91.18, "ticker": "PYPL", "timing_score": 0.614}
2026-08-05T14:50:06.241655-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.655, "option_liquidity_status": "low_volume", "option_open_interest": 2148.0, "option_spread_pct": 6.06, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "GEHC", "timing_score": 0.628}
2026-08-05T14:50:06.241655-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-05", "training_samples": 5567, "window": 5}
2026-08-05T12:00:04.693066-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805154506)

</details>
