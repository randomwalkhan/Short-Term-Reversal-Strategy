# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 15:50:02 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$15,257.25`
- Equity: `$31,134.75`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$912.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   0     73     14965.0                 15877.5         2.05           2.17       52.68         52.93          bid_ask_mid                       2.17                bid_ask_mid                    True           912.5                    6.1         93.55               31              0.59         45.34           44.19                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           84.21               19            0.94              0.55         82.95                69.62         0.700          pass              0.391             49.7                           0.589               -1.58             -0.103                                 ok            True                  False
    MU           80.00               15            3.82             25.37        938.41               111.98         0.550          pass              0.274             61.8                           0.690                1.91              0.069                                 ok            True                  False
   WMT           84.62               26            0.87              0.73        119.52                36.35         0.546          pass              0.414             43.2                           0.343                0.19              0.096                                 ok            True                  False
  TEAM           96.15               26            2.92              2.00         97.03                87.01         0.544          pass              0.716             51.5                           0.591               11.91              0.803                                 ok            True                  False
  CDNS           93.10               29            1.15              3.16        392.88                58.79         0.526          pass              0.750             73.6                           0.452                2.09              0.458                                 ok            True                  False
  WDAY           83.33               24            2.30              2.31        142.77                70.13         0.513          pass              0.422             62.9                           0.737               13.25              1.332                                 ok            True                  False
    ZS           71.43               14            3.36              3.04        127.95               157.94         0.850          pass              0.257             48.3                           0.649              -32.33             -1.872            downtrend_blocked_slope           False                  False
  DRAM          100.00               14            1.90              0.81         60.17               103.58         0.697          pass              0.728             77.3                           0.723               -1.88             -0.319            downtrend_blocked_slope           False                  False
  INTU           61.54               13            4.02              8.60        301.82               100.92         0.623          pass              0.125             14.2                           0.329               -3.66             -0.627 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                2            3.48              3.02        122.85                58.94         0.602          pass              0.576             38.7                           0.473                1.27              0.436                                 ok           False                  False
  MSFT           75.00                4            2.17              6.26        409.06                36.13         0.591          pass              0.157             32.5                           0.288               -3.18             -0.382            downtrend_blocked_slope           False                  False
  CTSH           94.74               38            0.15              0.06         52.97                51.28         0.557          pass              0.909             91.2                           0.700                2.12             -0.087                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-09T15:10:01.102188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T15:05:03.068175-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T15:00:05.106979-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:55:02.051864-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:50:06.133016-04:00       entry_1500                   entry {"allocated_cash": 14965.0, "asset_type": "option", "contract_symbol": "CTSH260717C00055000", "contracts": 73, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 2.05, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1420.0, "option_spread_pct": 9.76, "option_volume": 78.0, "success_rate": 93.55, "ticker": "CTSH", "timing_score": 0.576}
2026-06-09T14:50:06.133016-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.238, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 12.77, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.669}
2026-06-09T14:50:06.133016-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-09", "training_samples": 5214, "window": 5}
2026-06-09T12:00:03.055569-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609155002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609155002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609155002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609155002)

</details>
