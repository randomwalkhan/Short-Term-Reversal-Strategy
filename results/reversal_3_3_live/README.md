# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 12:05:05 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$14,090.00`
- Equity: `$26,892.50`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$-945.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 12802.5        15.28          14.22      245.93        242.15          bid_ask_mid                      14.22                bid_ask_mid                    True          -945.0                  -6.87         91.67               36              0.66         58.04            62.4                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.77               26            1.68              1.78        150.99               141.41         0.623          pass              0.444             84.8                           0.882                3.50              0.104                                 ok            True                  False
  GOOG           80.00               10            2.09              5.76        390.64                40.55         0.558          pass              0.101             15.2                           0.289                0.16              0.004                                 ok            True                  False
 GOOGL           80.00               10            2.23              6.21        394.28                40.53         0.552          pass              0.099             14.6                           0.287               -0.09              0.011                                 ok            True                  False
  SNPS           96.67               30            1.21              4.21        496.62                41.65         0.534          pass              0.657             23.3                           0.316               -2.01             -0.186                                 ok            True                  False
  ASML           83.33               30            1.02             10.56       1467.87                50.95         0.533          pass              0.430             51.5                           0.675                1.00             -0.156                                 ok            True                  False
   KDP           90.62               32            0.59              0.12         29.38                33.71         0.531          pass              0.596             37.5                           0.291                1.16              0.236                                 ok            True                  False
  NVDA           87.88               33            0.64              1.00        221.89                44.74         0.519          pass              0.618             67.6                           0.570               12.41              1.141                                 ok            True                  False
  AVGO           90.48               21            2.00              5.89        418.18                42.85         0.508          pass              0.533             43.3                           0.665               -3.53             -0.106                                 ok            True                  False
  KLAC           82.14               28            1.36             16.73       1749.28                51.34         0.504          pass              0.419             63.9                           0.722               -0.02             -0.035                                 ok            True                  False
  FAST           93.10               29            0.53              0.16         43.93                22.17         0.500          pass              0.740             71.3                           0.729               -1.27             -0.183                                 ok            True                  False
  INTC          100.00               35            0.37              0.28        108.05               114.00         0.731          pass              0.919             93.2                           0.871               -0.35             -0.399                                 ok           False                  False
  INSM           77.27               44            0.14              0.11        107.11               111.34         0.715          pass              0.550             93.0                           0.544              -23.26             -1.639 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-19T12:00:03.873446-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:40:06.318992-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:35:01.898801-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519120505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519120505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519120505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519120505)

</details>
