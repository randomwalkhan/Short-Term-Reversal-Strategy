# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 10:35:02 EDT`
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

- Cash: `$19,710.25`
- Equity: `$29,555.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$470.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9845.0        46.88          49.22      660.72        674.24          bid_ask_mid                      49.22                bid_ask_mid                    True           470.0                   5.01         81.82               22              1.27         53.38           49.25                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.00               20            2.24              4.79        303.50                65.52         0.574          pass              0.425             11.5                           0.166                0.21              0.246                                 ok            True                  False
   ADI           84.00               25            1.40              3.85        391.10                55.85         0.572          pass              0.351             29.0                           0.249               -2.50              0.070                                 ok            True                  False
   EXC           94.12               17            0.64              0.21         46.83                21.56         0.564          pass              0.624             48.3                           0.486                0.00             -0.048                                 ok            True                  False
   LIN          100.00               10            1.40              5.11        520.35                20.66         0.564          pass              0.500             14.6                           0.232               -0.71             -0.308                                 ok            True                  False
  NXPI           87.10               31            1.04              2.08        282.98                58.07         0.563          pass              0.423             12.5                           0.112               -0.04              0.270                                 ok            True                  False
   CSX           86.67               15            1.01              0.35         49.77                19.08         0.558          pass              0.356             29.9                           0.445                3.97              0.349                                 ok            True                  False
   AEP           83.33               18            0.97              0.92        134.55                21.64         0.542          pass              0.298             33.8                           0.362               -2.32             -0.199                                 ok            True                  False
   WBD           83.33               12            1.16              0.22         27.38                20.00         0.531          pass              0.199             14.7                           0.236                1.88              0.265                                 ok            True                  False
  AMAT           84.21               19            2.43             10.14        591.36                98.89         0.637          pass              0.312             25.2                           0.236              -19.61             -1.363 downtrend_blocked_slope_and_streak           False                  False
  SOXL           85.00               20            7.86              9.72        172.49               219.49         0.626          pass              0.296             11.0                           0.145              -38.97             -3.126            downtrend_blocked_slope           False                  False
  KLAC           78.57               14            3.81              6.15        227.74               109.33         0.623          pass              0.108              6.3                           0.092              -26.56             -2.085 downtrend_blocked_slope_and_streak           False                  False
  QCOM           84.85               33            0.73              0.91        177.71                61.79         0.590          pass              0.431             29.7                           0.201               -4.32             -0.077           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:30:03.936476-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:25:06.040216-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:20:02.772383-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:15:05.965611-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:10:03.001163-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:05:02.748975-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00315000", "fill_price": 13.45, "pnl": 2090.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.45, "ticker": "AAPL"}
2026-07-15T09:35:02.740173-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715103502)

</details>
