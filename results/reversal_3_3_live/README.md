# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:47:42 EDT`
Last processed slot: `early_entry_1145`

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

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               11            5.31              3.41         90.14               114.36         0.597          pass              0.155             13.5                           0.225               25.30              3.260                                 ok            True                  False
  GOOG           83.33               18            1.65              4.60        395.08                37.66         0.568          pass              0.263             21.2                           0.296               12.04              1.419                                 ok            True                  False
    ZS           82.61               23            2.15              2.29        151.15                58.64         0.537          pass              0.290             26.8                           0.491               11.00              1.343                                 ok            True                  False
   KDP           89.29               28            0.62              0.13         28.78                34.30         0.534          pass              0.558             45.8                           0.308                1.78             -0.012                                 ok            True                  False
  SNPS           97.30               37            0.60              2.18        515.55                46.53         0.533          pass              0.837             67.9                           0.473                2.97              0.608                                 ok            True                  False
  TMUS           86.21               29            0.93              1.26        193.09                36.59         0.533          pass              0.446             33.6                           0.313                4.97              0.267                                 ok            True                  False
  INTU           89.29               28            1.15              3.20        394.94                49.37         0.518          pass              0.598             59.5                           0.344                0.46              0.062                                 ok            True                  False
   ADP           93.55               31            0.54              0.81        212.65                34.95         0.516          pass              0.770             72.5                           0.635                7.41              0.500                                 ok            True                   True
  CHTR           75.00                8            4.00              4.33        153.00               119.48         0.748          pass              0.082              2.4                           0.074              -14.86             -1.281            downtrend_blocked_slope           False                  False
 CMCSA           91.67               12            1.12              0.20         25.31                62.19         0.724          pass              0.402              1.7                           0.186               -8.72             -0.841 downtrend_blocked_slope_and_streak           False                  False
  FTNT           96.00               50            0.06              0.05        114.05                70.49         0.570          pass              0.949             97.4                           0.765               33.07              3.110                                 ok           False                  False
  GEHC           58.33               24            1.59              0.71         63.17                57.03         0.559          pass              0.207             19.2                           0.207              -11.38             -0.716            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511114742)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511114742)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511114742)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511114742)

</details>
