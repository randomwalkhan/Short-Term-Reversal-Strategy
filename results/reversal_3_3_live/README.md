# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:30:05 EDT`
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
- Equity: `$28,637.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$320.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12460.0        30.35          31.15      415.18        411.19          bid_ask_mid                      31.15                bid_ask_mid                    True           320.0                   2.64         91.67               36              0.62         50.17           54.25                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.91              4.86        760.02                87.43         0.648          pass              0.477             63.3                           0.619                1.12             -0.603                                 ok            True                  False
  SBUX           93.33               15            1.01              0.74        103.81                32.97         0.605          pass              0.553             34.6                           0.379               -1.19             -0.050                                 ok            True                  False
  CHTR           84.00               25            1.58              1.64        148.20               115.38         0.535          pass              0.300             13.3                           0.162               -5.37             -0.335                                 ok            True                  False
  NVDA           86.36               22            1.54              2.36        218.50                44.83         0.524          pass              0.369             22.4                           0.225                0.43             -0.042                                 ok            True                  False
  INSM           73.53               34            1.18              0.91        109.14               111.27         0.745          pass              0.367             44.2                           0.239                6.79              0.054                                 ok           False                  False
  MELI           95.24               42            0.17              2.03       1677.03                61.16         0.590          pass              0.845             62.1                           0.266                2.60              0.536                                 ok           False                  False
   WMT           90.91               11            1.34              1.13        120.85                34.61         0.588          pass              0.456             33.3                           0.358               -8.21             -0.518            downtrend_blocked_slope           False                  False
   STX           94.87               39            0.26              1.46        809.83                68.63         0.584          pass              0.889             80.3                           0.719                3.29             -0.431                                 ok           False                  False
  REGN           93.10               29            0.97              4.35        640.72                49.06         0.551          pass              0.761             76.6                           0.449              -10.85             -1.537 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.16              0.54        486.23                59.01         0.545          pass              0.925             90.3                           0.743                1.19             -0.532                                 ok           False                  False
  COST           75.00                4            2.19             16.11       1043.55                22.19         0.517          pass              0.071              6.6                           0.171                1.85              0.535                                 ok           False                  False
 GOOGL           90.48               42            0.21              0.57        387.41                41.05         0.508          pass              0.763             77.7                           0.716               -3.48             -0.238                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped      {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped      {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh  data_refresh                   {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500  slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522103005)

</details>
