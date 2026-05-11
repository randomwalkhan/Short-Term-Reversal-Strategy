# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:15:52 EDT`
Last processed slot: `early_entry_1115`

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
  TEAM           87.50               16            4.63              2.97         90.33               114.36         0.613          pass              0.375             24.5                           0.500               26.20              3.292                                 ok            True                  False
  GOOG           82.35               17            1.68              4.66        395.05                37.66         0.571          pass              0.227             20.1                           0.308               12.01              1.418                                 ok            True                  False
  SNPS           97.22               36            0.77              2.77        515.29                46.53         0.530          pass              0.804             59.1                           0.386                2.80              0.600                                 ok            True                  False
  TMUS           84.38               32            0.71              0.97        193.22                36.59         0.524          pass              0.464             49.3                           0.439                5.20              0.277                                 ok            True                  False
    ZS           80.00               20            2.70              2.87        150.90                58.64         0.520          pass              0.143              8.2                           0.187               10.38              1.318                                 ok            True                  False
   ADP           93.10               29            0.69              1.03        212.55                34.95         0.519          pass              0.723             65.2                           0.370                7.25              0.493                                 ok            True                  False
   WMT           83.33               12            1.71              1.56        129.76                19.38         0.515          pass              0.164              3.5                           0.229                0.67              0.132                                 ok            True                  False
  MDLZ           84.00               25            0.65              0.28         61.43                24.76         0.502          pass              0.481             74.8                           0.474                6.50              0.493                                 ok            True                  False
  CHTR           83.33               18            2.26              2.45        153.81               119.48         0.790          pass              0.339             39.3                           0.432              -13.31             -1.200            downtrend_blocked_slope           False                  False
  NXPI           81.58               38            0.34              0.70        294.45                87.07         0.708          pass              0.520             73.5                           0.586               24.02              1.935                                 ok           False                  False
 CMCSA           90.00               20            0.75              0.13         25.34                62.19         0.702          pass              0.488             28.3                           0.311               -8.38             -0.824 downtrend_blocked_slope_and_streak           False                  False
  FTNT           95.56               45            0.42              0.34        113.93                70.49         0.579          pass              0.905             82.5                           0.497               32.59              3.093                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511111552)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511111552)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511111552)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511111552)

</details>
