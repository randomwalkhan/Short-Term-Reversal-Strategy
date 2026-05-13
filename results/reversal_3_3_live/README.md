# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 12:55:08 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$32,958.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-645.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12765.0         44.7          42.55      510.62        503.79          -645.0                  -4.81         97.14               35               0.5         52.16           55.89                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               18            4.52              2.69         83.85               115.69         0.600          pass              0.410             20.0                           0.405               15.14              1.342                                 ok            True                  False
  SNPS           96.00               25            1.84              6.60        510.38                43.23         0.541          pass              0.576              7.2                           0.178                4.69              0.652                                 ok            True                  False
  MDLZ           83.33               18            1.09              0.47         61.50                23.07         0.529          pass              0.277             27.2                           0.440               -0.02              0.021                                 ok            True                  False
  CDNS           96.00               25            1.78              4.47        356.13                38.69         0.522          pass              0.614             20.6                           0.210                6.58              0.846                                 ok            True                  False
  MSTR           87.50               24            3.00              3.87        182.76                75.69         0.500          pass              0.456             37.5                           0.422               13.08              1.230                                 ok            True                  False
  CHTR           66.67               12            3.21              3.32        146.50               118.13         0.765          pass              0.134             14.9                           0.296               -9.75             -1.385            downtrend_blocked_slope           False                  False
 CMCSA           92.31               26            0.56              0.10         24.86                62.10         0.687          pass              0.690             62.2                           0.500               -7.47             -1.002 downtrend_blocked_slope_and_streak           False                  False
  SHOP           77.78               18            3.04              2.12         98.93                84.62         0.555          pass              0.192             27.6                           0.391              -20.17             -2.553 downtrend_blocked_slope_and_streak           False                  False
  ORLY           75.00                4            2.61              1.68         91.12                35.45         0.548          pass              0.116             20.5                           0.279               -2.45             -0.579 downtrend_blocked_slope_and_streak           False                  False
  GEHC           79.17               48            0.01              0.00         62.29                57.10         0.545          pass              0.553             99.6                           0.854                4.71              0.401                                 ok           False                  False
   PEP           90.00               10            1.55              1.65        151.14                21.96         0.535          pass              0.345              8.2                           0.277               -3.73             -0.463            downtrend_blocked_slope           False                  False
  TMUS           84.62               26            1.20              1.62        192.61                36.44         0.521          pass              0.315             11.2                           0.187               -3.62             -0.290            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-13T12:00:04.870227-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:00:06.549783-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:55:05.050603-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:50:03.713971-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:45:06.364119-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513125508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513125508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513125508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513125508)

</details>
