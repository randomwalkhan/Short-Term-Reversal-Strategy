# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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
- Equity: `$27,817.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-500.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11640.0        30.35           29.1      415.18        414.11          bid_ask_mid                       29.1                bid_ask_mid                    True          -500.0                  -4.12         91.67               36              0.62         50.17           49.26                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           93.33               15            1.07              0.78        103.80                32.97         0.602            pass              0.542             31.1                           0.295               -1.24             -0.053                                 ok            True                  False
  MELI           94.44               36            0.89             10.47       1673.41                61.16         0.575            pass              0.665             16.2                           0.227                1.86              0.503                                 ok            True                  False
  NVDA           90.00               30            0.89              1.37        218.92                44.83         0.517            pass              0.617             55.2                           0.596                1.10             -0.012                                 ok            True                  False
  INSM           70.83               24            2.28              1.75        108.78               111.27         0.731            pass              0.227             20.1                           0.276                5.60              0.003                                 ok           False                  False
   TRI           80.00               20            0.60              0.36         85.41                54.99         0.603            pass              0.329             67.3                           0.300               -7.80             -0.302 downtrend_blocked_slope_and_streak           False                  False
  SHOP           84.09               44            0.28              0.20        104.77                78.48         0.602            pass              0.529             53.2                           0.360               -5.29              0.121                                 ok           False                  False
   WMT           92.86               14            1.23              1.05        120.89                34.61         0.577            pass              0.543             38.5                           0.553               -8.12             -0.514            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.03              0.01         64.32                59.89         0.575            pass              0.539             93.7                           0.477                1.32              0.270                                 ok           False                  False
  REGN           91.67               24            1.23              5.55        640.21                49.06         0.565            pass              0.671             70.2                           0.405              -11.09             -1.549 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.33             17.12       1043.11                22.19         0.509            pass              0.056              1.7                           0.241                1.71              0.528                                 ok           False                  False
  AVGO           90.48               42            0.09              0.27        414.45                40.36         0.497 below_threshold              0.802             91.1                           0.724               -3.68             -0.365            downtrend_blocked_slope           False                  False
  MSTR           90.32               31            2.15              2.48        163.79                63.46         0.492 below_threshold              0.569             34.9                           0.548              -14.01             -1.852            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522111501)

</details>
