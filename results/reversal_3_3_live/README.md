# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 16:00:05 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$33,483.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-120.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13290.0         44.7           44.3      510.62         500.1          -120.0                  -0.89         97.14               35               0.5         52.16           53.31                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               11            5.16              3.07         83.68               115.69         0.595          pass              0.140              8.5                           0.188               14.36              1.311                                 ok            True                  False
   ADP          100.00               10            2.39              3.58        212.27                33.54         0.540          pass              0.588             44.6                           0.509               -2.96             -0.108                                 ok            True                  False
  SNPS           97.14               35            0.76              2.74        512.03                43.23         0.535          pass              0.813             64.1                           0.582                5.83              0.702                                 ok            True                   True
  CDNS           97.06               34            0.98              2.45        356.99                38.69         0.511          pass              0.780             56.5                           0.527                7.45              0.884                                 ok            True                  False
  CHTR           66.67               12            3.33              3.44        146.44               118.13         0.756          pass              0.149             20.1                           0.463               -9.86             -1.390            downtrend_blocked_slope           False                  False
  INTC          100.00               38            0.29              0.24        120.51               109.00         0.662          pass              0.928             91.7                           0.434               26.92              3.181                                 ok           False                  False
  GEHC           73.68               38            0.63              0.27         62.17                57.10         0.561          pass              0.451             69.5                           0.523                4.06              0.373                                 ok           False                  False
  ORLY           85.71                7            2.33              1.50         91.20                35.45         0.561          pass              0.296             29.1                           0.291               -2.17             -0.566 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.89                9            1.71              1.81        151.07                21.96         0.529          pass              0.321             10.4                           0.190               -3.88             -0.470            downtrend_blocked_slope           False                  False
  MELI           90.91               33            1.06             11.67       1573.78                57.67         0.522          pass              0.737             80.1                           0.754              -11.60             -1.657            downtrend_blocked_slope           False                  False
  TMUS           80.95               21            1.59              2.15        192.38                36.44         0.521          pass              0.167              5.2                           0.181               -4.01             -0.308            downtrend_blocked_slope           False                  False
  PYPL           91.43               35            0.46              0.15         45.38                37.98         0.518          pass              0.750             75.4                           0.461              -11.21             -1.401 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T15:10:06.837461-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:05:03.914074-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513160005)

</details>
