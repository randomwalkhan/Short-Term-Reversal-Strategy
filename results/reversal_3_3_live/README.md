# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 09:45:01 EDT`
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

- Cash: `$15,257.25`
- Equity: `$31,682.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$1,460.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 16425.0         2.05           2.25       52.68         53.15     last_price_stale                        NaN                unavailable                   False          1460.0                   9.76         93.55               31              0.59         45.34            3.13                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           84.00               25            0.56              0.32         82.18                68.38         0.679          pass              0.523             82.8                           0.577               -0.38             -0.385                                 ok            True                  False
    MU           84.38               32            1.05              6.89        932.94               110.66         0.669          pass              0.566             78.6                           0.622               -0.25             -0.414                                 ok            True                  False
  CSCO           96.15               26            1.06              0.89        119.98                60.79         0.626          pass              0.679             36.5                           0.298               -0.48              0.132                                 ok            True                  False
   WMT           87.10               31            0.62              0.52        118.66                35.78         0.548          pass              0.457             24.3                           0.181               -0.34              0.182                                 ok            True                  False
   CSX           92.86               28            0.53              0.18         47.20                21.23         0.506          pass              0.694             60.3                           0.452                0.07              0.285                                 ok            True                  False
  DRAM          100.00               23            0.07              0.03         59.76               102.89         0.765          pass              0.859             98.7                           0.814               -1.65             -0.767            downtrend_blocked_slope           False                  False
  MRVL          100.00               30            0.37              0.70        266.58               141.19         0.752          pass              0.887             92.8                           0.854               33.81              3.631                                 ok           False                  False
  SOXL           93.55               31            0.39              0.55        201.55               192.17         0.736          pass              0.864             96.4                           0.909               -7.79             -1.331            downtrend_blocked_slope           False                  False
  INTU           78.12               32            1.04              2.14        292.86               101.32         0.726          pass              0.419             66.6                           0.636               -5.53             -1.090 downtrend_blocked_slope_and_streak           False                  False
  QCOM           94.12               17            1.57              2.25        204.46                99.46         0.681          pass              0.671             60.0                           0.647              -13.05             -1.705            downtrend_blocked_slope           False                  False
  TEAM           93.02               43            0.25              0.16         95.54                85.52         0.621          pass              0.893             94.5                           0.840                7.08             -0.202                                 ok           False                  False
  WDAY           90.70               43            0.21              0.20        140.14                67.85         0.578          pass              0.829             95.3                           0.894               12.40              0.599                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610094501)

</details>
