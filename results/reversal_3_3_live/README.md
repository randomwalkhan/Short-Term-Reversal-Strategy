# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 14:30:07 EDT`
Last processed slot: `manage_1430`

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
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12780.0         44.7           42.6      510.62        507.27          -630.0                   -4.7         97.14               35               0.5         52.16            52.7                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           85.71               14            4.79              2.85         83.78               115.69         0.604          pass              0.285             15.2                           0.359               14.81              1.329                                 ok            True                  False
  SNPS           96.97               33            1.16              4.16        511.43                43.23         0.527          pass              0.743             45.6                           0.714                5.41              0.684                                 ok            True                  False
  MDLZ           84.21               19            1.03              0.44         61.51                23.07         0.527          pass              0.318             31.0                           0.288                0.04              0.023                                 ok            True                  False
  MSTR           90.32               31            2.03              2.62        183.30                75.69         0.517          pass              0.640             57.7                           0.751               14.22              1.276                                 ok            True                  False
  CDNS           96.55               29            1.44              3.60        356.50                38.69         0.516          pass              0.687             36.1                           0.433                6.96              0.862                                 ok            True                  False
  CHTR           77.78                9            4.03              4.17        146.13               118.13         0.753          pass              0.079              1.1                           0.133              -10.52             -1.423            downtrend_blocked_slope           False                  False
 CMCSA           93.94               33            0.22              0.04         24.88                62.10         0.670          pass              0.847             85.1                           0.602               -7.16             -0.986 downtrend_blocked_slope_and_streak           False                  False
  GEHC           77.27               44            0.26              0.11         62.24                57.10         0.552          pass              0.518             87.5                           0.601                4.45              0.390                                 ok           False                  False
  ORLY           77.78                9            2.05              1.32         91.28                35.45         0.552          pass              0.168             37.7                           0.461               -1.89             -0.552 downtrend_blocked_slope_and_streak           False                  False
   ADP          100.00                9            2.61              3.91        212.13                33.54         0.535          pass              0.572             39.6                           0.762               -3.18             -0.118                                 ok           False                  False
   PEP           85.71                7            1.88              2.00        150.99                21.96         0.528          pass              0.207              0.7                           0.059               -4.05             -0.478            downtrend_blocked_slope           False                  False
  MELI           88.46               26            1.69             18.72       1570.76                57.67         0.523          pass              0.589             68.1                           0.657              -12.17             -1.687            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513143007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513143007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513143007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513143007)

</details>
