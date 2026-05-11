# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:09:25 EDT`
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
  TEAM           81.82               11            5.40              3.46         90.12               114.36         0.592          pass              0.151             12.1                           0.323               25.19              3.256                                 ok            True                  False
  GOOG           83.33               18            1.53              4.26        395.22                37.66         0.574          pass              0.281             27.0                           0.370               12.18              1.424                                 ok            True                  False
   KDP           88.46               26            0.68              0.14         28.77                34.30         0.541          pass              0.510             41.3                           0.264                1.72             -0.014                                 ok            True                  False
  SNPS           97.30               37            0.55              1.99        515.63                46.53         0.535          pass              0.845             70.6                           0.481                3.03              0.610                                 ok            True                  False
  TMUS           85.71               28            1.00              1.36        193.05                36.59         0.534          pass              0.412             28.7                           0.186                4.89              0.264                                 ok            True                  False
   WMT           83.33               12            1.47              1.34        129.85                19.38         0.529          pass              0.171              5.4                           0.207                0.91              0.143                                 ok            True                  False
   ADP           92.59               27            0.74              1.10        212.52                34.95         0.527          pass              0.690             62.8                           0.400                7.20              0.491                                 ok            True                  False
  INTU           90.00               30            1.12              3.09        394.98                49.37         0.509          pass              0.634             60.9                           0.302                0.51              0.064                                 ok            True                  False
  MDLZ           83.33               24            0.76              0.33         61.41                24.76         0.501          pass              0.443             70.3                           0.448                6.37              0.488                                 ok            True                  False
  CDNS           97.30               37            0.60              1.53        362.04                44.64         0.500          pass              0.855             74.9                           0.583                7.12              1.090                                 ok            True                   True
  CHTR           81.25               16            2.40              2.60        153.74               119.48         0.790          pass              0.259             35.4                           0.236              -13.44             -1.206            downtrend_blocked_slope           False                  False
 CMCSA           92.86               14            0.96              0.17         25.32                62.19         0.724          pass              0.465              7.5                           0.128               -8.58             -0.834 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511110925)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511110925)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511110925)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511110925)

</details>
