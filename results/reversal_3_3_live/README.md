# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:45:06 EDT`
Last processed slot: `manual`

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

- Cash: `$17,648.00`
- Equity: `$31,448.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   2      5     13425.0                 13800.0        26.85           27.6      307.66        326.04     last_price_stale                        NaN                unavailable                   False           375.0                   2.79          87.1               31              1.19         68.92             0.0                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.21              1.31        153.52               126.50         0.788          pass              0.472             56.9                           0.650               45.96              5.171                  ok            True                  False
  PYPL           93.75               32            0.85              0.35         58.85                59.96         0.645          pass              0.767             63.0                           0.781                0.26              0.222                  ok            True                   True
 CMCSA           88.24               17            1.13              0.20         25.56                42.38         0.629          pass              0.373             14.7                           0.179                7.14              0.689                  ok            True                  False
  ABNB           95.24               21            1.51              1.96        184.14                64.05         0.622          pass              0.683             49.0                           0.517               19.07              2.304                  ok            True                  False
  GEHC           95.45               22            1.47              0.75         72.43                54.33         0.621          pass              0.658             38.5                           0.367               -0.31              0.316                  ok            True                  False
   ROP          100.00               21            1.35              3.77        397.88                44.32         0.606          pass              0.669             45.1                           0.442                1.25              0.193                  ok            True                  False
  TMUS           88.24               34            0.62              0.77        178.26                55.82         0.606          pass              0.533             30.8                           0.285                2.39              0.271                  ok            True                  False
  PAYX          100.00               15            1.27              1.08        120.84                33.26         0.588          pass              0.539             15.5                           0.233                2.95              0.380                  ok            True                  False
  MDLZ           91.67               24            0.73              0.31         61.65                29.90         0.564          pass              0.603             47.4                           0.434               -2.77             -0.204                  ok            True                  False
   ADP           95.83               24            1.13              2.15        270.17                32.74         0.550          pass              0.623             24.9                           0.279                1.57              0.139                  ok            True                  False
  META           85.71               35            0.69              2.88        597.88                45.64         0.527          pass              0.541             56.3                           0.334                1.60              0.653                  ok            True                  False
  ADSK           80.65               31            1.09              1.91        250.77                45.76         0.523          pass              0.376             55.4                           0.588                5.91              0.863                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-12T09:35:01.769154-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:30:01.771593-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:25:01.593760-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:20:03.729351-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:15:01.696450-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:10:04.748220-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:05:02.776077-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:00:03.695691-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:55:02.907270-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:50:06.776266-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812094506)

</details>
