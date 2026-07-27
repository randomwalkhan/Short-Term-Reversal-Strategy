# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 09:35:01 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$34,293.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16625.0         6.55           6.65       129.9         130.1     last_price_stale                        NaN                unavailable                   False           250.0                   1.53         91.67               24              0.73         32.92             0.0                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           86.67               30            0.77              0.30         56.02                61.92         0.654            pass              0.438             20.4                           0.336               16.94              1.278                                 ok            True                  False
   EXC           95.00               20            0.67              0.22         47.43                24.01         0.564            pass              0.719             65.2                           0.523                0.25              0.119                                 ok            True                  False
   CSX           93.75               16            1.03              0.38         53.07                24.65         0.564            pass              0.463              0.0                           0.243                6.12              0.605                                 ok            True                  False
  ASML           92.59               27            1.75             21.53       1747.86                55.90         0.536            pass              0.541             12.8                           0.192                0.02             -0.077                                 ok            True                  False
  LRCX           89.19               37            0.00              0.01        305.21                85.02         0.679            pass              0.792             99.6                           0.486               -7.49             -0.934 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           93.10               29            0.16              0.07         60.49                31.78         0.573            pass              0.771             79.3                           0.552                0.94              0.172                                 ok           False                  False
   WBD           75.00                8            1.46              0.26         25.66                22.96         0.540            pass              0.138             27.9                           0.464               -6.26             -0.855            downtrend_blocked_slope           False                  False
   XEL          100.00               27            0.28              0.16         81.60                20.22         0.536            pass              0.611             14.8                           0.097                1.19              0.171                                 ok           False                  False
  NFLX           79.17               48            0.03              0.01         70.08                43.81         0.484 below_threshold              0.482             77.8                           0.403               -5.09             -0.735            downtrend_blocked_slope           False                  False
   AEP           80.00               30            0.51              0.48        135.33                20.37         0.470 below_threshold              0.307             42.3                           0.338               -0.58              0.013                                 ok           False                  False
   LIN           92.50               40            0.19              0.67        511.99                22.09         0.447 below_threshold              0.796             72.6                           0.442               -2.43             -0.280            downtrend_blocked_slope           False                  False
  NVDA           84.09               44            0.34              0.49        206.63                35.70         0.440 below_threshold              0.542             63.0                           0.394                1.28             -0.034                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-27T09:35:01.555025-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:30:04.489033-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:25:02.551278-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:20:01.575598-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:15:05.384671-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:10:05.509301-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:05:02.526128-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:00:04.546327-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:55:01.530928-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:50:01.513320-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727093501)

</details>
