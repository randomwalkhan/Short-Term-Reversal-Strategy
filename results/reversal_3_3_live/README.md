# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:40:01 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$28,357.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$40.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12180.0        30.35          30.45      415.18        412.83          bid_ask_mid                      30.45                bid_ask_mid                    True            40.0                   0.33         91.67               36              0.62         50.17           51.89                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.59               37            0.57              6.71       1675.03                61.16         0.593          pass              0.699             23.5                           0.229                2.19              0.518                                 ok            True                  False
  SBUX           95.65               23            0.59              0.43        103.95                32.97         0.582          pass              0.730             61.8                           0.642               -0.77             -0.031                                 ok            True                  False
  CHTR           85.71               28            1.40              1.46        148.27               115.38         0.528          pass              0.394             22.9                           0.268               -5.20             -0.327                                 ok            True                  False
  NVDA           89.29               28            1.14              1.75        218.76                44.83         0.513          pass              0.546             42.4                           0.443                0.84             -0.024                                 ok            True                  False
  INSM           70.37               27            1.73              1.33        108.96               111.27         0.750          pass              0.243             18.3                           0.136                6.20              0.029                                 ok           False                  False
    MU           81.08               37            0.21              1.14        761.61                87.43         0.668          pass              0.550             91.4                           0.791                1.83             -0.571                                 ok           False                  False
   TRI           83.33               24            0.27              0.16         85.49                54.99         0.602          pass              0.498             85.3                           0.356               -7.49             -0.287           downtrend_blocked_streak           False                  False
   WMT           90.00               10            1.58              1.34        120.76                34.61         0.578          pass              0.387             21.0                           0.369               -8.44             -0.530            downtrend_blocked_slope           False                  False
  REGN           93.94               33            0.76              3.41        641.13                49.06         0.538          pass              0.824             81.7                           0.495              -10.66             -1.527 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.27             16.72       1043.29                22.19         0.512          pass              0.060              3.0                           0.094                1.76              0.531                                 ok           False                  False
  AVGO           91.89               37            0.53              1.53        413.91                40.36         0.505          pass              0.697             49.9                           0.355               -4.10             -0.385            downtrend_blocked_slope           False                  False
 GOOGL           90.70               43            0.18              0.50        387.45                41.05         0.504          pass              0.777             80.6                           0.784               -3.46             -0.236                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh  data_refresh              {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522104001)

</details>
