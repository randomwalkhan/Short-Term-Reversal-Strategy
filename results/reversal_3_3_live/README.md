# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:45:04 EDT`
Last processed slot: `early_entry_1145`

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
- Equity: `$28,207.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-110.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12030.0        30.35          30.08      415.18        413.58          bid_ask_mid                      30.08                bid_ask_mid                    True          -110.0                  -0.91         91.67               36              0.62         50.17           50.58                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           93.75               16            1.00              0.73        103.82                32.97         0.600            pass              0.573             35.4                           0.382               -1.18             -0.049                                 ok            True                  False
  MELI           93.75               32            1.09             12.77       1672.43                61.16         0.586            pass              0.622             16.7                           0.262                1.66              0.494                                 ok            True                  False
   WDC           94.29               35            1.07              3.65        484.89                59.01         0.526            pass              0.702             34.0                           0.230                0.26             -0.574                                 ok            True                  False
  NVDA           89.29               28            1.03              1.58        218.83                44.83         0.520            pass              0.564             48.3                           0.489                0.96             -0.018                                 ok            True                  False
  INSM           69.23               26            1.85              1.42        108.92               111.27         0.741            pass              0.286             35.1                           0.542                6.07              0.023                                 ok           False                  False
   STX           94.87               39            0.41              2.35        809.45                68.63         0.574            pass              0.852             68.4                           0.366                3.13             -0.439                                 ok           False                  False
  REGN           93.10               29            0.94              4.21        640.79                49.06         0.553            pass              0.764             77.4                           0.534              -10.82             -1.535 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            1.86             13.67       1044.59                22.19         0.537            pass              0.121             22.4                           0.484                2.19              0.550                                 ok           False                  False
   WMT           92.00               25            0.75              0.64        121.07                34.61         0.532            pass              0.661             62.6                           0.765               -7.67             -0.491            downtrend_blocked_slope           False                  False
 GOOGL           90.70               43            0.06              0.15        387.59                41.05         0.512            pass              0.819             94.0                           0.618               -3.33             -0.231                                 ok           False                  False
  MSTR           90.91               33            1.95              2.25        163.88                63.46         0.492 below_threshold              0.616             40.9                           0.470              -13.84             -1.842            downtrend_blocked_slope           False                  False
  AVGO           90.48               42            0.25              0.71        414.26                40.36         0.487 below_threshold              0.758             76.6                           0.550               -3.83             -0.372            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:45:04.354154-04:00 early_entry_1145 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:35:01.410809-04:00 early_entry_1135 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522114504)

</details>
