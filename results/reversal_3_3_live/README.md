# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 09:55:06 EDT`
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

- Cash: `$4,915.25`
- Equity: `$26,875.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-120.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   1     11     12705.0                 12760.0        11.55           11.6      315.21        321.51     last_price_stale                        NaN                unavailable                   False            55.0                   0.43         95.83               24              0.66         28.20             0.0                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9200.0        46.88           46.0      660.72        659.63     last_price_stale                        NaN                unavailable                   False          -175.0                  -1.87         81.82               22              1.27         53.38             0.0                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.33               15            0.53              0.22         58.71                30.54         0.623          pass              0.650             66.3                           0.555                1.12             -0.084                                 ok            True                  False
   CSX           90.91               22            0.73              0.26         49.81                19.08         0.540          pass              0.510             28.4                           0.242                4.26              0.362                                 ok            True                  False
   AEP           80.00               25            0.51              0.48        134.73                21.64         0.528          pass              0.255             34.1                           0.239               -1.87             -0.178                                 ok            True                  False
  SOXL           86.67               30            1.93              2.39        175.64               219.49         0.904          pass              0.500             33.0                           0.217              -35.04             -2.842            downtrend_blocked_slope           False                  False
  MPWR           83.78               37            0.05              0.52       1376.19                84.79         0.699          pass              0.583             77.2                           0.348               -0.48              0.230                                 ok           False                  False
  KLAC           82.61               23            2.06              3.33        228.94               109.33         0.697          pass              0.286             19.9                           0.230              -25.22             -2.003 downtrend_blocked_slope_and_streak           False                  False
    MU           82.61               23            3.05             20.96        974.14               112.73         0.691          pass              0.268             14.4                           0.205              -17.41             -1.189            downtrend_blocked_slope           False                  False
  DRAM           83.33               18            3.79              1.62         60.53               112.33         0.682          pass              0.233              7.6                           0.131              -10.55             -0.788            downtrend_blocked_slope           False                  False
  AMAT           86.96               23            1.72              7.19        592.62                98.89         0.671          pass              0.412             24.2                           0.235              -19.03             -1.330 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.46               26            2.01              4.86        344.02                98.70         0.644          pass              0.464             22.5                           0.215              -21.73             -1.695 downtrend_blocked_slope_and_streak           False                  False
  MSTR           77.27               44            0.39              0.27         97.47               100.18         0.636          pass              0.396             44.1                           0.294               11.81              0.422                                 ok           False                  False
   WDC           88.24               17            4.49             17.69        555.74               117.61         0.634          pass              0.334              1.5                           0.175              -15.76             -0.893            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715095506)

</details>
