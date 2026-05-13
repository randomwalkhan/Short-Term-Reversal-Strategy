# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 15:00:02 EDT`
Last processed slot: `entry_1500`

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
- Equity: `$33,333.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-270.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13140.0         44.7           43.8      510.62        506.38          -270.0                  -2.01         97.14               35               0.5         52.16           55.24                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               18            4.41              2.62         83.88               115.69         0.606          pass              0.417             22.0                           0.394               15.27              1.347                                 ok            True                  False
  SNPS           96.67               30            1.33              4.78        511.16                43.23         0.535          pass              0.699             37.5                           0.455                5.23              0.676                                 ok            True                  False
   ADP           92.31               13            2.06              3.08        212.49                33.54         0.527          pass              0.558             52.5                           0.747               -2.62             -0.092                                 ok            True                  False
  CDNS           96.30               27            1.65              4.14        356.27                38.69         0.517          pass              0.644             26.4                           0.282                6.72              0.852                                 ok            True                  False
  MSTR           90.00               30            2.42              3.12        183.08                75.69         0.500          pass              0.599             49.6                           0.522               13.76              1.258                                 ok            True                  False
  CHTR           70.00               10            3.83              3.96        146.22               118.13         0.748          pass              0.095              6.8                           0.234              -10.33             -1.414            downtrend_blocked_slope           False                  False
  GEHC           75.00               40            0.48              0.21         62.20                57.10         0.559          pass              0.486             76.6                           0.539                4.21              0.380                                 ok           False                  False
  ORLY           72.73               11            1.92              1.23         91.31                35.45         0.539          pass              0.186             41.7                           0.543               -1.76             -0.546 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               10            1.58              1.68        151.13                21.96         0.532          pass              0.371             17.0                           0.451               -3.76             -0.464            downtrend_blocked_slope           False                  False
  MELI           88.89               27            1.55             17.13       1571.44                57.67         0.526          pass              0.615             70.8                           0.666              -12.04             -1.680            downtrend_blocked_slope           False                  False
  TMUS           84.00               25            1.27              1.71        192.57                36.44         0.519          pass              0.328             23.2                           0.433               -3.69             -0.294            downtrend_blocked_slope           False                  False
  ODFL           78.57               28            1.03              1.37        190.53                44.00         0.516          pass              0.300             42.7                           0.384               -9.64             -0.924            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513150002)

</details>
