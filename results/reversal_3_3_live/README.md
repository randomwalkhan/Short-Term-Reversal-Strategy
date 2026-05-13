# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 13:10:07 EDT`
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
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 12765.0         44.7          42.55      510.62        503.41          -645.0                  -4.81         97.14               35               0.5         52.16           56.25                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           86.67               15            4.69              2.79         83.80               115.69         0.604          pass              0.322             16.9                           0.346               14.92              1.333                                 ok            True                  False
  SNPS           96.00               25            1.91              6.86        510.27                43.23         0.537          pass              0.564              3.5                           0.108                4.61              0.649                                 ok            True                  False
  MDLZ           83.33               18            1.05              0.46         61.50                23.07         0.530          pass              0.283             29.3                           0.405                0.02              0.022                                 ok            True                  False
  CDNS           96.00               25            1.81              4.54        356.09                38.69         0.521          pass              0.610             19.3                           0.179                6.55              0.845                                 ok            True                  False
  CHTR           76.47               17            2.61              2.71        146.76               118.13         0.778          pass              0.216             30.6                           0.492               -9.20             -1.357            downtrend_blocked_slope           False                  False
 CMCSA           93.94               33            0.20              0.03         24.89                62.10         0.671          pass              0.852             86.5                           0.715               -7.14             -0.986 downtrend_blocked_slope_and_streak           False                  False
  ORLY           87.50                8            2.26              1.46         91.22                35.45         0.561          pass              0.349             31.1                           0.451               -2.10             -0.563 downtrend_blocked_slope_and_streak           False                  False
  SHOP           86.67               15            3.51              2.45         98.79                84.62         0.560          pass              0.317             16.5                           0.229              -20.55             -2.575 downtrend_blocked_slope_and_streak           False                  False
  GEHC           78.72               47            0.06              0.03         62.28                57.10         0.547          pass              0.545             96.9                           0.778                4.65              0.399                                 ok           False                  False
   PEP           90.91               11            1.53              1.62        151.15                21.96         0.532          pass              0.388             12.5                           0.282               -3.71             -0.462            downtrend_blocked_slope           False                  False
  PYPL           90.00               30            0.78              0.25         45.33                37.98         0.528          pass              0.628             58.5                           0.422              -11.49             -1.416 downtrend_blocked_slope_and_streak           False                  False
  TMUS           84.62               26            1.21              1.63        192.60                36.44         0.520          pass              0.312             10.2                           0.198               -3.64             -0.291            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513131007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513131007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513131007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513131007)

</details>
