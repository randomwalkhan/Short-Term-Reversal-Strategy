# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:02:58 EDT`
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
  TEAM           86.67               15            4.72              3.02         90.30               114.36         0.613          pass              0.342             23.2                           0.379               26.09              3.288                                 ok            True                  False
  GOOG           83.33               18            1.64              4.57        395.09                37.66         0.569          pass              0.264             21.7                           0.334               12.05              1.419                                 ok            True                  False
    ZS           80.00               20            2.45              2.61        151.01                58.64         0.535          pass              0.162             13.9                           0.187               10.66              1.329                                 ok            True                  False
  TMUS           86.21               29            0.96              1.30        193.07                36.59         0.532          pass              0.441             32.0                           0.228                4.94              0.266                                 ok            True                  False
   WMT           86.67               15            1.27              1.16        129.93                19.38         0.527          pass              0.319             18.2                           0.324                1.12              0.152                                 ok            True                  False
   KDP           87.10               31            0.50              0.10         28.79                34.30         0.519          pass              0.550             56.4                           0.299                1.90             -0.006                                 ok            True                  False
  ASML           84.62               13            3.20             35.67       1576.73                48.89         0.500          pass              0.275             27.4                           0.529                7.58              1.209                                 ok            True                  False
  CHTR           80.00               15            2.63              2.86        153.64               119.48         0.783          pass              0.199             29.2                           0.211              -13.65             -1.217            downtrend_blocked_slope           False                  False
  NXPI           81.58               38            0.27              0.57        294.51                87.07         0.711          pass              0.535             78.4                           0.600               24.09              1.938                                 ok           False                  False
 CMCSA           88.24               17            0.91              0.16         25.33                62.19         0.706          pass              0.377             13.2                           0.183               -8.52             -0.831 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               40            0.30              0.40        187.42                70.10         0.587          pass              0.793             89.3                           0.673               10.53              1.526                                 ok           False                  False
  SHOP           92.31               13            4.30              3.33        109.08                82.28         0.576          pass              0.438             10.6                           0.370              -14.87             -1.727            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511110258)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511110258)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511110258)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511110258)

</details>
