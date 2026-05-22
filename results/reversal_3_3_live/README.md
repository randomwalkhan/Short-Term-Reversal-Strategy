# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 13:05:08 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$28,057.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-260.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11880.0        30.35           29.7      415.18        413.98          bid_ask_mid                       29.7                bid_ask_mid                    True          -260.0                  -2.14         91.67               36              0.62         50.17           50.12                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           92.31               13            1.34              0.98        103.71                32.97         0.596          pass              0.461             17.7                           0.259               -1.52             -0.065                                 ok            True                  False
  MELI           93.33               30            1.14             13.44       1672.14                61.16         0.591          pass              0.641             30.9                           0.397                1.60              0.492                                 ok            True                  False
  NVDA           90.00               30            0.91              1.39        218.91                44.83         0.515          pass              0.614             54.3                           0.496                1.08             -0.013                                 ok            True                  False
  INSM           72.00               25            2.11              1.62        108.84               111.27         0.736          pass              0.252             26.2                           0.300                5.79              0.011                                 ok           False                  False
   WMT           94.12               17            1.01              0.86        120.97                34.61         0.572          pass              0.629             49.4                           0.392               -7.91             -0.503            downtrend_blocked_slope           False                  False
  GEHC           75.00               40            0.34              0.15         64.26                59.89         0.572          pass              0.351             31.3                           0.206                1.01              0.256                                 ok           False                  False
  REGN           92.31               26            1.16              5.24        640.35                49.06         0.557          pass              0.706             71.9                           0.462              -11.03             -1.546 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.33              1.14        485.97                59.01         0.534          pass              0.892             79.5                           0.672                1.01             -0.540                                 ok           False                  False
  COST           80.00                5            1.96             14.43       1044.26                22.19         0.531          pass              0.107             18.1                           0.279                2.09              0.545                                 ok           False                  False
 GOOGL           89.47               38            0.42              1.15        387.17                41.05         0.521          pass              0.658             55.4                           0.462               -3.69             -0.247                                 ok           False                  False
  GOOG           90.24               41            0.28              0.76        383.14                40.91         0.512          pass              0.720             65.3                           0.495               -3.69             -0.270 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.89               36            1.43              1.65        164.14                63.46         0.502          pass              0.631             56.7                           0.575              -13.38             -1.818            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522130508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522130508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522130508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522130508)

</details>
