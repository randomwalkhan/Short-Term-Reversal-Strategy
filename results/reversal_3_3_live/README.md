# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 09:50:01 EDT`
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

- Cash: `$15,257.25`
- Equity: `$31,682.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$1,460.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 16425.0         2.05           2.25       52.68         52.86     last_price_stale                        NaN                unavailable                   False          1460.0                   9.76         93.55               31              0.59         45.34            3.13                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           84.85               33            0.76              4.96        933.77               110.66         0.682          pass              0.605             84.6                           0.836                0.04             -0.401                                 ok            True                  False
  CSCO           96.67               30            0.56              0.47        120.16                60.79         0.631          pass              0.796             66.5                           0.540                0.02              0.155                                 ok            True                  False
   CSX           84.62               13            0.99              0.33         47.14                21.23         0.575          pass              0.277             25.4                           0.187               -0.40              0.263                                 ok            True                  False
   WMT           84.62               26            0.91              0.76        118.55                35.78         0.560          pass              0.344             19.4                           0.241               -0.63              0.169                                 ok            True                  False
  REGN           84.38               32            0.95              4.10        614.42                44.80         0.545          pass              0.333              5.0                           0.129               -2.78             -0.034                                 ok            True                  False
  INTU           78.12               32            1.11              2.28        292.80               101.32         0.723          pass              0.413             64.5                           0.720               -5.59             -1.093 downtrend_blocked_slope_and_streak           False                  False
  QCOM           94.74               19            1.36              1.96        204.58                99.46         0.682          pass              0.717             65.1                           0.754              -12.87             -1.696            downtrend_blocked_slope           False                  False
   TRI           78.95               19            1.04              0.60         82.06                68.38         0.682          pass              0.332             68.0                           0.568               -0.86             -0.407                                 ok           False                  False
  WDAY           90.00               40            0.46              0.45        140.04                67.85         0.580          pass              0.794             89.7                           0.892               12.12              0.587                                 ok           False                  False
  AVGO           88.89                9            3.23              8.85        388.37                69.58         0.578          pass              0.369             24.7                           0.268              -10.04             -1.558            downtrend_blocked_slope           False                  False
   EXC           78.57               14            0.54              0.17         45.26                22.56         0.575          pass              0.274             63.4                           0.347               -1.47             -0.019                                 ok           False                  False
   HON           75.00                8            1.65              2.49        214.63                29.75         0.570          pass              0.151             31.5                           0.390               -8.38             -1.248 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-06-10T09:20:01.107182-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:15:04.252289-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:10:02.279935-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:05:01.300064-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:00:02.291233-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:55:03.361552-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:50:01.278104-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:45:01.119334-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:40:02.326474-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:35:05.344979-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610095001)

</details>
