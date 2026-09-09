# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 15:05:04 EDT`
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

- Cash: `$3,078.10`
- Equity: `$73,033.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-4,115.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261009C00135000       2026-09-09                   0     34     36890.0                 36805.0        10.85          10.82      133.57        133.16          bid_ask_mid                      10.82                bid_ask_mid                    True           -85.0                  -0.23         80.65               31              2.16         74.55           75.43                 103.38                 254.0           23.0               0.03                      ok
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 33150.0        14.30          12.75      209.63        207.68          bid_ask_mid                      12.75                bid_ask_mid                    True         -4030.0                 -10.84         88.89               36              1.63         52.75           51.58                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.74               39            1.13              1.67        209.31                89.86         0.646          pass              0.581             21.2                           0.264               12.01              0.567                                 ok            True                  False
   STX           88.89               36            0.58              3.65        902.81                74.46         0.609          pass              0.681             69.8                           0.415                9.43              0.566                                 ok            True                  False
   PEP          100.00               11            0.85              0.82        138.10                16.46         0.569          pass              0.597             44.6                           0.483               -2.48             -0.197                                 ok            True                  False
  NVDA           90.32               31            0.97              1.53        225.08                44.12         0.536          pass              0.481              4.0                           0.170                4.93              0.619                                 ok            True                  False
   AEP           90.91               22            0.54              0.48        125.22                16.51         0.514          pass              0.586             54.7                           0.455                1.60              0.216                                 ok            True                  False
  CPRT           80.00               25            1.46              0.33         32.46                44.55         0.513          pass              0.285             44.7                           0.582               -3.62             -0.087                                 ok            True                  False
   CEG           85.71               14            1.60              3.35        297.62                32.90         0.509          pass              0.361             43.7                           0.367                5.69              0.755                                 ok            True                  False
   KDP           87.10               31            0.57              0.13         32.49                29.05         0.506          pass              0.571             63.7                           0.396                1.65              0.232                                 ok            True                  False
  PYPL           95.00               20            1.12              0.42         53.00                58.35         0.637          pass              0.719             62.8                           0.396              -15.34             -1.456 downtrend_blocked_slope_and_streak           False                  False
  MSTR           79.31               29            2.47              2.36        135.51               103.38         0.630          pass              0.216              8.6                           0.093                4.98              0.865                                 ok           False                  False
   KHC          100.00               13            0.48              0.08         24.86                28.58         0.619          pass              0.669             62.5                           0.347               -0.57              0.061                                 ok           False                  False
  WDAY           92.86               42            0.39              0.50        186.06                77.37         0.613          pass              0.825             73.6                           0.682               -4.56             -0.232                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-09T15:05:04.869479-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T15:00:02.977003-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:55:04.050096-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-09T14:50:05.027114-04:00       entry_1500              entry {"allocated_cash": 36890.0, "asset_type": "option", "contract_symbol": "MSTR261009C00135000", "contracts": 34, "early_entry_score": 0.281, "entry_mode": "regular", "entry_option_price": 10.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 254.0, "option_spread_pct": 2.76, "option_volume": 23.0, "success_rate": 80.65, "ticker": "MSTR", "timing_score": 0.638}
2026-09-09T14:50:05.027114-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-09", "training_samples": 5753, "window": 5}
2026-09-09T12:00:03.976220-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:55:03.977367-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:50:04.576506-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:45:06.789046-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:40:01.867073-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909150504)

</details>
