# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 14:55:09 EDT`
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
- Equity: `$28,237.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-80.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   0     38     13775.0                 14155.0         3.62           3.72      103.16        103.25          bid_ask_mid                       3.72                bid_ask_mid                    True           380.0                   2.76         94.74               19              0.93         28.13           28.60                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11680.0        30.35          29.20      415.18        413.28          bid_ask_mid                      29.20                bid_ask_mid                    True          -460.0                  -3.79         91.67               36              0.62         50.17           49.99                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.00               20            0.85              0.62        103.86                32.97         0.583            pass              0.672             49.1                           0.648               -1.03             -0.043                                 ok            True                  False
  MELI           94.44               36            0.76              8.96       1674.06                61.16         0.577            pass              0.778             53.9                           0.451                2.00              0.509                                 ok            True                  False
  NVDA           85.71               21            1.57              2.42        218.47                44.83         0.528            pass              0.341             20.7                           0.302                0.40             -0.043                                 ok            True                  False
  INSM           69.23               26            1.76              1.35        108.95               111.27         0.746            pass              0.296             38.3                           0.437                6.17              0.027                                 ok           False                  False
   WMT           93.33               15            1.14              0.97        120.93                34.61         0.577            pass              0.576             43.2                           0.391               -8.03             -0.509            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.08              0.04         64.31                59.89         0.570            pass              0.521             88.1                           0.512                1.28              0.268                                 ok           False                  False
  REGN           92.59               27            1.06              4.75        640.56                49.06         0.558            pass              0.728             74.5                           0.564              -10.93             -1.541 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           86.67               30            0.83              2.26        386.69                41.05         0.545            pass              0.403             12.4                           0.247               -4.08             -0.266            downtrend_blocked_slope           False                  False
    EA           84.62               13            0.39              0.55        201.63                 2.73         0.540            pass              0.350             51.1                           0.316                0.32              0.078                                 ok           False                  False
  GOOG           87.88               33            0.73              1.96        382.63                40.91         0.535            pass              0.450             11.0                           0.249               -4.13             -0.290 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.16             15.89       1043.64                22.19         0.518            pass              0.081              9.8                           0.190                1.88              0.536                                 ok           False                  False
  MSTR           90.32               31            2.10              2.43        163.81                63.46         0.495 below_threshold              0.574             36.3                           0.286              -13.97             -1.849            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-22T14:55:09.944950-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T14:50:09.909553-04:00       entry_1500          entry {"allocated_cash": 13775.0, "asset_type": "option", "contract_symbol": "SBUX260717C00105000", "contracts": 38, "early_entry_score": 0.644, "entry_mode": "regular", "entry_option_price": 3.625, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2147.0, "option_spread_pct": 6.9, "option_volume": 78.0, "success_rate": 94.74, "ticker": "SBUX", "timing_score": 0.584}
2026-05-22T14:50:09.909553-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-22", "training_samples": 5081, "window": 5}
2026-05-22T12:00:04.237005-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:55:01.324366-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:50:01.298135-04:00 early_entry_1150  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:35:01.410809-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522145509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522145509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522145509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522145509)

</details>
