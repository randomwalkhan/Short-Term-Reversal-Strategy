# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 10:35:03 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$47,058.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 22400.0         13.9           14.0      224.68        224.82          bid_ask_mid                       14.0                bid_ask_mid                    True           160.0                   0.72         84.62               26              1.73         43.62           42.59                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           86.96               23            2.04              3.21        223.64                39.09         0.510            pass              0.401             25.8                           0.525                4.01              0.326                                 ok            True                  False
    MU           82.61               23            5.60             39.63        994.76               104.10         0.503            pass              0.242             11.8                           0.285                7.00              1.074                                 ok            True                  False
  INSM           86.67               45            0.49              0.44        128.13               109.50         0.739            pass              0.655             67.6                           0.761               29.31              1.816                                 ok           False                  False
   APP           73.91               46            0.17              0.37        311.82                90.76         0.663            pass              0.525             86.2                           0.502              -25.79             -2.877            downtrend_blocked_slope           False                  False
  AMZN           84.44               45            0.07              0.13        261.25                61.74         0.611            pass              0.664             94.7                           0.901               -5.88             -0.657 downtrend_blocked_slope_and_streak           False                  False
  PCAR          100.00               11            1.76              1.61        130.15                28.21         0.568            pass              0.486              7.6                           0.146               -5.21             -0.389            downtrend_blocked_slope           False                  False
  UPRO           88.89                9            2.87              3.15        155.28                41.29         0.556            pass              0.335             14.3                           0.493               -1.30              0.017                                 ok           False                  False
  CSCO           77.78               18            1.60              1.26        112.36                42.21         0.552            pass              0.131              7.4                           0.189               -8.74             -1.021            downtrend_blocked_slope           False                  False
   HON           90.62               32            0.40              0.64        229.18                37.29         0.547            pass              0.615             43.5                           0.325               -7.86             -0.860            downtrend_blocked_slope           False                  False
 GOOGL           76.60               47            0.14              0.34        343.86                47.98         0.521            pass              0.514             87.4                           0.789               -9.04             -0.809            downtrend_blocked_slope           False                  False
  MCHP           80.00               10            4.86              2.73         79.09                73.04         0.503            pass              0.069              6.3                           0.272               -5.34             -0.284 downtrend_blocked_slope_and_streak           False                  False
   CEG           79.49               39            0.19              0.37        277.61                37.62         0.494 below_threshold              0.500             85.9                           0.628                3.74              0.603                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:35:07.917262-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:32:57.454440-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:15:02.899134-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818103503)

</details>
