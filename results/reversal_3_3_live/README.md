# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 09:35:06 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$65,704.80`
- Equity: `$130,714.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$1,980.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 65010.0         19.1           19.7       273.7        273.65     last_price_stale                        NaN                unavailable                   False          1980.0                   3.14         81.25               16              2.09         51.04             0.0                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           88.46               26            0.96              4.93        734.61                55.08         0.598            pass              0.392              0.0                           0.192                0.22              0.108                                 ok            True                  False
  SNPS           86.84               38            0.45              1.48        467.48                53.97         0.559            pass              0.595             56.8                           0.344               -4.88             -0.543 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.10               42            0.17              0.34        274.86                60.14         0.540            pass              0.709             79.7                           0.502                6.61              0.198                                 ok           False                  False
  CSCO           91.30               23            0.84              0.64        109.57                35.07         0.537            pass              0.511             23.0                           0.269               -2.91             -0.365 downtrend_blocked_slope_and_streak           False                  False
  QCOM           83.33               24            2.12              2.65        177.27                54.84         0.513            pass              0.318             28.3                           0.368               -5.54             -0.448 downtrend_blocked_slope_and_streak           False                  False
  ALNY           85.42               48            0.06              0.09        233.99                44.37         0.498 below_threshold              0.677             94.3                           0.502                6.45              0.523                                 ok           False                  False
   APP           84.44               45            0.46              0.90        278.91                54.48         0.496 below_threshold              0.514             48.6                           0.386                3.65             -0.129                                 ok           False                  False
  INTC           86.67               30            2.18              1.45         94.75                62.72         0.490 below_threshold              0.360              0.0                           0.227              -21.82             -2.434            downtrend_blocked_slope           False                  False
  MCHP           88.46               26            1.49              0.78         73.93                41.20         0.489 below_threshold              0.483             33.9                           0.379              -10.05             -1.290            downtrend_blocked_slope           False                  False
  UPRO           86.84               38            0.01              0.01        151.55                28.58         0.488 below_threshold              0.418              0.0                           0.298                0.44             -0.128                                 ok           False                  False
  MPWR           72.22               18            2.84             24.85       1238.55                56.34         0.486 below_threshold              0.127              8.5                           0.091              -15.70             -2.032            downtrend_blocked_slope           False                  False
  CDNS           85.71               42            0.10              0.22        324.28                38.31         0.475 below_threshold              0.672             90.5                           0.609               -7.77             -1.035 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-16T00:00:05.052179-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 91, 'empty': 2}
2026-10-15T15:10:06.431411-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T15:05:05.112020-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T15:00:05.139552-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T14:55:07.089564-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-15T14:50:07.219015-04:00       entry_1500              entry {"allocated_cash": 63030.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 33, "early_entry_score": 0.282, "entry_mode": "regular", "entry_option_price": 19.1, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 446.0, "option_spread_pct": 5.24, "option_volume": 21.0, "success_rate": 81.25, "ticker": "CEG", "timing_score": 0.554}
2026-10-15T14:50:07.219015-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-15", "training_samples": 6074, "window": 5}
2026-10-15T12:00:06.622764-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:55:05.998701-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:50:06.396498-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016093506)

</details>
