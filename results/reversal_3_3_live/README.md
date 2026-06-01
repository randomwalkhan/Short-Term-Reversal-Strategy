# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 11:35:04 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$31,029.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14280.0        35.25           35.7      477.34        480.03          bid_ask_mid                       35.7                bid_ask_mid                    True           180.0                   1.28         97.22               36              0.69         45.69            48.5                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           89.66               29            0.99              2.21        317.23                55.15         0.558          pass              0.655             71.8                           0.743               10.64              1.583                                 ok            True                  False
  INTC           96.30               27            1.64              1.32        114.11                88.16         0.539          pass              0.804             78.8                           0.902                3.70              0.696                                 ok            True                  False
  AAPL           92.31               13            1.64              3.59        310.52                17.18         0.515          pass              0.433             10.9                           0.298                2.23              0.452                                 ok            True                  False
  INSM           58.82               17            2.91              2.18        105.98               110.85         0.730          pass              0.156             12.1                           0.257               -4.90             -0.243                                 ok           False                  False
  REGN           78.57               14            1.90              8.18        611.27                42.14         0.559          pass              0.087              1.6                           0.180              -13.50             -0.849 downtrend_blocked_slope_and_streak           False                  False
  ROST           66.67                3            2.77              4.50        229.80                40.27         0.557          pass              0.063              2.3                           0.097                5.90              0.977                                 ok           False                  False
  KLAC           91.89               37            0.16              2.18       1920.78                50.27         0.543          pass              0.825             91.3                           0.768                6.47              1.093                                 ok           False                  False
   WMT           75.00               12            1.71              1.39        115.16                32.67         0.541          pass              0.096              9.6                           0.237              -13.45             -1.702 downtrend_blocked_slope_and_streak           False                  False
   AEP           60.00                5            1.87              1.66        125.96                24.34         0.538          pass              0.055              0.4                           0.052               -0.68             -0.066                                 ok           False                  False
   HON           76.92               13            1.30              2.17        236.93                24.41         0.531          pass              0.193             39.9                           0.658               10.09              1.105                                 ok           False                  False
   PEP           90.91               11            1.79              1.81        143.42                22.18         0.525          pass              0.350              0.0                           0.157               -5.04             -0.469            downtrend_blocked_slope           False                  False
   LIN           84.62               13            1.49              5.19        495.47                20.97         0.521          pass              0.243             15.9                           0.326               -3.13             -0.256 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-01T11:35:04.962377-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:30:03.931988-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:15:04.905942-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:10:06.144883-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:05:05.001730-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:00:06.868353-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:55:05.037823-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:50:02.030690-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601113504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601113504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601113504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601113504)

</details>
