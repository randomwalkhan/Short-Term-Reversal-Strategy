# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 09:35:02 EDT`
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
  AAPL     option         option AAPL260821C00315000       2026-07-14                   1     11     12705.0                 12760.0        11.55           11.6      315.21        319.27     last_price_stale                        NaN                unavailable                   False            55.0                   0.43         95.83               24              0.66         28.20             0.0                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9200.0        46.88           46.0      660.72        661.27     last_price_stale                        NaN                unavailable                   False          -175.0                  -1.87         81.82               22              1.27         53.38             0.0                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               13            1.62              1.33        116.52                36.51         0.573          pass              0.439             11.2                           0.310               -1.57              0.228                                 ok            True                  False
   CSX           87.50               16            0.92              0.32         49.78                19.08         0.563          pass              0.326              9.8                           0.279                4.06              0.353                                 ok            True                  False
   EXC           94.74               19            0.50              0.16         46.85                21.56         0.561          pass              0.674             54.8                           0.366                0.14             -0.041                                 ok            True                  False
  SBUX           85.00               20            1.00              0.74        105.85                22.72         0.509          pass              0.279              9.4                           0.168                2.86              0.361                                 ok            True                  False
   WDC           78.26               23            2.00              7.89        559.94               117.61         0.754          pass              0.175              4.2                           0.216              -13.57             -0.776            downtrend_blocked_slope           False                  False
    MU           80.00               25            2.08             14.32        976.98               112.73         0.740          pass              0.239             21.7                           0.302              -16.59             -1.144            downtrend_blocked_slope           False                  False
  DRAM           84.00               25            2.44              1.05         60.78               112.33         0.733          pass              0.293              4.5                           0.097               -9.31             -0.725            downtrend_blocked_slope           False                  False
  KLAC           86.21               29            1.18              1.90        229.55               109.33         0.730          pass              0.401             12.0                           0.213              -24.55             -1.963 downtrend_blocked_slope_and_streak           False                  False
  LRCX           89.29               28            0.89              2.15        345.18                98.70         0.716          pass              0.522             27.5                           0.259              -20.84             -1.644 downtrend_blocked_slope_and_streak           False                  False
  AMAT           90.62               32            0.58              2.40        594.67                98.89         0.708          pass              0.501              0.0                           0.190              -18.08             -1.277 downtrend_blocked_slope_and_streak           False                  False
   STX           85.71               21            1.72             10.56        873.78                92.39         0.677          pass              0.329             11.9                           0.192              -10.55             -0.440            downtrend_blocked_slope           False                  False
  MDLZ           93.33               15            0.43              0.18         58.72                30.54         0.628          pass              0.669             72.3                           0.554                1.22             -0.080                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-15T09:35:02.740173-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:30:04.740888-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:25:03.806265-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:20:04.874058-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:15:04.885771-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:10:05.907681-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:05:04.903172-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T09:00:02.786687-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T08:55:04.748908-04:00 data_refresh data_refresh {'saved': 93}
2026-07-15T08:50:02.886392-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715093502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715093502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715093502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715093502)

</details>
