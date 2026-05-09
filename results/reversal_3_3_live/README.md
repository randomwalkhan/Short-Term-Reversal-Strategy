# Reversal 3.4 Live Paper Test

Latest checkpoint (ET): `2026-05-08 16:00:00 EDT`
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
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one high-confidence candidate when `early_entry_score >= 0.62`; the one-new-entry-per-day limit still applies
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

- Cash: `$32,833.50`
- Equity: `$32,833.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option  TXN260618C00290000     10          2026-05-07         2026-05-08        13.10       15.50 2400.0   18.320611 take_profit_day1_hit_at_scan
  TEAM     option         option TEAM260618C00090000     19          2026-05-08         2026-05-08         7.75        9.25 2850.0   19.354839 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.86               35            2.29              1.48         91.74               115.49         0.621            pass              0.525             73.4               26.14              3.534                                 ok            True                  False
   XEL           90.91               11            1.29              0.73         80.12                27.43         0.559            pass              0.382              9.6                0.30              0.137                                 ok            True                  False
  FAST           95.83               24            0.96              0.30         44.23                33.68         0.547            pass              0.635             29.1               -1.17             -0.082                                 ok            True                   True
    ZS           82.05               39            0.84              0.90        152.40                60.77         0.501            pass              0.548             83.2               11.81              1.200                                 ok            True                  False
  CHTR           69.23               13            3.02              3.39        158.79               119.32         0.763            pass              0.134             12.6              -13.73             -1.262            downtrend_blocked_slope           False                  False
 CMCSA           75.00                4            2.93              0.54         26.01                61.43         0.633            pass              0.104             13.5               -7.58             -0.671 downtrend_blocked_slope_and_streak           False                  False
  SHOP           91.67               36            1.24              0.97        111.33                82.33         0.597            pass              0.750             68.6              -12.29             -1.550 downtrend_blocked_slope_and_streak           False                  False
  ORLY           77.78                9            1.92              1.27         94.03                34.97         0.538            pass              0.142             29.5               -0.40              0.191                                 ok           False                  False
   AEP           94.44               18            1.01              0.93        131.36                20.97         0.517            pass              0.564             24.7               -3.19             -0.281            downtrend_blocked_slope           False                  False
  PYPL           91.30               23            1.95              0.63         45.95                42.03         0.511            pass              0.446              2.2              -10.22             -1.113 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.18               39            0.37              0.50        193.99                36.72         0.500            pass              0.621             62.1                1.94              0.360                                 ok           False                  False
  INSM           75.00               28            1.72              1.26        104.26                99.84         0.496 below_threshold              0.377             69.0              -23.80             -2.050 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-05-08T16:05:06.142170-04:00 manage_1600         exit {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00 manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00 manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00 manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:00:03.172365-04:00  entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508160000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508160000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508160000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508160000)

</details>
