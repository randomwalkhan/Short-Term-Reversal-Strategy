# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:05:02 EDT`
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
- Equity: `$27,707.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-610.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11530.0        30.35          28.83      415.18        414.08          bid_ask_mid                      28.83                bid_ask_mid                    True          -610.0                  -5.02         91.67               36              0.62         50.17           49.32                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.00               20            0.85              0.62        103.86                32.97         0.584            pass              0.660             45.0                           0.567               -1.03             -0.043                                 ok            True                  False
  MELI           94.59               37            0.72              8.44       1674.28                61.16         0.580            pass              0.719             30.7                           0.285                2.04              0.511                                 ok            True                  False
  NVDA           89.29               28            1.00              1.54        218.85                44.83         0.522            pass              0.568             49.4                           0.583                0.98             -0.017                                 ok            True                  False
  INSM           64.71               17            2.71              2.08        108.64               111.27         0.741            pass              0.121              0.0                           0.150                5.14             -0.017                                 ok           False                  False
   TRI           80.95               21            0.50              0.30         85.43                54.99         0.604            pass              0.377             72.8                           0.311               -7.71             -0.297 downtrend_blocked_slope_and_streak           False                  False
  SHOP           83.72               43            0.44              0.32        104.72                78.48         0.598            pass              0.417             19.3                           0.226               -5.44              0.114                                 ok           False                  False
   WMT           93.33               15            1.21              1.03        120.90                34.61         0.572            pass              0.565             39.5                           0.524               -8.10             -0.513            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.08              0.04         64.31                59.89         0.572            pass              0.510             84.4                           0.355                1.28              0.268                                 ok           False                  False
  REGN           92.31               26            1.15              5.16        640.38                49.06         0.558            pass              0.707             72.3                           0.415              -11.01             -1.545 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            1.82             13.38       1044.71                22.19         0.540            pass              0.124             23.2                           0.460                2.23              0.552                                 ok           False                  False
  MSTR           90.32               31            2.11              2.44        163.81                63.46         0.494 below_threshold              0.573             36.1                           0.447              -13.98             -1.850            downtrend_blocked_slope           False                  False
  AVGO           90.48               42            0.15              0.44        414.38                40.36         0.493 below_threshold              0.785             85.4                           0.673               -3.74             -0.368            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522110502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522110502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522110502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522110502)

</details>
