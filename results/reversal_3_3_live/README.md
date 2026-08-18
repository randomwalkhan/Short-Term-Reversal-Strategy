# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 09:45:04 EDT`
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

- Cash: `$24,658.00`
- Equity: `$46,578.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$-320.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 21920.0         13.9           13.7      224.68        223.48          bid_ask_mid                       13.7                bid_ask_mid                    True          -320.0                  -1.44         84.62               26              1.73         43.62           49.73                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           86.84               38            0.94              1.48        223.96               127.60         0.811          pass              0.612             53.9                           0.345                1.59              0.224                                 ok            True                  False
  INSM           84.62               39            0.92              0.83        127.97               109.50         0.744          pass              0.496             35.2                           0.279               28.75              1.796                                 ok            True                  False
  UPRO           84.21               19            1.49              1.61        153.71                41.29         0.586          pass              0.296             21.8                           0.381               -1.32              0.016                                 ok            True                  False
    MU           82.61               23            4.41             31.20        998.38               104.10         0.582          pass              0.277             20.8                           0.563                8.35              1.131                                 ok            True                  False
  NVDA           88.46               26            1.92              3.02        223.72                39.09         0.504          pass              0.451             22.7                           0.467                4.13              0.331                                 ok            True                  False
   APP           72.73               44            0.54              1.17        311.48                90.76         0.655          pass              0.436             56.8                           0.493              -26.06             -2.893            downtrend_blocked_slope           False                  False
  AMZN           79.41               34            0.66              1.21        260.79                61.74         0.633          pass              0.377             51.1                           0.346               -6.43             -0.684 downtrend_blocked_slope_and_streak           False                  False
  PCAR          100.00               16            1.38              1.27        130.30                28.21         0.564          pass              0.519              7.7                           0.195               -4.85             -0.371            downtrend_blocked_slope           False                  False
   HON           91.18               34            0.31              0.49        229.24                37.29         0.541          pass              0.682             56.5                           0.487               -7.78             -0.856            downtrend_blocked_slope           False                  False
  CSCO           86.67               30            1.05              0.83        112.54                42.21         0.530          pass              0.468             34.5                           0.386               -8.23             -0.996            downtrend_blocked_slope           False                  False
 GOOGL           73.17               41            0.53              1.27        343.45                47.98         0.529          pass              0.410             52.2                           0.569               -9.39             -0.827            downtrend_blocked_slope           False                  False
  GOOG           77.78               45            0.42              1.00        341.02                46.40         0.513          pass              0.442             63.5                           0.626               -9.41             -0.848            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-18T09:38:41.008763-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:20:07.104993-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:15:08.426968-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T09:11:00.046303-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:52:52.256088-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:35:07.917262-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:32:57.454440-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:15:02.899134-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T08:12:27.971020-04:00 data_refresh data_refresh {'saved': 93}
2026-08-18T07:55:02.255122-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818094504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818094504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818094504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818094504)

</details>
