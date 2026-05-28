# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 14:50:05 EDT`
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
  INTC           97.14               35            0.73              0.62        121.50                92.16         0.624            pass              0.881             83.8                           0.695                0.49              0.795                                 ok            True                   True
  CSCO           92.59               27            0.66              0.55        119.43                51.65         0.624            pass              0.673             53.8                           0.399               16.70              0.878                                 ok            True                  False
  MNST           90.48               21            1.21              0.76         88.92                49.17         0.561            pass              0.498             29.9                           0.461                2.60              0.232                                 ok            True                  False
   LIN           88.24               17            1.38              4.90        505.77                20.85         0.500 below_threshold              0.390             24.7                           0.283               -2.41             -0.052                                 ok            True                  False
    MU           83.78               37            0.02              0.12        928.36               100.84         0.691            pass              0.649             99.6                           0.480               15.51              2.141                                 ok           False                  False
   XEL          100.00                8            1.91              1.08         80.54                25.49         0.570            pass              0.491             11.2                           0.183               -0.57              0.190                                 ok           False                  False
   AEP           71.43                7            1.56              1.41        128.97                25.33         0.556            pass              0.181             41.9                           0.257               -0.31              0.195                                 ok           False                  False
  AMAT           88.89               36            0.25              0.77        447.92                50.47         0.537            pass              0.731             89.0                           0.429                2.54              0.425                                 ok           False                  False
  REGN           87.50               32            0.76              3.35        626.30                48.81         0.525            pass              0.459             20.0                           0.244              -13.34             -1.316 downtrend_blocked_slope_and_streak           False                  False
  ROST           75.00                4            3.20              5.24        231.23                38.54         0.522            pass              0.064              4.0                           0.224                6.72              1.105                                 ok           False                  False
  LRCX           90.00               40            0.34              0.76        318.60                56.04         0.510            pass              0.786             89.3                           0.571                7.58              1.168                                 ok           False                  False
   WDC           97.56               41            0.09              0.33        530.46                62.28         0.508            pass              0.944             97.7                           0.426                7.29              1.005                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-28T14:50:05.035990-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T14:50:05.035990-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-28", "training_samples": 5117, "window": 5}
2026-05-28T12:40:01.998163-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:45:05.997889-04:00 early_entry_1145  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:40:03.231101-04:00 early_entry_1140  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:35:03.979729-04:00 early_entry_1135  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528145005)

</details>
