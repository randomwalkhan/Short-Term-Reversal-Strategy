# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 11:25:04 EDT`
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
- Equity: `$30,649.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$-200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 13900.0        35.25          34.75      477.34        479.43          bid_ask_mid                      34.75                bid_ask_mid                    True          -200.0                  -1.42         97.22               36              0.69         45.69           46.06                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           89.29               28            1.21              2.70        317.02                55.15         0.550          pass              0.619             65.5                           0.694               10.40              1.573                                 ok            True                  False
  INTC           95.65               23            2.01              1.62        113.99                88.16         0.540          pass              0.763             74.0                           0.790                3.31              0.678                                 ok            True                  False
  AAPL           92.31               13            1.75              3.83        310.42                17.18         0.508          pass              0.414              4.9                           0.170                2.12              0.447                                 ok            True                  False
  INSM           58.82               17            3.18              2.38        105.89               110.85         0.715          pass              0.130              4.1                           0.117               -5.16             -0.256            downtrend_blocked_slope           False                  False
  ROST           75.00                4            2.76              4.47        229.81                40.27         0.562          pass              0.056              0.0                           0.170                5.92              0.978                                 ok           False                  False
   AEP           60.00                5            1.72              1.53        126.02                24.34         0.549          pass              0.068              4.4                           0.225               -0.53             -0.059                                 ok           False                  False
   WMT           72.73               11            1.77              1.44        115.13                32.67         0.542          pass              0.080              6.4                           0.120              -13.50             -1.705 downtrend_blocked_slope_and_streak           False                  False
  REGN           81.82               22            1.41              6.08        612.18                42.14         0.541          pass              0.263             26.9                           0.444              -13.07             -0.826 downtrend_blocked_slope_and_streak           False                  False
  KLAC           91.67               36            0.36              4.81       1919.65                50.27         0.536          pass              0.780             80.8                           0.766                6.26              1.084                                 ok           False                  False
   HON           72.73               11            1.39              2.31        236.87                24.41         0.535          pass              0.168             36.0                           0.684               10.00              1.102                                 ok           False                  False
   PEP           91.67               12            1.60              1.62        143.50                22.18         0.533          pass              0.393              4.9                           0.102               -4.86             -0.461            downtrend_blocked_slope           False                  False
  COST           62.50                8            1.69             11.28        951.49                27.93         0.527          pass              0.070              5.8                           0.116              -10.37             -1.352 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:15:04.905942-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:10:06.144883-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:05:05.001730-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:00:06.868353-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:55:05.037823-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:50:02.030690-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:45:04.809408-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T10:40:02.889007-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601112504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601112504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601112504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601112504)

</details>
