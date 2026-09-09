# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:25:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$39,968.10`
- Equity: `$76,693.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-455.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 36725.0         14.3          14.12      209.63        208.89          bid_ask_mid                      14.12                bid_ask_mid                    True          -455.0                  -1.22         88.89               36              1.63         52.75           54.52                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           90.91               44            0.62              0.91        209.63                89.86         0.653          pass              0.631             24.9                           0.238               12.59              0.591                                 ok            True                  False
  WDAY           91.67               36            0.65              0.85        185.92                77.37         0.632          pass              0.713             55.3                           0.464               -4.81             -0.244                                 ok            True                  False
   WMT           82.76               29            0.80              0.59        105.80                40.18         0.555          pass              0.271              5.1                           0.151               -0.17              0.271                                 ok            True                  False
  TMUS           91.67               12            1.72              2.18        180.75                25.45         0.500          pass              0.398              8.0                           0.201               -1.11              0.185                                 ok            True                  False
  MSTR           85.00               40            0.26              0.25        136.41               103.38         0.711          pass              0.616             70.7                           0.377                7.36              0.967                                 ok           False                  False
  PYPL           94.12               34            0.36              0.13         53.12                58.35         0.600          pass              0.861             88.1                           0.758              -14.69             -1.421 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               16            1.22              1.00        116.50                30.90         0.568          pass              0.567             23.4                           0.390               -7.59             -0.755            downtrend_blocked_slope           False                  False
   PEP          100.00                9            1.17              1.13        137.96                16.46         0.565          pass              0.456              0.0                           0.211               -2.80             -0.212                                 ok           False                  False
  ADBE           94.59               37            0.26              0.48        257.06                50.01         0.556          pass              0.762             45.6                           0.341               -6.33             -0.819            downtrend_blocked_slope           False                  False
  PANW           85.37               41            0.83              1.96        336.14                67.50         0.553          pass              0.505             35.7                           0.192               -1.68             -0.823            downtrend_blocked_slope           False                  False
  MELI          100.00                6            2.83             38.10       1909.92                47.09         0.551          pass              0.532             25.7                           0.570               -6.27             -0.218           downtrend_blocked_streak           False                  False
   EXC           94.44               18            0.28              0.09         43.91                15.52         0.548          pass              0.680             62.1                           0.381               -0.15              0.023                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-09T10:25:04.909615-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:20:01.984247-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:15:03.852683-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909102504)

</details>
