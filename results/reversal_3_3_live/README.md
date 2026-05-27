# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 12:55:02 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,115.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-470.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11540.0        60.05           57.7       531.8        526.54          bid_ask_mid                       57.7                bid_ask_mid                    True          -470.0                  -3.91         97.22               36              0.52         54.56           55.95                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.24               21            3.41              2.95        122.26                91.80         0.571          pass              0.635             34.8                           0.472               -1.08              0.380                                 ok            True                  False
  ASML           88.89               27            2.04             23.35       1622.02                54.27         0.501          pass              0.496             32.0                           0.363                5.11              0.576                                 ok            True                  False
  INSM           70.37               27            2.10              1.60        108.18               110.60         0.719          pass              0.242             18.8                           0.353               -8.12             -0.895            downtrend_blocked_slope           False                  False
  NXPI           89.74               39            0.22              0.52        332.45                92.16         0.642          pass              0.780             87.5                           0.794               12.81              1.247                                 ok           False                  False
   AEP           66.67               12            0.71              0.65        130.62                25.21         0.606          pass              0.188             38.0                           0.261               -1.49              0.149                                 ok           False                  False
  REGN           86.67               30            0.85              3.79        632.99                48.91         0.583          pass              0.500             43.7                           0.414              -12.89             -1.494 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.83               24            0.21              0.14         94.74                30.13         0.576          pass              0.744             64.3                           0.376                2.25              0.590                                 ok           False                  False
  FTNT          100.00                5            4.38              4.11        132.20                66.88         0.573          pass              0.536             26.3                           0.279               12.49              1.384                                 ok           False                  False
  GEHC           73.53               34            0.86              0.39         64.01                58.90         0.565          pass              0.321             34.7                           0.467                2.14              0.439                                 ok           False                  False
  ORLY           73.33               15            1.59              1.00         89.44                38.82         0.553          pass              0.124             11.6                           0.247               -3.70             -0.021                                 ok           False                  False
  NVDA           85.71               21            1.59              2.40        213.83                40.94         0.514          pass              0.408             43.7                           0.634               -4.23             -0.667 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.44               36            0.21              0.21        145.77                30.88         0.510          pass              0.839             76.6                           0.640                4.32              0.289                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T12:00:02.710964-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527125502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527125502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527125502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527125502)

</details>
