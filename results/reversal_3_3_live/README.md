# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 13:40:08 EDT`
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
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12780.0         44.7           42.6      510.62        502.57          -630.0                   -4.7         97.14               35               0.5         52.16           57.13                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               11            5.20              3.09         83.67               115.69         0.593          pass              0.138              7.9                           0.104               14.31              1.309                                 ok            True                  False
  SNPS           95.00               20            2.07              7.45        510.02                43.23         0.555          pass              0.530              2.6                           0.139                4.44              0.641                                 ok            True                  False
  CDNS           96.15               26            1.71              4.29        356.20                38.69         0.520          pass              0.630             23.7                           0.309                6.65              0.850                                 ok            True                  False
  MDLZ           86.36               22            0.89              0.38         61.54                23.07         0.518          pass              0.422             40.2                           0.479                0.18              0.030                                 ok            True                  False
  MSTR           90.00               30            2.42              3.13        183.08                75.69         0.500          pass              0.598             49.5                           0.672               13.76              1.257                                 ok            True                  False
  CHTR           81.82               22            2.04              2.11        147.01               118.13         0.786          pass              0.344             45.8                           0.702               -8.67             -1.330            downtrend_blocked_slope           False                  False
 CMCSA           94.29               35            0.12              0.02         24.89                62.10         0.665          pass              0.890             91.9                           0.724               -7.06             -0.982 downtrend_blocked_slope_and_streak           False                  False
  ORLY           77.78                9            1.96              1.26         91.30                35.45         0.556          pass              0.177             40.4                           0.665               -1.80             -0.548 downtrend_blocked_slope_and_streak           False                  False
  GEHC           78.72               47            0.11              0.05         62.27                57.10         0.544          pass              0.538             94.5                           0.646                4.60              0.396                                 ok           False                  False
   PEP           90.00               10            1.54              1.64        151.15                21.96         0.535          pass              0.355             11.7                           0.390               -3.72             -0.463            downtrend_blocked_slope           False                  False
  MSFT           83.33               24            0.95              2.72        406.60                32.80         0.530          pass              0.362             42.3                           0.372               -4.85             -0.211           downtrend_blocked_streak           False                  False
  MELI           88.89               27            1.57             17.32       1571.36                57.67         0.525          pass              0.614             70.5                           0.715              -12.05             -1.681            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513134008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513134008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513134008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513134008)

</details>
