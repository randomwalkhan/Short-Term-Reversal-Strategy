# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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
- Equity: `$29,357.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$1,040.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 13180.0        30.35          32.95      415.18        414.67          bid_ask_mid                      32.95                bid_ask_mid                    True          1040.0                   8.57         91.67               36              0.62         50.17           54.29                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           92.31               13            1.41              1.03        103.69                32.97         0.593          pass              0.434              8.7                           0.156               -1.59             -0.068                                 ok            True                  False
  CHTR           85.71               28            1.45              1.52        148.25               115.38         0.530          pass              0.325              0.0                           0.170               -5.25             -0.329                                 ok            True                  False
  NVDA           88.00               25            1.35              2.07        218.62                44.83         0.520          pass              0.445             26.7                           0.194                0.63             -0.033                                 ok            True                  False
  INSM           75.68               37            0.96              0.73        109.22               111.27         0.743          pass              0.419             54.8                           0.294                7.04              0.064                                 ok           False                  False
    MU           80.00               35            0.43              2.28        761.12                87.43         0.667          pass              0.482             82.8                           0.679                1.61             -0.581                                 ok           False                  False
   STX           95.00               40            0.03              0.14        810.40                68.63         0.592          pass              0.953             98.1                           0.654                3.53             -0.421                                 ok           False                  False
  MELI           95.24               42            0.17              2.01       1677.04                61.16         0.590          pass              0.847             62.6                           0.314                2.60              0.536                                 ok           False                  False
   WMT           87.50                8            1.89              1.60        120.65                34.61         0.568          pass              0.274              5.8                           0.169               -8.72             -0.544            downtrend_blocked_slope           False                  False
  REGN           93.33               30            0.84              3.77        640.97                49.06         0.553          pass              0.783             79.7                           0.421              -10.73             -1.531 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.11              0.38        486.30                59.01         0.548          pass              0.934             93.2                           0.659                1.23             -0.530                                 ok           False                  False
 GOOGL           88.24               34            0.61              1.67        386.95                41.05         0.534          pass              0.539             35.3                           0.331               -3.87             -0.256            downtrend_blocked_slope           False                  False
  MSTR           88.89               36            1.42              1.64        164.15                63.46         0.520          pass              0.543             26.9                           0.259              -13.37             -1.818            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T14:50:05.768088-04:00       entry_1500 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522101504)

</details>
