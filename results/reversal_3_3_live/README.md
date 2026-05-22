# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:00:04 EDT`
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
- Equity: `$27,637.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-680.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11460.0        30.35          28.65      415.18        413.69          bid_ask_mid                      28.65                bid_ask_mid                    True          -680.0                   -5.6         91.67               36              0.62         50.17            49.0                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.59               37            0.66              7.81       1674.55                61.16         0.587          pass              0.677             16.3                           0.256                2.10              0.514                                 ok            True                  False
  SBUX           94.74               19            0.93              0.68        103.84                32.97         0.586          pass              0.631             39.8                           0.472               -1.11             -0.046                                 ok            True                  False
  NVDA           90.00               30            0.89              1.37        218.92                44.83         0.516          pass              0.616             54.9                           0.626                1.09             -0.012                                 ok            True                  False
  INSM           70.83               24            2.41              1.85        108.74               111.27         0.728          pass              0.180              4.5                           0.090                5.46             -0.003                                 ok           False                  False
  SHOP           84.09               44            0.23              0.17        104.79                78.48         0.609          pass              0.370              0.0                           0.201               -5.24              0.123                                 ok           False                  False
   TRI           80.00               20            0.64              0.38         85.40                54.99         0.600          pass              0.321             64.7                           0.282               -7.84             -0.304 downtrend_blocked_slope_and_streak           False                  False
   WMT           91.67               12            1.29              1.09        120.87                34.61         0.585          pass              0.490             35.8                           0.495               -8.17             -0.516            downtrend_blocked_slope           False                  False
  GEHC           75.00               40            0.27              0.12         64.28                59.89         0.577          pass              0.394             45.3                           0.206                1.08              0.259                                 ok           False                  False
  REGN           92.59               27            1.05              4.73        640.56                49.06         0.558          pass              0.729             74.6                           0.427              -10.93             -1.541 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            2.04             15.01       1044.02                22.19         0.526          pass              0.094             13.8                           0.377                2.00              0.542                                 ok           False                  False
 GOOGL           90.70               43            0.04              0.10        387.62                41.05         0.513          pass              0.825             96.2                           0.841               -3.31             -0.230                                 ok           False                  False
  CHTR           76.47               17            2.53              2.64        147.77               115.38         0.506          pass              0.107              3.2                           0.123               -6.28             -0.379            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522110004)

</details>
