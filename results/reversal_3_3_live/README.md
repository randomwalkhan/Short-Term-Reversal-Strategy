# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 09:30:04 EDT`
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

- Cash: `$17,608.25`
- Equity: `$33,793.25`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$-577.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260918C00100000       2026-08-06                   1     15     16762.5                 16185.0        11.18          10.79      100.37        103.33     last_price_stale                        NaN                unavailable                   False          -577.5                  -3.45          85.0               40              0.68         79.69             0.0                  86.71               28020.0         1406.0               0.03                      ok
```

## Today's Closed Trades (2026-08-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
 CMCSA           88.89               18            0.72              0.13         25.12                44.17         0.666          pass              0.373              5.3                           0.187               12.06              0.997                      ok            True                  False
  GEHC           93.55               31            0.82              0.41         70.14                58.07         0.646          pass              0.675             36.3                           0.332               15.10              1.353                      ok            True                  False
  SHOP           97.30               37            0.92              0.95        147.03                81.21         0.640          pass              0.824             60.0                           0.386               28.43              1.835                      ok            True                  False
  PAYX          100.00               18            0.87              0.73        119.82                34.54         0.589          pass              0.512              0.0                           0.217                5.96              0.389                      ok            True                  False
  MDLZ           88.89               18            0.88              0.38         62.59                30.17         0.578          pass              0.453             35.0                           0.229                2.78              0.149                      ok            True                  False
   PEP           80.00               20            0.90              0.87        138.07                22.07         0.536          pass              0.164             14.5                           0.146                0.41             -0.156                      ok            True                  False
  ROST           92.59               27            0.99              1.76        253.55                22.77         0.521          pass              0.501              0.0                           0.179                5.40              0.418                      ok            True                  False
  PCAR           96.67               30            0.67              0.62        131.80                29.35         0.519          pass              0.585              0.0                           0.309               -0.80             -0.156                      ok            True                  False
   TRI           88.57               35            1.11              0.78         99.82                78.05         0.511          pass              0.446              0.0                           0.181                9.86              0.462                      ok            True                  False
   WDC           83.87               31            0.93              2.95        450.26               109.48         0.641          pass              0.476             56.3                           0.332              -13.95             -0.427 downtrend_blocked_slope           False                  False
   STX           88.89               36            0.20              1.21        852.43                90.51         0.639          pass              0.690             71.8                           0.419               -0.06              0.626                      ok           False                  False
  PYPL           95.24               42            0.20              0.08         59.74                59.52         0.633          pass              0.834             56.9                           0.449                6.25              0.500                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T15:05:05.205099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:55:01.108594-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-08-06T14:50:04.202564-04:00       entry_1500              entry {"allocated_cash": 16762.5, "asset_type": "option", "contract_symbol": "INTC260918C00100000", "contracts": 15, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 11.175, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 28020.0, "option_spread_pct": 3.13, "option_volume": 1406.0, "success_rate": 85.0, "ticker": "INTC", "timing_score": 0.565}
2026-08-06T14:50:04.202564-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-06", "training_samples": 5584, "window": 5}
2026-08-06T12:00:02.173564-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:55:01.207054-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:50:03.918933-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807093004)

</details>
