# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 15:40:05 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$3,078.10`
- Equity: `$74,718.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-2,430.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261009C00135000       2026-09-09                   0     34     36890.0                 38165.0        10.85          11.23      133.57        133.99          bid_ask_mid                      11.23                bid_ask_mid                    True          1275.0                   3.46         80.65               31              2.16         74.55           75.54                 103.38                 254.0           23.0               0.03                      ok
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 33475.0        14.30          12.88      209.63        208.09          bid_ask_mid                      12.88                bid_ask_mid                    True         -3705.0                  -9.97         88.89               36              1.63         52.75           51.77                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.74               39            0.92              1.35        209.44                89.86         0.658          pass              0.627             36.1                           0.473               12.25              0.577                                 ok            True                  False
  MSTR           80.65               31            1.85              1.77        135.76               103.38         0.655          pass              0.317             31.4                           0.470                5.65              0.893                                 ok            True                  False
  WDAY           91.89               37            0.50              0.66        186.00                77.37         0.634          pass              0.757             65.6                           0.605               -4.67             -0.237                                 ok            True                   True
   STX           87.10               31            1.27              8.02        900.94                74.46         0.596          pass              0.490             33.7                           0.223                8.67              0.534                                 ok            True                  False
   PEP          100.00               10            0.96              0.93        138.05                16.46         0.568          pass              0.569             37.3                           0.432               -2.59             -0.202                                 ok            True                  False
  NVDA           90.91               33            0.82              1.30        225.17                44.12         0.533          pass              0.552             18.0                           0.340                5.08              0.626                                 ok            True                  False
   AEP           90.91               22            0.58              0.51        125.20                16.51         0.512          pass              0.577             51.7                           0.443                1.57              0.214                                 ok            True                  False
  CPRT           81.48               27            1.30              0.30         32.47                44.55         0.511          pass              0.356             50.6                           0.573               -3.47             -0.080                                 ok            True                  False
   CEG           86.67               15            1.49              3.13        297.71                32.90         0.510          pass              0.404             47.3                           0.448                5.80              0.760                                 ok            True                  False
  PYPL           93.33               15            1.48              0.55         52.94                58.35         0.643          pass              0.606             50.9                           0.318              -15.65             -1.472 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                9            1.00              0.18         24.82                28.58         0.612          pass              0.527             21.9                           0.142               -1.09              0.037                                 ok           False                  False
  AMGN           96.88               32            0.32              0.88        392.79                44.47         0.578          pass              0.808             67.7                           0.544              -11.38             -0.884 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-09T15:10:06.054053-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T15:05:04.869479-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T15:00:02.977003-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:55:04.050096-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:50:05.027114-04:00       entry_1500              entry {"allocated_cash": 36890.0, "asset_type": "option", "contract_symbol": "MSTR261009C00135000", "contracts": 34, "early_entry_score": 0.281, "entry_mode": "regular", "entry_option_price": 10.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 254.0, "option_spread_pct": 2.76, "option_volume": 23.0, "success_rate": 80.65, "ticker": "MSTR", "timing_score": 0.638}
2026-09-09T14:50:05.027114-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-09", "training_samples": 5753, "window": 5}
2026-09-09T12:00:03.976220-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:55:03.977367-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:50:04.576506-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:45:06.789046-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909154005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909154005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909154005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909154005)

</details>
