# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 09:30:04 EDT`
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
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16625.0         6.55           6.65       129.9        129.78     last_price_stale                        NaN                unavailable                   False           250.0                   1.53         91.67               24              0.73         32.92             0.0                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           94.12               34            0.83             10.16       1752.74                55.36         0.562              pass              0.665             24.0                           0.225                0.96             -0.012                                 ok            True                  False
  LRCX           88.89               36            0.18              0.39        305.04                84.70         0.674              pass              0.728             83.3                           0.407               -7.66             -0.919 downtrend_blocked_slope_and_streak           False                  False
  PYPL           88.64               44            0.04              0.01         56.14                61.60         0.619              pass              0.775             94.3                           0.549               17.80              1.357                                 ok           False                  False
   EXC           95.65               23            0.34              0.11         47.48                24.05         0.568              pass              0.791             82.6                           0.568                1.22              0.047                                 ok           False                  False
   WBD           71.43                7            1.61              0.29         25.65                22.62         0.533              pass              0.104             17.0                           0.326               -6.40             -0.851            downtrend_blocked_slope           False                  False
   CSX           96.67               30            0.34              0.13         53.18                24.58         0.530              pass              0.586              0.0                           0.284                6.87              0.665                                 ok           False                  False
   AEP           84.21               38            0.15              0.14        135.48                21.12         0.448   below_threshold              0.594             83.3                           0.528               -0.07             -0.102                                 ok           False                  False
  ODFL           83.33               30            0.94              1.53        232.34                28.18         0.426   below_threshold              0.265              0.0                           0.258               -0.90              0.050                                 ok           False                  False
  INSM           81.25               48            0.21              0.15        106.85                34.54         0.414   below_threshold              0.540             88.5                           0.735               -7.71             -0.534            downtrend_blocked_slope           False                  False
  AAPL             NaN                0            0.00              0.00        334.83                30.88           NaN no_signal_history                NaN              NaN                           0.630                5.52              0.376                                 ok           False                  False
  ABNB             NaN                0            0.00              0.00        143.76                33.42           NaN no_signal_history                NaN              NaN                           0.666               -1.76             -0.485           downtrend_blocked_streak           False                  False
  ADBE             NaN                0            0.00              0.00        231.50                51.32           NaN no_signal_history                NaN              NaN                           0.662                0.39             -0.153                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-27T09:30:04.489033-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:25:02.551278-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:20:01.575598-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:15:05.384671-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:10:05.509301-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:05:02.526128-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:00:04.546327-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:55:01.530928-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:50:01.513320-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:45:04.558373-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727093004)

</details>
