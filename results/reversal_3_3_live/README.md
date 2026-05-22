# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:55:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$27,577.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-740.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11400.0        30.35           28.5      415.18        413.12          bid_ask_mid                       28.5                bid_ask_mid                    True          -740.0                   -6.1         91.67               36              0.62         50.17           48.82                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.59               37            0.65              7.66       1674.62                61.16         0.588          pass              0.666             12.7                           0.150                2.11              0.514                                 ok            True                  False
  SBUX           95.45               22            0.73              0.53        103.90                32.97         0.579          pass              0.696             52.8                           0.669               -0.91             -0.037                                 ok            True                  False
  NVDA           89.29               28            1.04              1.60        218.82                44.83         0.519          pass              0.562             47.4                           0.593                0.94             -0.019                                 ok            True                  False
  INSM           70.83               24            2.37              1.82        108.75               111.27         0.730          pass              0.185              6.1                           0.107                5.51             -0.001                                 ok           False                  False
   TRI           83.33               24            0.29              0.18         85.48                54.99         0.601          pass              0.494             84.0                           0.351               -7.52             -0.288           downtrend_blocked_streak           False                  False
   WMT           90.00               10            1.52              1.29        120.79                34.61         0.582          pass              0.398             24.3                           0.410               -8.38             -0.527            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.05              0.02         64.32                59.89         0.574          pass              0.529             90.6                           0.363                1.31              0.270                                 ok           False                  False
  REGN           93.10               29            0.97              4.36        640.72                49.06         0.550          pass              0.761             76.6                           0.429              -10.85             -1.537 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            2.01             14.80       1044.11                22.19         0.528          pass              0.098             15.1                           0.347                2.03              0.543                                 ok           False                  False
 GOOGL           90.70               43            0.06              0.17        387.59                41.05         0.512          pass              0.817             93.5                           0.827               -3.34             -0.231                                 ok           False                  False
  CHTR           76.47               17            2.48              2.59        147.79               115.38         0.511          pass              0.098              0.0                           0.170               -6.24             -0.377                                 ok           False                  False
  AVGO           91.89               37            0.52              1.50        413.93                40.36         0.505          pass              0.700             50.7                           0.482               -4.09             -0.385            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522105505)

</details>
