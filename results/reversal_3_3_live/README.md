# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 14:25:13 EDT`
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
- Equity: `$27,957.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11780.0        30.35          29.45      415.18        412.36          bid_ask_mid                      29.45                bid_ask_mid                    True          -360.0                  -2.97         91.67               36              0.62         50.17           50.49                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           92.86               14            1.18              0.86        103.76                32.97         0.599            pass              0.517             29.1                           0.491               -1.36             -0.058                                 ok            True                  False
  MELI           94.59               37            0.63              7.42       1674.72                61.16         0.579            pass              0.812             61.8                           0.443                2.13              0.515                                 ok            True                  False
  NVDA           85.71               21            1.68              2.59        218.40                44.83         0.521            pass              0.323             15.1                           0.163                0.29             -0.049                                 ok            True                  False
  INSM           68.97               29            1.63              1.25        108.99               111.27         0.736            pass              0.329             43.0                           0.641                6.31              0.033                                 ok           False                  False
   WMT           93.75               16            1.12              0.95        120.93                34.61         0.572            pass              0.597             44.2                           0.377               -8.01             -0.508            downtrend_blocked_slope           False                  False
  REGN           92.59               27            1.11              4.98        640.45                49.06         0.554            pass              0.724             73.2                           0.448              -10.98             -1.543 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           86.67               30            0.83              2.25        386.70                41.05         0.545            pass              0.404             12.8                           0.133               -4.08             -0.266            downtrend_blocked_slope           False                  False
  GOOG           87.88               33            0.72              1.94        382.64                40.91         0.536            pass              0.453             11.9                           0.128               -4.12             -0.290 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            1.97             14.51       1044.23                22.19         0.530            pass              0.106             17.6                           0.364                2.07              0.545                                 ok           False                  False
  AVGO           91.89               37            0.50              1.45        413.95                40.36         0.507            pass              0.705             52.5                           0.368               -4.07             -0.384            downtrend_blocked_slope           False                  False
  MSTR           88.89               36            1.48              1.71        164.12                63.46         0.499 below_threshold              0.626             55.2                           0.539              -13.42             -1.821            downtrend_blocked_slope           False                  False
    EA           91.67               24            0.27              0.38        201.71                 2.73         0.483 below_threshold              0.652             66.4                           0.503                0.44              0.084                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522142513)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522142513)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522142513)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522142513)

</details>
