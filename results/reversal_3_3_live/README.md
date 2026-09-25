# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 09:50:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$35,513.30`
- Equity: `$72,393.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$4,440.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL261030C00145000       2026-09-24                   1     16     32440.0                 36880.0        20.27          23.05      145.35        151.37          bid_ask_mid                      23.05                bid_ask_mid                    True          4440.0                  13.69         83.33               36              0.62         109.9          106.82                 119.42                 341.0           51.0               0.08                      ok
```

## Today's Closed Trades (2026-09-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.75               32            1.53              1.74        160.87               109.71         0.717          pass              0.650             21.8                           0.179               21.50              2.833                                 ok            True                  False
  CRWD           86.11               36            1.60              2.90        258.43                96.70         0.675          pass              0.482             26.0                           0.240               22.34              2.079                                 ok            True                  False
  FTNT           85.19               27            1.82              2.28        177.69                58.17         0.552          pass              0.357             16.9                           0.157               10.43              1.096                                 ok            True                  False
  INTC           82.86               35            1.27              1.13        126.90                68.53         0.548          pass              0.423             41.8                           0.266               22.18              3.002                                 ok            True                  False
  SHOP           82.61               23            1.89              1.92        144.34                62.63         0.525          pass              0.314             35.1                           0.381               10.58              1.298                                 ok            True                  False
   ADP           92.31               26            0.51              0.94        262.71                22.88         0.508          pass              0.608             40.7                           0.267               -1.45             -0.318                                 ok            True                  False
  PANW           62.50               16            3.27              8.93        386.09                80.20         0.590          pass              0.151             17.3                           0.198               11.43              1.183                                 ok           False                  False
   TRI           88.57               35            0.37              0.26        100.21                57.78         0.583          pass              0.731             92.4                           0.972                4.43             -0.087                                 ok           False                  False
   WBD           93.02               43            0.05              0.01         30.84                38.24         0.549          pass              0.827             75.0                           0.555                9.31              1.160                                 ok           False                  False
   KHC           94.44               18            0.61              0.10         23.81                23.05         0.549          pass              0.564             23.7                           0.182               -2.79             -0.332            downtrend_blocked_slope           False                  False
   XEL           94.12               17            0.70              0.34         69.41                16.48         0.527          pass              0.516             13.4                           0.123               -7.66             -0.762 downtrend_blocked_slope_and_streak           False                  False
  META           66.67               12            2.37             12.90        772.06                47.68         0.527          pass              0.152             28.7                           0.373               17.24              1.819                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-25T00:00:05.872425-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-24T15:10:03.736877-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T15:05:05.616892-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T15:00:06.644624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T14:55:04.772794-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-24T14:50:06.859646-04:00       entry_1500              entry {"allocated_cash": 32440.0, "asset_type": "option", "contract_symbol": "SOXL261030C00145000", "contracts": 16, "early_entry_score": 0.614, "entry_mode": "regular", "entry_option_price": 20.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 341.0, "option_spread_pct": 7.64, "option_volume": 51.0, "success_rate": 83.33, "ticker": "SOXL", "timing_score": 0.762}
2026-09-24T14:50:06.859646-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-24", "training_samples": 5815, "window": 5}
2026-09-24T12:00:04.840325-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:55:06.286422-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:50:04.896304-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925095004)

</details>
