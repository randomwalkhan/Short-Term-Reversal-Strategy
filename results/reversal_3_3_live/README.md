# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 13:30:08 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$28,097.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-220.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11920.0        30.35           29.8      415.18        414.21          bid_ask_mid                       29.8                bid_ask_mid                    True          -220.0                  -1.81         91.67               36              0.62         50.17           50.17                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           92.31               13            1.28              0.93        103.73                32.97         0.600          pass              0.473             21.5                           0.358               -1.46             -0.062                                 ok            True                  False
  NVDA           87.88               33            0.76              1.17        219.01                44.83         0.501          pass              0.598             61.6                           0.720                1.23             -0.006                                 ok            True                  False
  INSM           72.00               25            2.20              1.69        108.81               111.27         0.732          pass              0.242             23.0                           0.342                5.69              0.007                                 ok           False                  False
  MELI           94.87               39            0.39              4.58       1675.94                61.16         0.581          pass              0.877             76.4                           0.725                2.38              0.526                                 ok           False                  False
   WMT           93.33               15            1.13              0.96        120.93                34.61         0.577          pass              0.577             43.6                           0.311               -8.02             -0.509            downtrend_blocked_slope           False                  False
  GEHC           75.00               40            0.26              0.12         64.28                59.89         0.575          pass              0.436             59.5                           0.373                1.09              0.260                                 ok           False                  False
  REGN           93.10               29            0.98              4.41        640.70                49.06         0.550          pass              0.760             76.3                           0.420              -10.86             -1.537 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.26              0.89        486.08                59.01         0.538          pass              0.905             83.9                           0.668                1.08             -0.537                                 ok           False                  False
  COST           80.00                5            2.04             14.97       1044.04                22.19         0.526          pass              0.098             15.1                           0.259                2.01              0.542                                 ok           False                  False
  MSTR           90.00               40            0.80              0.92        164.45                63.46         0.518          pass              0.746             75.8                           0.722              -12.83             -1.789            downtrend_blocked_slope           False                  False
  GOOG           90.24               41            0.30              0.81        383.12                40.91         0.511          pass              0.714             63.3                           0.392               -3.71             -0.270 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.00               40            0.38              1.04        387.21                41.05         0.510          pass              0.696             59.5                           0.401               -3.65             -0.245                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522133008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522133008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522133008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522133008)

</details>
