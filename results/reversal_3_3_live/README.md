# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 14:50:09 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$2,402.75`
- Equity: `$27,907.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-410.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   0     38     13775.0                 13775.0         3.62           3.62      103.16        103.16          bid_ask_mid                       3.62                bid_ask_mid                    True             0.0                   0.00         94.74               19              0.93         28.13           28.13                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11730.0        30.35          29.32      415.18        412.68          bid_ask_mid                      29.32                bid_ask_mid                    True          -410.0                  -3.38         91.67               36              0.62         50.17           50.16                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           94.74               19            0.93              0.68        103.84                32.97         0.584            pass              0.644             44.3                           0.626               -1.11             -0.046                                 ok            True                  False
  MELI           94.59               37            0.71              8.36       1674.32                61.16         0.573            pass              0.798             57.0                           0.485                2.05              0.511                                 ok            True                  False
  NVDA           85.71               21            1.71              2.63        218.38                44.83         0.519            pass              0.319             13.8                           0.242                0.26             -0.050                                 ok            True                  False
  INSM           69.23               26            1.81              1.39        108.94               111.27         0.743            pass              0.291             36.7                           0.444                6.12              0.025                                 ok           False                  False
   WMT           93.33               15            1.16              0.99        120.92                34.61         0.575            pass              0.572             42.0                           0.354               -8.05             -0.510            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.08              0.04         64.31                59.89         0.570            pass              0.521             88.1                           0.539                1.28              0.268                                 ok           False                  False
  REGN           92.86               28            1.02              4.60        640.62                49.06         0.553            pass              0.744             75.3                           0.570              -10.90             -1.539 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           87.10               31            0.81              2.20        386.72                41.05         0.540            pass              0.427             14.7                           0.265               -4.06             -0.265            downtrend_blocked_slope           False                  False
    EA           85.71               14            0.36              0.51        201.65                 2.73         0.537            pass              0.398             54.9                           0.344                0.35              0.080                                 ok           False                  False
  GOOG           87.88               33            0.73              1.95        382.63                40.91         0.535            pass              0.451             11.3                           0.249               -4.12             -0.290 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.12             15.60       1043.77                22.19         0.521            pass              0.087             11.5                           0.214                1.92              0.538                                 ok           False                  False
  AVGO           89.47               38            0.49              1.41        413.96                40.36         0.497 below_threshold              0.650             53.7                           0.392               -4.06             -0.383            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-22T14:50:09.909553-04:00       entry_1500          entry {"allocated_cash": 13775.0, "asset_type": "option", "contract_symbol": "SBUX260717C00105000", "contracts": 38, "early_entry_score": 0.644, "entry_mode": "regular", "entry_option_price": 3.625, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2147.0, "option_spread_pct": 6.9, "option_volume": 78.0, "success_rate": 94.74, "ticker": "SBUX", "timing_score": 0.584}
2026-05-22T14:50:09.909553-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-22", "training_samples": 5081, "window": 5}
2026-05-22T12:00:04.237005-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:55:01.324366-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:50:01.298135-04:00 early_entry_1150  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:35:01.410809-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522145009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522145009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522145009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522145009)

</details>
