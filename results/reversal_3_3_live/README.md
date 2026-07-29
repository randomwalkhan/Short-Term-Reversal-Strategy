# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 09:45:02 EDT`
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

- Cash: `$18,410.50`
- Equity: `$33,568.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$-3,225.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   1    129     18382.5                 15157.5         1.42           1.18       51.22         50.61          bid_ask_mid                       1.18                bid_ask_mid                    True         -3225.0                 -17.54         92.86               14              1.11         25.66           30.62                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               16            0.91              0.31         47.97                27.18         0.580          pass              0.653             51.6                           0.452                4.77              0.472                                 ok            True                  False
   CSX           95.65               23            0.63              0.22         50.74                28.82         0.549          pass              0.567              8.6                           0.113                2.21              0.298                                 ok            True                  False
  GILD           88.46               26            0.64              0.60        134.06                34.28         0.527          pass              0.506             40.3                           0.244                2.63             -0.022                                 ok            True                  False
   HON           87.50               24            0.92              1.59        246.37                39.75         0.522          pass              0.411             21.8                           0.272                9.92              1.180                                 ok            True                  False
  SOXL           85.29               34            0.20              0.15        109.44               173.28         0.690          pass              0.665             98.3                           0.902              -33.98             -2.926 downtrend_blocked_slope_and_streak           False                  False
  ISRG           66.67               12            2.26              5.73        359.34                72.57         0.643          pass              0.098              6.8                           0.198               -9.09             -0.926            downtrend_blocked_slope           False                  False
  DRAM           81.25               32            0.45              0.15         47.69               100.66         0.622          pass              0.530             95.9                           0.731              -17.18             -1.162 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           85.00               20            0.17              0.03         24.18                39.20         0.610          pass              0.527             88.6                           0.614                2.81             -0.214                                 ok           False                  False
  LRCX           88.89               36            0.18              0.34        269.47                78.60         0.579          pass              0.759             96.9                           0.933              -19.77             -1.811 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.62               32            0.65              0.83        182.04                56.22         0.573          pass              0.636             49.6                           0.284               -3.42             -0.875            downtrend_blocked_slope           False                  False
  META           93.02               43            0.33              1.37        592.82                53.87         0.565          pass              0.749             48.4                           0.336              -13.19             -1.504 downtrend_blocked_slope_and_streak           False                  False
    MU           82.35               34            0.50              2.88        819.30                86.39         0.565          pass              0.560             93.7                           0.575               -9.72             -0.255 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729094502)

</details>
