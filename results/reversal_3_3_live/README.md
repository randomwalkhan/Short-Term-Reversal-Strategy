# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:55:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$17,080.75`
- Equity: `$34,180.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 17100.0          4.1           4.28      138.68        138.37          bid_ask_mid                       4.28                bid_ask_mid                    True           700.0                   4.27         83.33               24              0.68          24.5           26.34                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
 CMCSA           80.00               10            1.78              0.31         24.80                44.00         0.600          pass              0.117             19.1                           0.335                4.10              0.984                       ok            True                  False
  CTAS           91.30               23            1.04              1.48        203.02                37.77         0.590          pass              0.532             28.3                           0.363                0.09             -0.105                       ok            True                  False
  PAYX          100.00               17            0.77              0.64        118.39                35.13         0.580          pass              0.730             75.1                           0.411                7.44              0.763                       ok            True                  False
   CSX           91.67               24            0.63              0.22         50.93                29.11         0.558          pass              0.474              4.5                           0.178                1.56             -0.296                       ok            True                  False
   PEP           84.00               25            0.52              0.51        138.88                25.68         0.550          pass              0.376             38.1                           0.379                2.01              0.239                       ok            True                  False
  VRSK           94.44               36            0.68              0.92        192.41                43.54         0.525          pass              0.747             45.4                           0.335               -0.41             -0.299                       ok            True                  False
  CPRT           85.71               21            1.79              0.37         29.24                38.86         0.513          pass              0.350             24.5                           0.365                6.28              0.619                       ok            True                  False
   WDC           83.33               36            0.09              0.36        548.40                99.34         0.716          pass              0.615             93.8                           0.416               -1.55              0.194 downtrend_blocked_streak           False                  False
  DRAM           77.42               31            1.46              0.56         54.65               109.93         0.690          pass              0.399             63.3                           0.351               -6.37             -0.616 downtrend_blocked_streak           False                  False
  GEHC           95.12               41            0.04              0.02         70.25                58.11         0.623          pass              0.944             93.8                           0.399               14.43              1.727                       ok           False                  False
  TMUS           80.00                5            3.02              3.74        175.61                55.59         0.618          pass              0.093             10.5                           0.257               -9.99             -0.475  downtrend_blocked_slope           False                  False
  AMAT           86.96               23            2.67             10.22        542.24                87.24         0.606          pass              0.360              9.0                           0.183               -3.95             -0.368 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T10:55:04.718712-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:50:01.771343-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:45:01.734892-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:40:05.699069-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:35:01.163054-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:30:06.205244-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:25:05.700806-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:20:05.967417-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805105504)

</details>
