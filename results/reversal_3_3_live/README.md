# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:00:03 EDT`
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

- Cash: `$19,710.25`
- Equity: `$30,265.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$1,180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                 10555.0        46.88          52.78      660.72        671.11          bid_ask_mid                      52.78                bid_ask_mid                    True          1180.0                  12.59         81.82               22              1.27         53.38           53.29                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           84.62               26            1.22              3.35        391.31                55.85         0.576          pass              0.417             43.2                           0.440               -2.32              0.078                                 ok            True                  False
   TXN           90.91               22            2.05              4.38        303.67                65.52         0.571          pass              0.516             29.3                           0.379                0.41              0.255                                 ok            True                  False
   CSX           86.67               15            0.98              0.34         49.77                19.08         0.560          pass              0.363             31.9                           0.403                4.00              0.350                                 ok            True                  False
   LIN          100.00               14            1.12              4.08        520.79                20.66         0.555          pass              0.577             31.8                           0.424               -0.43             -0.295                                 ok            True                  False
  NXPI           85.71               28            1.28              2.55        282.78                58.07         0.550          pass              0.470             47.6                           0.334               -0.29              0.259                                 ok            True                  False
   WBD           83.33               12            1.16              0.22         27.38                20.00         0.531          pass              0.199             14.7                           0.261                1.88              0.265                                 ok            True                  False
  KLAC           82.35               17            3.38              5.45        228.03               109.33         0.628          pass              0.261             29.5                           0.425              -26.23             -2.065 downtrend_blocked_slope_and_streak           False                  False
  AMAT           83.33               18            2.70             11.26        590.87                98.89         0.615          pass              0.307             34.5                           0.404              -19.83             -1.375 downtrend_blocked_slope_and_streak           False                  False
  SOXL           85.00               20            8.04              9.94        172.40               219.49         0.587          pass              0.340             27.3                           0.374              -39.09             -3.134            downtrend_blocked_slope           False                  False
  QCOM           86.84               38            0.30              0.37        177.94                61.79         0.584          pass              0.657             76.6                           0.591               -3.91             -0.057           downtrend_blocked_streak           False                  False
  MPWR           79.31               29            2.02             19.46       1368.07                84.79         0.578          pass              0.306             40.7                           0.444               -2.44              0.140                                 ok           False                  False
  MCHP           93.10               29            1.63              0.99         86.68                68.63         0.567          pass              0.644             37.2                           0.444               -6.04             -0.269            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-15T11:00:03.028836-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:55:06.408548-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:50:02.878047-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:45:02.900716-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:30:03.936476-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:25:06.040216-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:20:02.772383-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:15:05.965611-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715110003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715110003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715110003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715110003)

</details>
