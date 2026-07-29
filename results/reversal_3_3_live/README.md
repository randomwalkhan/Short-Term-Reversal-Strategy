# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 09:40:02 EDT`
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

- Cash: `$18,410.50`
- Equity: `$36,470.50`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$-322.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   1    129     18382.5                 18060.0         1.42            1.4       51.22         50.74     last_price_stale                        NaN                unavailable                   False          -322.5                  -1.75         92.86               14              1.11         25.66            3.13                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               10            1.41              0.48         47.90                27.18         0.586          pass              0.534             25.3                           0.244                4.24              0.449                                 ok            True                  False
  BKNG           93.33               30            0.80              1.11        198.83                45.62         0.571          pass              0.749             67.6                           0.655               13.08              0.753                                 ok            True                   True
   HON           84.21               19            1.03              1.78        246.29                39.75         0.544          pass              0.265             12.7                           0.252                9.80              1.175                                 ok            True                  False
  ORLY           80.77               26            1.23              0.78         90.83                45.72         0.512          pass              0.353             58.1                           0.502                5.01              0.664                                 ok            True                  False
  AVGO           81.25               32            0.88              2.36        379.90                41.80         0.502          pass              0.384             51.3                           0.331               -4.24             -0.024                                 ok            True                  False
  ISRG           73.91               23            1.30              3.30        360.39                72.57         0.648          pass              0.279             42.4                           0.322               -8.20             -0.882                                 ok           False                  False
  SOXL           85.29               34            0.87              0.67        109.22               173.28         0.647          pass              0.643             92.4                           0.857              -34.43             -2.957 downtrend_blocked_slope_and_streak           False                  False
  DRAM           81.25               32            0.64              0.21         47.66               100.66         0.610          pass              0.524             94.2                           0.755              -17.33             -1.170 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           82.35               17            0.37              0.06         24.16                39.20         0.610          pass              0.393             74.3                           0.419                2.60             -0.223                                 ok           False                  False
   TRI           87.18               39            0.46              0.34        103.15                68.18         0.576          pass              0.637             64.7                           0.385               12.07              0.459                                 ok           False                  False
    MU           82.35               34            0.48              2.73        819.36                86.39         0.567          pass              0.562             94.0                           0.667               -9.69             -0.254 downtrend_blocked_slope_and_streak           False                  False
   APP           81.82               44            0.99              2.90        416.98                74.36         0.547          pass              0.475             57.1                           0.459               -8.54             -0.852            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-29T09:35:02.435322-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:30:03.798822-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:25:01.530149-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:20:02.789351-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:15:01.480372-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:10:04.312418-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:05:01.483120-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:00:02.430762-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T08:55:05.405467-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T08:50:01.443256-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729094002)

</details>
