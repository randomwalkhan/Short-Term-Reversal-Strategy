# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 09:30:06 EDT`
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
  TEAM     option         option TEAM260717C00100000       2026-06-08                   1     17     15725.0                 14960.0         9.25            8.8       97.75         94.75     last_price_stale                        NaN                unavailable                   False          -765.0                  -4.86         93.94               33              1.73         79.38            3.13                  86.36                1396.0           69.0               0.05                      ok
```

## Today's Closed Trades (2026-06-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.36              0.79         82.84                69.62         0.687          pass              0.224              4.2                           0.179               -1.99             -0.122                      ok            True                  False
  PAYX          100.00               11            1.37              0.95         98.51                34.09         0.649          pass              0.472              0.0                           0.168                2.91              0.449                      ok            True                  False
  CSCO           96.43               28            0.70              0.61        123.89                58.94         0.645          pass              0.766             60.5                           0.442                4.19              0.565                      ok            True                  False
  CTSH           92.59               27            0.92              0.34         52.84                51.28         0.590          pass              0.647             46.2                           0.347                1.33             -0.123                      ok            True                  False
  PANW           92.11               38            0.55              1.03        265.89                58.75         0.589          pass              0.754             61.7                           0.420                3.16              0.462                      ok            True                  False
  TEAM           95.65               23            3.21              2.20         96.95                87.01         0.586          pass              0.545              0.0                           0.217               11.58              0.789                      ok            True                  False
  ADBE           83.78               37            0.80              1.37        244.40                49.77         0.528          pass              0.452             39.3                           0.438                1.06              0.193                      ok            True                  False
  WDAY           83.33               12            4.00              4.02        142.04                70.13         0.519          pass              0.154              0.0                           0.177               11.28              1.252                      ok            True                  False
  AMGN           92.86               14            1.10              2.70        348.43                22.55         0.517          pass              0.646             75.0                           0.586                2.91              0.410                      ok            True                  False
   ROP           88.89               18            1.48              3.45        332.27                34.53         0.514          pass              0.342              0.0                           0.164                2.66              0.416                      ok            True                  False
   ADP           95.24               21            1.22              1.96        228.24                32.89         0.502          pass              0.658             44.9                           0.326                3.63              0.547                      ok            True                  False
    ZS           81.82               33            0.94              0.85        128.88               157.94         0.901          pass              0.409             39.0                           0.361              -30.64             -1.760 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609093006)

</details>
