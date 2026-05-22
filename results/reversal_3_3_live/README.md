# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:50:01 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$28,367.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12190.0        30.35          30.48      415.18        413.51          bid_ask_mid                      30.48                bid_ask_mid                    True            50.0                   0.41         91.67               36              0.62         50.17           51.13                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           93.75               16            0.99              0.72        103.82                32.97         0.601            pass              0.575             36.0                           0.383               -1.17             -0.049                                 ok            True                  False
  MELI           93.94               33            1.07             12.54       1672.53                61.16         0.580            pass              0.638             18.2                           0.304                1.68              0.495                                 ok            True                  False
   WDC           93.75               32            1.27              4.32        484.61                59.01         0.533            pass              0.633             22.0                           0.147                0.06             -0.583                                 ok            True                  False
  NVDA           89.29               28            1.16              1.79        218.74                44.83         0.511            pass              0.543             41.3                           0.381                0.82             -0.025                                 ok            True                  False
  INSM           69.23               26            1.93              1.48        108.90               111.27         0.737            pass              0.278             32.6                           0.520                5.99              0.019                                 ok           False                  False
   STX           94.87               39            0.44              2.52        809.38                68.63         0.572            pass              0.845             66.0                           0.323                3.10             -0.440                                 ok           False                  False
  REGN           93.10               29            1.00              4.51        640.66                49.06         0.548            pass              0.758             75.8                           0.551              -10.88             -1.538 downtrend_blocked_slope_and_streak           False                  False
   WMT           90.48               21            0.91              0.77        121.01                34.61         0.546            pass              0.571             54.5                           0.674               -7.82             -0.499            downtrend_blocked_slope           False                  False
  COST           80.00                5            1.86             13.70       1044.58                22.19         0.537            pass              0.120             22.3                           0.501                2.19              0.550                                 ok           False                  False
 GOOGL           90.48               42            0.21              0.57        387.42                41.05         0.509            pass              0.764             77.8                           0.555               -3.48             -0.238                                 ok           False                  False
  GOOG           88.64               44            0.12              0.32        383.33                40.91         0.500            pass              0.737             85.7                           0.569               -3.53             -0.262 downtrend_blocked_slope_and_streak           False                  False
  AVGO           90.00               40            0.33              0.95        414.16                40.36         0.495 below_threshold              0.723             68.8                           0.464               -3.90             -0.376            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:50:01.298135-04:00 early_entry_1150 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:35:01.410809-04:00 early_entry_1135 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522115001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522115001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522115001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522115001)

</details>
