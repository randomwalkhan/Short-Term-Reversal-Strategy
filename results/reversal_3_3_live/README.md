# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:35:07 EDT`
Last processed slot: `manage_1130`

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
  TEAM           81.82               11            5.40              3.46         90.12               114.36         0.592          pass              0.150             12.0                           0.211               25.18              3.256                                 ok            True                  False
  GOOG           83.33               18            1.57              4.37        395.18                37.66         0.572          pass              0.275             25.1                           0.313               12.13              1.422                                 ok            True                  False
  TMUS           86.21               29            0.79              1.07        193.17                36.59         0.541          pass              0.477             43.8                           0.446                5.12              0.274                                 ok            True                  False
   KDP           88.46               26            0.75              0.15         28.77                34.30         0.538          pass              0.492             35.3                           0.301                1.65             -0.017                                 ok            True                  False
    ZS           81.48               27            1.87              2.00        151.27                58.64         0.526          pass              0.314             36.2                           0.505               11.31              1.356                                 ok            True                  False
  INTU           89.29               28            1.18              3.27        394.91                49.37         0.516          pass              0.595             58.7                           0.337                0.44              0.061                                 ok            True                  False
  MDLZ           85.71               21            0.87              0.38         61.39                24.76         0.516          pass              0.475             65.9                           0.428                6.25              0.483                                 ok            True                  False
  CHTR           70.00               10            3.17              3.44        153.39               119.48         0.771          pass              0.121             14.8                           0.185              -14.12             -1.242            downtrend_blocked_slope           False                  False
  NXPI           82.05               39            0.27              0.55        294.51                87.07         0.707          pass              0.556             78.9                           0.537               24.10              1.938                                 ok           False                  False
 CMCSA           90.00               20            0.77              0.14         25.34                62.19         0.701          pass              0.483             26.4                           0.419               -8.40             -0.825 downtrend_blocked_slope_and_streak           False                  False
  FTNT           96.00               50            0.06              0.05        114.05                70.49         0.570          pass              0.949             97.4                           0.704               33.07              3.110                                 ok           False                  False
  GEHC           58.33               24            1.58              0.70         63.17                57.03         0.564          pass              0.167              5.7                           0.182              -11.36             -0.715            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511113507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511113507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511113507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511113507)

</details>
