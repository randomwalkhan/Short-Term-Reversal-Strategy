# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 10:05:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,668.00`
- Equity: `$34,480.50`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$437.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16812.5         6.55           6.72       129.9        131.38          bid_ask_mid                       6.72                bid_ask_mid                    True           437.5                   2.67         91.67               24              0.73         32.92           34.11                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           86.36               22            2.41             14.39        845.52               103.51         0.668          pass              0.343              8.7                           0.121               -3.43              0.512                                 ok            True                  False
  MDLZ           94.74               19            0.62              0.26         60.41                31.78         0.609          pass              0.569             18.5                           0.126                0.48              0.151                                 ok            True                  False
   WDC           90.00               20            4.18             15.20        513.28               113.75         0.589          pass              0.398              2.1                           0.048              -10.34             -0.080                                 ok            True                  False
  MPWR           84.21               38            0.65              6.09       1331.20                65.61         0.561          pass              0.356              0.3                           0.065                2.61              0.315                                 ok            True                  False
  DRAM           80.65               31            0.81              0.30         53.07                97.77         0.701          pass              0.346             39.4                           0.253               -7.91             -0.465            downtrend_blocked_slope           False                  False
  PYPL           90.00               40            0.23              0.09         56.11                61.92         0.628          pass              0.771             80.6                           0.660               17.57              1.302                                 ok           False                  False
  KLAC           87.50               24            2.88              4.24        208.70                94.03         0.622          pass              0.356              0.0                           0.183               -8.00             -0.784 downtrend_blocked_slope_and_streak           False                  False
  MRVL           85.29               34            1.29              1.76        193.48                90.44         0.619          pass              0.406             14.3                           0.129              -11.87             -0.677            downtrend_blocked_slope           False                  False
  AMAT           90.48               21            2.60              9.78        532.06                84.50         0.592          pass              0.448             12.2                           0.215               -9.23             -0.844 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               24            5.79              5.54        134.43               179.12         0.592          pass              0.241              0.0                           0.150              -22.06             -1.750            downtrend_blocked_slope           False                  False
   CSX          100.00                9            1.45              0.54         53.00                24.65         0.582          pass              0.517             19.4                           0.214                5.67              0.586                                 ok           False                  False
   WBD           88.24               17            0.72              0.13         25.71                22.96         0.547          pass              0.514             64.4                           0.772               -5.56             -0.822            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-27T10:05:02.641100-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T10:00:03.474876-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T09:35:01.555025-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:30:04.489033-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:25:02.551278-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:20:01.575598-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:15:05.384671-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:10:05.509301-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:05:02.526128-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:00:04.546327-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727100502)

</details>
