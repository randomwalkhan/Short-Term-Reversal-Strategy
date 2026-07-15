# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 09:30:04 EDT`
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

- Cash: `$4,915.25`
- Equity: `$26,875.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-120.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   1     11     12705.0                 12760.0        11.55           11.6      315.21        318.74     last_price_stale                        NaN                unavailable                   False            55.0                   0.43         95.83               24              0.66         28.20             0.0                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9200.0        46.88           46.0      660.72        659.82     last_price_stale                        NaN                unavailable                   False          -175.0                  -1.87         81.82               22              1.27         53.38             0.0                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               10            1.24              0.22         24.99                35.59         0.647            pass              0.350              6.1                           0.223               -0.96             -0.082                                 ok            True                  False
   CSX           92.59               27            0.50              0.18         49.84                19.04         0.527            pass              0.593             30.6                           0.363                4.50              0.384                                 ok            True                  False
    MU           82.35               34            0.48              3.30        981.70               112.93         0.783            pass              0.535             77.9                           0.580              -15.22             -1.051            downtrend_blocked_slope           False                  False
  DRAM           84.62               26            1.82              0.78         60.89               112.24         0.763            pass              0.354             15.9                           0.205               -8.73             -0.655            downtrend_blocked_slope           False                  False
  MRVL           90.32               31            1.26              1.97        221.60               102.11         0.707            pass              0.486              0.0                           0.263              -26.25             -2.530            downtrend_blocked_slope           False                  False
  MDLZ          100.00                6            1.45              0.60         58.54                30.90         0.635            pass              0.463              0.0                           0.238                0.18             -0.142                                 ok           False                  False
   KDP           85.71               14            0.86              0.18         30.18                35.85         0.608            pass              0.259              6.5                           0.326               -8.34             -0.953 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               20            0.49              0.46        135.25                30.96         0.606            pass              0.394              0.0                           0.376               -0.45             -0.422                                 ok           False                  False
   EXC           95.45               22            0.44              0.14         46.86                21.55         0.546            pass              0.716             60.6                           0.517                0.20             -0.038                                 ok           False                  False
  META           88.89               45            0.18              0.85        660.67                54.53         0.545            pass              0.680             62.7                           0.451                7.65              1.267                                 ok           False                  False
  GILD           90.91               33            0.25              0.23        129.94                33.56         0.520            pass              0.678             60.7                           0.388                2.67              0.222                                 ok           False                  False
   AEP           84.85               33            0.25              0.23        134.84                21.50         0.496 below_threshold              0.536             67.8                           0.508               -2.44             -0.199                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-15T09:30:04.740888-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:25:03.806265-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:20:04.874058-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:15:04.885771-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:10:05.907681-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:05:04.903172-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:00:02.786687-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T08:55:04.748908-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T08:50:02.886392-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T08:45:02.757806-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715093004)

</details>
