# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 13:00:06 EDT`
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
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12765.0         44.7          42.55      510.62        503.96          -645.0                  -4.81         97.14               35               0.5         52.16           55.76                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               18            4.39              2.61         83.88               115.69         0.607          pass              0.418             22.3                           0.434               15.29              1.348                                 ok            True                  False
  SNPS           96.00               25            1.80              6.47        510.44                43.23         0.542          pass              0.581              9.0                           0.166                4.73              0.654                                 ok            True                  False
  MDLZ           82.35               17            1.15              0.50         61.49                23.07         0.530          pass              0.231             22.8                           0.389               -0.08              0.018                                 ok            True                  False
  CDNS           96.00               25            1.76              4.42        356.15                38.69         0.523          pass              0.617             21.5                           0.210                6.60              0.847                                 ok            True                  False
  CHTR           66.67               12            3.29              3.41        146.46               118.13         0.761          pass              0.127             12.6                           0.254               -9.83             -1.389            downtrend_blocked_slope           False                  False
 CMCSA           91.30               23            0.66              0.12         24.85                62.10         0.697          pass              0.624             55.4                           0.440               -7.57             -1.007 downtrend_blocked_slope_and_streak           False                  False
  SHOP           80.00               20            2.86              2.00         98.98                84.62         0.557          pass              0.218             31.7                           0.500              -20.02             -2.545 downtrend_blocked_slope_and_streak           False                  False
  ORLY           83.33                6            2.53              1.62         91.14                35.45         0.553          pass              0.214             23.2                           0.329               -2.37             -0.575 downtrend_blocked_slope_and_streak           False                  False
  GEHC           77.78               45            0.18              0.08         62.26                57.10         0.550          pass              0.528             91.0                           0.788                4.52              0.393                                 ok           False                  False
   PEP           90.00               10            1.67              1.77        151.09                21.96         0.530          pass              0.324              1.6                           0.205               -3.84             -0.468            downtrend_blocked_slope           False                  False
  MELI           88.46               26            1.71             18.89       1570.68                57.67         0.522          pass              0.588             67.8                           0.761              -12.18             -1.687            downtrend_blocked_slope           False                  False
  TMUS           84.62               26            1.20              1.62        192.61                36.44         0.521          pass              0.315             11.2                           0.165               -3.62             -0.290            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513130006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513130006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513130006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513130006)

</details>
