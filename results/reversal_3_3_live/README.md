# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 09:50:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.00               25            0.95              1.74        262.52                41.90         0.553          pass              0.532             54.3                           0.498               -1.43              0.041                                 ok            True                  False
  MPWR           85.19               27            1.55             14.84       1361.07                54.48         0.526          pass              0.483             59.6                           0.443               17.76              2.192                                 ok            True                  False
  SOXL           80.00               25            5.38              5.70        149.01               120.87         0.525          pass              0.253             33.5                           0.256               41.79              4.578                                 ok            True                  False
  UPRO           85.00               20            1.39              1.48        151.60                32.02         0.518          pass              0.319             22.5                           0.230                3.01              0.582                                 ok            True                  False
  PYPL           86.67               15            1.78              0.69         54.75                60.08         0.508          pass              0.422             53.3                           0.474                0.06              0.072                                 ok            True                  False
  NXPI           85.19               27            1.20              2.00        237.22                39.27         0.502          pass              0.489             62.5                           0.419                5.37              0.670                                 ok            True                  False
   STX           89.29               28            2.13             13.64        910.98                54.25         0.500          pass              0.504             28.9                           0.256               11.48              1.840                                 ok            True                  False
  MSTR           94.59               37            0.44              0.49        158.40               104.19         0.736          pass              0.900             85.7                           0.707               15.31              2.504                                 ok           False                  False
   TRI           83.33               18            2.33              1.61         98.30                56.74         0.575          pass              0.222              7.4                           0.082               -8.63             -0.575 downtrend_blocked_slope_and_streak           False                  False
  AMAT           83.33               42            0.19              0.64        484.73                51.73         0.537          pass              0.626             94.6                           0.867               14.12              1.763                                 ok           False                  False
  CHTR           79.55               44            0.21              0.16        112.84                64.54         0.516          pass              0.524             90.8                           0.602              -21.40             -2.610 downtrend_blocked_slope_and_streak           False                  False
  KLAC           75.61               41            0.34              0.45        187.73                50.67         0.512          pass              0.521             89.8                           0.771               10.75              1.425                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                              detail
2026-09-28T09:50:05.886543-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-28T03:00:06.642645-04:00   data_refresh  data_refresh                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00 share_ext_0255 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00 share_ext_0250 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00 share_ext_0245 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:40:05.820539-04:00 share_ext_0240 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:35:05.219756-04:00 share_ext_0235 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:30:04.108962-04:00 share_ext_0230 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:25:06.088084-04:00 share_ext_0225 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:20:05.261496-04:00 share_ext_0220 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928095005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928095005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928095005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928095005)

</details>
