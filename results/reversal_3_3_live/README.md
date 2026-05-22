# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:35:05 EDT`
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
- Equity: `$28,437.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$120.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12260.0        30.35          30.65      415.18        412.14          bid_ask_mid                      30.65                bid_ask_mid                    True           120.0                   0.99         91.67               36              0.62         50.17           52.52                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.82              4.38        760.22                87.43         0.653          pass              0.489             66.9                           0.643                1.21             -0.599                                 ok            True                  False
  SBUX           93.75               16            1.00              0.73        103.82                32.97         0.600          pass              0.572             35.1                           0.373               -1.18             -0.050                                 ok            True                  False
  MELI           94.59               37            0.61              7.20       1674.81                61.16         0.592          pass              0.652              7.8                           0.182                2.15              0.516                                 ok            True                  False
  CHTR           85.71               28            1.39              1.45        148.28               115.38         0.529          pass              0.396             23.4                           0.231               -5.19             -0.327                                 ok            True                  False
  NVDA           87.50               24            1.46              2.24        218.55                44.83         0.517          pass              0.424             26.4                           0.306                0.52             -0.038                                 ok            True                  False
  INSM           70.97               31            1.58              1.21        109.01               111.27         0.738          pass              0.290             25.4                           0.164                6.36              0.036                                 ok           False                  False
   TRI           81.82               22            0.39              0.23         85.46                54.99         0.606          pass              0.426             78.8                           0.333               -7.60             -0.292           downtrend_blocked_streak           False                  False
   WMT           90.00               10            1.50              1.27        120.79                34.61         0.583          pass              0.400             25.1                           0.362               -8.36             -0.526            downtrend_blocked_slope           False                  False
  REGN           93.33               30            0.85              3.82        640.95                49.06         0.552          pass              0.782             79.5                           0.455              -10.74             -1.531 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.23             16.42       1043.41                22.19         0.515          pass              0.066              4.8                           0.090                1.81              0.533                                 ok           False                  False
  AVGO           91.67               36            0.57              1.65        413.86                40.36         0.509          pass              0.673             46.0                           0.307               -4.14             -0.387            downtrend_blocked_slope           False                  False
 GOOGL           90.48               42            0.25              0.69        387.37                41.05         0.506          pass              0.750             73.3                           0.731               -3.52             -0.240                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522103505)

</details>
