# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:50:01 EDT`
Last processed slot: `manage_1100`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26       30.350     36.1500  2320.0   19.110379 take_profit_day2_hit_at_scan
  SBUX     option         option SBUX260717C00105000     38          2026-05-22         2026-05-26        3.625      3.2625 -1377.5  -10.000000        stop_loss_hit_at_scan
  TTWO     option         option TTWO260717C00230000     15          2026-05-26         2026-05-26        9.800     11.3500  2325.0   15.816327 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.91               44            0.64              0.38         85.26               109.49         0.671          pass              0.810             83.9                           0.563               -2.79              0.049                                 ok            True                   True
  MELI           92.31               26            1.75             20.44       1655.66                60.80         0.571          pass              0.609             39.1                           0.515                5.00              0.686                                 ok            True                  False
  PAYX           90.00               10            1.39              0.94         96.60                28.52         0.552          pass              0.483             53.6                           0.601                3.20              0.593                                 ok            True                  False
  CTSH           85.00               20            1.55              0.57         52.50                46.65         0.542          pass              0.405             50.3                           0.446                6.19              1.319                                 ok            True                  False
   ADP           93.33               15            2.04              3.21        223.93                37.70         0.540          pass              0.500             19.0                           0.286                4.28              0.656                                 ok            True                  False
   ROP           88.89               18            1.58              3.60        325.40                26.18         0.514          pass              0.397             18.5                           0.217               -2.13              0.054                                 ok            True                  False
 CMCSA           84.21               19            0.99              0.18         25.13                20.74         0.506          pass              0.338             38.3                           0.218               -0.30              0.027                                 ok            True                  False
  INTU           78.57               14            3.24              7.26        316.83                90.56         0.658          pass              0.113              7.0                           0.085              -21.29             -2.266            downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.33              0.80         85.52                55.00         0.623          pass              0.247             50.4                           0.383               -4.33              0.105                                 ok           False                  False
  CSCO           80.00                5            2.56              2.16        119.48                52.25         0.621          pass              0.083              6.9                           0.252               18.85              1.851                                 ok           False                  False
  SBUX           92.31               13            1.23              0.89        102.73                33.02         0.607          pass              0.544             44.9                           0.492               -3.12             -0.266            downtrend_blocked_slope           False                  False
   WMT           93.75               16            1.13              0.95        119.86                34.37         0.595          pass              0.511             15.0                           0.286               -6.80             -0.835 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-26T10:50:01.303434-04:00 early_entry_1050 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260717C00230000", "fill_price": 11.35, "pnl": 2325.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.82, "ticker": "TTWO"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit      {"asset_type": "option", "contract_symbol": "SBUX260717C00105000", "fill_price": 3.2625, "pnl": -1377.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SBUX"}
2026-05-26T10:45:02.313357-04:00 early_entry_1045 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:40:05.315818-04:00 early_entry_1040 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:35:01.414005-04:00 early_entry_1035 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:30:01.317125-04:00 early_entry_1030 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:25:03.305112-04:00 early_entry_1025 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:20:01.300698-04:00 early_entry_1020 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:15:02.302661-04:00 early_entry_1015 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526105001)

</details>
