# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 12:55:05 EDT`
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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0      -10.00        stop_loss_hit_at_scan
  AVGO     option         option AVGO260717C00420000      4          2026-05-28         2026-05-28        31.25      35.950  1880.0       15.04 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           97.14               35            0.77              0.66        121.49                92.16         0.621            pass              0.878             82.9                           0.696                0.45              0.793                                 ok            True                   True
   XEL           94.12               17            1.23              0.70         80.70                25.49         0.549            pass              0.606             42.5                           0.689                0.11              0.221                                 ok            True                  False
  MNST           91.67               36            0.54              0.34         89.10                49.17         0.507            pass              0.719             61.3                           0.592                3.29              0.263                                 ok            True                   True
  CSCO           94.29               35            0.27              0.23        119.57                51.65         0.598            pass              0.850             81.0                           0.649               17.15              0.896                                 ok           False                  False
  ROST           83.33                6            2.41              3.93        231.78                38.54         0.573            pass              0.216             23.1                           0.389                7.60              1.142                                 ok           False                  False
   AEP           75.00               12            1.07              0.97        129.15                25.33         0.559            pass              0.249             59.9                           0.565                0.18              0.218                                 ok           False                  False
  REGN           87.50               32            0.77              3.37        626.30                48.81         0.525            pass              0.458             19.7                           0.185              -13.34             -1.316 downtrend_blocked_slope_and_streak           False                  False
  GOOG           90.91               44            0.10              0.26        384.72                41.06         0.516            pass              0.811             89.6                           0.410               -3.65             -0.411 downtrend_blocked_slope_and_streak           False                  False
   CEG           82.93               41            0.25              0.50        288.46                55.24         0.506            pass              0.606             92.3                           0.637                4.92              1.021                                 ok           False                  False
   CSX           75.00                8            1.92              0.63         46.87                21.52         0.494 below_threshold              0.199             50.0                           0.698                4.13              0.305                                 ok           False                  False
  CHTR           88.89               36            0.87              0.89        146.80                56.79         0.492 below_threshold              0.584             41.5                           0.424                1.99              0.230                                 ok           False                  False
  AMGN           91.67               36            0.14              0.32        335.92                27.08         0.490 below_threshold              0.770             78.9                           0.579                0.50              0.227                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-28T12:40:01.998163-04:00      manage_1230          exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:45:05.997889-04:00 early_entry_1145 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:40:03.231101-04:00 early_entry_1140 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:35:03.979729-04:00 early_entry_1135 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:25:06.570222-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528125505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528125505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528125505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528125505)

</details>
