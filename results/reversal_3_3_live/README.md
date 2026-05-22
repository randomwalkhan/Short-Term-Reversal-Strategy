# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 14:20:09 EDT`
Last processed slot: `manage_1430`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$16,177.75`
- Equity: `$27,987.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-330.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11810.0        30.35          29.52      415.18        412.63          bid_ask_mid                      29.52                bid_ask_mid                    True          -330.0                  -2.72         91.67               36              0.62         50.17           50.66                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           92.31               13            1.33              0.97        103.71                32.97         0.596            pass              0.468             20.1                           0.397               -1.51             -0.065                                 ok            True                  False
  MELI           94.59               37            0.65              7.63       1674.63                61.16         0.577            pass              0.809             60.7                           0.400                2.11              0.514                                 ok            True                  False
  NVDA           85.71               21            1.74              2.67        218.36                44.83         0.517            pass              0.314             12.2                           0.161                0.23             -0.051                                 ok            True                  False
  INSM           69.23               26            1.80              1.38        108.94               111.27         0.744            pass              0.292             36.9                           0.465                6.12              0.025                                 ok           False                  False
   WMT           93.75               16            1.12              0.96        120.93                34.61         0.572            pass              0.595             43.8                           0.387               -8.02             -0.509            downtrend_blocked_slope           False                  False
  REGN           92.00               25            1.19              5.35        640.30                49.06         0.562            pass              0.690             71.3                           0.417              -11.05             -1.547 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           86.67               30            0.83              2.24        386.70                41.05         0.545            pass              0.405             13.0                           0.123               -4.08             -0.266            downtrend_blocked_slope           False                  False
  GOOG           87.88               33            0.72              1.94        382.64                40.91         0.536            pass              0.453             11.9                           0.116               -4.12             -0.290 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            2.04             15.01       1044.02                22.19         0.526            pass              0.097             14.8                           0.340                2.00              0.542                                 ok           False                  False
  AVGO           89.74               39            0.45              1.32        414.01                40.36         0.493 below_threshold              0.673             56.9                           0.397               -4.03             -0.382            downtrend_blocked_slope           False                  False
  MSTR           91.43               35            1.77              2.04        163.98                63.46         0.491 below_threshold              0.660             46.6                           0.320              -13.67             -1.834            downtrend_blocked_slope           False                  False
  PYPL           87.50               40            0.40              0.12         44.25                33.02         0.470 below_threshold              0.505             19.2                           0.249               -2.74             -0.324 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T12:00:04.237005-04:00 early_entry_1200 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:55:01.324366-04:00 early_entry_1155 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:50:01.298135-04:00 early_entry_1150 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:35:01.410809-04:00 early_entry_1135 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522142009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522142009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522142009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522142009)

</details>
