# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 12:50:07 EDT`
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
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12765.0         44.7          42.55      510.62        503.88          -645.0                  -4.81         97.14               35               0.5         52.16           55.87                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               18            4.35              2.59         83.89               115.69         0.609          pass              0.420             22.9                           0.422               15.34              1.349                                 ok            True                  False
  SNPS           96.00               25            1.82              6.53        510.41                43.23         0.542          pass              0.579              8.1                           0.220                4.71              0.653                                 ok            True                  False
   CSX           87.50               32            0.56              0.18         44.45                30.18         0.528          pass              0.456             18.9                           0.177               -0.90             -0.142                                 ok            True                  False
  MDLZ           83.33               18            1.09              0.47         61.50                23.07         0.528          pass              0.276             26.8                           0.466               -0.02              0.020                                 ok            True                  False
  CDNS           96.30               27            1.60              4.02        356.32                38.69         0.520          pass              0.651             28.6                           0.256                6.77              0.855                                 ok            True                  False
  CHTR           71.43               14            2.96              3.07        146.61               118.13         0.772          pass              0.168             21.4                           0.334               -9.52             -1.373            downtrend_blocked_slope           False                  False
 CMCSA           93.10               29            0.45              0.08         24.87                62.10         0.678          pass              0.753             69.7                           0.543               -7.37             -0.997 downtrend_blocked_slope_and_streak           False                  False
  SHOP           78.95               19            2.90              2.03         98.97                84.62         0.559          pass              0.208             30.8                           0.449              -20.06             -2.546 downtrend_blocked_slope_and_streak           False                  False
  MELI           84.62               13            2.50             27.62       1566.94                57.67         0.548          pass              0.357             52.9                           0.645              -12.89             -1.724            downtrend_blocked_slope           False                  False
  ORLY           75.00                4            2.64              1.69         91.11                35.45         0.547          pass              0.114             19.9                           0.275               -2.48             -0.580 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               11            1.51              1.60        151.16                21.96         0.533          pass              0.384             10.9                           0.317               -3.69             -0.461            downtrend_blocked_slope           False                  False
   ADP          100.00                2            3.69              5.53        211.44                33.54         0.529          pass              0.474              7.2                           0.089               -4.25             -0.169                                 ok           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513125007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513125007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513125007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513125007)

</details>
