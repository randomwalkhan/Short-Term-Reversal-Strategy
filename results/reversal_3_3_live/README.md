# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 11:45:04 EDT`
Last processed slot: `early_entry_1145`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$16,749.25`
- Equity: `$31,149.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$300.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14400.0        35.25           36.0      477.34        478.95          bid_ask_mid                       36.0                bid_ask_mid                    True           300.0                   2.13         97.22               36              0.69         45.69           50.32                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           91.89               37            0.50              1.12        317.70                55.15         0.538          pass              0.808             85.7                           0.819               11.19              1.605                                 ok            True                   True
  INTC           95.65               23            2.10              1.69        113.96                88.16         0.534          pass              0.759             72.9                           0.771                3.22              0.674                                 ok            True                  False
   HON           81.25               16            1.01              1.69        237.14                24.41         0.534          pass              0.287             53.3                           0.727               10.42              1.119                                 ok            True                  False
  AAPL           92.31               13            1.68              3.68        310.48                17.18         0.513          pass              0.426              8.9                           0.300                2.19              0.450                                 ok            True                  False
  INSM           63.64               22            2.59              1.94        106.08               110.85         0.724          pass              0.218             21.9                           0.416               -4.58             -0.228                                 ok           False                  False
  ROST           80.00                5            2.56              4.15        229.95                40.27         0.573          pass              0.087              9.9                           0.256                6.13              0.987                                 ok           False                  False
  REGN           83.33               18            1.74              7.48        611.57                42.14         0.548          pass              0.227             10.2                           0.249              -13.36             -0.842 downtrend_blocked_slope_and_streak           False                  False
   WMT           75.00               12            1.64              1.33        115.18                32.67         0.546          pass              0.108             13.2                           0.361              -13.39             -1.699 downtrend_blocked_slope_and_streak           False                  False
   AEP           60.00                5            1.84              1.63        125.97                24.34         0.539          pass              0.067              4.5                           0.184               -0.65             -0.064                                 ok           False                  False
  KLAC           92.50               40            0.06              0.80       1921.37                50.27         0.529          pass              0.877             96.8                           0.793                6.58              1.098                                 ok           False                  False
   PEP           90.91               11            1.72              1.74        143.45                22.18         0.529          pass              0.371              6.8                           0.189               -4.97             -0.466            downtrend_blocked_slope           False                  False
   LIN           84.62               13            1.51              5.27        495.43                20.97         0.519          pass              0.239             14.6                           0.249               -3.15             -0.257 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-01T11:45:04.960036-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:40:03.918897-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:35:04.962377-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:30:03.931988-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:15:04.905942-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:10:06.144883-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:05:05.001730-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:00:06.868353-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601114504)

</details>
