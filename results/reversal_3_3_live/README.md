# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 11:40:03 EDT`
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
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14280.0        35.25           35.7      477.34         478.0          bid_ask_mid                       35.7                bid_ask_mid                    True           180.0                   1.28         97.22               36              0.69         45.69           49.48                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           89.66               29            1.03              2.30        317.20                55.15         0.555          pass              0.652             70.7                           0.731               10.60              1.581                                 ok            True                  False
  INTC           95.65               23            2.08              1.67        113.97                88.16         0.536          pass              0.760             73.2                           0.877                3.25              0.676                                 ok            True                  False
  AAPL           92.31               13            1.65              3.59        310.52                17.18         0.515          pass              0.432             10.9                           0.319                2.23              0.452                                 ok            True                  False
  INSM           66.67               24            2.44              1.83        106.13               110.85         0.724          pass              0.245             26.4                           0.401               -4.43             -0.221                                 ok           False                  False
  ROST           80.00                5            2.74              4.45        229.82                40.27         0.560          pass              0.066              3.3                           0.137                5.93              0.978                                 ok           False                  False
  REGN           83.33               18            1.74              7.47        611.58                42.14         0.548          pass              0.228             10.3                           0.274              -13.35             -0.841 downtrend_blocked_slope_and_streak           False                  False
   WMT           75.00               12            1.65              1.34        115.18                32.67         0.545          pass              0.106             12.8                           0.327              -13.40             -1.699 downtrend_blocked_slope_and_streak           False                  False
   HON           78.57               14            1.10              1.83        237.07                24.41         0.539          pass              0.228             49.2                           0.703               10.32              1.115                                 ok           False                  False
  KLAC           91.89               37            0.26              3.45       1920.23                50.27         0.536          pass              0.809             86.2                           0.741                6.37              1.089                                 ok           False                  False
   AEP           60.00                5            1.92              1.70        125.94                24.34         0.534          pass              0.053              0.0                           0.005               -0.73             -0.068                                 ok           False                  False
   PEP           90.91               11            1.75              1.76        143.43                22.18         0.528          pass              0.364              4.5                           0.108               -5.00             -0.467            downtrend_blocked_slope           False                  False
   LIN           84.62               13            1.49              5.21        495.46                20.97         0.520          pass              0.242             15.6                           0.286               -3.13             -0.257 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-01T11:40:03.918897-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:35:04.962377-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:30:03.931988-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:15:04.905942-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:10:06.144883-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:05:05.001730-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:00:06.868353-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:55:05.037823-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601114003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601114003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601114003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601114003)

</details>
