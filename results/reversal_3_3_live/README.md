# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:20:04 EDT`
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
- Equity: `$29,117.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12940.0        30.35          32.35      415.18        413.21          bid_ask_mid                      32.35                bid_ask_mid                    True           800.0                   6.59         91.67               36              0.62         50.17           54.72                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.95              5.05        759.93                87.43         0.646          pass              0.473             61.9                           0.619                1.08             -0.605                                 ok            True                  False
  SBUX           95.00               20            0.85              0.62        103.86                32.97         0.584          pass              0.659             44.7                           0.489               -1.03             -0.043                                 ok            True                  False
  CHTR           83.33               24            1.69              1.76        148.14               115.38         0.534          pass              0.248              4.3                           0.163               -5.47             -0.340                                 ok            True                  False
  NVDA           86.96               23            1.53              2.34        218.51                44.83         0.521          pass              0.375             16.9                           0.137                0.45             -0.041                                 ok            True                  False
  INSM           75.68               37            1.00              0.77        109.20               111.27         0.741          pass              0.412             52.6                           0.272                6.99              0.062                                 ok           False                  False
   STX           94.87               39            0.31              1.76        809.71                68.63         0.580          pass              0.877             76.2                           0.529                3.23             -0.434                                 ok           False                  False
   WMT           88.89                9            1.76              1.50        120.70                34.61         0.571          pass              0.330             11.9                           0.196               -8.61             -0.538            downtrend_blocked_slope           False                  False
   WDC           95.12               41            0.24              0.82        486.11                59.01         0.540          pass              0.910             85.3                           0.668                1.10             -0.536                                 ok           False                  False
  REGN           94.12               34            0.70              3.15        641.24                49.06         0.536          pass              0.839             83.1                           0.411              -10.61             -1.524 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           88.89               36            0.57              1.55        386.99                41.05         0.524          pass              0.582             39.7                           0.361               -3.83             -0.254            downtrend_blocked_slope           False                  False
  COST           75.00                4            2.14             15.77       1043.69                22.19         0.520          pass              0.072              6.7                           0.159                1.90              0.537                                 ok           False                  False
  GOOG           89.74               39            0.43              1.15        382.98                40.91         0.516          pass              0.647             47.5                           0.390               -3.84             -0.276 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522102004)

</details>
