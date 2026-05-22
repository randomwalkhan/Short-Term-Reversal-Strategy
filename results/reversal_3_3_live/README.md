# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:20:06 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$27,637.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-680.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11460.0        30.35          28.65      415.18        415.11          bid_ask_mid                      28.65                bid_ask_mid                    True          -680.0                   -5.6         91.67               36              0.62         50.17           47.71                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           93.33               15            1.06              0.77        103.80                32.97         0.602            pass              0.544             31.5                           0.266               -1.24             -0.052                                 ok            True                  False
  MELI           93.33               30            1.15             13.53       1672.10                61.16         0.595            pass              0.560              3.9                           0.136                1.60              0.491                                 ok            True                  False
  NVDA           90.00               30            0.91              1.40        218.91                44.83         0.515            pass              0.614             54.0                           0.584                1.07             -0.013                                 ok            True                  False
  INSM           72.00               25            2.16              1.66        108.82               111.27         0.734            pass              0.246             24.3                           0.369                5.73              0.008                                 ok           False                  False
  SHOP           84.09               44            0.05              0.04        104.84                78.48         0.617            pass              0.647             91.9                           0.491               -5.07              0.132                                 ok           False                  False
   TRI           80.95               21            0.51              0.30         85.43                54.99         0.603            pass              0.375             72.1                           0.315               -7.72             -0.298 downtrend_blocked_slope_and_streak           False                  False
   WMT           93.33               15            1.15              0.97        120.92                34.61         0.576            pass              0.575             42.8                           0.579               -8.03             -0.510            downtrend_blocked_slope           False                  False
  REGN           92.00               25            1.20              5.39        640.28                49.06         0.561            pass              0.689             71.1                           0.425              -11.06             -1.547 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.17             15.92       1043.63                22.19         0.518            pass              0.081              9.6                           0.315                1.88              0.536                                 ok           False                  False
  MSTR           90.91               33            1.97              2.27        163.88                63.46         0.491 below_threshold              0.615             40.6                           0.614              -13.85             -1.843            downtrend_blocked_slope           False                  False
  ODFL           85.37               41            0.33              0.48        207.48                44.32         0.473 below_threshold              0.615             74.7                           0.438                4.37              0.841                                 ok           False                  False
  PYPL           88.89               45            0.06              0.02         44.29                33.02         0.462 below_threshold              0.740             85.7                           0.456               -2.41             -0.309 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522112006)

</details>
