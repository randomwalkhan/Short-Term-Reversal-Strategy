# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 09:30:01 EDT`
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

- Cash: `$167.25`
- Equity: `$34,561.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,339.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option  CSX260918C00050000       2026-07-30                   2     86     16555.0                 17630.0         1.92           2.05       50.11         50.36     last_price_stale                        NaN                unavailable                   False          1075.0                   6.49         92.31               13              1.24         25.34             0.0                  28.82                2759.0          136.0               0.03                      ok
  PYPL     option         option PYPL260918C00057500       2026-07-31                   1     66     16500.0                 16764.0         2.50           2.54       57.10         58.02     last_price_stale                        NaN                unavailable                   False           264.0                   1.60         86.21               29              0.95         31.54             0.0                  60.55                6425.0          263.0               0.05                      ok
```

## Today's Closed Trades (2026-08-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMAT           89.29               28            1.51              5.37        505.37                87.25         0.610            pass              0.598             56.6                           0.557               -4.89             -1.453 downtrend_blocked_slope_and_streak           False                  False
  GILD           85.71               28            0.82              0.75        130.96                32.59         0.529            pass              0.527             67.1                           0.565               -2.25             -0.026           downtrend_blocked_streak           False                  False
  LRCX           82.61               23            2.80              5.74        290.56                90.68         0.523            pass              0.303             31.4                           0.390               -7.15             -1.414 downtrend_blocked_slope_and_streak           False                  False
  DRAM           75.00               24            3.48              1.22         49.82               111.30         0.522            pass              0.189             14.4                           0.318               -8.42             -1.809 downtrend_blocked_slope_and_streak           False                  False
  ASML           89.66               29            1.26             14.36       1622.84                49.80         0.511            pass              0.485             16.6                           0.290               -7.39             -1.310 downtrend_blocked_slope_and_streak           False                  False
  ADSK           83.33               42            0.33              0.54        234.74                48.22         0.502            pass              0.606             89.0                           0.696                7.53              1.535                                 ok           False                  False
   MAR          100.00                5            2.57              6.70        369.96                24.83         0.484 below_threshold              0.587             46.3                           0.513               -1.00              0.148                                 ok           False                  False
  KLAC           84.00               25            2.41              3.08        181.50                69.24         0.482 below_threshold              0.361             35.5                           0.451              -14.06             -2.342 downtrend_blocked_slope_and_streak           False                  False
  ABNB           92.50               40            0.37              0.39        151.91                33.42         0.474 below_threshold              0.835             84.7                           0.519                4.54              0.877                                 ok           False                  False
  NVDA           81.82               33            1.21              1.70        200.02                42.43         0.467 below_threshold              0.366             39.3                           0.432               -2.44             -0.672            downtrend_blocked_slope           False                  False
  INTC           83.33               36            1.98              1.25         89.66                83.69         0.464 below_threshold              0.428             39.9                           0.532               -8.91             -1.745 downtrend_blocked_slope_and_streak           False                  False
  AVGO           76.67               30            1.35              3.67        387.71                43.85         0.458 below_threshold              0.255             25.1                           0.340                1.55             -0.074                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-03T03:00:01.318857-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-01T02:55:05.543757-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:50:03.559727-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:45:01.711119-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:40:01.558683-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:35:03.491522-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:30:02.590104-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:25:05.555029-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:20:01.118394-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:15:04.473515-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803093001)

</details>
