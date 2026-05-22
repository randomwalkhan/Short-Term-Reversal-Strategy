# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 15:20:09 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$28,702.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$385.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   0     38     13775.0                 14630.0         3.62           3.85      103.16        103.25          bid_ask_mid                       3.85                bid_ask_mid                    True           855.0                   6.21         94.74               19              0.93         28.13           29.19                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11670.0        30.35          29.18      415.18        412.20          bid_ask_mid                      29.18                bid_ask_mid                    True          -470.0                  -3.87         91.67               36              0.62         50.17           50.18                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.00               20            0.85              0.62        103.87                32.97         0.583          pass              0.673             49.4                           0.577               -1.02             -0.042                                 ok            True                  False
  MELI           94.44               36            0.78              9.13       1673.99                61.16         0.576          pass              0.775             53.0                           0.381                1.98              0.508                                 ok            True                  False
  NVDA           82.35               17            1.97              3.02        218.21                44.83         0.524          pass              0.183              7.1                           0.212               -0.00             -0.062                                 ok            True                  False
   WBD           80.00               20            0.55              0.10         27.06                 9.31         0.506          pass              0.117              0.0                           0.187               -0.59             -0.035                                 ok            True                  False
  INSM           70.83               24            2.40              1.84        108.74               111.27         0.725          pass              0.214             16.1                           0.184                5.48             -0.002                                 ok           False                  False
  SHOP           84.09               44            0.30              0.22        104.77                78.48         0.601          pass              0.519             49.9                           0.259               -5.31              0.120                                 ok           False                  False
   WMT           93.75               16            1.05              0.90        120.96                34.61         0.576          pass              0.606             47.3                           0.526               -7.95             -0.505            downtrend_blocked_slope           False                  False
  GEHC           76.74               43            0.12              0.05         64.31                59.89         0.567          pass              0.503             82.2                           0.511                1.24              0.266                                 ok           False                  False
 GOOGL           84.00               25            1.15              3.13        386.32                41.05         0.552          pass              0.274              4.1                           0.125               -4.39             -0.281            downtrend_blocked_slope           False                  False
  REGN           93.10               29            1.00              4.50        640.66                49.06         0.548          pass              0.758             75.8                           0.578              -10.88             -1.538 downtrend_blocked_slope_and_streak           False                  False
  GOOG           85.71               28            1.03              2.77        382.28                40.91         0.544          pass              0.345              6.1                           0.166               -4.42             -0.304 downtrend_blocked_slope_and_streak           False                  False
    EA           83.33               12            0.43              0.61        201.61                 2.73         0.543          pass              0.295             46.3                           0.343                0.28              0.077                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-22T15:10:09.874412-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T15:05:09.997978-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T15:00:10.044120-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T14:55:09.944950-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T14:50:09.909553-04:00       entry_1500          entry {"allocated_cash": 13775.0, "asset_type": "option", "contract_symbol": "SBUX260717C00105000", "contracts": 38, "early_entry_score": 0.644, "entry_mode": "regular", "entry_option_price": 3.625, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2147.0, "option_spread_pct": 6.9, "option_volume": 78.0, "success_rate": 94.74, "ticker": "SBUX", "timing_score": 0.584}
2026-05-22T14:50:09.909553-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-22", "training_samples": 5081, "window": 5}
2026-05-22T12:00:04.237005-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:55:01.324366-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:50:01.298135-04:00 early_entry_1150  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522152009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522152009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522152009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522152009)

</details>
