# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 14:55:01 EDT`
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

- Cash: `$30,388.00`
- Equity: `$57,523.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   0      9     27315.0                 27135.0        30.35          30.15      310.66        310.57          bid_ask_mid                      30.15                bid_ask_mid                    True          -180.0                  -0.66          87.5               32              1.06         63.04           63.01                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           87.50               32            1.13              2.48        312.94                88.60         0.662          pass              0.647             78.1                           0.706                1.32             -0.224                                 ok            True                  False
  GEHC           97.06               34            0.74              0.39         74.65                48.71         0.587          pass              0.722             34.5                           0.505                1.82              0.258                                 ok            True                  False
  ASML           88.24               34            0.58              7.18       1760.68                48.84         0.560          pass              0.654             72.8                           0.607                1.16             -0.230                                 ok            True                  False
  DXCM           87.88               33            0.89              0.58         92.09                49.72         0.560          pass              0.472             17.5                           0.305                4.41              0.257                                 ok            True                  False
  PCAR          100.00               20            1.24              1.13        130.54                25.90         0.525          pass              0.553             11.4                           0.289               -1.13             -0.193                                 ok            True                  False
  REGN          100.00               31            0.66              3.86        832.39                30.64         0.511          pass              0.736             48.2                           0.616                2.65              0.476                                 ok            True                  False
  CPRT           82.61               23            1.63              0.38         33.63                47.97         0.508          pass              0.255             16.0                           0.247               12.37              1.752                                 ok            True                  False
  ALNY           87.18               39            0.49              0.81        235.87               131.78         0.803          pass              0.719             84.8                           0.821                8.33              0.787                                 ok           False                  False
  INSM           80.00               25            1.77              1.56        125.10               110.84         0.783          pass              0.248             23.1                           0.192               -8.32             -0.644 downtrend_blocked_slope_and_streak           False                  False
  AMAT           90.32               31            1.33              4.60        490.35                82.60         0.661          pass              0.676             64.8                           0.526               -6.87             -0.949            downtrend_blocked_slope           False                  False
  WDAY           82.50               40            0.15              0.21        199.92                82.42         0.640          pass              0.609             92.9                           0.564                8.43              0.939                                 ok           False                  False
   APP           67.57               37            1.76              3.77        304.15                90.15         0.617          pass              0.346             34.8                           0.436              -11.39             -0.690            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-24T14:55:01.386568-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:50:01.463647-04:00       entry_1500              entry {"allocated_cash": 27315.0, "asset_type": "option", "contract_symbol": "LRCX261016C00310000", "contracts": 9, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 5.27, "option_volume": 30.0, "success_rate": 87.5, "ticker": "LRCX", "timing_score": 0.666}
2026-08-24T14:50:01.463647-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-24", "training_samples": 5698, "window": 5}
2026-08-24T12:00:04.404720-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:55:01.402592-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:50:02.380511-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:45:05.900318-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:40:01.544592-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:35:02.435409-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:30:05.214831-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824145501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824145501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824145501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824145501)

</details>
