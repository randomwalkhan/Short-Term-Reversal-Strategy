# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 13:55:04 EDT`
Last processed slot: `manage_1400`

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
- Equity: `$28,007.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-310.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11830.0        30.35          29.58      415.18        412.93          bid_ask_mid                      29.58                bid_ask_mid                    True          -310.0                  -2.55         91.67               36              0.62         50.17           50.43                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           91.67               12            1.53              1.11        103.65                32.97         0.590          pass              0.402              6.2                           0.273               -1.70             -0.074                                 ok            True                  False
  MELI           94.59               37            0.62              7.23       1674.80                61.16         0.580          pass              0.816             62.8                           0.534                2.15              0.516                                 ok            True                  False
  NVDA           85.71               21            1.63              2.50        218.44                44.83         0.524          pass              0.332             17.9                           0.175                0.34             -0.046                                 ok            True                  False
  INSM           70.83               24            2.31              1.77        108.77               111.27         0.730          pass              0.224             19.2                           0.240                5.57              0.002                                 ok           False                  False
   TRI           85.19               27            0.09              0.06         85.54                54.99         0.596          pass              0.596             94.9                           0.461               -7.33             -0.279           downtrend_blocked_streak           False                  False
   WMT           93.75               16            1.06              0.90        120.95                34.61         0.575          pass              0.605             46.9                           0.430               -7.96             -0.506            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.12              0.06         64.31                59.89         0.567          pass              0.500             81.0                           0.631                1.23              0.266                                 ok           False                  False
  REGN           92.86               28            1.02              4.60        640.62                49.06         0.553          pass              0.744             75.3                           0.588              -10.90             -1.539 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           88.24               34            0.62              1.69        386.93                41.05         0.533          pass              0.536             34.2                           0.309               -3.88             -0.256            downtrend_blocked_slope           False                  False
  COST           80.00                5            2.10             15.44       1043.83                22.19         0.523          pass              0.089             12.4                           0.220                1.94              0.539                                 ok           False                  False
  GOOG           89.47               38            0.53              1.41        382.86                40.91         0.516          pass              0.598             35.8                           0.291               -3.93             -0.281 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.89               36            1.43              1.64        164.14                63.46         0.503          pass              0.631             56.9                           0.505              -13.37             -1.818            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522135504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522135504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522135504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522135504)

</details>
