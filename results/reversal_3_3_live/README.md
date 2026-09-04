# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:15:04 EDT`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               14            1.18              3.66        442.55                21.54         0.549          pass              0.609             42.6                           0.335               -0.10             -0.023                                 ok            True                  False
  PAYX          100.00               11            1.77              1.55        124.42                25.54         0.544          pass              0.568             35.6                           0.578               -1.29             -0.091                                 ok            True                  False
    ZS          100.00               16            3.11              3.87        176.14                62.66         0.526          pass              0.662             56.6                           0.513               -5.21             -0.049                                 ok            True                  False
  NFLX           83.33               18            1.69              0.98         82.25                32.95         0.521          pass              0.226             10.6                           0.127                2.12              0.230                                 ok            True                  False
  REGN          100.00               21            1.05              6.19        840.82                28.19         0.518          pass              0.579             18.1                           0.139                0.07              0.138                                 ok            True                  False
 CMCSA           92.86               28            0.62              0.12         26.60                25.91         0.517          pass              0.547             10.8                           0.148               -1.36             -0.196                                 ok            True                  False
  WDAY           84.21               19            3.84              5.56        204.54                73.93         0.508          pass              0.306             27.6                           0.466               -0.52              0.294                                 ok            True                  False
  MSFT           89.47               19            1.33              4.77        508.08                22.07         0.504          pass              0.387              8.1                           0.154                4.15              0.400                                 ok            True                  False
  CHTR           90.70               43            0.73              0.77        151.05                61.35         0.502          pass              0.596             20.3                           0.156                0.07              0.027                                 ok            True                  False
  MNST           88.24               34            0.41              0.13         44.03               424.09         0.998          pass              0.654             58.1                           0.435               -8.14             -1.143 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                5            3.01              1.20         56.31                56.63         0.608          pass              0.499             12.8                           0.293              -10.46             -1.597 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.00               25            3.20              3.25        143.43               101.55         0.580          pass              0.312             51.2                           0.613               17.55              1.255                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                     detail
2026-09-04T10:15:04.189474-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00      manage_1000                    exit                                                                      {"asset_type": "option", "contract_symbol": "CSCO261016C00110000", "fill_price": 4.4, "pnl": 6682.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.12, "ticker": "CSCO"}
2026-09-04T10:05:05.442075-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:00:02.334638-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T00:00:05.130277-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 93}
2026-09-03T15:10:05.000086-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.72, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 85.0, "option_spread_pct": 12.16, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.542}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904101504)

</details>
