# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 10:15:06 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$1,161.80`
- Equity: `$138,474.30`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-6,357.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 73912.5         1.10           1.12       44.42         44.68          bid_ask_mid                       1.12                bid_ask_mid                    True          1642.5                   2.27          80.0               15              0.97         20.09           23.85                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   2     40     71400.0                 63400.0        17.85          15.85      223.97        224.35          bid_ask_mid                      15.85                bid_ask_mid                    True         -8000.0                 -11.20         100.0               38              0.68         80.16           76.78                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            0.80              0.36         63.65                25.23         0.583            pass              0.520             37.8                           0.457                2.43              0.347                                 ok            True                  False
  CTSH           94.59               37            0.60              0.30         70.41                46.28         0.517            pass              0.769             49.4                           0.419               17.48              1.824                                 ok            True                  False
  TMUS           80.00               25            0.93              0.96        146.13                64.13         0.648            pass              0.253             29.4                           0.251               -4.41             -0.408            downtrend_blocked_slope           False                  False
   CEG           83.33               36            0.66              1.17        252.95                65.46         0.598            pass              0.504             60.7                           0.390              -14.33             -1.584 downtrend_blocked_slope_and_streak           False                  False
   STX           76.19               42            0.15              0.66        630.21                71.81         0.578            pass              0.526             89.3                           0.485              -16.42             -1.655 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           87.50                8            1.21              0.19         22.61                23.68         0.536            pass              0.425             57.0                           0.776                8.39              0.936                                 ok           False                  False
  MRVL           89.47               38            0.75              1.20        228.00                64.81         0.534            pass              0.685             64.0                           0.394              -14.69             -1.491            downtrend_blocked_slope           False                  False
   KDP           96.97               33            0.12              0.03         34.67                26.07         0.521            pass              0.859             84.6                           0.587                5.77              0.654                                 ok           False                  False
  AAPL           90.00               20            0.95              2.31        346.74                16.45         0.495 below_threshold              0.535             50.8                           0.691                1.01              0.156                                 ok           False                  False
   ADP           94.44               36            0.11              0.23        304.06                24.93         0.489 below_threshold              0.844             78.8                           0.526               10.97              1.151                                 ok           False                  False
  TEAM          100.00               32            1.43              2.29        226.63                47.89         0.486 below_threshold              0.768             57.6                           0.637                7.99              1.038                                 ok           False                  False
  META           80.95               21            1.15              5.19        640.39                42.27         0.486 below_threshold              0.369             74.1                           0.536              -14.50             -1.803 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T10:15:06.813436-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:10:04.818104-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:05:04.929222-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ABNB261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "entry_ask": 12.55, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 11.3, "hypothetical_budget": 1161.8, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 540.0, "option_spread_pct": 22.12, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "matched_signals": 35, "recovery_stability_score": 0.623, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:00:02.755892-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T03:00:06.095406-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:45:06.637393-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:40:05.798457-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:35:04.182353-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026101506)

</details>
