# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 10:00:03 EDT`
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
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16812.5         6.55           6.72       129.9        131.32          bid_ask_mid                       6.72                bid_ask_mid                    True           437.5                   2.67         91.67               24              0.73         32.92           33.86                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           88.00               25            1.78             10.64        847.13               103.51         0.696          pass              0.410              8.9                           0.169               -2.81              0.541                                 ok            True                  False
   WDC           86.36               22            2.76             10.06        515.49               113.75         0.671          pass              0.349             10.8                           0.206               -9.02             -0.013                                 ok            True                  False
  PYPL           87.10               31            0.64              0.25         56.04                61.92         0.654          pass              0.533             46.3                           0.352               17.08              1.284                                 ok            True                  False
    MU           81.25               32            1.64             10.57        916.42                86.08         0.581          pass              0.240              0.6                           0.044               -3.32              0.200                                 ok            True                  False
  DRAM           78.79               33            0.15              0.06         53.18                97.77         0.734          pass              0.244              5.9                           0.023               -7.29             -0.435            downtrend_blocked_slope           False                  False
  SOXL           83.87               31            3.14              3.01        135.52               179.12         0.732          pass              0.361             14.8                           0.196              -19.87             -1.624            downtrend_blocked_slope           False                  False
  MRVL           86.49               37            0.30              0.41        194.06                90.44         0.672          pass              0.565             48.3                           0.315              -10.98             -0.631            downtrend_blocked_slope           False                  False
  KLAC           88.46               26            2.10              3.10        209.19                94.03         0.665          pass              0.423              7.9                           0.107               -7.27             -0.748 downtrend_blocked_slope_and_streak           False                  False
  AMAT           92.31               26            1.69              6.36        533.53                84.50         0.626          pass              0.590             30.8                           0.210               -8.38             -0.802 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.48               21            0.40              0.17         60.45                31.78         0.605          pass              0.557             47.8                           0.244                0.70              0.161                                 ok           False                  False
   CSX          100.00                8            1.47              0.55         53.00                24.65         0.588          pass              0.515             18.8                           0.213                5.66              0.585                                 ok           False                  False
  INTC           86.11               36            1.57              1.01         91.89                79.50         0.552          pass              0.437             15.2                           0.212              -11.88             -0.955 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-27T10:00:03.474876-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T09:35:01.555025-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:30:04.489033-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:25:02.551278-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:20:01.575598-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:15:05.384671-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:10:05.509301-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:05:02.526128-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T09:00:04.546327-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-27T08:55:01.530928-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727100003)

</details>
