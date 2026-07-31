# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 13:19:56 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$16,667.25`
- Equity: `$34,727.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,505.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-07-30                   1     86     16555.0                 18060.0         1.92            2.1       50.11         50.31          bid_ask_mid                        2.1                bid_ask_mid                    True          1505.0                   9.09         92.31               13              1.24         25.34           26.64                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.88               33            0.77              0.31         57.52                60.55         0.629          pass              0.603             58.8                           0.642                1.14              0.315                                 ok            True                  False
   KHC           91.67               12            1.57              0.29         26.26                32.41         0.577          pass              0.456             24.5                           0.271                0.33              0.396                                 ok            True                  False
  CTAS           92.86               28            0.81              1.17        206.29                40.09         0.564          pass              0.703             61.4                           0.560                0.33              0.467                                 ok            True                  False
   PEP           84.00               25            0.55              0.54        139.97                27.40         0.547          pass              0.434             57.7                           0.549                1.68              0.494                                 ok            True                  False
  GILD           85.19               27            0.79              0.73        130.97                35.61         0.532          pass              0.509             68.0                           0.671               -3.01             -0.089                                 ok            True                  False
  MNST           88.89               18            1.30              0.89         97.27                23.72         0.522          pass              0.366              7.7                           0.243               -1.14              0.165                                 ok            True                  False
  AMGN          100.00               25            0.83              2.25        386.68                28.18         0.520          pass              0.736             61.3                           0.722                4.95              0.743                                 ok            True                  False
   TRI           86.84               38            1.05              0.73         98.52                65.88         0.508          pass              0.618             66.1                           0.556                1.66              1.061                                 ok            True                  False
  ALNY           76.47               17            2.14              3.07        204.16               124.46         0.766          pass              0.171             16.1                           0.263              -24.82             -2.004            downtrend_blocked_slope           False                  False
  DRAM           79.31               29            1.53              0.56         52.10               113.92         0.627          pass              0.374             61.5                           0.620               -2.24             -1.336 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.91               22            1.16              1.40        172.74                56.67         0.625          pass              0.569             45.3                           0.359              -10.96             -1.151            downtrend_blocked_slope           False                  False
  MDLZ          100.00                9            1.72              0.76         62.75                34.51         0.593          pass              0.479              6.5                           0.162                1.63              0.521                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:50:04.061730-04:00       entry_1500              entry {"allocated_cash": 16555.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 86, "early_entry_score": 0.509, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 2759.0, "option_spread_pct": 2.6, "option_volume": 136.0, "success_rate": 92.31, "ticker": "CSX", "timing_score": 0.578}
2026-07-30T14:50:04.061730-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-30", "training_samples": 5504, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731131956)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731131956)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731131956)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731131956)

</details>
