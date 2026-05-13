# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 13:30:04 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$32,973.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-630.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12780.0         44.7           42.6      510.62        502.79          -630.0                   -4.7         97.14               35               0.5         52.16           56.85                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.33               12            5.08              3.02         83.70               115.69         0.596          pass              0.192             10.0                           0.143               14.46              1.315                                 ok            True                  False
  SNPS           95.65               23            2.03              7.30        510.08                43.23         0.541          pass              0.554              4.5                           0.148                4.48              0.643                                 ok            True                  False
  MDLZ           82.35               17            1.15              0.50         61.49                23.07         0.530          pass              0.231             22.8                           0.318               -0.08              0.018                                 ok            True                  False
  CDNS           95.83               24            1.84              4.61        356.06                38.69         0.525          pass              0.600             18.0                           0.208                6.52              0.844                                 ok            True                  False
  CHTR           81.82               22            2.06              2.14        147.00               118.13         0.785          pass              0.343             45.2                           0.736               -8.69             -1.331            downtrend_blocked_slope           False                  False
 CMCSA           94.12               34            0.16              0.03         24.89                62.10         0.668          pass              0.871             89.2                           0.777               -7.10             -0.984 downtrend_blocked_slope_and_streak           False                  False
  ORLY           77.78                9            2.08              1.34         91.27                35.45         0.550          pass              0.165             36.8                           0.561               -1.92             -0.554 downtrend_blocked_slope_and_streak           False                  False
  GEHC           78.72               47            0.11              0.05         62.27                57.10         0.544          pass              0.538             94.5                           0.678                4.60              0.396                                 ok           False                  False
   PEP           90.00               10            1.59              1.69        151.13                21.96         0.533          pass              0.347              8.9                           0.308               -3.77             -0.465            downtrend_blocked_slope           False                  False
  MSFT           83.33               24            0.93              2.66        406.63                32.80         0.531          pass              0.366             43.6                           0.396               -4.83             -0.210           downtrend_blocked_streak           False                  False
  SHOP           84.62               13            4.19              2.93         98.59                84.62         0.531          pass              0.197              0.2                           0.058              -21.11             -2.607 downtrend_blocked_slope_and_streak           False                  False
  PYPL           90.32               31            0.69              0.22         45.35                37.98         0.527          pass              0.657             63.2                           0.517              -11.42             -1.412 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513133004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513133004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513133004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513133004)

</details>
