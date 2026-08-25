# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 09:55:04 EDT`
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

- Cash: `$30,388.00`
- Equity: `$59,368.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$1,665.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 28980.0        30.35           32.2      310.66        314.33          bid_ask_mid                       32.2                bid_ask_mid                    True          1665.0                    6.1          87.5               32              1.06         63.04           63.18                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               33            1.77              2.12        170.42               115.46         0.752          pass              0.395             39.3                           0.343                9.23              1.078                  ok            True                  False
  GEHC           95.45               22            1.25              0.65         73.91                49.18         0.625          pass              0.572              9.7                           0.189                0.70              0.201                  ok            True                  False
  DXCM           88.24               34            0.70              0.44         90.87                50.36         0.580          pass              0.579             47.0                           0.267                1.00              0.102                  ok            True                  False
  WDAY           80.00               30            1.96              2.74        197.98                78.88         0.574          pass              0.300             36.4                           0.335                7.71              0.736                  ok            True                  False
   TRI           88.46               26            1.90              1.44        108.00                67.11         0.562          pass              0.518             43.1                           0.445                2.30              0.448                  ok            True                  False
   KHC           86.36               22            1.09              0.20         25.59                37.91         0.560          pass              0.415             36.4                           0.394                3.00              0.359                  ok            True                  False
  PAYX          100.00               23            0.81              0.71        125.71                34.31         0.546          pass              0.687             48.5                           0.507                3.05              0.326                  ok            True                  False
 CMCSA           90.00               20            1.05              0.20         26.94                32.81         0.544          pass              0.431             14.3                           0.205                4.24              0.525                  ok            True                  False
  FAST          100.00               21            0.88              0.31         51.15                22.00         0.542          pass              0.610             27.4                           0.274               -2.96             -0.216                  ok            True                  False
  CTSH           87.10               31            1.06              0.46         62.00                52.34         0.537          pass              0.509             42.1                           0.415                5.63              0.792                  ok            True                  False
  MDLZ           94.44               18            1.50              0.68         64.41                26.88         0.528          pass              0.532             13.4                           0.200                3.16              0.369                  ok            True                  False
  SBUX           89.47               19            0.70              0.53        107.26                20.57         0.519          pass              0.557             64.1                           0.602                0.65             -0.094                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-25T00:00:04.661538-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-24T15:10:01.417381-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:05:03.439109-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:00:02.474855-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:55:01.386568-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:50:01.463647-04:00       entry_1500              entry {"allocated_cash": 27315.0, "asset_type": "option", "contract_symbol": "LRCX261016C00310000", "contracts": 9, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 5.27, "option_volume": 30.0, "success_rate": 87.5, "ticker": "LRCX", "timing_score": 0.666}
2026-08-24T14:50:01.463647-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-24", "training_samples": 5698, "window": 5}
2026-08-24T12:00:04.404720-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:55:01.402592-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:50:02.380511-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825095504)

</details>
