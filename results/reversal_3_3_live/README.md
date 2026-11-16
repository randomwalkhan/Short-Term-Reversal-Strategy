# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 16:00:04 EST`
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

- Cash: `$59,174.80`
- Equity: `$112,864.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$-4,160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  QCOM     option         option QCOM261218C00170000       2026-11-16                   0     52     57850.0                 53690.0        11.12          10.32      170.26        168.56          bid_ask_mid                      10.32                bid_ask_mid                    True         -4160.0                  -7.19         85.19               27              1.28         54.03           54.48                  68.34                3371.0          163.0               0.02                      ok
```

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           85.00               20            2.27              2.74        171.30                68.34         0.582          pass              0.296             12.5                           0.176                4.00              0.673                      ok            True                  False
  ISRG           88.46               26            1.29              4.00        441.87                45.74         0.562          pass              0.439             16.7                           0.283                0.23             -0.297                      ok            True                  False
  CTAS           95.00               20            0.91              1.45        225.62                28.07         0.561          pass              0.594             23.6                           0.418               -0.04              0.048                      ok            True                  False
  AAPL          100.00               19            1.13              2.83        355.06                27.52         0.559          pass              0.572             18.5                           0.382                4.19              0.566                      ok            True                  False
   CEG           86.84               38            0.72              1.42        279.17                61.55         0.556          pass              0.635             70.0                           0.797                7.97              1.264                      ok            True                  False
  MSFT           96.00               25            1.11              4.07        522.14                36.51         0.542          pass              0.607             17.6                           0.349                2.16             -0.095                      ok            True                  False
  ALNY           54.55               11            3.21              3.70        163.45               110.81         0.715          pass              0.129             16.8                           0.284                1.11              0.101                      ok           False                  False
  IDXX           97.44               39            0.47              2.33        703.23                78.00         0.697          pass              0.770             35.6                           0.337                4.36              0.474                      ok           False                  False
  FTNT           57.14               14            3.09              2.75        126.04                93.31         0.658          pass              0.128             11.9                           0.156               -2.31             -0.012                      ok           False                  False
  INTC           50.00                6            7.04              2.94         58.40               143.21         0.620          pass              0.097             11.8                           0.318               -7.52              0.080                      ok           False                  False
   KDP           83.33                6            2.04              0.52         36.12                45.67         0.601          pass              0.171              7.5                           0.172               -3.31             -0.004                      ok           False                  False
   TRI           85.71               35            0.94              0.72        108.99                62.00         0.593          pass              0.451             24.4                           0.325              -11.42             -0.956 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:50:05.632368-05:00       entry_1500              entry {"allocated_cash": 57850.0, "asset_type": "option", "contract_symbol": "QCOM261218C00170000", "contracts": 52, "early_entry_score": 0.463, "entry_mode": "regular", "entry_option_price": 11.125, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 2.25, "option_volume": 163.0, "success_rate": 85.19, "ticker": "QCOM", "timing_score": 0.599}
2026-11-16T14:50:05.632368-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-16", "training_samples": 6252, "window": 5}
2026-11-16T12:00:06.189973-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:55:04.372932-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:50:05.541562-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:45:04.541902-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116160004)

</details>
