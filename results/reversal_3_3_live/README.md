# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:41:24 EDT`
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
  TEAM           80.00               10            5.51              3.53         90.09               114.36         0.589          pass              0.090             10.3                           0.197               25.04              3.251                                 ok            True                  False
  GOOG           83.33               18            1.52              4.22        395.24                37.66         0.575          pass              0.283             27.6                           0.313               12.19              1.425                                 ok            True                  False
   KDP           88.46               26            0.75              0.15         28.77                34.30         0.538          pass              0.492             35.3                           0.273                1.65             -0.017                                 ok            True                  False
    ZS           82.61               23            2.14              2.27        151.16                58.64         0.537          pass              0.292             27.3                           0.501               11.01              1.344                                 ok            True                  False
  TMUS           86.21               29            0.96              1.30        193.07                36.59         0.531          pass              0.440             31.6                           0.357                4.94              0.266                                 ok            True                  False
  INTU           89.29               28            1.18              3.28        394.91                49.37         0.516          pass              0.595             58.6                           0.322                0.44              0.061                                 ok            True                  False
  MDLZ           83.33               24            0.77              0.33         61.41                24.76         0.501          pass              0.442             70.0                           0.446                6.37              0.487                                 ok            True                  False
  CHTR           75.00                8            3.89              4.22        153.05               119.48         0.753          pass              0.081              1.8                           0.197              -14.76             -1.276            downtrend_blocked_slope           False                  False
 CMCSA           92.86               14            1.02              0.18         25.32                62.19         0.721          pass              0.447              1.9                           0.233               -8.63             -0.837 downtrend_blocked_slope_and_streak           False                  False
  NXPI           81.58               38            0.28              0.57        294.50                87.07         0.711          pass              0.534             78.1                           0.490               24.09              1.938                                 ok           False                  False
  GEHC           57.14               21            1.73              0.77         63.14                57.03         0.570          pass              0.130              0.0                           0.157              -11.51             -0.723            downtrend_blocked_slope           False                  False
  FTNT           96.00               50            0.14              0.11        114.02                70.49         0.566          pass              0.939             94.2                           0.638               32.96              3.106                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511114124)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511114124)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511114124)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511114124)

</details>
